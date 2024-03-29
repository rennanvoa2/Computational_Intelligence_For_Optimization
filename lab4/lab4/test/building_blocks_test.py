# -------------------------------------------------------------------------------------------------
# CIFO - Computation Intelligence for Optmization
# Bulding Blocks UNIT Tests
# Content
# - class ProblemTest
# -------------------------------------------------------------------------------------------------

from lab4.problem.solution import LinearSolution
from lab4.problem.problem_template import ProblemTemplate
from lab4.util.terminal import Terminal, FontColor

# -------------------------------------------------------------------------------------------------
# Class: Problem Test
# -------------------------------------------------------------------------------------------------
class ProblemTest:
    # Constructor
    #----------------------------------------------------------------------------------------------
    def __init__(self, problem_instance, require_feedback = False):
        self._problem_instance = problem_instance
        self._errors           = []
        self._warnings         = []
        self._require_feedback = require_feedback

    # Run the class test
    #----------------------------------------------------------------------------------------------
    def run(self):
        self._errors = []

        Terminal.clear()
        Terminal.print_box(messages = ["Name: " + self._problem_instance._name ], font_color=FontColor.Yellow)
        try:
            print( f" Objective       = {self._problem_instance.objective}" )
        except:
            print( "ERROR: " + self._problem_instance.objective)
            self._errors.append()

        print( f" Multi-objective = {self._problem_instance.is_multi_objective}" )

        print( f" Encoding Rule = {self._problem_instance.encoding_rule }" )

        self._build_solution()

        self._evaluate()

    # Test the build_solution
    #----------------------------------------------------------------------------------------------
    def _build_solution(self):
        Terminal.print_box(messages = [f"Build Solution - ENCODING: Can repeat = {self._problem_instance.encoding.can_repeat_elements} - Is Ordered = {self._problem_instance.encoding.is_ordered }"] )
        solution = None
        for _ in range(0,8):
            try:
                solution = self._problem_instance.build_solution()
                print(f"solution = {solution.representation}")
            except:
                self._errors.append("Build Solution Failed!")
                if solution == None: print(" - Error: Check if build solution is OK or if it was implemented")


    def _evaluate(self):
        Terminal.print_box(messages = ["Objective Function" ] )

        feedback = None
        if self._require_feedback:
            feedback = self._problem_instance.build_solution()
            for _ in range(0,8):
                solution = self._problem_instance.build_solution()
                self._problem_instance.evaluate_solution( solution = solution  , feedback = feedback )
                print( f" solution = {solution.representation} | feedback = { feedback.representation } | fitness = {solution.fitness}" )
        else:
            for _ in range(0,8):
                solution = self._problem_instance.build_solution()
                self._problem_instance.evaluate_solution( solution = solution  )
                print( f" solution = {solution.representation} | fitness = {solution.fitness}" )


# -------------------------------------------------------------------------------------------------
# Class: Neighborhood Function Test
# -------------------------------------------------------------------------------------------------
class NeighborhoodFunctionTest:
    # Constructor
    #----------------------------------------------------------------------------------------------
    def __init__(self, problem_instance, neighborhood_function):
        self._problem_instance      = problem_instance
        self._neighborhood_function = neighborhood_function
        self._errors                = []
        self._warnings              = []

    # Run
    #----------------------------------------------------------------------------------------------
    def run(self):
        Terminal.print_box(messages = [ f"Neighborhood Function - ENCODING: Can repeat = {self._problem_instance.encoding.can_repeat_elements} - Is Ordered = {self._problem_instance.encoding.is_ordered }" ] )
        for _ in range(0, 2):
            solution = self._problem_instance.build_solution()
            neighbors = self._neighborhood_function( solution = solution, problem = self._problem_instance )

            Terminal.print_line( message = f"\nNeighbors of {solution.representation} are:")
            for neighbor in neighbors:
                print(f"             {neighbor.representation} ")
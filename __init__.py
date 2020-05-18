"""ProjectEuler problems solver! Has methods to solve ProjectEuler problems."""
# Throughout this file it might help to remember, the goal is to import "solve" on all the problem files in the current
#   directory as their file name. In sudocode, we want to do:
#       for x in os.listdir(os.path.dirname(__file__)):
#           from x import solve as x

import importlib
import os
import logging
import re

logger = logging.getLogger()


class InvalidProblemSolver(object):
    """An invalid problem solver, for problems that can't be loaded, that will handle calls and print errors."""
    def __init__(self, problem):
        self.problem = problem

    def __call__(self, *args, **kwargs):
        logger.error('Problem {} was executed, but there was an error loading it!'.format(self.problem))
        return None


# Import all the problems into a dict.
PROBLEMS = dict()

# These problems should all be working, and will affect the test argument.
COMPLETED_PROBLEMS = dict()

# We've completed problems 1 through:
MAX_SEQUENTIAL_COMPLETED_PROBLEM = 126
__COMPLETED_PROBLEMS = sorted(
    # Use this to define problems after sequential completion fails.
    {'p131', 'p137', 'p146', 'p148', 'p149', 'p243'}
    | set('p{:03}'.format(p) for p in range(1, MAX_SEQUENTIAL_COMPLETED_PROBLEM + 1))
)


# Import anything in the current directory that looks like a problem solver
for problem in os.listdir(os.path.dirname(__file__)):
    if not re.match('p[0-9]*\.py', problem):
        # This doesn't look like a problem solver...
        continue

    problem, _ = os.path.splitext(problem)

    try:
        # If this module was executed, __package__ will be None and we can just import our problem.
        #   Otherwise, we must have imported this method, and must import child modules another way.
        if __package__:
            problem_module = importlib.import_module('.{}'.format(problem), __package__)
        else:
            problem_module = importlib.import_module('{}'.format(problem))

        if not getattr(problem_module, '__doc__', ''):
            logger.warning('Module for problem %s is missing the problem statement!', problem)

        PROBLEMS[problem] = problem_module.solve
    except Exception:
        logger.error('Could not import solver for problem %r', problem, exc_info=True)
        PROBLEMS[problem] = InvalidProblemSolver(problem)

    if problem in __COMPLETED_PROBLEMS:
        COMPLETED_PROBLEMS[problem] = PROBLEMS[problem]

# Add the problems to the local namespace for __all__.
locals().update(PROBLEMS)
__all__ = ['InvalidProblemSolver', 'utils']
__all__ += list(PROBLEMS.keys())

# Also import all the utils.
if __package__:
    utils = importlib.import_module('.utils', __package__)
else:
    utils = importlib.import_module('utils')

import argparse
import logging

from timeit import default_timer as timer

from __init__ import PROBLEMS, COMPLETED_PROBLEMS, InvalidProblemSolver
from utils import output_answer, human_readable_time

logger = logging.getLogger()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve some problems.')
    parser.add_argument('problems', metavar='N', nargs='*',
                        help='Problem numbers to solve. 1, 001, p001 are all acceptable.')
    parser.add_argument('--test', '-t', action='store_true', default=False,
                        help="Include test problems? Not used if problems are specified manually.")
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
                        help="Verbose output. Currently only changes timing output.")

    # TODO: Add an optional argument, --python, -py, that takes in a list of Python versions to test with.
    #   eg, -py 3.8 -py 2.7
    #   If a -py version is specified, we shouldn't even bother executing stuff here,
    #       just search for Python executables and call them.

    args = parser.parse_args()

    # region Process arguments
    problems_to_solve = dict()
    if args.problems:
        for problem in args.problems:
            # Cut off the first character if it is a p, eg, p001
            problem_number = problem[1:] if problem[0].lower() == 'p' else problem

            try:
                problem_number = int(problem_number)
            except ValueError:
                logger.error('There was an error processing the problem number: %r', problem)
                continue

            problem_key = 'p{:03}'.format(problem_number)
            this_problem_solver = PROBLEMS.get(problem_key)
            if this_problem_solver is None:
                logger.error('There is no problem for problem number: %r', problem)
                continue
            elif isinstance(this_problem_solver, InvalidProblemSolver):
                logger.error('Could not load solver for problem number: %r', problem)
                continue

            problems_to_solve[problem_key] = this_problem_solver
    else:
        for problem_key, solver in (PROBLEMS if args.test else COMPLETED_PROBLEMS).items():
            if isinstance(solver, InvalidProblemSolver):
                logger.error('Could not load solver for problem number: %r', problem_key)
                continue

            problems_to_solve[problem_key] = solver

    if not problems_to_solve:
        logger.critical('There are no problems to solve! Likely because of argument errors.')
        exit(1)
    # endregion

    logger.info('Loading done. Beginning problem solving...')

    # TODO: Process pool? Only concern is ensuring that output text is ordered.
    total_start_time = timer()
    for problem_key, problem_solver in sorted(problems_to_solve.items()):
        output_answer(problem_key, problem_solver, args.verbose)
    total_end_time = timer()

    if args.verbose:
        logger.critical("Total execution time: %s", human_readable_time(total_end_time - total_start_time))

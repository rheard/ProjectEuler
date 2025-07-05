import argparse
import importlib
import logging
import re

from pathlib import Path
from timeit import default_timer as timer


logger = logging.getLogger()


def load_problem_solver(problem):
    """Load the problem solver package, inspect it, and return the solver"""
    if __package__:
        problem_module = importlib.import_module(f".{problem}", __package__)
    else:
        problem_module = importlib.import_module(problem)

    if not getattr(problem_module, '__doc__', ''):
        logger.warning('Module for problem %s is missing the problem statement!', problem)

    solver = getattr(problem_module, 'solve', None)
    if solver is None:
        logger.warning('Module for problem %s is missing the problem solver!', problem)

    elif not getattr(solver, '__doc__', ''):
        logger.warning('Module for problem %s is missing the problem explanation!', problem)

    return solver


def human_readable_time(seconds):
    """Converts seconds to a human readable time."""
    # TODO: Days? Months? etc?
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    output = []

    if hours:
        output.append(f'{hours} hours')

    if minutes:
        output.append(f'{minutes} minutes')

    # If seconds is 0, we don't to output it,
    #   UNLESS there is no other output, then we will output "0 seconds"
    if not output or seconds:
        output.append(f'{seconds:.6f} seconds')

    return ', '.join(output)


def output_answer(problem_solver, verbose=False):
    """
    Outputs the answer to the logger.

    Args:
        problem_solver (callable): The problem solver.
        verbose (bool, optional): Verbose timing output. Defaults to False.
    """
    problem_key = Path(problem_solver.__code__.co_filename).stem

    try:
        start_time = timer()
        answer = str(problem_solver())
        end_time = timer()

        expected_answer = str(getattr(problem_solver, 'answer', ''))

        verified = ''
        if not expected_answer:
            verified = ' (answer could not be verified!)'
        elif answer != expected_answer and expected_answer:
            verified = f' (answer does not match expected answer {expected_answer})'

        if not getattr(problem_solver, '__doc__', None):
            verified += ' (missing strategy docstring)'

        elapsed_time = end_time - start_time
        if verbose:
            verified += f'\n\tTime: {human_readable_time(elapsed_time)}'
        elif elapsed_time > 60:
            verified += f' (failed speed challenge {human_readable_time(elapsed_time)})'

        logger.critical('%s: %s%s', problem_key, answer, verified)
    except Exception:
        logger.error("Could not complete problem %s", problem_key, exc_info=True)


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

            problem_key = f'p{problem_number:03}'
            this_problem_solver = load_problem_solver(problem_key)
            if this_problem_solver is None:
                logger.error('There is no problem solver for problem number: %r', problem)
                continue

            problems_to_solve[problem_key] = this_problem_solver
    else:
        for problem in Path(__file__).parent.iterdir():
            if not re.match('p[0-9]*\.py', problem):
                # This doesn't look like a problem solver...
                continue

            problem_key = problem.stem

            problem_solver = load_problem_solver(problem_key)
            if hasattr(problem_solver, 'answer') and not args.test:
                # Only execute problems in general execution if they are confirmed solved
                problems_to_solve[problem_key] = problem_solver

    if not problems_to_solve:
        logger.critical('There are no problems to solve! Likely because of argument errors.')
        exit(1)
    # endregion

    logger.info('Loading done. Beginning problem solving...')

    # TODO: Process pool?
    #   Only concern is ensuring problems which are already multi-process don't fail the speed challenge
    total_start_time = timer()
    for problem_key, problem_solver in sorted(problems_to_solve.items()):
        output_answer(problem_solver, args.verbose)
    total_end_time = timer()

    if args.verbose:
        logger.critical("Total execution time: %s", human_readable_time(total_end_time - total_start_time))

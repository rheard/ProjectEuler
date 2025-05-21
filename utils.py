from __future__ import division
import functools
import inspect
import math
import logging
import operator
import os

from itertools import accumulate, count
from timeit import default_timer as timer

# gcd was deprecated in fractions and moved to math.
try:
    from math import gcd as _gcd
except ImportError:
    from fractions import gcd as _gcd

__all__ = ['prod', 'PHI', 'fibonacci', 'fibonacci_generator', 'triangle_generator', 'triangle', 'gcd', 'lcm',
           'binomial', 'output_answer', 'human_readable_time']

prod = lambda x: functools.reduce(operator.mul, x, 1)
PHI = (1 + math.sqrt(5)) / 2
logger = logging.getLogger()


def human_readable_time(seconds):
    """Converts seconds to a human readable time."""
    # TODO: Days? Months? etc?
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    output = []

    if hours:
        output.append('{} hours'.format(int(hours)))

    if minutes:
        output.append('{} minutes'.format(int(minutes)))

    # If seconds is 0, we don't to output it,
    #   UNLESS there is no other output, then we will output "0 seconds"
    if not output or seconds:
        output.append('{:.6f} seconds'.format(seconds))

    return ', '.join(output)


def output_answer(problem_solver, verbose=False):
    """
    Outputs the answer to the logger.

    Args:
        problem_solver (callable): The problem solver.
        verbose (bool, optional): Verbose timing output. Defaults to False.
    """
    caller_frame = inspect.stack()[1]
    problem_key = os.path.splitext(os.path.basename(caller_frame.filename))[0]

    try:
        start_time = timer()
        answer = str(problem_solver())
        end_time = timer()

        expected_answer = str(getattr(problem_solver, 'answer', ''))

        verified = ''
        if expected_answer is None:
            verified = ' (answer could not be verified!)'
        elif answer != expected_answer:
            verified = ' (answer does not match expected answer {})'.format(expected_answer)

        if not getattr(problem_solver, '__doc__', None):
            verified += ' (missing strategy docstring)'

        if verbose:
            verified += '\n\tTime: {}'.format(human_readable_time(end_time - start_time))

        logger.critical('%s: %s%s', problem_key, answer, verified)
    except Exception:
        logger.error("Could not complete problem %s", problem_key, exc_info=True)


def fibonacci_generator(a=0, b=1):
    """An infinite generator for the fibonacci numbers."""
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


def fibonacci(n):
    """Get the nth fibonacci number"""
    return int(round((PHI**n - (-PHI)**-n) / math.sqrt(5), 0))


def triangle_generator():
    """An infinite generator for triangle numbers."""
    yield from accumulate(count(1))


def triangle(n):
    """Get the nth triangle number"""
    return n * (n + 1) // 2


def gcd(*numbers):
    """A modified version of gcd that accepts more than 2 integers."""
    return functools.reduce(_gcd, numbers)


try:
    # lcm was added in Python 3.9
    from math import lcm as _lcm
except ImportError:
    try:
        # numpy's lcm can handle this, if its installed.
        from numpy import lcm as _lcm
    except ImportError:
        def _lcm(a, b):
            return abs(a * b) // gcd(a, b)


def lcm(*numbers):
    """lcm that accepts more than 2 integers."""
    return functools.reduce(_lcm, numbers, 1)


try:
    # Binomial coefficient was added in Python 3.8
    from math import comb as binomial
except ImportError:
    try:
        # scipy's comb can handle this, if its installed.
        from scipy.special import comb

        def binomial(n, k):
            return comb(n, k, exact=True)
    except ImportError:
        def binomial(n, k):
            """
            A function to compute binomial.

            https://stackoverflow.com/questions/26560726
            """
            # When k out of sensible range, should probably throw an exception.
            # For compatibility with scipy.special.{comb, binom} returns 0 instead.
            if k < 0 or k > n:
                return 0

            if k == 0 or k == n:
                return 1

            total_ways = 1
            for i in range(min(k, n - k)):
                total_ways = total_ways * (n - i) // (i + 1)

            return total_ways

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=1000):
    """No strategy here. Bruteforce."""
    target_sum = 0
    for num in range(3, n, 3):
        target_sum += num

    for num in range(5, n, 5):
        if num % 3 != 0:
            target_sum += num

    return target_sum


solve.answer = 233168


if __name__ == '__main__':
    output_answer(solve)

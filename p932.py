"""
For the year 2025

2025 = (20 + 25)**2

Given positive integers a and b, the concatenation ab we call a 2025-number if ab = (a + b)**2.
Other examples are 3025 and 81.
Note 9801 is not a 2025-number because the concatenation of 98 and 1 is 981.

Let T(n) be the sum of all 2025-numbers with n digits or less. You are given T(4) = 5131.

Find T(16).
"""

import os

from multiprocessing import Pool

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def processor(i):
    i_sq = i**2
    i_sq_str = str(i_sq)

    for k in range(1, len(i_sq_str)):
        if i_sq_str[k] == '0':
            continue

        x, y = int(i_sq_str[:k]), int(i_sq_str[k:])
        if x + y == i:
            # Found one!
            return i_sq

    return 0


def solve(n=16):  # T
    """
    Has to be a square number, so just go over the square numbers and check.

    That worked but took 70 seconds. Adding multiprocessing and calling it a day.
    """

    with Pool() as p:
        return sum(p.map(processor, range(9, 10**(n // 2))))


solve.answer = 72673459417881349


if __name__ == '__main__':
    output_answer(solve)

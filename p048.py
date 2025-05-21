"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=1000):
    """No strategy here. Bruteforce."""
    return str(sum(x**x for x in range(1, n + 1)))[-10:]


solve.answer = 9110846700


if __name__ == '__main__':
    output_answer(solve)

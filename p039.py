"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from __future__ import print_function

import os

from collections import deque

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=1000):
    """
    This is similar to the solution for problem 9.
    """
    solution_count = [0] * (n + 1)
    forest = deque([(2, 1), (3, 1)])
    while forest:
        m, n_ = forest.popleft()

        m_sq, n_sq = m**2, n_**2
        base_a = m_sq - n_sq
        base_b = 2 * m * n_
        base_c = m_sq + n_sq

        # Multiply the base perimeter by k values while it stays under n.
        base_perimeter = base_a + base_b + base_c
        for perimeter in range(base_perimeter, n, base_perimeter):
            solution_count[perimeter] += 1

        if base_perimeter <= n:
            forest.append((2 * m - n_, m))
            forest.append((2 * m + n_, m))
            forest.append((m + 2 * n_, n_))

    return max(range(n + 1), key=lambda x: solution_count[x])


solve.answer = 840


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

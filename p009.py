"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import os

from collections import deque

try:
    from .utils import output_answer, prod
except ImportError:
    from utils import output_answer, prod


def solve(target_sum=1000):
    """
    We want to generate all pythagorean triples, and stop when we find a triples that adds to 1000.

    To generate Pythagorean triples, you first need 2 coprime numbers (m, n):
        a = k * m**2 - n**2
        b = k * 2mn
        c = k * m**2 + n**2

    To generate coprime pairs, we start with seeds of (m, n): (2, 1), (3, 1)
        Then each seed creates a tree, where 3 new coprime pairs are:
            (2m - n, m)
            (2m + n, m)
            (m + 2n, n)

    So, we get a (m, n) from the forest of coprime pairs, and generate a Pythagorean triple with k=1.
        If the sum of that triple evenly divides 1000, then k is that quotient, and we found our triple.
    """
    forest = deque([(2, 1), (3, 1)])
    while forest:
        m, n = forest.popleft()

        m_sq, n_sq = m**2, n**2
        base_a = m_sq - n_sq
        base_b = 2 * m * n
        base_c = m_sq + n_sq

        base_count = base_a + base_b + base_c
        k, r = divmod(target_sum, base_count)

        if not r:
            return prod((base_a * k, base_b * k, base_c * k))

        forest.append((2 * m - n, m))
        forest.append((2 * m + n, m))
        forest.append((m + 2 * n, n))


solve.answer = 31875000


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

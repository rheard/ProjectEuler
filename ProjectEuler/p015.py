"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20*20 grid?
"""

from ProjectEuler.utils import binomial


def solve(n=20):
    """
    Solving manually for grids 1x1, 2x2, 3x3, 4x4, we get the sequence 1, 2, 6, 20. OEIS gives us A000984, which
        gives the formula binomial(2 * n, n).
    """
    return binomial(2 * n, n)


solve.answer = 137846528820

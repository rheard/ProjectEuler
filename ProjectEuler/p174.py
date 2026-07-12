"""
We shall define a square lamina to be a square outline with a square "hole"
    so that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3 x 3 square with a 1 x 1 hole in the middle.
    However, using thirty-two tiles it is possible to form two distinct laminae.

https://projecteuler.net/resources/images/0173_square_laminas.gif

If t represents the number of tiles used, we shall say that t=8 is type L(1) and t=32 is type L(2).

Let N(n) be the number of t<=1000000 such that t is type L(n); for example, N(15) = 832.

What is sum(N(n) for n in range(1, 10 + 1))?
"""

from collections import Counter, defaultdict


def solve(tiles=1_000_000):
    """
    This is a rather simple extension of problem 173.

    Instead of keeping track of how many tiles it is possible to make, we need to make a data structure of the
        corresponding tiles used (which we already calculated anyway) which corresponds to the output of L.

    Then by counting the values of L, we can build all the possible outputs of N, and validate that N[15] = 832.

    From there, solving the problem is just a matter of adding up some numbers in N.
    """
    max_square_side = (tiles // 4) + 1
    L_values = defaultdict(int)

    for square_side in range(3, max_square_side + 1):
        for hole_side in range(square_side - 2, 0, -2):
            tiles_used = square_side**2 - hole_side**2
            if tiles_used > tiles:
                break
            L_values[tiles_used] += 1

    N_values = Counter(L_values.values())

    return sum(N_values[x] for x in range(1, 11))


solve.answer = 209566

"""
How many 20 digit numbers n (without any leading zero) exist
    such that no three consecutive digits of n have a sum greater than 9?
"""

import os

import numpy as np

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


# These are all the options for 2 digits that are valid for this problem (they sum to less than 9)
TWO_DIGIT_OPTS = [f"{x}{y}" for x in range(10) for y in range(10) if x + y <= 9]

# See the below explanation for this matrix. Basically it is 1 when two options are "compatible" and 0 when they are not
# For instance, the numbers 12 and 24 can be combined because they have the same number in the middle
#   between them (12 24 becomes 124), and as a 3 digit number the sum is still less than 9 (1 + 2 + 4 < 9).
T = [
    [1 if opt1[1] == opt2[0] and sum(int(x) for x in opt1) + int(opt2[1]) <= 9 else 0
     for opt1 in TWO_DIGIT_OPTS]
    for opt2 in TWO_DIGIT_OPTS
]


def solve(r=20):
    """
    First I brute forced the solution for 4, 5 and 6 (990, 5445, 27588)

    OEIS reported that these were the deltas for the values in A241615

    Robert Israel has a great write-up showcasing the matrix math involved, but basically
        we start with all the 2 digit numbers possible for this problem (2 digits sum to less than 9, TWO_DIGIT_OPTS).

        Then construct a 55 x 55 matrix with 1 entry per pair of 2 digit numbers.

        If the pair of 2 digit numbers for that point in the matrix can be "combined", then there is a 1. Otherwise 0.
        For instance, the numbers 12 and 24 can be combined because they have the same number in the middle
        between them (12 24 becomes 124), and as a 3 digit number the sum is still less than 9 (1 + 2 + 4 < 9).

    Now we create a second matrix of all 1s, and repeatedly transpose and multiply it with the created matrix above.

    Almost magically this produces the number of solutions for all numbers with digits equal to or less than the target.
        However we are only interested in numbers with digits equal to the target (with no leading zeroes).
        So get the solution and subtract the solution for r - 1

    Beautiful maths Robert, thanks!
    """
    U1, U2 = None, np.ones(55)
    for _ in range(r):
        U1 = U2
        U2 = np.matmul(U2.T, T)

    return int(U2[0] - U1[0])


solve.answer = 378158756814587


if __name__ == '__main__':
    output_answer(solve)

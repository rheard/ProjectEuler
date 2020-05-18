"""
A row of five black square tiles is to have a number of its tiles replaced with
    coloured oblong tiles chosen from red (length two), green (length three),
    or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

[x|x| | | ]     [ |x|x| | ]     [ | |x|x| ]     [ | | |x|x]
[x|x|x|x| ]     [x|x| |x|x]     [ |x|x|x|x]

If green tiles are chosen there are three ways.

[x|x|x| | ]     [ |x|x|x| ]     [ | |x|x|x]

And if blue tiles are chosen there are two ways.

[ |x|x|x|x]     [x|x|x|x| ]

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
    replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in
    length be replaced if colours cannot be mixed and at least one coloured
    tile must be used?

NOTE: This is related to Problem 117.
"""

from __future__ import division

import os

from math import floor

try:
    from .utils import output_answer, binomial
except ImportError:
    from utils import output_answer, binomial


def arrangements(n, m):
    return sum(binomial(n-(m-1)*k, k) for k in range(1, floor(n/m) + 1))


def solve(n=50):
    """
    We cannot use our equations from the previous problem because
     * The tiles can be touching.
     * Different size tiles cannot be mixed.

    The sequence of the number of arrangements for the red (2-length) tiles can be
        found on OEIS (A000071), which is the n-th Fibonacci number minus 1.
        Surprisingly, a similar formula to the previous equation is found, giving...

    red arrangements = sum(binomial(n-k, k) for k in range(1, floor(n/2) + 1))

    Just as surprisingly, this can be extrapolated in a similar fashion:
    m-length arrangements = sum(binomial(n-(m-1)*k, k) for k in range(1, floor(n/m) + 1))
    """
    return int(arrangements(n, 2) + arrangements(n, 3) + arrangements(n, 4))


solve.answer = 20492570929


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

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

from __future__ import print_function, division
from lib import binomial
from math import floor

"""
We cannot use our equations from the previous problem because
 * The tiles can be touching.
 * Different size tiles cannot be mixed.

The sequence of the number of arrangements for the red (2-length) tiles can be
    found on OEIS (A000071). Surprisingly, a similar formula to the previous equation is
    found, giving...

red arrangements = sum(binomial(n-k, k) for k in range(1, floor(n/2) + 1))

Just as surprisingly, this can be extrapolated in a similar fashion:
m-length arrangements = sum(binomial(n-(m-1)*k, k) for k in range(1, floor(n/m) + 1))
"""


def arrangements(n, m):
    return sum(binomial(n-(m-1)*k, k) for k in range(1, floor(n/m) + 1))


def solve(l=50):
    return int(arrangements(l, 2) + arrangements(l, 3) + arrangements(l, 4))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p116_ans.txt', 'w') as wb:
        wb.write(str(answer))

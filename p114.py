"""
A row measuring seven units in length has red blocks with a minimum
    length of three units placed on it, such that any two red blocks
    (which are allowed to be different lengths) are separated by at
    least one black square. There are exactly seventeen ways of doing
    this.

[ | | | | | | ]     [x|x|x| | | | ]     [ |x|x|x| | | ]
[ | |x|x|x| | ]     [ | | |x|x|x| ]     [ | | | |x|x|x]
[x|x|x| |x|x|x]     [x|x|x|x| | | ]     [ |x|x|x|x| | ]
[ | |x|x|x|x| ]     [ | | |x|x|x|x]     [x|x|x|x|x| | ]
[ |x|x|x|x|x| ]     [ | |x|x|x|x|x]     [x|x|x|x|x|x| ]
[ |x|x|x|x|x|x]     [x|x|x|x|x|x|x]

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility,
    in general it is permitted to mix block sizes. For example, on a
    row measuring eight units in length you could use red (3), black (1),
    and red (4).
"""

from __future__ import print_function, division
from math import floor

from utils import binomial

"""
Brute forcing this problem for all 50 units is too inefficient.

However all in the range(2, 11) can be solved by brute force and printed.
    This yields the sequence [1, 2, 4, 7, 11, 17, 27, 44, 72, ...]

After searching on OEIS this is sequnce A005252, which has the formula:
    sum(binomial(n - 2*k, 2*k) for k in range(floor(n/4) + 1))
    where n = l + 1
"""


def solve(n=50):
    return int(sum(binomial(n - 2*k + 1, 2*k) for k in range(floor((n + 1)/4) + 1)))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p114_ans.txt', 'w') as wb:
        wb.write(str(answer))

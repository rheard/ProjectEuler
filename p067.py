"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
    a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
    as there are 2**99 altogether! If you could check one trillion (10**12) routes every second it would take over twenty
    billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

try:
    from .p018 import solve as _solve
except ImportError:
    from p018 import solve as _solve


with open('ProjectEuler/p067_triangle.txt', 'r') as rb:
    __PUZZLE = [[int(x) for x in line.strip().split(' ')] for line in rb.readlines()]


def solve(puzzle=None):
    return _solve(puzzle or __PUZZLE)


solve.__doc__ = _solve.__doc__
solve.answer = 7273


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

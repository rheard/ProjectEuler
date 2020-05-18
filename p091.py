"""
The points P (x_1, y_1) and Q (x_2, y_2) are plotted at integer co-ordinates and are joined to the origin,
    O(0,0), to form triangle OPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate
    lies between 0 and 2 inclusive; that is,

    0 <= x_1, y_1, x_2, y_2 <= 2.

Given that 0 <= x_1, y_1, x_2, y_2 <= 50, how many right triangles can be formed?
"""

from __future__ import print_function, division

import os

from fractions import Fraction

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def triangle_count(n):
    if n == 0:
        return 0

    # Triangles from a (n - 1) * (n - 1) grid + the triangles of type 1 for this size grid.
    triangle_cnt = 3 * (2 * n - 1) + triangle_count(n - 1)

    # Triangles of type 2.A that have a corner not on the top row but on the last column.
    for point in ((x, y) for x in range(1, n) for y in range(1, n)):
        slope = Fraction(point[1], point[0])
        slope_i = (n - point[0]) / slope.numerator
        if slope_i.is_integer():
            new_pt_y = point[1] - slope.denominator * slope_i
            if new_pt_y >= 0:
                triangle_cnt += 2

    # Triangles of type 2.A that have a right angle on the top row.
    for point in ((x, n) for x in range(2, n)):
        slope = Fraction(point[1], point[0])
        point = (point[0] + slope.numerator, point[1] - slope.denominator)
        while point[0] <= n and point[1] > 0:
            triangle_cnt += 2
            point = (point[0] + slope.numerator, point[1] - slope.denominator)

    return triangle_cnt


def solve(n=50):
    """
    For this problem, there appears to be 2 fundamental cases.
        All triangles that are not fundamental cases can be found from fundamental cases by rotation.


    A fundamental case will either:
        1. have it's 90 degree angle on the origin.
            In this case, there are 3 possible rotations (including not rotating at all).
        2. have it's 90 degree angle NOT on an axis. If it is not on the axis it will be located somewhere in the grid.
            We will say that for this type of triangle to be fundamental, one leg of the 90 degrees will go towards the
            origin, and the other towards the x-axis. In this case, there are 2 possible triangles
            (1 fundamental, 1 mirror).

    Also it can be observed that the triangles possible on an n * n grid will be the triangles possible on a
        (n - 1) * (n - 1) grid + all the new triangles that have a corner on the last column or highest row.
        So this problem can be solved with a recursive function.

    It is easy to test and observe that for the first type of fundamental triangle, there are n**2 possible.
        Since we are making a recursive function, we are only concerned with the possible triangles of type 1 that have
        a corner on the highest row or last column. Of these, there are 3 *(2*n - 1). 2 * n for each row and column and
        subtract 1 because there is only 1 that goes from the top of the first column to the outside of the first row.
        Then multiply by 3 for all 3 rotations.

    Triangles of type 2 have 2 subtypes. The first is with a corner on the farthest column. The second is with a corner
        on the highest row. Those with corner on the farthest column come first, and the right angle may be anywhere.
        This means all points must be tested to find some that satisfy this. For those with the right angle on the
        highest row, the 3rd corner may or may not be on the farthest right column. Also count 2 for each fundamental
        triangle found for their mirrors.
    """
    return triangle_count(n)


solve.answer = 14234


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F,
    sits in the opposite corner. By travelling on the surfaces of the room the shortest
    "straight line" distance from S to F is 10 and the path is shown on the diagram.

https://projecteuler.net/project/images/p086.gif

However, there are up to three "shortest" path candidates for any given cuboid and
    the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations,
    with integer dimensions, up to a maximum size of M by M by M, for which the
    shortest route has integer length when M = 100. This is the least value of M
    for which the number of solutions first exceeds two thousand; the number of
    solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""

from itertools import count
from math import sqrt


def count_for_M(M):
    output = 0
    l = M

    for wh in range(1, 2 * M + 1):
        if sqrt(l**2 + wh**2).is_integer():
            output += wh // 2 if wh <= l else 1 + (M - (wh + 1) // 2)

    return int(output)


def solve(distict_count=10**6):
    """
    If we call the room a cube and reduce the cube to a net, then the shortest distance is the
        hypotenuse of a triangle.

    It may be possible to use the equations from problem 75 to solve this, however it gets too
        messy too fast, my math is not reliable enough to come up with a working solution,
        and this is fast enough.

    For this, we are just going to generate all possible 'rooms' with length M until the sum
        reaches the desired value. To find the amount for a particular M,
        cycle through all w+h for all w+h in 2 * M. If there is an integer hypotenuse
        then we must find out the number of possible w+h for this M that we care about.
        If the w+h is less than l, it is easy to see we must include them all.
        If not, w must be between h and M.
    """
    running_sum = 0

    for M in count(1):
        running_sum += count_for_M(M)
        if running_sum >= distict_count:
            return M


solve.answer = 1818

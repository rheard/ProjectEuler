from __future__ import division

from math import atan2, pi

with open('ProjectEuler/p102_triangles.txt', 'r') as rb:
    __TRIANGLES = [list(map(int, line.split(','))) for line in rb.readlines()]
    __TRIANGLES = [list(zip(*[triangle[i::2] for i in range(2)])) for triangle in __TRIANGLES]


def origin_contained(triangle):
    # First, find the angle from the origin to all the points of the triangle.
    angles = [atan2(point[1], point[0]) for point in triangle]

    # Make sure our angles are 0 to 2*pi instead of -pi to pi.
    angles = [angle if angle >= 0 else angle + 2 * pi for angle in angles]

    # Rotate the triangle around the origin such that 1 point lies on the x-axis
    min_angle = min(angles)
    angles = [angle - min_angle for angle in angles]

    # Are all points above the x-axis
    # or are all points below the x-axis.
    if all(angle < pi for angle in angles) \
        or all(angle > pi or angle == 0 for angle in angles):
        return False

    # We need to rotate one more time to check for the possibility that it is possible
    #   to rotate such that all points are above the x-axis.
    min_angle = min(angle for angle in angles if angle != 0)
    angles = [angle - min_angle for angle in angles]
    angles = [angle if angle >= 0 else angle + 2 * pi for angle in angles]
    return not all(angle > pi for angle in angles if angle != 0)


def solve(triangles=None):
    """
    Here is how I'm going to approach this problem. If all points are on 1 side of the origin,
        then the origin is not contained in the triangle. To put this more formally,
        if the angle from the origin to each point (with respect to the x-axis) are all within
        180 degrees of each other, then the origin is not contained in the triangle.

    Note: In the following code, degrees are not used. Everyone knows angles ought to be
        measured in radians.
    """
    triangles = triangles or __TRIANGLES
    return sum(1 for triangle in triangles if origin_contained(triangle))


solve.answer = 228

"""
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of
    m units placed on it, such that any two red blocks (which are allowed
    to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a
    row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for
    which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711
    and F(10, 57) = 1148904, so n = 57 is the least value for which the
    fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function
    first exceeds one million.
"""

from __future__ import division

from itertools import count
from math import floor

from ProjectEuler.utils import binomial


def F(m, n):
    return int(sum(binomial(n - (m - 1)*k + 1, 2*k) for k in range(floor((n + 1)/(m + 1)) + 1)))


def solve(m=50, least_n=10**6):
    """
    Continuing from the previous problem...

    For m = 3 and a given l, we know from the previous problem the solution is
        a(n) = sum(binomial(n - 2*k, 2*k) for k in range(floor(n/4) + 1))
        where n = l + 1

    We modified this equation using n = l to give:
        a(n) = sum(binomial(n - 2*k + 1, 2*k) for k in range(floor((n + 1)/4) + 1))

    Now we need to generalize the equation for any m and n. It was fairly easy by
        testing to find
        F(m, n) = sum(binomial(n - (m - 1)*k + 1, 2*k) for k in range(floor((n + 1)/(m + 1)) + 1))
        which solves the problem.
    """
    for n in count(1):
        if F(m, n) > least_n:
            return n


solve.answer = 168

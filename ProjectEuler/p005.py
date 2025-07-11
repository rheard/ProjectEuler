"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from ProjectEuler.utils import lcm


def solve(max_n=20):
    """This is just asking "What is the LCM of all the numbers from 1 to 20?"."""
    return lcm(*range(1, max_n + 1))


solve.answer = 232792560

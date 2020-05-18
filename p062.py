"""
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3).
    In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

import os

from itertools import count

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=5):
    """
    We solve this problem in a similar way to previous problems, by creating a hashmap using a "digit hash",
        that is unique for each combination of digits, but identical for permutations of the same combination.

    We then group the cubes in the hashmap, first to 5 cubes wins.
    """
    h_table = {}

    for i in count(1):
        cube = i**3
        cube_str = str(cube)
        sorted_cube_str = "".join(sorted(cube_str))

        if sorted_cube_str not in h_table:
            h_table[sorted_cube_str] = []

        h_table[sorted_cube_str].append(i)

        if len(h_table[sorted_cube_str]) == n:
            return min(h_table[sorted_cube_str]) ** 3


solve.answer = 127035954683


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

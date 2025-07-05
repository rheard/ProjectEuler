"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
    However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
    it cannot be solved by brute force, and requires a clever method! ;o)
"""

import os

from copy import deepcopy

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

# We're going to solve this using a clever method for problem 67 later.
# First lets build the puzzle of interest for this problem.
__PUZZLE = [[int(x) for x in line.split(' ')] for line in """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split('\n')]


# This is the function we will use later.
def max_total_path(puzzle):
    # We're going to mangle this mutable argument, so lets make a copy.
    puzzle = deepcopy(puzzle)

    while len(puzzle) != 1:
        # Remove the last line
        current_line = puzzle.pop()
        last_line = puzzle[-1]

        # For each element in the new last line, find the optimal path,
        #   IF we were at that point coming from the top.
        for i in range(len(last_line)):
            last_line[i] += max(current_line[i:i + 2])

    # The only element now is a single element in a single row. This is the answer.
    return puzzle[0][0]


def solve(puzzle=None):
    """
    This puzzle doesn't require a clever solution, but a later problem does, so we must solve this efficiently.

    We do this by solving the problem in reverse:
        1. Start on the second to last row
        2. For each element in the row, add the max of the two below it.
        3. Eliminate the last row.
        4. If there is more than 1 row left, go to 1.

    The last element at the top of the puzzle after addition is the answer.
    """
    return max_total_path(puzzle or __PUZZLE)


solve.answer = 1074


if __name__ == '__main__':
    output_answer(solve)

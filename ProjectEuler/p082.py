"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column
    and finishing in any cell in the right column, and only moving up, down, and right,
    is indicated in red and bold; the sum is equal to 994.

(   131 673'234'103'18'
   '201'96''342'965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524 37  331 )

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
    a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
"""

import os

from copy import deepcopy

with open('ProjectEuler/p081_matrix.txt', 'r') as rb:
    __GRID = [[int(x) for x in line.split(',')] for line in rb.readlines()]


def solve(grid=None):
    """
    We can use a similar process to problem 81, except that we need to go back for a second pass on the column
        to determine if moving upwards would be a better choice than downwards. And we modify the solution slightly
        to seek out the right column instead of the bottom right cell.
    """
    grid = deepcopy(grid or __GRID)

    while len(grid[0]) > 1:
        # Step 1.1 Assume on the bottom row, we must go to the right
        grid[-1][-2] = [grid[-1][-2], grid[-1][-1]]

        # Step 1.2 Walk up the second to last column to determine if we should move down or to the right
        for i in reversed(range(len(grid) - 1)):
            grid[i][-2] = [grid[i][-2], min(sum(grid[i + 1][-2]), grid[i][-1])]

        # Step 2 Walk down the second to last column to determine if we should keep the current movement, or go up
        for i in range(1, len(grid)):
            grid[i][-2][1] = min(grid[i][-2][1], sum(grid[i - 1][-2]))

        # Step 3 convert second to last column to single integers and resize the grid
        for i in range(len(grid)):
            grid[i].pop()
            grid[i][-1] = sum(grid[i][-1])

    return min(x[0] for x in grid)


solve.answer = 260324

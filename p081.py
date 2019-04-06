'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
    by only moving to the right and down, is indicated in bold red and is equal to 2427.

(   131 673 234 103 18
    201 96  342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524 37  331 )

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
    a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
    by only moving right and down.
'''

from __future__ import print_function
from copy import deepcopy

with open('ProjectEuler/matrix.txt', 'r') as rb:
    _grid = [[int(x) for x in line.split(',')] for line in rb.readlines()]


def solve(grid=_grid):
    grid = deepcopy(grid)

    # Step 1 adjust the edges to be sums to the target
    for i in reversed(range(len(grid) - 1)):
        grid[i][-1] += grid[i + 1][-1]
        grid[-1][i] += grid[-1][i + 1]

    while len(grid) > 1:
        # Step 2 determine future path
        # Step 2.1 determine future path for closest to bottom left corner
        grid[-2][-2] += min(grid[-1][-2], grid[-2][-1])

        # Step 2.2 determine future path for remaining second to last column/row
        for i in reversed(range(len(grid) - 2)):
            grid[-2][i] += min(grid[-2][i + 1], grid[-1][i])
            grid[i][-2] += min(grid[i + 1][-2], grid[i][-1])

        # Step 3 resize the grid
        grid.pop()
        for x in grid:
            x.pop()

    return grid[0][0]


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p081_ans.txt', 'w') as wb:
        wb.write(str(answer))

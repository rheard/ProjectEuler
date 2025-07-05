"""
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
"""

from copy import deepcopy


with open('ProjectEuler/p081_matrix.txt', 'r') as rb:
    __GRID = [[int(x) for x in line.split(',')] for line in rb.readlines()]


def solve(grid=None):
    """
    Here is the algorithm we will use to solve this. It is inspired by the answers to problems 67 and 18, in that we
        will start by working backwards.

    1. Consider that if we get to the bottom row or the left column, our only option is to follow that row/column
        to the bottom right of the grid. Thus we can replace that row/column with the cost to travel to the
        bottom right. If we do that to the example, it would look like:

        131 673 234 103 1566
        201 96  342 965 1548
        630 803 746 422 1398
        537 699 497 121 1287
       2429 1624 892 368 331

    2. Next, we go along the row/column directly inward of this, choosing the best path possible,
        working from the inside out. This is what I mean:
            Start with 121, just inside the bottom right corner. It can either complete the puzzle by going right
                (costing 1287) or down (costing 368). Obviously we would go down, so the cost to finish the puzzle
                going through this cell is 368

            Now we can repeat that process of deciding to go down or right with all the values in the same column
                (422, 965, 103) and in the same row (497, 699, 537).

    3. Now we can eliminate the right and bottom rows.

    4. If there is only 1 value left, that is our answer. Otherwise go back to step 1.
    """
    grid = deepcopy(grid or __GRID)

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


solve.answer = 427337

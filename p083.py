'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
    by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

(  '131'    673     '234'   '103'   '18'
   '201'    '96'    '342'   965     '150'
    630     803     746     '422'   '111'
    537     699     497     '121'   956
    805     732     524     '37'    '331'   )

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
    a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
    by moving left, right, up, and down.
'''

from __future__ import print_function

with open('ProjectEuler/matrix.txt', 'r') as rb:
    _grid = [[int(x) for x in line.split(',')] for line in rb.readlines()]


def get_grid_cell(grid, dimensions):
    return grid[dimensions[0]][dimensions[1]]


def solve(grid=_grid):
    float_inf = float('inf')
    distances = [[float_inf] * len(row) for row in grid]
    distances[0][0] = grid[0][0]
    Q_0 = set([(0, 0)])
    target = (len(grid) - 1, len(grid[-1]) - 1)
    float_inf = float('inf')

    answer = None

    while Q_0:
        target_node = min(Q_0, key=lambda x: get_grid_cell(distances, x))
        min_distance = get_grid_cell(distances, target_node)
        Q_0.remove(target_node)

        move_left = (target_node[0], target_node[1] - 1)
        move_right = (target_node[0], target_node[1] + 1)
        move_up = (target_node[0] - 1, target_node[1])
        move_down = (target_node[0] + 1, target_node[1])

        if move_left[1] >= 0:
            left_distance = min_distance + get_grid_cell(grid, move_left)
            if get_grid_cell(distances, move_left) > left_distance:
                distances[move_left[0]][move_left[1]] = left_distance
                Q_0.add(move_left)

        if move_right[1] < len(grid[move_right[0]]):
            right_distance = min_distance + get_grid_cell(grid, move_right)
            if get_grid_cell(distances, move_right) > right_distance:
                distances[move_right[0]][move_right[1]] = right_distance
                Q_0.add(move_right)

        if move_up[0] >= 0:
            up_distance = min_distance + get_grid_cell(grid, move_up)
            if get_grid_cell(distances, move_up) > up_distance:
                distances[move_up[0]][move_up[1]] = up_distance
                Q_0.add(move_up)

        if move_down[0] < len(grid):
            down_distance = min_distance + get_grid_cell(grid, move_down)
            if get_grid_cell(distances, move_down) > down_distance:
                distances[move_down[0]][move_down[1]] = down_distance
                Q_0.add(move_down)

        target_dist = get_grid_cell(distances, target)
        if target_dist != float_inf:
            answer = target_dist
            break

    return answer


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p083_ans.txt', 'w') as wb:
        wb.write(str(answer))

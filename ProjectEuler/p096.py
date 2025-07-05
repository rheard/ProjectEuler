"""
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
    Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
    and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however,
    is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
    and 3 by 3 box contains each of the digits 1 to 9.
    Below is an example of a typical starting puzzle grid and its solution grid.

0 0 3	0 2 0	6 0 0           4 8 3   9 2 1	6 5 7
9 0 0   3 0 5   0 0 1           9 6 7   3 4 5   8 2 1
0 0 1   8 0 6   4 0 0           2 5 1   8 7 6   4 9 3

0 0 8	1 0 2	9 0 0           5 4 8	1 3 2	9 7 6
7 0 0   0 0 0   0 0 8           7 2 9   5 6 4   1 3 8
0 0 6   7 0 8   2 0 0           1 3 6   7 9 8   2 4 5

0 0 2	6 0 9	5 0 0           3 7 2	6 8 9	5 1 4
8 0 0   2 0 3   0 0 9           8 1 4   2 5 3   7 6 9
0 0 5   0 1 0   3 0 0           6 9 5   4 1 7   3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
    although it may be necessary to employ "guess and test" methods in order to eliminate options
    (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle;
    the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
    ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
    for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""

from copy import deepcopy
from multiprocessing import Pool


_square_defs = [[(x + row_shift, y + column_shift)
                 for row_shift in range(-1, 2)
                 for column_shift in range(-1, 2)]
                for x in range(1, 8, 3)
                for y in range(1, 8, 3)]


def works_in_unknown(unknown_i, puzzle, solution=None):
    """
    Returns all values that work for unknown with index i in the puzzle, with a possible solution.
    Puzzle should be a dictionary as formatted in solve_puzzle below.
    """
    unknown_i_location = puzzle['unknowns'][unknown_i]
    found_vals = set()
    solution = solution or []

    for column_i, column_val in enumerate(puzzle['puzzle'][unknown_i_location[0]]):
        if column_i == unknown_i_location[1]:
            continue
        elif column_i > unknown_i_location[1] and column_val is None:
            continue
        elif column_val is not None:
            found_vals.add(column_val)
        else:
            unk_index = puzzle['unknowns'].index((unknown_i_location[0], column_i))
            if len(solution) > unk_index:
                found_vals.add(solution[unk_index])

    for row_i, row in enumerate(puzzle['puzzle']):
        row_val = row[unknown_i_location[1]]
        if row_i == unknown_i_location[0]:
            continue
        elif row_i > unknown_i_location[0] and row_val is None:
            continue
        elif row_val is not None:
            found_vals.add(row_val)
        else:
            unk_index = puzzle['unknowns'].index((row_i, unknown_i_location[1]))
            if len(solution) > unk_index:
                found_vals.add(solution[unk_index])

    square_top_left = ((unknown_i_location[0] // 3) * 3, (unknown_i_location[1] // 3) * 3)
    for row_i in range(square_top_left[0], square_top_left[0] + 3):
        if row_i == unknown_i_location[0]:
            continue

        for column_i in range(square_top_left[1], square_top_left[1] + 3):
            if column_i == unknown_i_location[1]:
                continue
            puzzle_val = puzzle['puzzle'][row_i][column_i]
            if puzzle_val is None and row_i > unknown_i_location[0]:
                continue
            elif puzzle_val is not None:
                found_vals.add(puzzle_val)
            else:
                unk_index = puzzle['unknowns'].index((row_i, column_i))
                if len(solution) > unk_index:
                    found_vals.add(solution[unk_index])

    return set(range(1, 10)) - found_vals


def presolve_puzzle(puzzle):
    """
    Continually tries to solve the puzzle using logic. If a value is found for a position, then it will go back to the beginning and run again.
    """
    # If, for any unknown, there is only 1 possible value for a position then fill it with that possible value.
    for i, unk in enumerate(puzzle['unknowns']):
        possible_vals = works_in_unknown(i, puzzle)
        if len(possible_vals) == 1:
            puzzle['puzzle'][unk[0]][unk[1]] = next(iter(possible_vals))
            puzzle['unknowns'].remove(unk)
            presolve_puzzle(puzzle)
            return

    # If, for any row, there is only 1 possible position for a value, then that is where that value goes.
    for row_i, row in enumerate(puzzle['puzzle']):
        vals_to_find = set(range(1, 10)) - set(x for x in row if x)

        for val in vals_to_find:
            possible_location = None
            possible_val = None

            for column_i, puzzle_val in enumerate(row):
                if not puzzle_val and val in works_in_unknown(puzzle['unknowns'].index((row_i, column_i)), puzzle):
                    if possible_location:
                        possible_location = None
                        possible_val = None
                        break
                    else:
                        possible_location = (row_i, column_i)
                        possible_val = val

            if possible_location:
                puzzle['puzzle'][possible_location[0]][possible_location[1]] = possible_val
                puzzle['unknowns'].remove(possible_location)
                presolve_puzzle(puzzle)
                return

    # If, for any column, there is only 1 possible position for a value, then that is where that value goes.
    for column_i in range(9):
        vals_to_find = set(range(1, 10)) - set(x[column_i] for x in puzzle['puzzle'] if x[column_i])

        for val in vals_to_find:
            possible_location = None
            possible_val = None

            for row_i in range(9):
                puzzle_val = puzzle['puzzle'][row_i][column_i]
                if not puzzle_val and val in works_in_unknown(puzzle['unknowns'].index((row_i, column_i)), puzzle):
                    if possible_location:
                        possible_location = None
                        possible_val = None
                        break
                    else:
                        possible_location = (row_i, column_i)
                        possible_val = val

            if possible_location:
                puzzle['puzzle'][possible_location[0]][possible_location[1]] = possible_val
                puzzle['unknowns'].remove(possible_location)
                presolve_puzzle(puzzle)
                return

    # If, for any square, there is only 1 possible position for a value, then that is where that value goes.
    for square in _square_defs:
        vals_to_find = set(range(1, 10)) - set(puzzle['puzzle'][x[0]][x[1]] for x in square if puzzle['puzzle'][x[0]][x[1]])

        for val in vals_to_find:
            possible_location = None
            possible_val = None

            for location in square:
                puzzle_val = puzzle['puzzle'][location[0]][location[1]]

                if not puzzle_val and val in works_in_unknown(puzzle['unknowns'].index(location), puzzle):
                    if possible_location:
                        possible_location = None
                        possible_val = None
                        break
                    else:
                        possible_location = location
                        possible_val = val

            if possible_location:
                puzzle['puzzle'][possible_location[0]][possible_location[1]] = possible_val
                puzzle['unknowns'].remove(possible_location)
                presolve_puzzle(puzzle)
                return


def solve_puzzle(puzzle):
    """
    Returns a completed sudoku puzzle given puzzle.
    Puzzle should be a 2 dimensional sudoku puzzle in the format of a list of rows where each row is a list of values.
    Unknowns should be 0 or None.
    """
    puzzle = {'puzzle': deepcopy(puzzle), 'unknowns': []}
    for row_i, row in enumerate(puzzle['puzzle']):
        for column_i, column in enumerate(row):
            if column in [0, None]:
                puzzle['puzzle'][row_i][column_i] = None
                puzzle['unknowns'].append((row_i, column_i))

    presolve_puzzle(puzzle)

    if len(puzzle['unknowns']) == 0:
        return puzzle['puzzle']

    possible_solutions = [(x, ) for x in works_in_unknown(0, puzzle)]
    new_possible_solutions = []
    while possible_solutions:
        for i, possible_solution in enumerate(possible_solutions):
            if len(possible_solution) == len(puzzle['unknowns']):
                return [[column if column is not None else possible_solution[puzzle['unknowns'].index((row_i, column_i))] for column_i, column in enumerate(row)] for row_i, row in enumerate(puzzle['puzzle'])]
            new_possible_solutions += [possible_solution + (x, ) for x in works_in_unknown(len(possible_solution), puzzle, possible_solution)]

        possible_solutions = new_possible_solutions
        new_possible_solutions = []

    return None


__PUZZLES = []
with open('ProjectEuler/p096_sudoku.txt', 'r') as rb:
    this_puzzle = []
    for line in rb.readlines():
        if line[0] == 'G' and this_puzzle:
            __PUZZLES.append(this_puzzle)
            this_puzzle = []
        elif line[0] != 'G':
            this_puzzle.append([int(x) if x != '0' else None for x in line.strip()])
    __PUZZLES.append(this_puzzle)


def solve(puzzles=None):
    """
    There is some logic that can be performed to drastically increase speed.
        Any logic holes are filled with bruteforce computation.
    """
    running_sum = 0
    # I feel like multiprocessing is cheating, but it does run 3x faster (3 seconds vs 1 seconds)
    tp = Pool(8)
    answers = tp.map(solve_puzzle, puzzles or __PUZZLES)
    tp.close()
    tp.join()

    for answer in answers:
        running_sum += int(answer[0][0] * 10**2 + answer[0][1] * 10 + answer[0][2])

    return running_sum


solve.answer = 24702

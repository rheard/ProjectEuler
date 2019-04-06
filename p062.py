'''
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3).
    In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from __future__ import print_function
from itertools import count


def solve(n=5):
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


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p062_ans.txt', 'w') as wb:
        wb.write(str(answer))

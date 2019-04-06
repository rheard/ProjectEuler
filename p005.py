'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from __future__ import print_function
from lib import lcm


def solve(max_n=20):
    return lcm(*range(1, max_n + 1))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p005_ans.txt', 'w') as wb:
        wb.write(str(answer))

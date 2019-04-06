'''
Pentagonal numbers are generated by the formula, P_n=n(3n-1)/2.
    The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_4 + P_7 = 22 + 70 = 92 = P_8.
    However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_j and P_k,
    for which their sum and difference are pentagonal and D = |P_k - P_j| is minimised;
    what is the value of D?
'''

from __future__ import print_function
from itertools import count
from math import sqrt


def is_pentagonal_number(n):
    return (sqrt(24 * n + 1) + 1) / 6 % 1 == 0


def pentagonal_number(n):
    return int(n * (3 * n - 1) / 2)


def solve():
    for i in count(3):
        this_num = pentagonal_number(i)

        for j in range(i - 1, 1, -1):
            prev_num = pentagonal_number(j)
            difference = this_num - prev_num

            if is_pentagonal_number(difference) and is_pentagonal_number(this_num + prev_num):
                return difference


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p044_ans.txt', 'w') as wb:
        wb.write(str(answer))

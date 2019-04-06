'''
Let p(n) represent the number of different ways in which n coins can be separated into piles.
    For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
'''

from __future__ import print_function
from itertools import count
from p076 import p


def solve(multiple=10**6):
    for n in count(1):
        if p(n) % multiple == 0:
            return n


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p078_ans.txt', 'w') as wb:
        wb.write(str(answer))

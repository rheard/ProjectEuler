'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''

from __future__ import print_function
from sympy import prime


def solve(n=10001):
    return prime(n)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p007_ans.txt', 'w') as wb:
        wb.write(str(answer))

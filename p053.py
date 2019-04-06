'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, ^5C_3 = 10.

In general,

^nC_r =
n!
/
r! * (n-r)!
where r <= n, n! = n * (n-1) * ... * 3 * 2 * 1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: ^23C_10 = 1144066.

How many, not necessarily distinct, values of  ^nC_r, for 1 <= n <= 100, are greater than one-million?
'''

from __future__ import print_function
from math import factorial


def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def solve():
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if C(n, r) > 1000000:
                count += 1

    return count


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p053_ans.txt', 'w') as wb:
        wb.write(str(answer))

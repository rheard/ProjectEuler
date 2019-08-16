'''
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n-1) + F_(n-2), where F_1 = 1 and F_2 = 1.
It turns out that F_541, which contains 113 digits, is the first
    Fibonacci number for which the last nine digits are 1-9 pandigital
    (contain all the digits 1 to 9, but not necessarily in order).
    And F_2749, which contains 575 digits, is the first Fibonacci number
    for which the first nine digits are 1-9 pandigital.

Given that F_k is the first Fibonacci number for which the first nine digits
    AND the last nine digits are 1-9 pandigital, find k.
'''

from ProjectEuler.lib import fib_generator
from math import log10


def solve():
    pandigital_def = set(str(x) for x in range(1, 10))
    gener = enumerate(fib_generator())

    for n, fib in gener:
        if n >= 2749 - 1:
            break

    for n, fib in gener:
        if set(str(fib % 10**9)) != pandigital_def:
            continue

        if set(str(fib)[:9]) != pandigital_def:
            continue

        return n + 1


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p104_ans.txt', 'w') as wb:
        wb.write(str(answer))

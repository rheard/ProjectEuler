'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from __future__ import print_function
from sympy import sieve


def solve(n=2 * 10**6):
    return sum(sieve.primerange(2, n))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p010_ans.txt', 'w') as wb:
        wb.write(str(answer))

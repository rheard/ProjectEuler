'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
'''

from __future__ import print_function
from sympy import sieve

'''
The number of reduced proper fractions for d is the number of numbers less than d and relatively prime to d.

This is phi(d).
'''


def solve(max_d=10**6):
    # Build a phi_sieve, so we only have to calculate 1 - 1/p once. Then divide all multiples of p by 1 - 1/p.
    phi_sieve = [d for d in range(2, max_d + 1)]

    for p in sieve.primerange(2, max_d):
        partial_totient = 1 - 1.0 / p

        for multiple in range(p, max_d + 1, p):
            phi_sieve[multiple - 2] *= partial_totient

    return int(sum(phi_sieve))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p072_ans.txt', 'w') as wb:
        wb.write(str(answer))

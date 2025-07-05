"""
Euler's Totient function, phi(n),
    is used to determine the number of numbers less than n which are relatively prime to n.
    For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.

n   Relatively Prime    phi(n)  n/phi(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5
It can be seen that n=6 produces a maximum n/phi(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
"""

import os

from itertools import count

from sympy import prime


def solve(max_n=10**6):
    """
    phi(n) = n * prod(1 - 1/p for p in primefactors(n))
    n / phi(n) = 1 / prod(1 - 1/p for p in primefactors(n))

    The maximum value will occur when we minimize the product.
    This will occur with the most product operations,
        since each multiplication is less than 1, each multiplication brings the value down.

    In order to minize the product, we need the most prime factors. So the n with the most
        prime factors will work.
    """
    n = 1

    for i in count(1):
        prime_i = prime(i)

        new_n = n * prime_i

        if new_n > max_n:
            return n
        else:
            n = new_n


solve.answer = 510510

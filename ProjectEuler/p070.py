"""
Euler's Totient function, phi(n), is used to determine the number of positive numbers
    less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7,
    and 8, are all less than nine and relatively prime to nine, phi(9)=6.

The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
"""

import os

from multiprocessing import Pool
from itertools import repeat
from math import sqrt

from sympy import prevprime, sieve


def find_permutation_val_for_prime(prime, max_n):
    start_prime = prevprime(float(max_n) / prime)

    while start_prime != prime:
        phi_val = (start_prime - 1) * (prime - 1)
        n = start_prime * prime

        if sorted(str(n)) == sorted(str(phi_val)):
            return n, float(n) / phi_val

        start_prime = prevprime(start_prime)

    return None


def find_permutation_val_for_prime_wrapper(args):
    return find_permutation_val_for_prime(*args)


def solve(max_n=10**7):
    """
    To minimize n/phi(n), we want to maximize phi(n). By looking at values of phi(n), an interesting property is noted
        about the minimums.

        They consist of two primes, and further, the smaller prime is the larger prime of the previous minimum.

        So, we only really need to iterate over the pairs of primes.

    We can use the fact that n = start_prime * prime to compute phi quickly
    phi(n) = n * prod(1 - 1/p for p in primefactors(n))
    phi(n) = n * (1 - 1/start_prime) * (1 - 1/prime)
    phi(n) = start_prime * prime * (1 - 1/start_prime) * (1 - 1/prime)
    phi(n) = (start_prime - 1) * (prime - 1)
    """
    sqrt_max_n = sqrt(max_n)
    this_prime = prevprime(sqrt_max_n)

    tp = Pool(8)

    phi_info = tp.map(find_permutation_val_for_prime_wrapper,
                      zip(reversed(list(sieve.primerange(2, this_prime))), repeat(max_n)))

    tp.close()
    return min(phi_info, key=lambda x: x[1] if x else float('inf'))[0]


solve.answer = 8319823

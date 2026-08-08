"""
Let totient be Euler's totient function, i.e. for a natural number n, totient(n) is the number of k, 1 <= k <= n,
    for which gcd(k,n) = 1.

By iterating totient, each positive integer generates a decreasing chain of numbers ending in 1.
    E.g. if we start with 5 the sequence 5,4,2,1 is generated.
Here is a listing of all chains with length 4:

5,4,2,1
7,6,2,1
8,4,2,1
9,6,2,1
10,4,2,1
12,4,2,1
14,6,2,1
18,6,2,1

Only two of these chains start with a prime, their sum is 12.

What is the sum of all primes less than 40000000 which generate a chain of length 25?
"""

import numpy as np

from sympy import sieve


def follow_chain(chain_counts, totients, i):
    """
    Follow a chain through and return the count found.
        Provide the chain_count cache, the totients, and the target number.
    """
    this_chain_count = chain_counts[i - 1]
    if this_chain_count:
        return this_chain_count

    t = totients[i - 2]
    this_chain_count = follow_chain(chain_counts, totients, t) + 1
    chain_counts[i - 1] = this_chain_count
    return this_chain_count


def solve(n=40000000, k=25):
    """
    My first thought was to use the sieve to go over all the primes and use sympy's totient function to try to
        somewhat brute force it.

    Then I notice that sympy's sieve has a `totientrange` method!
        "Surely computing all totients in the range can't be faster than the directed search with the totient method"
        I thought.
        Turns out it is. How convenient.
    """
    totients = list(sieve.totientrange(2, n))

    chain_count = np.zeros(n - 1)
    chain_count[0] = 1

    return sum(
        p
        for p in sieve.primerange(2, n)
        if follow_chain(chain_count, totients, p) == k
    )


solve.answer = 1677366278943

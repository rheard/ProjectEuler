"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
    In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

from itertools import count
from math import ceil, sqrt

from sympy import sieve


def solve(max_n=5 * 10**7):
    """
    We are just going to iterate over all combinations of squares, cubes and fourth powers that sum to less than
        50 million, and keep track of all the sums we generate.
    """
    numbers_of_interest = set()
    sieve.extend(int(ceil(sqrt(max_n))))

    for i in count(1):
        i_fr = sieve[i]**4

        if i_fr > max_n:
            break

        for j in count(1):
            j_cu = sieve[j]**3
            i_fr_j_cu = i_fr + j_cu

            if i_fr_j_cu > max_n:
                break

            for k in count(1):
                k_sq = sieve[k]**2
                i_fr_j_cu_k_sq = i_fr_j_cu + k_sq

                if i_fr_j_cu_k_sq > max_n:
                    break

                numbers_of_interest.add(i_fr_j_cu_k_sq)
    return len(numbers_of_interest)


solve.answer = 1097343

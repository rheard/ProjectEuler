"""
The smallest positive integer n for which the numbers n**2 + 1, n**2 + 3, n**2 + 7, n**2 + 9,
    n**2 + 13, and n**2 + 27 are consecutive primes is 10. The sum of all such
    integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""

import os

from multiprocessing import Pool
from itertools import chain

from sympy import nextprime, isprime

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def is_of_interest(n_range):
    addition_ordering = [3, 7, 9, 13, 27]
    ret = []
    for n in n_range:
        if n % 3 == 0:
            continue

        p_base = n**2
        if p_base % 3 != 1 or p_base % 7 != 2:
            continue

        p_1 = p_base + 1
        if not isprime(p_1):
            continue

        p_i = p_1
        for addition in addition_ordering:
            p_i = nextprime(p_i)

            if p_i - addition != p_base:
                break
        else:
            ret.append(n)
    return ret


def solve(max_n=150 * 10**6, process_count=8):
    """
    After brute forcing the for n < 10**7, we find the sequence:
        10, 315410, 927070, 2525870, 8146100, ...

    We know this is a subset of A057095, since that sequence is for sequential
        primes with the forms n**2 + 1, n**2 + 3, n**2 + 7, n**2 + 9 and n**2 + 13.

    It can also be noted that for the ones found, they are all divisible by 10. Combine this
        fact with multiprocessing and the true answer can be found in just over 3 minutes.

    Now that we have all the ones we are interested in, we just need to optimize the algorithm.
        There appears to be no decernable pattern in the prime factoring of the answers,
            beyond the fact they are divisible by 10.
        Taking each answer mod i for i in range(2, 10), we see that the only pattern is
            that answer mod 2 and answer mod 5 are both 0, refelcting the divisibility by 10
            rule, so nothing...
        Taking each answer**2 mod i for i in range(2, 10) reveals some patterns. First is that
            answer**2 mod 4 is 0, reflecting the fact that answer mod 2 is 0, so nothing new here.

            Though we can see these always hold:
            answer**2 mod 3 == 1
            answer**2 mod 7 == 2

            A similar process can be used to discover this fact:
            answer mod 3 != 0.

        These 3 facts combined with multiprocessing can tackle this problem in under 40 seconds.
    """
    total_range = range(10, max_n, 10)

    with Pool(process_count) as p:
        results = [x for x in p.map(is_of_interest, [total_range[i::process_count] for i in range(process_count)]) if x]

    return sum(chain(*results))


solve.answer = 676333270


if __name__ == '__main__':
    output_answer(solve)

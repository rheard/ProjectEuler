"""
Consider the fraction, n/d, where n and d are positive integers.
    If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size,
    we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions
    for d <= 12,000?
"""

import os

from math import ceil
from multiprocessing import Pool

from ProjectEuler.utils import gcd


def fraction_count_in_target_range_for_d(d):
    fraction_count = 0

    for n in range(int(ceil((d + 1.0) / 3)), int(ceil(float(d) / 2))):
        if gcd(n, d) != 1:
            continue

        fraction_count += 1

    return fraction_count


def solve(max_d=12000):
    """No strategy here. Bruteforce."""
    tp = Pool(8)
    fraction_counts = tp.map(fraction_count_in_target_range_for_d, range(4, max_d + 1))
    tp.close()

    return sum(fraction_counts)


solve.answer = 7295372

"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import os

from decimal import Decimal, getcontext
from math import ceil, floor


def repeating_pattern_len(a, b):
    # The upper limit for a repetend is (b - 1). Ensure there is
    #   enough precision to get at least 2 cycles.
    desired_precision = int(ceil(2.5 * (b - 1)))
    if getcontext().prec < desired_precision:
        getcontext().prec = desired_precision

    dec_val = Decimal(a) / Decimal(b)
    str_dec_val = str(dec_val)

    if len(str_dec_val) - 1 < getcontext().prec:
        return 0

    str_dec_val = str_dec_val.split('.')[-1]
    search_space = str_dec_val[int(floor(0.25 * (b - 1))):-1] + 'x'

    for possible_len in range(1, b):
        search_pattern = search_space[-possible_len - 1:-1]
        working_len = True
        for test_string in (search_space[i * -possible_len - 1:(i - 1) * -possible_len - 1]
                            for i in range(len(search_space) // possible_len)):
            if not test_string:
                continue

            if test_string != search_pattern:
                working_len = False
                break

        if working_len:
            return possible_len

    return -1


def solve():
    """
    Nothing super fancy here, simply computing 1/d to a very long number of digits
        and looking for the longest possible repeating pattern. Then repeat that process for all numbers in our range.
    """
    longest_d = 0
    longest_len = 0
    for d in range(7, 1000):
        repetend_len = repeating_pattern_len(1, d)
        if repetend_len > longest_len:
            longest_len = repetend_len
            longest_d = d

    return longest_d


solve.answer = 983

"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import os

from itertools import count

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """No strategy here. Bruteforce."""
    powerful_digit_count = 0

    for n in range(1, 10):
        for e in count(1):
            str_len = len(str(n ** e))
            if str_len != e:
                break

            powerful_digit_count += 1

    return powerful_digit_count


solve.answer = 49


if __name__ == '__main__':
    output_answer(solve)

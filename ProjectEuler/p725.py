"""
A number where one digit is the sum of the other digits is called a digit sum number or DS-number for short.
    For example, 352, 3003 and 32812 are DS-numbers.

We define S(n) to be the sum of all DS-numbers of n digits or less.

You are given S(3) = 63270 and S(7) = 85499991450.

Find S(2020). Give your answer modulo 10**16.
"""

from collections import defaultdict
from itertools import permutations
from math import factorial
from pprint import pprint
from time import time

from ProjectEuler.utils import prod


def partitions(n, max_value=None):
    if max_value is None:
        max_value = n
    if n == 0:
        return [[]]
    result = []
    for i in range(1, min(n, max_value) + 1):
        for p in partitions(n - i, i):
            result.append([i] + p)
    return result

counts = defaultdict(lambda: defaultdict(int))
def build_number(digits: list) -> int:
    n = len(digits)
    for pos, d in enumerate(reversed(digits)):
        counts[pos][d] += 1
    return sum(d * 10**(n - i - 1) for i, d in enumerate(digits))


def S(n=2020):
    total = 0
    for d_sum in range(1, 10):
        print(f"Digit {d_sum}")
        for digits in partitions(d_sum):
            raw_digit_count = len(digits) + 1
            if raw_digit_count > n:  # This partitioning with the digit itself would be more than n digits
                continue  # TODO: This will never happen for n=2020

            zeroes = n - raw_digit_count
            digits.append(d_sum)
            digits.extend([0] * zeroes)

            assert len(digits) == n

            for p in set(permutations(digits, n)):
                total += build_number(p)

    return total


def new_S(n=2020):
    total = 0
    for d_sum in range(1, 10):
        print(f"Digit {d_sum}")
        for digits in partitions(d_sum):
            raw_digit_count = len(digits) + 1
            if raw_digit_count > n:  # This partitioning with the digit itself would be more than n digits
                continue  # TODO: This will never happen for n=2020

            digits = {
                d: digits.count(d) for d in digits
            }

            if d_sum in digits:
                digits[d_sum] += 1
            else:
                digits[d_sum] = 1

            for pos in range(1, n + 1):
                for d in digits:
                    digit_count = 1
                    # TODO: Somehow calculate how many times each digit would appear at each location
                    total += 10**pos * d * digit_count

    return total


def solve(n=2020):
    """
    My first idea is quite straight forward (I think): partition all of the numbers from 1 to 9,
        then count all the unique ways to permute that permutation with the digit itself added in.

    This works however it starts to become apparent around S(12) that this is far too slow.
        I tried using `more_itertools.distinct_permutations`, however it doesn't seem that much faster...
        It certainly won't get us to S(2020).

    """
    return S(n) % 10**16


# solve.answer = 233168

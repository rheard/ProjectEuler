"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
    which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
    By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
    However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that
    cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """The solution for this problem is inspired by problem 21."""
    def is_abundant(d, n):
        return d[n] > n

    limit = 28123
    d = [0] * limit

    for num in range(1, limit):
        for multiple in range(2 * num, limit, num):
            d[multiple] += num

    abundant_numbers = []
    for i in range(1, limit):
        if is_abundant(d, i):
            abundant_numbers.append(i)
    first_abundant_number = abundant_numbers[0]
    abundant_numbers = set(abundant_numbers)

    running_sum = 0
    for i in range(1, limit):
        can_be_written = False

        for abundant_num in abundant_numbers:
            if abundant_num > i - first_abundant_number:
                break

            if i - abundant_num in abundant_numbers:
                can_be_written = True
                break

        if not can_be_written:
            running_sum += i

    return running_sum


solve.answer = 4179871


if __name__ == '__main__':
    output_answer(solve)

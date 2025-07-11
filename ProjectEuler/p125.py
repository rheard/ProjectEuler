"""
The palindromic number 595 is interesting because it can be written
    as the sum of consecutive squares:

    6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2.

There are exactly eleven palindromes below one-thousand that can be
    written as consecutive square sums, and the sum of these palindromes
    is 4164. Note that 1 = 02 + 12 has not been included as this problem
    is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic
    and can be written as the sum of consecutive squares.
"""

from itertools import count


def consecutive_square_sums(max_n=10**8):
    for start_number in count(1):
        start_number_sq = start_number**2

        if start_number_sq > max_n:
            break

        running_sum = start_number_sq

        for end_number in count(start_number + 1):
            running_sum += end_number**2

            if running_sum > max_n:
                break

            yield running_sum


def palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]


def solve(max_n=10**8):
    """No strategy here. Bruteforce."""
    return sum(set(x for x in consecutive_square_sums(max_n) if palindrome(x)))


solve.answer = 2906969179

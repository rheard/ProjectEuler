"""
A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from __future__ import print_function

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def is_palindromic(n):
    """Is n a palindrome?"""
    n = str(n)
    return n == n[::-1]


def solve(n=3):
    """
    We start with (i, j) being the 2 largest 3 digit numbers possible ((999, 999)), then work down j to the lowest
        3 digit number (100) until we find a palindrome. If it is larger than the largest palindrome found yet, save it.

    Note that we can move on to the next i once we find 1 palindrome, since we're starting with the largest number
        for it, the first palindrome found will be the largest for that number.
    """
    largest_ans = 0
    min_number = 10**(n - 1) - 1
    for i in range(10**n - 1, min_number, -1):
        for j in range(i, min_number, -1):
            target_num = i * j
            if is_palindromic(target_num):
                if target_num > largest_ans:
                    largest_ans = target_num

                # This is the largest palindrome we can make with this i, so move on to another
                break

    return largest_ans


solve.answer = 906609


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

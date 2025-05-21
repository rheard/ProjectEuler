"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
    0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d_2*d_3*d_4=406 is divisible by 2
d_3*d_4*d_5=063 is divisible by 3
d_4*d_5*d_6=635 is divisible by 5
d_5*d_6*d_7=357 is divisible by 7
d_6*d_7*d_8=572 is divisible by 11
d_7*d_8*d_9=728 is divisible by 13
d_8*d_9*d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import os
import string

from collections import deque

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def numbers_of_interest():
    primes = [2, 3, 5, 7, 11, 13, 17]
    digits = set(string.digits)
    possibilities = deque()
    # Start by taking all 3 digit numbers with unique digits that are divisible by 2,
    #   and add the number with a missing digit prepended to the list of possibilities.
    for possibility in range(102, 988, 2):
        possibility_str = str(possibility)
        if len(set(possibility_str)) != 3:
            # Must have 3 unique digits, for pandigital property
            continue

        for new_char in (digits - set(possibility_str)):
            possibilities.append(new_char + possibility_str)

    # Now go through the possibilities, and try to append digits while satisfying the properties.
    while possibilities:
        possibility = possibilities.popleft()
        prime = primes[len(possibility) - 3]
        for new_char in (digits - set(possibility)):
            i = int(possibility[-2:] + new_char)

            if i % prime == 0:
                found_possibility = possibility + new_char

                if len(found_possibility) == 10:
                    yield int(found_possibility)  # We found a number that satisfies the conditions!
                else:
                    possibilities.append(found_possibility)


def solve():
    """
    We will solve this problem in reverse.

    Start with all the 3 digit pandigital numbers divisible by 2.

    For each of those numbers, try to add on a digit so the number remains pandigital,
        and the last 3 digits are divisible by the next prime.
    """
    return sum(numbers_of_interest())


solve.answer = 16695334890


if __name__ == '__main__':
    output_answer(solve)

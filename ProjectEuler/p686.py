"""
2**7 = 128 is the first power of two whose leading digits are "12".
    The next power of two whose leading digits are "12" is 2**80.

Define p(L, n) to be the nth-smallest value of j such that the base 10 representation of
    2**j begins with the digits of L.
        So p(12, 1) = 7 and p(12, 2) = 80.

You are also given that p(123, 45) = 12710.

Find p(123, 678910).
"""

import math

from itertools import count


def first_x_digits(base, exp, x):
    """Provides faster compute of first few digits than converting to string."""
    # To start, we rely on the identity log(base ** exp) = exp * log(base) to avoid computing base ** exp directly.
    #   log10 because we interested in base 10 digits
    y = exp * math.log10(base)

    # Now get the fractional part of the number
    #   This can be thought of as simply moving the decimal of the base-10 number
    #       123456 => 0.123456
    f = y - math.floor(y)

    # Now move the number back by the number of digits needed, ie:
    #   0.123456 => 123.456
    f += x

    # Now undo the log from above and compute the actual number
    target_number = 10**(f - 1)
    return int(target_number)  # Only the integer part because thats the digits we're interested in


def p(L: int, i):
    """Method p as defined in the problem. Very dumb"""
    L_len = len(str(L))
    for exp in count(1):
        if first_x_digits(2, exp, L_len) == L:
            # Found an exponent that starts with L, so subtract from i and return if we've found the target
            i -= 1
            if i == 0:
                return exp


def solve(L=123, n=678910):
    """
    Quite a simple solution.

    Started by creating an efficient method to compute the first X digits of a number.

    That was fast enough to solve the problem.
    """
    return p(L, n)


solve.answer = 193060223

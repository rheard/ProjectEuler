"""
Working from left-to-right if no digit is exceeded by the digit to its
    left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called
    a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
    a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
    there are only 12951 numbers below one-million that are not bouncy and
    only 277032 non-bouncy numbers below 10**10.

How many numbers below a googol (10**100) are not bouncy?
"""

import os

from math import factorial

from ProjectEuler.utils import prod


def nonbouncy(n):
    """Returns the number of non-bouncy numbers with a digit length of n"""
    return ((18 + n) / factorial(9)) * prod(i for i in range(n + 1, n + 9)) - 10


def nonbouncy_count(n):
    """Returns the number of non-bouncy numbers with a digit length less than or equal to n"""
    return int(sum(nonbouncy(i) for i in range(1, n + 1)))


def solve(n=100):
    """
    Approaching this problem, I figured that the number of non-bouncy numbers must
        be represented by a logical formula. After much testing and experimentation
        of generating all the non-bouncy numbers of for a length, the following facts
        were found with OEIS:

     * The number of increasing numbers a(n) of length n is found by the following formula:
        binomial(n + 8, 8)
        given by A000581

     * The number of decreasing numbers a(n) of length n is found by the following formula:
        binomial(n + 9, 9) - 1
        given by A035927 which is A000582 - 1.

    This includes the duplicates however, which the number of duplicates of length n is
        9, 1 for each of the repdigits. ie, 11...1, 2...2, 3...3, 4...4, 5...5.

    Thus, for numbers of length n, the number of increasing and decreasing numbers (non-bouncy)
        is given by:
    binomial(n + 8, 8) + binomial(n + 9, 9) - 1 - 9

    Now start simplification...
    factorial(n + 8)/(factorial(n)*factorial(8)) + factorial(n + 9)/(factorial(n)*factorial(9)) - 10
    (factorial(9)*factorial(n + 8) + factorial(8)*factorial(n + 9))/(factorial(n)*factorial(9)*factorial(8)) - 10
    (9 * factorial(n + 8) + factorial(n + 9))/(factorial(n)*factorial(9)) - 10
    (9 * product(i for i in range(n + 1, n + 9)) + product(i for i in range(n + 1, n + 10)))/factorial(9) - 10
    product(i for i in range(n + 1, n + 9)) * (9 + (n + 9))/factorial(9) - 10
    (18 + n)/factorial(9) * product(i for i in range(n + 1, n + 9)) - 10
    """
    return nonbouncy_count(n)


solve.answer = 51161058134250

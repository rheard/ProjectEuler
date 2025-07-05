"""
A positive fraction whose numerator is less than its denominator is
    called a proper fraction. For any denominator, d, there will be
    d-1 proper fractions; for example, with d = 12:

1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12, 8/12, 9/12, 10/12, 11/12.

We shall call a fraction that cannot be cancelled down a resilient
    fraction. Furthermore we shall define the resilience of a denominator,
    R(d), to be the ratio of its proper fractions that are resilient;
    for example, R(12) = 4/11.

In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

import os

from itertools import count
from fractions import Fraction

from sympy import totient, nextprime


def R(d):
    return Fraction(totient(d), d - 1)


def solve(target=Fraction(15499, 94744)):
    """
    To start with, we are given that there are d - 1 proper fractions,
        which is the denominator of our ratio.

    The numerator should obviously be the number of numbers less than d
        that are relatively prime to d. This is given by Euler's totient
        function.

    So we are wanting to minimize totient(d)/d - 1. Recall that:
        totient(d) = d * product(1 - 1/p for p in primefactors(d))

    Thus we want to form a d that consists of many prime numbers. To start
        with we will find a d by multiplying primes together until we get a
        R(d) value that is below our target. Since we are multiplying primes
        as we go along, they are all relatively prime to each other, so we can
        also keep track of the totient as we go along by multiplying the previous
        totient by p * (1 - 1/p) each time (which is just p - 1).

    Once we get past our target ratio, we know that somewhere between this d
        and the last d was the number of interest. So we'll go back to the last d,
        and count up to multiples to the current d. This is the algorithm used
        to solve this problem.
    """
    # Step 1, exceed the ratio using primes to the first power only
    #   Pre-calculated for 2. Our loop can't start at None, because 
    #   that would give a fraction with a denominator of 0.
    running_totient = 1
    running_n = 2
    prime = 2
    while Fraction(running_totient, running_n - 1) >= target:
        prime = nextprime(prime)
        running_totient *= prime - 1
        running_n *= prime

    # Step 2, walk back the last prime
    running_n //= prime
    # Walk the multiples of this number to find when we break our ratio.
    for multiple in count(2*running_n, running_n):
        this_ratio = R(multiple)
        if this_ratio < target:
            break

    return multiple


solve.answer = 892371480

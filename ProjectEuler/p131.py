"""
There are some prime values, p, for which there exists a positive integer,
    n, such that the expression n**3 + p * n**2 is a perfect cube.

For example, when p = 19, 8**3 + 19 * 8**2 = 12**3.

What is perhaps most surprising is that for each prime with this property
    the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

import os

from itertools import count

from sympy import isprime


def cuban_primes():
    for primitive in count(1):
        p = 3*primitive**2 + 3*primitive + 1
        if isprime(p):
            yield p


def solve(max_p=10**6):
    """
    To narrow this problem down, it was first brute forced for primes under 1000
        and then 2500 to find some patterns. The question asks to find solutions to
        n**3 + p*n**2 = i**3

        for some prime p under 10**6.

    The possible values for p are known as cuban primes (A002407), which are numbers of the form
        (x**3 - y**3) / (x - y). They are also the centered hexagonal numbers that are prime.

    It is seen that the possible n values are n values where 3*n**2 + 3*n + 1 is prime (A111251).
        This can be restated as n values where (n+1)**3 - n**3 is prime, ie the difference of 2
        consecutive cubes is prime.
        Also all possible values for n are themselves cubes.

    The most interesting property yet. For every integer k, if 3*k**2 + 3*k + 1 is prime, that prime
        is our p and our n is k**3. Using this, we can rewrite the problem equation as:
        k**9 + k**6 * (3*k**2 + 3*k + 1) = i**3
        k**6 * (k**3 + 3*k**2 + 3*k + 1) = i**3

    Whats more, every single k put into this will produce a cube. So all that matters is that
        3*k**2 + 3*k + 1 is prime for an integer k. Nothing else needs to be checked.

    In other words, the answer to this problem is just how many cuban primes are below 10**6.
    """
    ret = 0
    for cuban_prime in cuban_primes():
        if cuban_prime >= max_p:
            break
        ret += 1
    return ret


solve.answer = 173

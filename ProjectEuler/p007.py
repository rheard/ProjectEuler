"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

from sympy import prime


def solve(n=10001):
    """No strategy here. Bruteforce."""
    return prime(n)


solve.answer = 104743

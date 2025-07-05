"""
Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be
    the remainder when (p_n−1)**n + (p_n+1)**n is divided by p_n**2.

For example, when n = 3, p_3 = 5, and 4**3 + 6**3 = 280 = 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10.
"""

from itertools import count

from sympy import sieve


def prime_square_remainder(n):
    p_n = sieve[n]
    return n * p_n * 2


def solve(n=10**10):
    """
    This is very similar to problem 120, except that we cannot use the same
        universal equation for all n.

    Instead, we can recall from problem 120 that the problem is
        r_max = max(((a-1)**n + (a+1)**n) % a**2 for n in count(1))

        We must find the maximum remainder of ((a-1)**n + (a+1)**n) / a**2
        for all possible n.

        One of the equations given for this is
        r_max = a**2 - 2*a if a is even, otherwise a**2 - a.

    We can derive a similar if/then statement to solve this problem. By printing
        out the remainders for n in range(1, 25), a pattern starts to emerge.

        Easy enough, if n is even, then r is 2.
        If n is 3, p_n is 5, and the remainder is 5
        For all other cases, (n is odd and greater than 5):
            r = 2 * n * p_n

    Now that we know how to get the remainder quickly without doing multiple
        exponentiation and division, we only need to try each n and break
        when we reach our target. Even better, we know we don't have to try
        even n's and we can start with n = 5 since n = 3 is far too low.
    """
    if n < 0:
        return 1
    elif n < 2:
        return 2
    elif n < 5:
        return 3

    for i in count(5, 2):
        if prime_square_remainder(i) > n:
            return i


solve.answer = 21035

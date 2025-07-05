"""
Euler discovered the remarkable quadratic formula:

n**2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
However, when n=40, 40**2 + 40 + 41 = 40*(40+1) + 41 is divisible by 41,
    and certainly when n=41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 - 79*n + 1601 was discovered, which produces 80 primes for the
    consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n**2 + a*n + b, where |a|<1000 and |b|<=1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces
    the maximum number of primes for consecutive values of n, starting with n=0.
"""

from sympy import sieve


def consecutive_prime_count(a, b, _primes):
    n = 0
    while True:
        if n**2 + a * n + b not in _primes:
            return n

        n += 1


def solve():
    """
    Nothing fancy here except caching of the primes in a set.

    If the numbers in this problem were to change, this wouldn't work.
    """
    highest_prime_count = 0
    highest_a = 0
    highest_b = 0

    primes = set(sieve.primerange(2, 5 * 10**6))

    for a in range(-999, 1000, 1):
        for b in range(-1000, 1001, 1):
            prime_count = consecutive_prime_count(a, b, primes)

            if prime_count > highest_prime_count:
                highest_prime_count = prime_count
                highest_a = a
                highest_b = b

    return highest_a * highest_b


solve.answer = -59231

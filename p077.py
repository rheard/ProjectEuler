"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

import os

from itertools import count

from sympy import primefactors

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

_prime_sums = {
    0: 1,  # This doesn't make sense to me, but is needed for the recursion to work... It must be true?
    1: 0,  # 1 is not a prime. There is no way to add primes to sum to 1.
}


def prime_sums(n):
    if n not in _prime_sums:
        _prime_sums[n] = int((1 / n) * sum(sum(primefactors(k)) * prime_sums(n - k) for k in range(1, n + 1)))
    return _prime_sums[n]


def solve(max_ways=5000):
    """
    Solving for the first 10 numbers manually and searching on OEIS for this sequence, we find A000607.

    There are not really any good formulas, but one given is (1/n) * Sum(k=1..n) A008472(k) * a(n-k)
        Where A008472(k) is the sum of the distinct prime factors of k.
    """
    for i in count(2):
        if prime_sums(i) > max_ways:
            return i


solve.answer = 71


if __name__ == '__main__':
    output_answer(solve)

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import os
import string

from sympy import sieve

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """
    First we can use the divisibility rule for 3 to reduce the search space.

    The rule states that if the sum of the digits is divisible by 3, then the number is divisible by 3.

    sum(range(1, 10)) == 45

    so any 9 digit pandigital number is divisible by 3, so there are no pandigital primes of length 9.
        We can repeat this process:

    sum(range(1, 9)) == 36, divisible by 3
    sum(range(1, 8)) == 28, NOT divisible by 3
    sum(range(1, 7)) == 21, divisible by 3

    So there can be a 7 digit pandigital number not divisible by 3. That is where the largest prime should lie.
    """
    seven_digits = set(string.digits[1:8])
    for prime_num in reversed(list(sieve.primerange(10**6, 10**7))):
        if seven_digits == set(str(prime_num)):
            return prime_num


solve.answer = 7652413


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

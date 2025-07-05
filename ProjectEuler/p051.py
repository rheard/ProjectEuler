"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
    13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
    this 5-digit number is the first example having seven primes among the ten generated numbers,
    yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.

    Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
    with the same digit, is part of an eight prime value family.
"""

from collections import defaultdict
from itertools import count

from sympy import sieve


def generate_digit_permutations(n, c):
    yield n

    for i, digit in enumerate(n):
        if digit == c:
            left_val = n[:i] + '*'
            right_vals = generate_digit_permutations(n[i + 1:], c)
            for right_val in right_vals:
                yield left_val + right_val


def generate_permutations(n):
    for digit in sorted(set(n)):
        for permutation in generate_digit_permutations(n, digit):
            yield permutation


def solve(n=8):
    """
    This problem is similar to the solution to problem 49. The difference is that we generate multiple "digit hashes"
        for a number, and add it to a bucket for each digit hash. The first bucket to 8 primes wins.

    For instance with 56003, that number will generate the digit hashes:
        5600*
        560**
        560*3
        56*03
        56*03
        56*0*
        etc...
    """
    hash_map = defaultdict(list)
    for i in count(1):
        prime_i = sieve[i]

        for permutation in generate_permutations(str(prime_i)):
            hash_map[permutation].append(prime_i)

            if len(hash_map[permutation]) == n:
                return min(hash_map[permutation])


solve.answer = 121313

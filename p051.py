'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
    13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
    this 5-digit number is the first example having seven primes among the ten generated numbers,
    yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.

    Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
    with the same digit, is part of an eight prime value family.
'''

# This runs in 40s on Python 3. Less than 1 minute rule done, next problem.

from __future__ import print_function
from collections import defaultdict
from itertools import count
from sympy.utilities.iterables import kbins
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
    hash_map = defaultdict(list)
    for i in count():
        if len(sieve._list) <= i:
            sieve.extend_to_no(i + 1)

        prime_i = sieve._list[i]

        for permutation in generate_permutations(str(prime_i)):
            hash_map[permutation].append(prime_i)

            if len(hash_map[permutation]) == n:
                return min(hash_map[permutation])


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p051_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# We're given there are 11, so do not use a fixed upper limit. Just iterate till we find 11.

from __future__ import print_function
from sympy import Sieve, isprime
from math import log10, floor
from itertools import count


def two_sided_primes():
    def right_truncatable(n):
        for possible_prime in (n // 10**i for i in range(int(floor(log10(n))) + 1)):
            if not isprime(possible_prime):
                return False

        return True

    def left_truncatable(n):
        for possible_prime in (n % 10**i for i in range(int(floor(log10(n))) + 1, 0, -1)):
            if not isprime(possible_prime):
                return False

        return True

    s = Sieve()
    for i in count(5):
        if len(s._list) < i:
            s.extend_to_no(i)

        prime_i = s._list[i - 1]

        if left_truncatable(prime_i) and right_truncatable(prime_i):
            yield prime_i


def solve():
    gener = two_sided_primes()
    return sum(next(gener) for x in range(11))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p037_ans.txt', 'w') as wb:
        wb.write(str(answer))

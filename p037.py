'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# We're given there are 11, so do not use a fixed upper limit. Just iterate till we find 11.
# If not left-truncatable, then don't check for right-truncatable.

from ProjectEuler.lib import segmented_sieve
from math import log10, floor


def two_sided_primes():
    def right_truncatable(n, primes):
        for possible_prime in (n // 10**i for i in range(floor(log10(n)) + 1)):
            if possible_prime not in primes:
                return False

        return True

    def left_truncatable(n, primes):
        for possible_prime in (n % 10**i for i in range(floor(log10(n)) + 1, 0, -1)):
            if possible_prime not in primes:
                return False

        return True

    primes = []
    found_count = 0
    for prime in segmented_sieve():
        primes.append(prime)

        if prime > 10 and left_truncatable(prime, primes) and right_truncatable(prime, primes):
            yield prime
            found_count += 1
            if found_count == 11:
                break


def solve():
    return sum(two_sided_primes())


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p037_ans.txt', 'w') as wb:
        wb.write(str(answer))

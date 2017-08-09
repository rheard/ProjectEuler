'''
The number, 197, is called a circular prime because all rotations of the digits:
    197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from ProjectEuler.lib import sieve
from math import ceil, log10


# For all functionss, primes should contain all primes up to 10**(ceil(log(n) / log(10)))
def circular(n, primes):
    def rotate(n, shift):
        return n[shift:] + n[:shift]

    is_circular = True
    str_n = str(n)
    for i in range(len(str_n)):
        if int(rotate(str_n, i)) not in primes:
            is_circular = False
            break

    return is_circular


def circular_numbers(n=10**6, primes=None):
    if primes is None:
        target_numbers = set(str(x) for x in range(2, 10, 2))
        primes = set(prime for prime in sieve(10 ** ceil(log10(n))) if len(set(str(prime)).union(target_numbers)) != 0)

    for prime in primes:
        if prime >= n:
            break

        if circular(prime, primes):
            yield prime


def solve(n=10**6, primes=None):
    return len(set(circular_numbers(n, primes)))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p035_ans.txt', 'w') as wb:
        wb.write(str(answer))
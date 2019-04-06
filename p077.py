'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''

from __future__ import print_function
from sympy import sieve
from itertools import count

_prime_sums = {}
def prime_sums(n):
    if n not in _prime_sums:
        _prime_sums[n] = set()
        for p in reversed(list(sieve.primerange(1, n + 1))):
            n_p = n - p
            if n_p == 0:
                _prime_sums[n].add((p, ))
            elif n_p > 1:
                for prime_sum in prime_sums(n_p):
                    _prime_sums[n].add(tuple(sorted((p, ) + prime_sum, reverse=True)))
    return _prime_sums[n]


def solve(max_ways=5000):
    for i in count(2):
        if len(prime_sums(i)) > max_ways:
            return i


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p077_ans.txt', 'w') as wb:
        wb.write(str(answer))

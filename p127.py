"""
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 * 32 * 7,
    so rad(504) = 2 * 3 * 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

    1. GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    2. a < b
    3. a + b = c
    4. rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:

    1. GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
    2. 5 < 27
    3. 5 + 27 = 32
    4. rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with sum(c) = 12523.

Find sum(c for c < 120000)
"""

from collections import deque
from functools import lru_cache
from ProjectEuler.lib import prod
from sympy import primefactors
from itertools import chain, starmap
from multiprocessing import Pool, Array
from fractions import gcd
from timeit import timeit
from numpy import array

'''
To start solving this, we are going to need to generate co-prime pairs (a, b).
    Then we check if a + b is co-prime to a and b. Lastly check if rad(abc) < c.

    Wikipedia gives us a nice way to generate co-prime pairs in a tree fashion.
    We start with 2 trees with the seeds being (2, 1) and (3, 1). Each node (m, n)
    has 3 branches:
    (2m - n, m)
    (2m + n, m)
    (m + 2n, n)

    Whats more this is non-redundant. It should be obvious that m > n.

    Using this we can find all c values under 1000, which leads us to A120498.
    Turns out this is a famous unsolved problem in mathematics known as the abc conjecture.

    Through testing it is found that if gcd(a, b) = 1, then gcd(a, c) = 1 and
    gcd(b, c) = 1.

    Hopefully it should be obvious that if a, b and c are coprime, then 
    rad(abc) == rad(a) * rad(b) * rad(c)
    We can use this fact to reduce the space of radicals we have to compute,
    and by cacheing the calls to rad(), this is a massive speed boost.

    While the co-prime tree is much more efficient for c < 1000, the runtime gets much
    worse very quickly (roughly O(n**2)) and requires gigabytes of memory to hold the
    tree. A brute force approach seems to have a runtime roughly O(n) and uses no memory.
'''

factor_cache = dict()
def factor(n):
    if n not in factor_cache:
        factor_cache[n] = primefactors(n)
    return factor_cache[n]


rad_cache = dict()
def rad(n):
    if n not in rad_cache:
        rad_cache[n] = prod(factor(n))
    return rad_cache[n]


def pool_callee(max_c, a):
    factor_a = factor(a)
    if len(factor_a) > 3:
        return 0
    rad_a = prod(factor_a)
    ret = 0
    is_a_even = not a & 1
    for b in range(a + 1, max_c - a, 2 if is_a_even else 1):
        c = a + b
        rad_b = rad(b)
        rad_c = rad(c)
        if rad_a * rad_b * rad_c >= c or gcd(rad_a, rad_b) != 1:
            continue
        ret += c
    return ret


def solve(max_c=120 * 10**3):
    with Pool(8) as tp:
        return sum(tp.starmap(pool_callee, ((max_c, a) for a in range(1, max_c))))


def solve_not_threaded(max_c=120 * 10**3):
    return sum(starmap(pool_callee, ((max_c, a) for a in range(1, max_c))))


if __name__ == '__main__':
    print(solve(120000))
    print(timeit(lambda: solve(120000), number=1))
    '''
    with open('p127_ans.txt', 'w') as wb:
        wb.write(str(ans))
    '''
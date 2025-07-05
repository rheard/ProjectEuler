"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
    it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms,
    but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

import os

from math import factorial

_chain_counts = {145: 1,
                 169: 3,
                 363601: 3,
                 1454: 3,
                 871: 2,
                 45361: 2,
                 872: 2,
                 45362: 2}


def chain_count(n):
    if n not in _chain_counts:
        new_n = sum(factorial(int(x)) for x in str(n))
        _chain_counts[n] = (0 if new_n == n else chain_count(new_n)) + 1
    return _chain_counts[n]


def solve(n=10**6, chain_len=60):
    """
    The solution to this problem is similar to the solution to problem 14.

    When we compute the chain length for a number, that chain length is the same for all numbers in the chain, and they
        can be cached.
    """
    return sum(1 for x in range(1, n) if chain_count(x) == chain_len)


solve.answer = 402

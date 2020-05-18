"""
A number chain is created by continuously adding the square of the digits in a number to form a new number
    until it has been seen before.

For example,

    44 -> 32 -> 13 -> 10 -> 1 -> 1
    85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
    What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import os

from itertools import permutations

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

_last_ans = {1: 1, 89: 89}


def get_chain_last(n):
    if n not in _last_ans:
        str_n = str(n)
        next_n = sum(int(digit)**2 for digit in str(n))
        last_ans = get_chain_last(next_n)
        _last_ans[n] = last_ans

        for perm in permutations(str_n):
            _last_ans[int("".join(perm))] = last_ans

    return _last_ans[n]


def solve(n=10**7):
    """
    To begin with it is worth noting that if a number ends in 1 it is known as a happy number.
        Numbers that get caught in a loop are called sad numbers.

    There are not very many speed improvement to be made here short of brute forcing this.

    However there are 1 or 2.

    The major speed improvement is that if we know where a number ends up, then we know know
        that every number which is a permutation of it's digits will also end up there.

    It can also be seen that if we know where a number ends up, then all the permutations of
        it's digits with any amount of 0's will also end there. This does not add a statistically
        significant speed up so it was not included.
    """
    return sum(1 for x in range(1, n) if get_chain_last(x) == 89)


solve.answer = 8581146


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

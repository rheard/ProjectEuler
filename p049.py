"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways: (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import os

from itertools import permutations
from collections import defaultdict

from sympy import sieve

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """
    We solve this by grouping primes in "digit hashmaps" and then analyzing "difference sets".

    First the primes have a "hash" generated based on their digits, which is sum(10**digit) for all digits.
        For example, for 1487, 4817 and 8147, we will get a sum that looks like:
        10**1 + 10**4 + 10**8 + 10**7 = 110010010

        Since all of these numbers have the same "digit hash", they grouped together.

    Next we go through each grouping and generate a difference matrix for it.
        These are square symmetric matrices representing the absolute differences between each element in the group.

        Duplicate differences in a row represent a prime with primes in an arithmetic sequence around it.
    """
    hash_map = defaultdict(list)
    for prime in sieve.primerange(10**3, 10**4):
        prime_str = str(prime)
        hash_map[sum(10**int(digit) for digit in prime_str)].append(prime)

    answers = []
    for grouping in hash_map.values():
        difference_matrix = [[x for x in (abs(a - b) for a in grouping) if x != 0] for b in grouping]
        for i, difference_set in enumerate(difference_matrix):
            possible_differences = set(difference_set)
            for difference in possible_differences:
                if difference_set.count(difference) == 2:
                    answers.append((grouping[i] - difference, grouping[i], grouping[i] + difference))
                    break

    return int("".join(str(x) for x in answers[1]))


solve.answer = 296962999629


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

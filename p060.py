"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
    result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
    The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import os

from collections import defaultdict
from itertools import count

from sympy import Sieve, isprime

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=5):
    """
    It can be seen that 2 can be excluded, because if that is concatenated to any prime, that prime isn't prime anymore.

    We solve this simply by keeping a list of potential solutions and going through each prime starting with 3.
        First we go through each solution in the potential solutions, and see if this prime can be added to it.
            If the prime can be added, we create a new potential solution with this prime.
        Secondly a new solution is added to the list of potential solutions for the prime, [prime].
    """
    sieve = Sieve()
    combinations = defaultdict(set)
    answer = None

    for i in count(2):
        sieve.extend_to_no(i)
        prime_i = sieve._list[i - 1]

        for prime_existing in sieve.primerange(3, prime_i):
            if isprime(int(str(prime_i) + str(prime_existing))) \
                    and isprime(int(str(prime_existing) + str(prime_i))):
                combinations[prime_i].add(prime_existing)
                combinations[prime_existing].add(prime_i)

        possible_solutions = {
            (matching_prime, prime_i): combinations[matching_prime].intersection(combinations[prime_i])
            for matching_prime in combinations[prime_i]
        }
        possible_solutions = {k: i for k, i in possible_solutions.items() if i}
        while possible_solutions:
            possible_solutions = {
                tuple(sorted(prime_set + (matching_prime, ))): this_set.intersection(combinations[matching_prime])
                for prime_set, this_set in possible_solutions.items() for matching_prime in this_set}

            for possible_solution in possible_solutions:
                if len(possible_solution) == n:
                    answer = possible_solution
                    break

            possible_solutions = {k: i for k, i in possible_solutions.items() if i}

        if answer:
            break

    return sum(answer)


solve.answer = 26033


if __name__ == '__main__':
    output_answer(solve)

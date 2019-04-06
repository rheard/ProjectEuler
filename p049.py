'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways: (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from __future__ import print_function
from sympy import sieve
from itertools import permutations


def solve():
    hash_map = {}
    for prime in sieve.primerange(2, 10**4):
        prime_str = str(prime)
        if len(prime_str) < 4:
            continue

        sq_sum = sum(int(x)**2 for x in prime_str)
        if sq_sum not in hash_map:
            hash_map[sq_sum] = []

        hash_map[sq_sum].append(prime_str)

    answers = []
    for sq_sum in hash_map:
        while len(hash_map[sq_sum]) != 0:
            prime = hash_map[sq_sum][-1]
            prime_permutations = set(x for x in ["".join(x) for x in permutations(prime)] if x in hash_map[sq_sum])
            hash_map[sq_sum] = sorted(list(set(hash_map[sq_sum]) - prime_permutations))
            possible_primes = sorted([int(x) for x in prime_permutations])
            if len(possible_primes) < 3:
                continue

            difference_sets = [[x for x in (abs(a - b) for a in possible_primes) if x != 0] for b in possible_primes]
            for i, difference_set in enumerate(difference_sets):
                possible_differences = set(difference_set)
                for difference in possible_differences:
                    if difference_set.count(difference) == 2:
                        answers.append((possible_primes[i] - difference, possible_primes[i], possible_primes[i] + difference))

    return "".join(str(x) for x in answers[1])


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p049_ans.txt', 'w') as wb:
        wb.write(str(answer))

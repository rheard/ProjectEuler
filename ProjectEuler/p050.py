"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import os

from sympy import sieve


def solve(n=10**6):
    """
    First we calculate all the "basic consecutive sums" for each prime p. This value is the sum of consecutive primes
        less than or equal to p.

    These "basic consective sums" are then subtracted to make differences that represent portions of the sums.
        For instance, the basic consecutive sum for 5 is 2 + 3 + 5 = 10. The basic consecutive sum for 13,
            as given in the example, is 41. We can create a consecutive sum from 7 + 11 + 13 by doing the basic
            consecutive sum for 13 - the basic consecutive sum for 5, and we see that indeed 7 + 11 + 13 = 41 - 10 = 31

    So we can calculate any consecutive sum of primes by simply using 1 or 2 of these basic consecutive sums.
        Then we just need to find the maximum consecutive sum that is prime under 1 million.
    """
    longest_chain = []
    primes = list(sieve.primerange(2, n))
    running_sums = [0]
    running_sum = 0
    for prime in primes:
        running_sum += prime
        running_sums.append(running_sum)

    for i, possible_prime_sum in enumerate(primes):
        found_chain = []
        for chain_length in range(len(longest_chain) + 1, i):
            if running_sums[chain_length] - running_sums[0] > possible_prime_sum:
                break

            for start_position in range(i - chain_length):
                this_sum = running_sums[start_position + chain_length] - running_sums[start_position]
                if this_sum > possible_prime_sum:
                    break

                if this_sum == possible_prime_sum:
                    found_chain = primes[start_position:start_position + chain_length]
                    break

        if found_chain != [] and len(found_chain) >= len(longest_chain):
            longest_chain = found_chain

    return sum(longest_chain)


solve.answer = 997651

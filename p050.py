'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from __future__ import print_function
from sympy import sieve


def solve(n=10**6):
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


if __name__ == '__main__':
    answer = solve(10**4)
    print(answer)
    with open('p050_ans.txt', 'w') as wb:
        wb.write(str(answer))

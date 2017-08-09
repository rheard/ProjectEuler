'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from ProjectEuler.lib import segmented_sieve, prime_factors_dict


def solve(max_n=20):
    primes = list(segmented_sieve(max_n + 1))

    total_factors = {x: 0 for x in primes}
    # Calculate GCD of 1 to max_n using prime factors
    for num in range(1, max_n):
        factors = prime_factors_dict(num, primes)
        for prime in factors:
            this_factor_count = factors[prime]
            if this_factor_count > total_factors[prime]:
                total_factors[prime] = this_factor_count

    answer = 1
    for prime in total_factors:
        answer *= prime ** total_factors[prime]

    return answer


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p005_ans.txt', 'w') as wb:
        wb.write(str(answer))

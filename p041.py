'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from ProjectEuler.lib import sieve
from math import log10, ceil

'''
First we can use the divisibility rule for 3 to reduce the search space.

The rule states that if the sum of the digits is divisible by 3, then the number is divisible by 3.

sum(range(1, 10)) == 45

so any 9 digit pandigital number is divisible by 3, so there are no pandigital primes of length 9.
    We can repeat this process:

sum(range(1, 9)) == 36, divisible by 3
sum(range(1, 8)) == 28, NOT divisible by 3
sum(range(1, 7)) == 21, divisible by 3

So there can be a 7 digit pandigital number not divisible by 3. That is where the largest prime should lie.
'''


def solve():
    largest_pandigital = 0
    seven_digits = [str(x) for x in range(1, 8)]
    for prime in sieve(10**7):
        if ceil(log10(prime)) < 7:
            continue

        if seven_digits == sorted(str(prime)):
            largest_pandigital = prime

    return largest_pandigital


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p041_ans.txt', 'w') as wb:
        wb.write(str(answer))

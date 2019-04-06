'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1**2
15 = 7 + 2*2**2
21 = 3 + 2*3**2
25 = 7 + 2*3**2
27 = 19 + 2*2**2
33 = 31 + 2*1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from __future__ import print_function
from sympy import prevprime, isprime
from itertools import count


def solve():
    for odd_composite in count(start=9, step=2):
        if isprime(odd_composite):
            continue

        can_be_found = False
        prime = prevprime(odd_composite)

        while prime != 2:
            for i in count(1):
                n = prime + 2 * i**2
                if n > odd_composite:
                    break

                if n == odd_composite:
                    can_be_found = True
                    break

            if can_be_found:
                break

            prime = prevprime(prime)

        if not can_be_found:
            return odd_composite


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p046_ans.txt', 'w') as wb:
        wb.write(str(answer))

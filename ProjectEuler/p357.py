from __future__ import print_function
from sympy import primerange, divisors, isprime
from math import sqrt

"""
We can start by reducing our search space. We can start this by using
    the example of 30. Lets start with the divisor 1:

    1 + 30/1 = 1 + 30 = 31

    Great, but now if we do 30 we see

    30 + 30/30 = 30 + 1

    So we don't actually have to test all the divisors, we only have
    to test divisors up to (and including) the sqrt(n).

That will limit our d-space, but we can also reduce our n-space. We know
    that every number must have itself (n) and 1 as divisors. By plugging
    n in for d we get that n + n/n must be prime, or that n + 1 must be prime.
    A consequence of this is that the only prime that will be included is
    the prime where n + 1 is a prime, so 2.
"""

def solve(max_p=10**8):
    running_sum = 0
    for n in range(2, max_p + 1, 4):
        if not isprime(n + 1):
            continue
        works = True
        sqrt_n = sqrt(n)
        for d in divisors(n)[1:-1]:
            if d > sqrt_n:
                break
            new_p = d + n//d
            if not isprime(new_p):
                works = False
                break
        if works:
            print(n)
            running_sum += 1
    return running_sum
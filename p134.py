'''
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest
    number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes,
    p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2.
    Let S be the smallest of these values of n.

Find the sum of S for every pair of consecutive primes with 5 <= p1 <= 1000000.
'''


from sympy import sieve, nextprime
from itertools import count


'''
The solution to this problem smacked me in the face while I was out on a walk one day.
    I literally ran back to my desk to solve it.

The best way to illustrate this is with an example. Say p1 = 23.
    p2 is then 29. We declare our decimal position to be 0 (the least significant decimal position).
    We want position 0 in n to equal position 0 in p1. Start with k = 1, delta_k = 10**position == 1

    If position 0 in n does not equal position 0 in p1, then increase k by delta_k and recompute n.
    We do this until position 0 in n equals position 0 in p1. This happens when k = 7.

    From this, we know that position 0 in k is 7. Now we increase our position to position 1. 
    This means our delta_k = 10 and we repeat the process.

    If position 1 in n does not equal position 1 in p1, then increase k by delta_k and recompute n.
    We do this until position 1 in n equals position 1 in p1. This happens when k = 47.

By doing this we reduced our k's to check from 46 in a brute force approach to just 10.
    The complexity will increase by log(n) as opposed to n in a brute force approach.
    This is enough to complete the problem in a few seconds. 
'''


def S(p1, p2):
    str_p1 = str(p1)
    position = 0
    position_value = int(str_p1[-1])
    k = delta_k = 1
    # Compute these once and use the value, since these could potentially be costly operations.
    next_10 = 10**(position + 1)
    # Because delta_k is the change in the current 10s position, this_10 == delta_k always.
    #   However, it helps me think logically to keep them seperate values.
    this_10 = 10**position
    while True:
        multiple = k * p2
        if ((multiple % next_10) // this_10) == position_value:
            position += 1
            if position == len(str_p1):
                break
            position_value = int(str_p1[-1 - position])
            # this_10 is the previous next_10
            this_10 = next_10
            # delta_k just happens to be this_10. Logically I like to think of the next line as
            #   delta_k = 10**position, but that may be a costly operation.
            delta = this_10
            next_10 *= 10
        else:
            k += delta
    return multiple


def solve(min_p=5, max_p=10**6):
    # First generate the primes I need. The problem is concerned with
    #   min_p <= p1 <= max_p. Thus we will need 1 prime past max_p
    #   for p2 when p1 is the largest prime in the range.
    primes = list(sieve.primerange(min_p, max_p + 1))
    primes.append(nextprime(primes[-1]))
    ret = 0

    for p1, p2 in zip(primes, primes[1:]):
        ret += S(p1, p2)

    return ret
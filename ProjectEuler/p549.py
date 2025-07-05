from __future__ import print_function

from itertools import count

from sympy import factorint, sieve


"""
The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
    So s(10)=5 and s(25)=10.

Let S(n) be sum(s(i) for 2 <= i <= n).
    S(100)=2012.

Find S(10**8).
"""

# TODO: Change the approach below to use a different strategy:
#   Start with 2!, get its factors, and count that for the integers that it works for
#   next is 3, get its factors, and count that for the integers it works for that haven't been counted
#   continue to 4, etc.

_s = {1: 1}
def s(n):
    factors = factorint(n, multiple=True)
    for i in count(2):
        if not factors:
            return i - 1
        found_factors = factorint(i, multiple=True)
        for factor in found_factors:
            if factor in factors:
                factors.remove(factor)

def S(n):
    return sum(s(i) for i in range(2, n + 1))

# Or according to A002034, 
#   s(1) = 1
#   s(n!) = n
#   s(p) = p where p is prime
#   s(p_1*p_2*p_3*...*p_u) = p_u if p_1 < p_2 < ... < p_u are primes.
#   s(p**k) = p*k for p prime and k <= p
#   s(p_1**e_1 * p_2**e_2 * ... * p_u**e_u) = max(s(p_1**e_1), s(p_2**e_2), ..., s(p_u**e_u))

def old_s(n):
    factors = factorint(n, multiple=True)
    for i in count(2):
        orig_i = i
        for factor in reversed(factors):
            new_i, i_mod_factor = divmod(i, factor)
            if i_mod_factor == 0:
                i = new_i
                factors.remove(factor)
        if len(factors) == 0:
            return orig_i

s_vals = {1: 1}
def s(n):
    if n in s_vals:
        return s_vals[n]
    factors = factorint(n)
    if all(v < k for k, v in factors.items()):
        return max(s(k**v) for k, v in factors.items())
    else:
        return old_s(n)

def S(n):
    sieve.extend(n)
    # Perform s(p) = p and s(p**k) = p*k if k <= p
    for p in sieve._list:
        for k, multiple in enumerate(range(p, min(n, p**p) + 1, p)):
            s_vals[multiple] = p*(k + 1)
    # Perform s(p_1*p_2*...*p_u) = p_u for primes p_x
    running_prod = 1
    for p in sieve._list:
        running_prod *= p
        if running_prod > n:
            break
        s_vals[running_prod] = p
    # Perform s(n!) = n
    running_factorial = 1
    for i in count(2):
        running_factorial *= i
        if running_factorial > n:
            break
        s_vals[running_factorial] = i
    return sum(s(i) for i in range(2, n + 1))
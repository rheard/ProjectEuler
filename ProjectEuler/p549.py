"""
The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
    So s(10) = 5 and s(25) = 10.

Let S(n) be sum(s(i) for 2 <= i <= n).
    S(100) = 2012.

Find S(10**8).
"""

from itertools import count
from math import floor, log

import numpy as np
from sympy import sieve


def v(p, n):
    L = int(floor(log(n, p)))
    return sum(n // p**i for i in range(1, L + 1))


def sub_s(factor, exp):
    """
    This is `s`, however it only works for a prime number with an exponent.

    `s` would be defined as the maximum value of the output of this method for each factor of a number.

    However I'm using it with primes directly with my sieve idea...
    """
    if exp <= factor:
        return factor * exp

    for i in count(1):
        if v(factor, i) >= exp:
            return i


def S(n):
    s_sieve = np.zeros(n + 1, dtype=np.int64)

    for p in sieve.primerange(n + 1):
        p_q = p
        q = 1
        while p_q <= n:
            ans = sub_s(p, q)
            s_sieve[p_q::p_q] = np.maximum(s_sieve[p_q::p_q], ans)

            p_q *= p
            q += 1

    return sum(s_sieve)


def solve(n=10**8):
    """
    Okay, I started by making a simple solution which just factors n, then counts up from 2 factoring numbers and
        removing factors from n's factoring until all numbers have been removed.
    This worked for small numbers and was better than general brute force so I could check up to ~10**5 or so.
        This is obviously too dumb for the entire problem space however. Time for optimization...

    My first thought was that to find s(n) for a number which factors like p**q (a single power raised), we would need
        q factors of p, which would happen around p * q... except this undercounts square numbers which have 2 factors,
            and cubes which 3, etc etc...

    Not sure how to solve this, I started by looking at the Wikipedia page for the factorial function,
        which just so happens to have a section on "divisibility and digits", which states:
            "More precise information about its divisibility is given by Legendre's formula."

    Looking at and learning about Legendre's formula I was immediately put off as it has an infinite sum and I didn't
        want to deal with that... (probably better to look at this formula on the Wikipedia page):

        v_p(n!) = sum(floor(n / p**i) for i in range(1, float("inf")))

        however reading on, we learn:
            "While the sum on the right side is an infinite sum,
                for any particular values of n and p it has only finitely many nonzero terms"

    Looking at the example on Wikipedia this makes sense: essentially what this algorithm is doing with the infinite sum
        is correcting for the problem I observed previously. That is, it counts the prime numbers first, then their
            squares, then their cubes, etc, up until the number raided to a power can no longer divide into n.

        Wikipedia even gives a nice, finite method for this:

        v_p(n!) = sum(floor(n / p**i) for i in range(1, L) where L = floor(log_p(n))

    So, going back to the problem, for each prime p**q in the factorization we need to find the smallest m where
        v_p(m!) >= q

    After testing 2 through 100, this is actually about 4 times faster than the algorithm I started with! Cool!

    After looking in OEIS at A002034, I've found a few more facts about s(n),
            including partial confirmation of my original suspicion:
        s(p**k) = p*k for p prime and k <= p

    After adding this logic, we're looking at a major speed up, on the order of an additional 29x faster!
        With multiprocessing and doing some testing, I can compute S(10**7) in 59 seconds, and based on scaling
            I could get the answer to the problem in roughly 13 minutes... this is why I need a threadripper...

    After some testing an observation: this method requires factoring all of the numbers 2 to n, in this case 10**8.
        That factoring alone takes a LONG time...
            While `primerange(10**8)` is not much faster, `sieve.primerange(10**8)` is, and only takes ~22 seconds.

    Here is the new idea: we create a sieve of integers of n length. For each exponent q where p**q <= n,
        we compute the solution using v_p(m!) >= q. For every multiple p**q * k <= n, we go to sieve
        and store the solution if it is the largest solution yet.

    Using this method I was able to compute the solution in 3.5 minutes.
        Some minor optimizations brought that down to 2.5 minutes.

    For my last trick... I started with a class for the sieve which used a normal Python list offset by 2.
        However if I use a numpy array, then I can do a neat trick with `np.maximum` and apply the answer over the array
            all at once like so:

        s_sieve[start::step] = np.maximum(s_sieve[start::step], ans)

    Doing this we are finally below the 60s requirement!
        Also nicely I don't even actually need to offset by 2 because the 0 and 1-index will just be 0 and won't
            contribute to the sum.
    """
    return S(n)


solve.answer = 476001479068717

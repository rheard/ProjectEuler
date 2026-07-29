"""
A Hamming number is a positive number which has no prime factor larger than 5.
    So the first few Hamming numbers are 1,2,3,4,5,6,8,9,10,12,15.
    There are 1105 Hamming numbers not exceeding 10**8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
    Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10**9?
"""

from factorgen import Factorizations
from sympy import nextprime


def ghamming_count(t, n):

    def bounded_nextprime(p):
        next_p = nextprime(p)
        if next_p >= t:
            return None
        return next_p

    return sum(1 for _ in Factorizations(max_i=n, nextprime=bounded_nextprime))



def solve(t=100, n=10**9):
    """
    First thought: I've been using sieves a lot lately, how about a sieve?

    An observation that should be obvious: if t is the type number, then all numbers < t qualify.
        Similarly we only need to exclude numbers which are multiples of primes >= t.

    My final idea is to use numpy. The bottleneck then became generating all primes <= 1 billion with sympy.
        Doing tests with a smaller n value, it became clear it was spending most of its time in extending
        the prime sieve.

        After reading the docs I noticed a newly added `sieve_interval` option. By increasing this value to 10**8,
            I was able to solve the problem in 2.5 minutes.

    Not being sure what to do, it occurs to me.... I'm keeping track of a sieve for the generalized Hamming numbers,
        while also using a sieve to generate prime numbers.

        Here is how I will do it: 1 will be the default and means "prime".
            Starting with all primes <= 100, we'll mark all of their multiples >100 as 2,
                meaning they are generalized Hamming numbers but are not prime.
            Then for each number we find with a 1 that is >= 100, mark all of their multiples as 0.

            By the end there should be no more 1s. We just need to count the 2s.

        Hm. Somehow that is worse.

    After eating: an idea occurs to me. I could just start with all the factors below 100, and enumerate
        the factorizations from that. In fact, I've already written a beautiful Python library for this EXACT purpose!!

        What a glorious realization that was. I just had to release a new version of `factorgen` which supports bounded
            prime generators (a good feature to have honestly), and then just use that to enumerate
            all the 100-smooth numbers.
    """
    return ghamming_count(t, n)


solve.answer = 2944730

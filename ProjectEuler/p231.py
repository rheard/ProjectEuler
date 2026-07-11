"""
The binomial coefficient (10 3) = 120.
120 = 2**3 * 3 * 5 = 2 * 2 * 2 * 3 * 5, and 2 + 2 + 2 + 3 + 5 = 14.
So the sum of the terms in the prime factorization of (10 3) is 14.

Find the sum of the terms in the prime factorization of (20_000_000 15_000_000).
"""

from sympy import sieve


def kummer(n, m, p):
    n_sub = n - m
    carry = 0
    output = 0
    while m or n_sub:
        m, m_digit = divmod(m, p)
        n_sub, n_sub_digit = divmod(n_sub, p)
        digit_sum = m_digit + n_sub_digit + carry
        carry, digit = divmod(digit_sum, p)
        if carry:
            output += 1

    return output


def solve(n=20_000_000, m=15_000_000):
    """
    At first I thought maybe I could just brute force this.
        I was certain the hardest part would be computing the binomial coefficient.
        It took about 5 minutes to compute, but I was not able to complete the factoring step.

    Not being sure what to do, I looked at the Wikipedia page for binomial coefficient,
        which has a section helpfully titled "divisibility properties" where there is a link to
        "Kummer's theorem."

    For the ignorant (me), Kummer's theorem is fascinating and basically exactly what I need.
        I highly recommend just reading the Wikipedia article for it as that will do better justice than I can here.
        Essentially it details an algorithm for computing the exponents of primes in the prime factorization,
            without having to compute the entire binomial coefficient and factoring it.

    Using that, solving the problem is trivial.
    """
    return sum(p * kummer(n, m, p) for p in sieve.primerange(2, n + 1))


solve.answer = 7526965179680

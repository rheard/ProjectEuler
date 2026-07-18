"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11 * 41 * 271 * 9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(10**9).
"""

from sympy import factorint, primerange, n_order


def solve(n=10**9):
    """
    Well to start I thought the hard part would be factorization, but it turns out the hard part is that
        trying to compute
            (10**10**9 - 1) // 9

        is actually quite difficult.

    Not being sure what to do, I took a look at the Wikipedia article for repunits.
        In the section titled "properties", the very last property has some division information, which finalizes with
            the fact:

        "Therefor, if gcd(m, n) = d, then gcd(R_m, R_n) = R_d."

    It should be clear that this can be used to start to pull apart larger repunits using smaller ones.
        For instance, lets say you want to factor R(32), and 32 = 2**5.

        Lets first start by computing R(2) and factoring that, which is already a prime: 11.
        Next we can compute R(4) and divide out the 11 we already know is there, then factor the rest to get: 101.
        Next compute R(8), divide out the 11 and 101 we already know is there, then factor the rest again to get:
            73 and 137.
        Next compute R(16), divide out the 11, 73, 101 and 137 we already know are there, factoring again we get:
            17, 5882353.

        Finally repeating this process for R(32) with the primes we already know are in it, we get the last primes in
            the factorization: 353, 449, 641, 1409, 69857.

        By repeating this process for both 2 and 5 (the primes in the factorization of 10**9) up to exponents of 9
            should give us the prime factorization of R(10**9) without having to just brute force factor it.

    However we would still need to calculate R(10**9) and that is the part where I had a difficult start.
        Using this method I was able to factor R(10**5) in about a minute and a half by limiting
            the factorization search.

    Keep in mind that we can be confident that all primes in this factorization will also appear in the
        final factorization of R(10**9). There will only be new primes to add according to the method we have
        laid out above.

        Again finding myself not being sure what to do, I printed out the factors I have found from
            the prime factorization of R(10**5).

        The Wikipedia article for repunits mentions good old OEIS a lot, so I searched just the first four in OEIS:
            11, 17, 41, 73.

        That brought me to A178070, which is helpfully exactly what I need.

    A178070 states that: "A prime p > 5 is here if the multiplicative order of 10 mod p is of the form 2^i * 5^j."
        Helpfully, sympy has a method to calculate the multiplicative order of a number mod another number.

    So to solve the problem, we are looking for the first 40 primes which are greather than 5,
        where the multiplicative order of 10 mod p has a prime factorization of 2^i * 5^j,
        where i and j are both >=0 but <=9.
    """
    master_factors = factorint(n)
    found = []
    for prime in primerange(7, 10**8):  # just an arbitrarily large number
        order = n_order(10, prime)
        factors = factorint(order)
        if all(e <= master_factors.get(p, 0) for p, e in factors.items()):
            found.append(prime)

        if len(found) >= 40:
            break

    return sum(found)


solve.answer = 843296

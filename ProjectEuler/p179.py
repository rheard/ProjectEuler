"""
Find the number of integers 1 < n < 10**7, for which n and n + 1 have the same number of positive divisors.
    For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""


def solve(n=10**7):
    """
    I was already aware of things like Euler's totient function and the divisor function.
        Looking at the Wikipedia page for the divisor function gives a nice and easy formula based on the prime
            factorization.

    That was enough to solve the problem... in 4.0 minutes. :(

    The only other thing I could think to do was a sieve, but surely thats not faster (I thought).
        Turns out its about 5x as fast. 4 minutes / 5 = <60s.
    """
    sieve = [1] * (n - 2)
    for d in range(2, n):
        for d_mul in range(d, n, d):
            sieve[d_mul - 2] += 1

    return sum(1 for k, i in enumerate(sieve[:-1]) if i == sieve[k + 1])


solve.answer = 986262

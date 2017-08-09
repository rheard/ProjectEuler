from math import sqrt, ceil, floor
from multiprocessing.pool import ThreadPool
import operator
import functools

prod = lambda x: functools.reduce(operator.mul, x, 1)


# Generator to cycle through all Fibonacci numbers cleanly
def fib_generator():
    a = 1
    b = 1

    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


# Generator to cycle through all triangle numbers cleanly
def tri_generator():
    running_sum = 0
    i = 1
    while True:
        running_sum += i
        yield running_sum
        i += 1


# Runs a single instance of the Sieve of Eratosthenes
def sieve(n, start=2, in_primes=[]):
    def mark_multiples(prime, start, n, sieve):
        for multiple in range(ceil(start / prime) * prime, n, prime):
            sieve[multiple - start] = False

    new_primes = []
    sieve = [True] * (n - start)
    for prime in in_primes:
        mark_multiples(prime, start, n, sieve)

    for i, is_prime in enumerate(sieve):
        this_prime = i + start
        if is_prime and this_prime not in in_primes:
            mark_multiples(this_prime, start, n, sieve)
            new_primes.append(this_prime)

    return new_primes


# Runs a segmented Sieve of Eratosthenes.
# Each thread in thread_count will compute the primes in a range of block_size.
# If n is not specified, then it will be an open ended sieve.
def segmented_sieve(n=None, thread_count=8, block_size=100000):
    sqrt_n = block_size // 10
    if n is not None:
        sqrt_n = floor(sqrt(n)) + 1
    start_primes = sieve(sqrt_n)

    for prime in start_primes:
        yield prime

    with ThreadPool(thread_count) as tp:
        last_n = sqrt_n
        while n is None or last_n <= n:
            results = tp.map(lambda x: sieve(*x), ((last_n + block_size * (i + 1), last_n + block_size * i, start_primes) for i in range(thread_count)))
            last_n += thread_count * block_size
            for new_primes in results:
                if n is None:
                    start_primes += new_primes

                for new_prime in new_primes:
                    if n is not None and new_prime >= n:
                        break
                    yield new_prime


# Note: Primes should include all primes less than or equal to floor(sqrt(n))
def prime_factors(n, primes=None):
    sqrt_n = floor(sqrt(n))
    if primes is None:
        primes = list(segmented_sieve(sqrt_n, primes))

    factors = []
    for prime in primes:
        if n == 1:
            break

        div, mod = divmod(n, prime)
        while mod == 0:
            factors.append(prime)
            n = div
            div, mod = divmod(n, prime)

    return factors


def prime_factors_dict(n, primes=None):
    factors = prime_factors(n, primes)
    prime_factorization = {}
    for prime in factors:
        if prime not in prime_factorization:
            prime_factorization[prime] = factors.count(prime)

    return prime_factorization

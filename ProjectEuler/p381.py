"""
For a prime p let S(p) = (sum(p-k)!) % p for 1 <= k <= 5.

For example, if p = 7
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720 + 120 + 24 + 6 + 2 = 872.
As 872 % 7 = 4, S(7) = 4.

It can be verified that sum(S(p)) = 480 for 5 <= p < 100.

Find sum(S(p)) for 5 <= p < 10**8.
"""

from sympy import sieve


def factorial_mod(n, modulus):
    ans = 1
    if n <= modulus // 2:
        #calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1, n + 1):
            ans = (ans * i) % modulus
    else:
        #Fancypants method for large n
        for i in range(1, modulus - n):
            ans = (ans * i) % modulus
        ans = pow(ans, -1, modulus)

        #Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
        if n % 2 == 0:
            ans = -1 * ans + modulus

    return ans % modulus


def S(p):
    return (factorial_mod(p - 5, p) * (p + 9)) % p


def solve(n=10**8):
    """
    (p - 1)! + (p - 2)! + (p - 3)! + (p - 4)! + (p - 5)!
    (p - 1) * (p - 2)! + (p - 2)! + (p - 3)! + (p - 4)! + (p - 5)!
    (p - 2)! * p + (p - 3)! + (p - 4)! + (p - 5)!
    (p - 2) * (p - 3)! * p + (p - 3)! + (p - 4)! + (p - 5)!
    (p - 3)! ((p - 2) * p) + 1) + (p - 4)! + (p - 5)!
    (p - 3) * (p - 4)! ((p - 2) * ((p - 1) + 1) + 1) + (p - 4)! + (p - 5)!
    (p - 4)! * ((p - 3) * ((p - 2) * ((p - 1) + 1) + 1) + 1) + (p - 5)!
    (p - 5)! * ((p - 4) * ((p - 3) * ((p - 2) * ((p - 1) + 1) + 1) + 1) + 1)
    (p - 5)! * ((p - 4) * ((p - 3) * ((p - 2) * p + 1) + 1) + 1)
    (p - 5)! * ((p - 4) * ((p - 3) * (p**2 - 2*p + 1) + 1) + 1)
    (p - 5)! * (p**4 - 9*p**3 + 27*p**2 - 30*p + 9)

    Okay, this absolutely blew my mind...
        Looking for an optimization, I thought to replace p**3 with pow using the modulo input... but, the modulo
            input is p, so that would be pow(p, 3, p)? Well, thats obviously just p. So I can replace the above with:

    (p - 5)! * (p - 9*p + 27*p - 30*p + 9)
    (p - 5)! * (-11*p + 9)

    I found it odd that we're multiplying by a negative number, especially just to modulo...
        turns out, doesn't matter. It can bet removed.

    (p - 5)! * (11*p + 9)

    Well, if the negative can be removed then surely something else can be too right? Turns out yes, this works too:

    (p - 5)! * (p + 9)

    From here I hit a wall. I couldn't think of a way to further simplify this, and (p - 5)! was just too
        much to compute for all the large primes.

    So I went online looking for some sort of "factorial with a mod arg" like `pow` already has builtin.
        Turns out such a thing exists, as shown by Danny Pflughoeft, by taking advantage of Wilson's theorem.

    By adding that I was able to solve the problem in ~30 seconds.
    """
    return sum(S(p) for p in sieve.primerange(5, n))


solve.answer = 139602943319822

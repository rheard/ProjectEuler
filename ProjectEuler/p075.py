"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an
    integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle,
    and other lengths allow more than one solution to be found; for example,
    using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000
    can exactly one integer sided right angle triangle be formed?
"""

from math import floor, sqrt

from ProjectEuler.utils import gcd


def solve(max_L=1500000):
    """
    Generating Pythagorean triples:
    a = k * (m**2 - n**2)
    b = k * 2*m*n
    c = k * (m**2 + n**2)
    where m, n, k are positive integers
        m > n and m and n are coprime and m and n are not both odd

    L = a + b + c
    L = k * (m**2 - n**2) + k * 2*m*n + k * (m **2 + n**2)
        min(k) == 1
    L = m**2 - n**2 + 2*m*n + m**2 + n**2
    L = 2 * m * (m + n)
    max_L = 2 * max_m * (max_m + min_n)
        min_n = 1
    max_L = 2 * max_m * (max_m + 1)
    max_m = (sqrt(2 * max_L + 1) + 1) / 2
    """
    sieve = [0] * (max_L + 1)
    max_m = int(floor((sqrt(2 * max_L + 1) - 1) / 2))

    for m in range(2, max_m + 1):
        m_sq = m**2

        for n in range(2 if m & 1 else 1, m, 2):
            if gcd(m, n) != 1:
                continue

            n_sq = n**2
            base_a = m_sq - n_sq
            base_b = 2 * m * n
            base_c = m_sq + n_sq
            base_L = base_a + base_b + base_c

            for L in range(base_L, max_L + 1, base_L):
                sieve[L] += 1

    return sum(1 for x in sieve if x == 1)


solve.answer = 161667

"""
All square roots are periodic when written as continued fractions and can be written in the form:

sqrt(N) = a_0 + (1 / a_1 + (1 / a_2 + (1 / a_3 + ...)))

For example, let us consider sqrt(23):

    sqrt(23) = 4 + sqrt(23) - 4 = 4 + 1 / (1 / (sqrt(23) - 4)) =
        4 + 1 / (1 + ((sqrt(23) - 3) / 7))

If we continue we would get the following expansion:

    sqrt(23) = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

The process can be summarised as follows:

a_0 = 4,  1 / (sqrt(23) - 4) = (sqrt(23) + 4) / 7       = 1 + (sqrt(23) - 3) / 7
a_1 = 1,  7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14  = 3 + (sqrt(23) - 3) / 2
a_2 = 3,  2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14  = 1 + (sqrt(23) - 4) / 7
a_3 = 1,  7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7   = 8 + sqrt(23) - 4
a_4 = 8,  1 / (sqrt(23) - 4) = (sqrt(23) + 4) / 7       = 1 + (sqrt(23) - 3) / 7
a_5 = 1,  7 / (sqrt(23) - 3) = 7 * (sqrt(23) + 3) / 14  = 3 + (sqrt(23) - 3) / 2
a_6 = 3,  2 / (sqrt(23) - 3) = 2 * (sqrt(23) + 3) / 14  = 1 + (sqrt(23) - 4) / 7
a_7 = 1,  7 / (sqrt(23) - 4) = 7 * (sqrt(23) + 4) / 7   = 8 + sqrt(23) - 4

It can be seen that the sequence is repeating. For conciseness, we use the notation sqrt(23) = [4;(1,3,1,8)],
    to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

sqrt(2)=[1;(2)], period=1
sqrt(3)=[1;(1,2)], period=2
sqrt(5)=[2;(4)], period=1
sqrt(6)=[2;(2,4)], period=2
sqrt(7)=[2;(1,1,1,4)], period=4
sqrt(8)=[2;(1,4)], period=2
sqrt(10)=[3;(6)], period=1
sqrt(11)=[3;(3,6)], period=2
sqrt(12)= [3;(2,6)], period=2
sqrt(13)=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
"""

from decimal import Decimal, getcontext
from math import floor


def continued_fraction(n):
    sqrt_n = Decimal(n).sqrt()
    m = 0
    d = 1
    a = [int(floor(sqrt_n))]
    double_a_0 = a[0] * 2

    if sqrt_n != sqrt_n.to_integral_value():
        while True:
            m = d * a[-1] - m
            d = (n - m**2) // d
            a.append((a[0] + m) // d)

            if a[-1] == double_a_0:
                break

    return a[0], a[1:]


def solve(N=10000):
    """
    We just have to compute the continued fraction using an arbitrary precision.
        An algorithm for this is available online.
    """
    if getcontext().prec < 0.1 * N:
        getcontext().prec = int(0.1 * N)

    return sum(1 for x in range(2, N + 1) if len(continued_fraction(x)[1]) & 1)


solve.answer = 1322

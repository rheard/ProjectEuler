"""
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
    and two discs were taken at random, it can be seen that the probability of taking
    two blue discs, P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
    is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total,
    determine the number of blue discs that the box would contain.
"""

from __future__ import division

from decimal import ROUND_CEILING, Decimal
from itertools import count


def solve(n=10**12):
    """
    To start solving this, we should do a little bit of math. We should think of this problem as...
        0.5 = (a / b) * ((a - 1) / (b - 1))
        0.5 = a*(a - 1) / b*(b - 1)
        b*(b - 1) = 2*a*(a - 1)
    where a, b are both integers.

    This is interesting. If we were to solve for b though we would see that:
        a = 0.5 * sqrt(2*b**2 - 2*b + 1) + 0.5

    It can be seen that sqrt(2*b**2 - 2*b + 1) must be odd. Since only odd numbers squared produce
        odd squares,  2*b**2 - 2*b + 1 must also be odd. It can be proved however that 2*b**2 - 2*b + 1
        is always odd, so this is irrelevant.

    It can be found that for a to be an integer, b must be 1, 4, 21, 120, 697. This is OEIS A046090,
        which has the following formula:

    b = 1/2 + ((1-2^{1/2})/4)*(3 - 2^{3/2})^i + ((1+2^{1/2})/4)*(3 + 2^{3/2})^i

    or if we define w,x,y,z such that:
    w = (1-2**(1/2)) / 4
    x = 3 - 2**(3/2)
    y = (1+2**(1/2)) / 4
    z = 3 + 2**(3/2)

    then

    b = 0.5 + y*w**i + x*z**i
    """
    w = (1 - Decimal(2).sqrt()) / 4
    x = 3 - Decimal(2).sqrt()**3
    y = (1 + Decimal(2).sqrt()) / 4
    z = 3 + Decimal(2).sqrt()**3
    point_5 = Decimal(0.5)

    for i in count():
        b = point_5 + w * x**i + y * z**i

        if b <= n:
            continue

        a = point_5 * (2*b**2 - 2*b + 1).to_integral_value(ROUND_CEILING).sqrt() + point_5

        if a == a.to_integral_value():
            return int(a.to_integral_value())


solve.answer = 756872327473

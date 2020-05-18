"""
Consider quadratic Diophantine equations of the form:

x**2 - D * y**2 = 1

For example, when D=13, the minimal solution in x is 649**2 - 13 * 180**2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3**2 - 2*2**2 = 1
2**2 - 3*1**2 = 1
9**2 - 5*4**2 = 1
5**2 - 6*2**2 = 1
8**2 - 7*3**2 = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

import os

from fractions import Fraction
from decimal import getcontext
from itertools import count
from math import sqrt

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

try:
    from .p064 import continued_fraction
except ImportError:
    from p064 import continued_fraction


def estimate_fraction(fraction, max_i, i=0):
    if i == 0:
        return fraction[0] + estimate_fraction(fraction, max_i, i + 1)
    elif i >= max_i:
        return Fraction(0, 1)
    else:
        return 1 / (fraction[1][(i - 1) % len(fraction[1])] + estimate_fraction(fraction, max_i, i + 1))


def solve(max_D=1000):
    """
    Quadratic Diophantine equations can be solved using continued fractions, meaning we can reuse code from problem 64.
    """
    if getcontext().prec < (0.1 * max_D):
        getcontext().prec = int(0.1 * max_D)

    max_x = 0
    max_x_D = 0

    for D in range(2, max_D + 1):
        if sqrt(D).is_integer():
            continue

        min_x = 0

        this_fraction = continued_fraction(D)

        for estimation_index in count(2):
            estimation = estimate_fraction(this_fraction, estimation_index)

            x, y = estimation.numerator, estimation.denominator

            if x**2 == D * y**2 + 1:
                min_x = x
                break

        if min_x > max_x:
            max_x = min_x
            max_x_D = D

    return max_x_D


solve.answer = 661


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

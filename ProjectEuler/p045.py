"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        T_n=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      P_n=n(3n-1)/2        1, 5, 12, 22, 35, ...
Hexagonal       H_n=n(2n-1)      1, 6, 15, 28, 45, ...
It can be verified that T_285 = P_165 = H_143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from math import sqrt


def hexagonal_numbers(start=1):
    n = start
    while True:
        yield n * (2 * n - 1)
        n += 1


def is_triangle_number(x):
    return ((sqrt(8 * x + 1) - 1) / 2).is_integer()


def is_pentagonal_number(x):
    return ((sqrt(24 * x + 1) + 1) / 6).is_integer()


def solve():
    """
    The only optimization is to iterate over the hexagonal numbers,
        because theres fewer of those than triangle numbers.
    """
    for hexagonal_number in hexagonal_numbers(start=144):
        if is_pentagonal_number(hexagonal_number) and is_triangle_number(hexagonal_number):
            return hexagonal_number


solve.answer = 1533776805

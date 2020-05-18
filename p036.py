"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def is_double_palindromic(n):
    str_n = str(n)
    bin_n = bin(n)[2:]
    return str_n == str_n[::-1] and bin_n == bin_n[::-1]


def double_palindromic_numbers(maximum=None):
    i = 1
    while True:
        if is_double_palindromic(i):
            yield i

        i += 1

        if maximum <= i:
            break


def solve():
    """No strategy here. Bruteforce."""
    return sum(double_palindromic_numbers(10**6))


solve.answer = 872187


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

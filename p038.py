"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product of
    9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
    concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

from __future__ import print_function

import os
import string

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """No strategy here. Bruteforce."""
    digits = set(string.digits[1:])
    maximum = 0
    for n in range(1, 10000):
        concatenated_products = ''
        i = 1
        while len(concatenated_products) < 9:
            concatenated_products += str(n * i)
            i += 1

        if len(concatenated_products) == 9 \
                and digits == set(concatenated_products) \
                and int(concatenated_products) > maximum:
            maximum = int(concatenated_products)

    return maximum


solve.answer = 932718654


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

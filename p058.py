"""
Starting with 1 and spiralling anticlockwise in the following way,
    a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
    but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
    that is, a ratio of 8/13 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
    If this process is continued, what is the side length of the square spiral for which the ratio of primes
    along both diagonals first falls below 10%?
"""

import os

from sympy import isprime

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


try:
    from .p028 import \
        top_left_diagonal as bottom_left_diagonal, \
        bottom_left_diagonal as top_left_diagonal, \
        bottom_right_diagonal as top_right_diagonal
except ImportError:
    from p028 import \
        top_left_diagonal as bottom_left_diagonal, \
        bottom_left_diagonal as top_left_diagonal, \
        bottom_right_diagonal as top_right_diagonal


def solve(n=0.1):
    """
    The only trick here is to use the previously defined methods from the similar problem 28.

    Note though that the grid rotated between problems.
    """
    prime_count = 0
    number_count = 1
    half_side_length = 0

    while True:
        half_side_length += 1
        number_count += 4

        corners = [bottom_left_diagonal(half_side_length),
                   top_left_diagonal(half_side_length),
                   top_right_diagonal(half_side_length)]

        for number in corners:
            if isprime(number):
                prime_count += 1

        if prime_count / number_count < n:
            break

    return half_side_length * 2 + 1


solve.answer = 26241


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

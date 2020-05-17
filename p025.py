"""
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n-1) + F_(n-2), where F_1 = 1 and F_2 = 1
Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144
The 12th term, F_12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

from __future__ import print_function

import os

from math import log10

try:
    from .utils import output_answer, fibonacci_generator
except ImportError:
    from utils import output_answer, fibonacci_generator


def solve(n=1000):
    """Simply find the first fibonacci number where the log base 10 is equal to n."""
    for i, fib_num in enumerate(fibonacci_generator(1)):
        if int(round(log10(fib_num), 10) + 1) == n:
            return i + 1


solve.answer = 4782


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

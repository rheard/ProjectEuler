"""
Let p(n) represent the number of different ways in which n coins can be separated into piles.
    For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

import os

from itertools import count

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

try:
    from .p076 import p
except ImportError:
    from p076 import p


def solve(multiple=10**6):
    """This is really the exact same problem as problem 76, just presented in a different way."""
    for n in count(1):
        if p(n) % multiple == 0:
            return n


solve.answer = 55374


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

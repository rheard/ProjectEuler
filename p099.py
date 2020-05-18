"""
Comparing two numbers written in index form like 2**11 and 3**7 is not difficult,
    as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult,
    as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines
    with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

from __future__ import division

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

with open('ProjectEuler/p099_base_exp.txt', 'r') as rb:
    __NUM_EXPONENTS = [list(int(i) for i in x.strip().split(',')) for x in rb.readlines()]


def solve(num_exponents=None):
    """
    We can reduce all the exponents by dividing them by the greatest exponent.

    From there, it is much simpler to do the full computation on the reduced numbers.
    """
    num_exponents = num_exponents or __NUM_EXPONENTS
    minimum_exponent = min(x for x in num_exponents[1])
    for number in num_exponents:
        number[1] /= minimum_exponent

    numbers = [x[0] ** x[1] for x in num_exponents]

    return numbers.index(max(numbers)) + 1


solve.answer = 709


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

"""
Working from left-to-right if no digit is exceeded by the digit to its left
    it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
    decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
    "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over
    half of the numbers below one-thousand (525) are bouncy. In fact,
    the least number for which the proportion of bouncy numbers first reaches
    50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
    reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

from __future__ import division

import os

from collections import defaultdict

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def bouncy(n):
    if not isinstance(n, str):
        n = str(n)
    sorted_n = "".join(sorted(n))
    return n != sorted_n and n[::-1] != sorted_n


def solve(n=0.99):
    """
    The heart of this solution is this...

    If a number is bouncy, then any number containing this number is also bouncy.

    ie, 155349 is bouncy, but any number of the form 1553** is also bouncy.
    """
    l = 3

    # Lets just count all of the numbers below 100 already.
    bouncy_nums = 0
    total_nums = 99
    not_bouncy = defaultdict(set)

    # Setup not_bouncy. All of the numbers below 100 are not bouncy,
    #   but we only care about the prefixs that are of length 2.
    for i in range(10, 100):
        not_bouncy[2].add(i)

    while True:
        # The min and max for numbers of length l
        num = 10**(l - 1)
        max_num = 10**l

        while num < max_num:
            prefix = num // 10

            if prefix in not_bouncy[l - 1]:
                # This number may or may not be bouncy
                if bouncy(num):
                    # This number is bouncy, add one and check.
                    bouncy_nums += 1
                    total_nums += 1

                    if bouncy_nums / total_nums >= n:
                        return num
                else:
                    # This number is not bouncy. Add it to the list of non-bouncy prefixes
                    #   of length l, add one and continue.
                    not_bouncy[l].add(num)
                    total_nums += 1

                num += 1
            else:
                # This number is definitely bouncy, and so are any with a shared prefix
                bouncy_nums += 10
                total_nums += 10
                num += 10

                if bouncy_nums / total_nums >= n:
                    # Uhoh, the proportion went over n somewhere in the range of bouncy
                    #   numbers. Backtrack and check each one.
                    bouncy_nums -= 10
                    total_nums -= 10
                    num -= 10

                    for _ in range(10):
                        bouncy_nums += 1
                        total_nums += 1
                        if bouncy_nums / total_nums >= n:
                            return num
                        num += 1

        l += 1


solve.answer = 1587000


if __name__ == '__main__':
    output_answer(solve)

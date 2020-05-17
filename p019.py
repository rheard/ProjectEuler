"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from __future__ import print_function

import os

from datetime import date

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve():
    """Thanks to datetime, this is super simple. All we have to do is iterate over the given timeframe."""
    # Now all we have to do is cycle the target time range.
    # We don't don't even have to bother with all the day calcuation facts given.
    return sum(1 if date(year, month, 1).isoweekday() == 7 else 0

               for month in range(1, 13) for year in range(1901, 2001))


solve.answer = 171


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

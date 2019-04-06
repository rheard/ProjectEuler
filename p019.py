'''
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
'''

from __future__ import print_function
# Python makes this real easy thanks to
from datetime import date


def solve():
    # Now all we have to do is cycle the target time range.
    # We don't don't even have to bother with all the day calcuation facts given.
    return sum(1 if date(year, month, 1).isoweekday() == 7 else 0 for month in range(1, 13) for year in range(1901, 2001))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p019_ans.txt', 'w') as wb:
        wb.write(str(answer))

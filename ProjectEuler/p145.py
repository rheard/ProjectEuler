"""
Some positive integers n have the property that the sum [n + reverse(n)] consists entirely of odd (decimal) digits.
    For instance, 36 + 63 = 99 and 409 + 904 = 1313.
    We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
    Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?
"""

import multiprocessing
import time

from multiprocessing.pool import Pool


count = 0


def inc_count(x):
    global count
    if x:
        count += 1


def reversible(n):
    this_sum = str(n + int(str(n)[::-1]))
    for c in this_sum:
        if c in '02468':
            return False
    return True


def solve(n=10**9):
    """No strategy here. Bruteforce."""
    global count
    with Pool(multiprocessing.cpu_count() - 2) as tp:
        add_more = True
        for i in range(1, n):
            while True:
                if tp._taskqueue.qsize() < 1000000:
                    add_more = True
                if tp._taskqueue.qsize() > 2000000:
                    add_more = False
                if not add_more:
                    time.sleep(5)
                    continue
                a = tp.apply_async(reversible, args=[i], callback=inc_count)
                break
    return count


solve.answer = 608720

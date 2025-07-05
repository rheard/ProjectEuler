"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from itertools import count

_p_vals = {0: 1}


def p(n):
    if n not in _p_vals:
        running_sum = 0
        for i in count(1):
            sign = int((-1) ** (i - 1))
            for g_i in [i, -i]:
                g_pentagonal_number_i = g_i * (3 * g_i - 1) // 2

                if g_pentagonal_number_i > n:
                    _p_vals[n] = running_sum
                    break

                running_sum += sign * p(n - g_pentagonal_number_i)
            else:
                continue

            break

    return _p_vals[n]


def solve(n=100):
    """
    Solving for the first few values of n and searching on OEIS for the sequence, we're greated with A000041.

    This is the partitioning problem that Ramanujan worked on. OEIS gives several formulas for this, but the one that
        I chose has to do with generalized pentagonal numbers
    """
    return p(n) - 1


solve.answer = 190569291

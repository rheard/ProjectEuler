'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

from __future__ import print_function
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
    return p(n) - 1


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p076_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

from __future__ import print_function
from itertools import count


def solve():
    powerful_digit_count = 0

    for n in range(1, 10):
        for e in count(1):
            str_len = len(str(n ** e))
            if str_len != e:
                break

            powerful_digit_count += 1

    return powerful_digit_count


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p063_ans.txt', 'w') as wb:
        wb.write(str(answer))

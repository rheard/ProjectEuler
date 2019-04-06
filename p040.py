'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
'''

from __future__ import print_function


def irrational_decimal_string(n=None):
    i = 1
    str_location = 0
    while True:
        str_i = str(i)
        finished = False
        for digit in str_i:
            yield digit
            str_location += 1
            if n is not None and n < str_location:
                finished = True
                break

        i += 1
        if finished:
            break


def solve():
    d = [0] + [int(x) for x in irrational_decimal_string(1000001)]
    return d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p040_ans.txt', 'w') as wb:
        wb.write(str(answer))

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
"""


def irrational_decimal_string():
    i = 1
    while True:
        str_i = str(i)
        for digit in str_i:
            yield digit

        i += 1


def solve():
    """No strategy here. Bruteforce."""
    generator = irrational_decimal_string()
    d = [0] + [int(next(generator)) for _ in range(1000001)]
    return d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]


solve.answer = 210

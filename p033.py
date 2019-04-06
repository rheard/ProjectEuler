'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
    may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
    and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from __future__ import print_function
from decimal import Decimal
from fractions import Fraction
from lib import prod


def digit_canceling_fractions():
    for numerator in range(11, 100):
        if numerator % 10 == 0:
            continue

        str_numerator = str(numerator)

        for denominator in range(numerator + 1, 100):
            if denominator % 10 == 0:
                continue

            original_fraction = Decimal(numerator) / Decimal(denominator)
            str_denominator = str(denominator)

            for i, num_digit in enumerate(str_numerator):
                for j, den_digit in enumerate(str_denominator):
                    if num_digit == den_digit:
                        if original_fraction == Decimal(int(str_numerator[(i + 1) % 2])) / Decimal(int(str_denominator[(j + 1) % 2])):
                            yield Decimal(numerator), Decimal(denominator)


def solve():
    return prod(Fraction(Decimal(numerator) / Decimal(denominator)) for numerator, denominator in digit_canceling_fractions()).denominator


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p033_ans.txt', 'w') as wb:
        wb.write(str(answer))

"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
    is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

from fractions import Fraction


def solve(n=1000):
    """No strategy here. Bruteforce."""
    property_count = 0
    continued_fraction = Fraction(1, 2)

    for i in range(n):
        this_iter = 1 + continued_fraction

        if len(str(this_iter.numerator)) > len(str(this_iter.denominator)):
            property_count += 1

        continued_fraction = Fraction(1, 2 + continued_fraction)

    return property_count


solve.answer = 153

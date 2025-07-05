"""
We shall say that an n-digit number is pandigital if it makes use of all the digits
    1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand,
    multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations


def solve():
    """
    We're going to go through all the possible orderings of the digits 1 through 9 and try to split it to form
        a working equation.
    """
    def pandigital_products():
        for string_eq in permutations(list(str(x) for x in range(1, 10)), 9):
            string_eq = "".join(string_eq)
            for multiplation_i in range(2, 7):
                for equal_i in range(multiplation_i + 1, 8):
                    multiplicand = int(string_eq[:multiplation_i])
                    multiplier = int(string_eq[multiplation_i:equal_i])
                    product = int(string_eq[equal_i:])
                    if multiplicand * multiplier == product:
                        yield product

    return sum(set(pandigital_products()))


solve.answer = 45228

"""
The binomial coefficients (n k) can be arranged in triangular form, Pascal's triangle, like this:

                            1
                        1		1
                    1		2		1
                1		3		3		1
            1		4		6		4		1
        1		5		10		10		5		1
    1		6		15		20		15		6		1
1		7		21		35		35		21		7		1
                        .........

It can be seen that the first eight rows of Pascal's triangle contain twelve distinct numbers:
    1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n.
    Of the twelve distinct numbers in the first eight rows of Pascal's triangle, all except 4 and 20 are squarefree.
    The sum of the distinct squarefree numbers in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of Pascal's triangle.
"""

import math

from sympy import factorint

from ProjectEuler.utils import ceildiv


def is_squarefree(n: int) -> bool:
    n = abs(n)
    if n <= 1:
        return False

    facts = factorint(n)

    return all(i < 2 for i in facts.values())


def solve(rows=51):
    """
    I solved problem 231 prior to this, and thought I would need to use Kummer's theorem for this.

    However, by simply eliminating duplicate entries (the triangle is symmetrical and m=0 always produces 1),
        and using my existing optimized `is_squarefree` method from my `quadint` package,
        solving the problem is very easy and fast.
    """
    output = 1
    found = {1}
    for n in range(2, rows):
        for m in range(1, ceildiv(n, 2) + 1):
            entry = math.comb(n, m)
            if entry in found:
                continue

            if is_squarefree(entry):
                output += entry

            found.add(entry)

    return output


solve.answer = 34029210557338

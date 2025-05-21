"""
Considering 4-digit primes containing repeated digits it is clear
    that they cannot all be the same: 1111 is divisible by 11, 
    2222 is divisible by 22, and so on. But there are nine 4-digit
    primes containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated
    digits for an n-digit prime where d is the repeated digit, N(n, d)
    represents the number of such primes, and S(n, d) represents the sum
    of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit
    prime where one is the repeated digit, there are N(4, 1) = 9 such primes,
    and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0,
    it is only possible to have M(4, 0) = 2 repeated digits, but there are
    N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d    M(4, d) N(4, d) S(4, d)
0           2       13      67061
1           3       9       22275
2           3       1       2221
3           3       12      46214
4           3       2       8888
5           3       1       5557
6           3       1       6661
7           3       9       57863
8           3       1       8887
9           3       7       48073

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""

import os

from itertools import product, combinations

from sympy import isprime

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def M_N_S(n, d, _non=1):
    # Attributes:
    #   n (int): The total number of digits in the target number
    #   d (int): The digit to repeat
    #   _non (int): Used internally. The number of digits in the target
    #       number that are not the rep digit.
    M = n - _non
    N = 0
    S = 0

    perm_set = set(x for x in range(10) if x != d)
    minimum = 10**(n - 1)
    for replace_digits  in product(perm_set, repeat=_non):
        for replace_locations in combinations(range(n), _non):
            number = 0
            for i in range(n):
                if i in replace_locations:
                    number += replace_digits[replace_locations.index(i)] * 10**(n - i - 1)
                else:
                    number += d * 10**(n - i - 1)
            if number < minimum or not isprime(number):
                continue
            N += 1
            S += number

    if N:
        return M, N, S

    return M_N_S(n, d, _non + 1)


def solve(n=10):
    """
    Pretty easy solution.

    For each digit d as our repdigit, get all the possible numbers
        consisting of n - 1 ds and 1 other digit. Are any prime?
        If no, then repeat but with all the possible numbers consisting of
            n - 2 ds and 2 other digits.
        If yes then we found our M, N and S all at the same time.
    """
    return sum(M_N_S(n, d)[2] for d in range(10))


solve.answer = 612407567715


if __name__ == '__main__':
    output_answer(solve)

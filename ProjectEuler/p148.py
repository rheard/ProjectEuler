"""
We can easily verify that none of the entries in the first seven rows of Pascal's triangle
    are divisible by 7:

                         1
                     1       1
                 1       2       1
             1       3       3       1
         1       4       6       4       1
     1       5      10      10       5       1
1        6      15      20      15       6       1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries
    are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (10**9)
    rows of Pascal's triangle.
"""


def baseDigits(n, b):
    base_repr = []
    while n:
        d, m = divmod(n, b)
        base_repr.append(m)
        n = d
    return base_repr[::-1]


def count_nondivisible(x):
    # If x is the base-7 representation of n, and e is the exponents, then this is
    #   f(x) = T_x[0] * 28**e[0] + (x[0] + 1) * f(x[1:])
    #   f(x) = 0 if len(x) == 0
    return ((x[0] * (x[0] + 1)) // 2) * 28**(len(x) - 1) + ((x[0] + 1) * count_nondivisible(x[1:]) if len(x) > 1 else 0)


def solve(n=10**9):
    """
    Through printing out divisibility of C(i, j) for i in range(2, 30) for j in range(1, i)
        it can be determined that the number of j where C(i, j) is divisible by 7 is
        dependent on i % 7. In fact the number where it is divisible is given by

        a, b = divmod(i, 7)
        d = (7 - b - 1) * a

        And the number where it is not divisible is then given by
        n = (i + 1) - d

        After substituting in the variables, we can use Sympy to simplify this to:
        a, b = divmod(i, 7)
        n = i + (b - 6) * a + 1

        After printing out some test values for this it should be obvious that
        a, b = divmod(i, 7)
        n = (a + 1) * (b + 1)

        This works until we get to i=7**2=49. The correct answer should be 2,
        but using this we get 8.

        Looking at the above formula, and realizing it fails at 7**2, I am deeply
        curious that looking at this in base-7 will help. After printing all the numbers
        in base 7 and looking at their values, it is clear to see that
        n = (i % 7 + 1) * ((i //= 7) % 7 + 1) * ((i //= 7) % 7 + 1) * ...
        until i is 0. This is sort of a mix of python (with the //=) and C (using variable assignment values)

        In other words, if a = (a_0, a_1, a_2, ...) are the integers in the base-7 representation,
        n = product(i + 1 for i in a)

    This is good but still quite slow. So instead of going through all i in range(n), instead
        we'll start with the base-7 0 and go through all base-7 numbers until we reach the base-7
        representation of n.

    Sadly this is STILL too slow... More analysis is required.

    A breakthrough has been found. It has been discovered that the first 7**i rows are
        equal to 28**i. Further more, this can extended to the first x*7**i rows which are
        equal to sum(range(1, x + 1)) * 28**i.

    After hours of testing, a total closed formula has been found.
        Say we have a number represented in base7, say
        n = k_1 * 7**i_j + ... + k_j * 7**0

        where i is reversed(range(j)). We can represent this in an array by
        [k_1, k_2, ..., k_j]

        The solution can be defined iteratively as
        sum(range(1, k[0] + 1)) * 28**i[0] + (k[0] + 1) * solve(k[1:])

        So we take the top level multiplier and exponent, sum all integers <= the multiplier
        and multiply by 28**explonent. Then we do this for the rest of the array, and multiply the answer
        given by this multiplier + 1.

    NOTE: Yet another slight speedup, since sum(range(1, x)) is equal to the xth triangle number,
        we can replace that with the formula for the xth triangle number, which is (x * (x + 1))/2
    """
    return count_nondivisible(baseDigits(n, 7))


solve.answer = 2129970655314432

"""
A dominating number is a positive integer that has more than half of its digits equal.

For example, 2022 is a dominating number because three of its four digits are equal to 2.
    But 2021 is not a dominating number.

Let D(N) be how many dominating numbers are less than 10**N. For example, D(4) = 603 and D(10) = 21893256.

Find D(2022). Give your answer modulo 1_000_000_007.
"""

from functools import cache
from math import factorial as _factorial

# In order to meet the speed requirement I need to cache the calls to factorial... and comb...
factorial = cache(_factorial)


@cache
def comb(N, k):
    """Binomial coefficient, using the cached factorial method (this is actually faster than using cache(math.comb))"""
    return factorial(N) // (factorial(N - k) * factorial(k))


def modulo(N, mod=None):
    """Simple wrapper to handle if mod is None"""
    if mod:
        return N % mod
    else:
        return N


def D_instance(N, mod=None):
    """
    D but only for numbers of a specific length N, instead of all numbers less than or equal to length N.
        This can be multi-threaded.
    """
    ans = 9 * (  # The things below happened to share a factor of 9 even if for different reasons, so I pulled it out

        # This is for all the numbers of the form xii...iii of length N
        #   where i may or may not be a dominating number, but x definitely isn't
        9 * sum(
            # Note: This is also for all the numbers where the dominating number is 0.
            #   They will also be of this form even if I handled them separately
            comb(N - 1, k) * pow(9, N - 1 - k, mod)

            # For the digits i, we need at least N // 2 + 1 to be a dominating digit and up to all the digits except 1,
            #   because the above 1 handles if all digits are the dominating digit
            for k in range(N // 2 + 1, N)
        )

        # This is for all the numbers of the form xi...iii of length N
        #   where i may or may not be a dominating number, but x definitely is
        + sum(
            comb(N - 1, k) * pow(9, N - 1 - k, mod)
            for k in range(N // 2, N)
        )
    )
    return modulo(ans, mod)


def D(N, mod=None):
    ans = sum(
        D_instance(n, mod) for n in range(1, N + 1)
    )
    return modulo(ans, mod)


def solve(N=2022):
    """
    The problem is to look at all numbers which are N digits or less.
        To simplify let's first make D(N) a recursive method which only calculates solutions for exactly N digits,
            and sums with lower values.

    There are 2 groups of dominating numbers I can think of:
        1. Dominating numbers where the dominating number is 1 through 9
        2. Dominating numbers where the dominating number is 0

    Let's start with the first case:
        It should be fairly obvious that this should be a multiple of 9, because of every number 2022 there are
            corresponding numbers 1011, 3033, 4044, etc...

        So I will only look at dominating numbers where the dominating number is 1, and multiply that by 9.

        Again I see two cases with these numbers:
            1. Where the dominating number is the leading digit.
            2. The dominating number is not the leading digit, and therefor the leading digit can be any digit except 0.

        If the dominating number is the leading digit, then for the remaining N - 1 digits,
            at least (N - 1) // 2 + 1 need to be the dominating number.

            It should be obvious this is basic combinatorics:
                sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range((N - 1) // 2 + 1, N))

                the 9**(N - 1 - k) is for the 9 possible digits that any place
                    which isn't a dominating number could be excluding the dominating number itself.
                This is how many dominating numbers there are with the dominating number is 1,
                    and a leading digit of the dominating number.

        If the dominating number is NOT the leading digit, it is a fairly similar sum:
            8 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))

            The leading 8 is from the 8 possible first digits excluding 0 and the dominating number,
                and then the remaining N - 1 digits need to be at least N // 2 + 1
                digits consisting of the dominating digit.

        So bringing this all together, the number of possible dominating numbers with a dominating digit of 1
            of length N can be represented with:
            sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range((N - 1) // 2 + 1, N))
            + 8 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))

            Multiply by 9 to make generic for any digit from 1 to 9.

    Now for numbers where the dominating digit is 0:
        9 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))

    Bringing this all together, we can see the answer should be:
        9 * (
            sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range((N - 1) // 2 + 1, N))
            + 8 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))
        ) +
        9 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))

        Since they share a multiple of 9 lets remove that. Also lets merge the two sums that share a range
            (we'll need to move the 8* into the sum first):
        9 * (
            sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range((N - 1) // 2 + 1, N))
            + sum(8 * (N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k)
                  + (N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))
        )

        It should be fairly obvious that the inner part of the second sum can be combined,
            and the multiple of 9 extracted back out:

            sum(9 * (N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))
            9 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))

    This gives a final answer of:
        9 * (
            sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range((N - 1) // 2 + 1, N))
            + 9 * sum((N - 1)! / ((N - 1 - k)! * k!) * 9**(N - 1 - k) for k in range(N // 2 + 1, N))
        )

    I might've broken the problem into more steps than are required,
        but we've reached a nice svelte solution in the end.

    One optimization is that (N - 1)! / ((N - 1 - k)! * k!) is clearly the binomial coefficient, with
        args N - 1 and k
    """
    return D(N, 1_000_000_007)


solve.answer = 471745499

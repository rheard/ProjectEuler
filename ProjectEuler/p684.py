"""
Define s(n) to be the smallest number that has a digit sum of n. For example s(10) = 19.

Let S(k) = sum(s(n) for n in range(1, k + 1)). You are given S(20) = 1074.

Further let f_i be the Fibonacci sequence defined by f_0 = 0, f_1 = 1 and f_i = f_i - 2 + f_i - 1 for all i >= 2.

Find sum(S(f_i) for i in range(2, 91)). Give your answer modulo 1_000_000_007.
"""

from multiprocessing import Pool

from ProjectEuler.utils import fibonacci_generator


def S(k, mod=None):
    q, r = divmod(k, 9)
    ten_q_pow = pow(10, q, mod)
    res = 6 * (ten_q_pow - 1) - 9*q + ten_q_pow * r * (r + 3) // 2 - r
    if mod:
        return res % mod
    return res


def solve():
    """
    Starting with s(n): after doing some testing and applying some logic, it should be obvious that
        all answers must be of the form: r9999...999.

    In other words, a lot of 9s to the right followed by the smallest possible number to get to 9; or n % 9.

    So if n = 9*q + r, s(n) = (r + 1) * 10**q - 1

    Now for S(k):
        It should be clear that for a given k the solution will be of the general form:
            1 + 2 + ... + 8 + 9 + 19 + 29 + ... + 89 + 99 + 199 + 299 + ...

        That is generally the solution will be of the form:
            sum(m * 10**0 - 1 for m in range(2, 11))
            + sum(m * 10**1 - 1 for m in range(2, 11))
            + ...
            + sum(m * 10**(q - 1) - 1 for m in range(2, 11))
            + sum(m * 10**q - 1 for m in range(2, r + 2))

            Notice it is limited by the remainder of dividing by 9 on the last option

        Walking through the first sum it should be clearly that the answer is 54 * 10**0 - 9 = 45.
            Similarly, for the second sum the answer comes to 54 * 10**1 - 9.

        So all except the last sum can be reduced to:
            sum(54 * 10**m - 9 for m in range(0, q))
            pulling out the 54:
            54 * sum(10**m - 9 for m in range(0, q))
            with q from the original divmod of the input number with 9.

            Now pulling out the - 9 (muliplying by q for each time):
            54 * sum(10**m for m in range(0, q)) - 9*q

            To reduce the sum: Notice that it is essentially going to be 111...111 of length q.
                The formula for this is (10**q - 1) // 9

            Substituting that in we get:
                6 * (10**q - 1) - 9*q

        Now for the remaining sum...
            sum(m * 10**q - 1 for m in range(2, r + 2))

            First split the sum:
            sum(m * 10**q for m in range(2, r + 2)) - sum(1 for m in range(2, r + 2))

            The second sum here can be moved since it is a constant:
                sum(1 for m in range(0, r))

            It should be clear that this reduces to simply r.

            Now for the remaining, it should be clear that for the sum 10**q is actually a constant:
                10**q * sum(m for m in range(2, r + 2))

            Applying similar logic to the last sum, it should be clear that summing all the numbers from 2 to r + 2
                can be simply reduced via basic geometric sequence formula:

                10**q * r*(2 + r + 1) / 2

            Bringing things together for the last sum we get:
                10**q * r * (2 + r + 1) / 2 - r

        Then everything all together:
            6 * (10**q - 1) - 9*q + 10**q * r * (2 + r + 1) / 2 - r

            where q, r = divmod(k, 9)

    My last trick is to just randomly try to use `pow` with a modulo argument...
        I can't prove thats mathematically sound, but I got the right answer in a second
    """
    with Pool() as tp:
        mod = 1_000_000_007
        fib_numbers_in_question = [(f, mod)
                                   for _, f in zip(range(2, 91), fibonacci_generator(1, 2))]

        return sum(
            res for res in tp.starmap(S, fib_numbers_in_question)
        ) % mod


solve.answer = 922058210

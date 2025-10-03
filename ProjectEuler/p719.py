"""
We define an S-number to be a natural number, n, that is a perfect square
    and its square root can be obtained by splitting the decimal representation of n
    into 2 or more numbers then adding the numbers.

For example, 81 is an S-number because sqrt(81) = 8 + 1.
    6724 is an S-number: sqrt(6724) = 6 + 72 + 4.
    8281 is an S-number: sqrt(8281) = 8 + 2 + 81 = 82 + 8 + 1.
    9801 is an S-number: sqrt(9801) = 98 + 0 + 1.

Further we define T(N) to be the sum of all S numbers n <= N.
    You are given T(10**4) = 41333.

Find T(10**12).
"""

from math import isqrt, log10
from multiprocessing import Pool


def canpartition(i, n=None, orig_n=None, digits=None, cur_digits=0, total=0):
    """
    Can the digits i**2 be partitioned to sum to i?

    Args:
        i (int): The original non-square number to validate.
        n (int): Whats left of the number to partition
        orig_n (int): i**2, simply for convenience.
        digits (int): How many digits are left in n
        cur_digits (int): The number of digits in the current partition.
        total (int): Running total of the partitioning.

    Returns:
        bool: Can this number's square be partitioned?
    """
    if n is None:
        n = orig_n = i**2

    if digits is None:
        digits = int(log10(n)) + 1

    cur_digits += 1
    if digits == cur_digits:
        if orig_n == n:
            return False  # No partitioning was done, we just took the original number!

        total += n
        return total == i

    # Check was happens if we DON'T partition here and just continue
    if canpartition(i, n=n, orig_n=orig_n, digits=digits, cur_digits=cur_digits, total=total):
        return True

    # Check was happens if we DO partition here
    new_n, digit = divmod(n, 10**cur_digits)
    if canpartition(i, n=new_n, orig_n=orig_n, digits=digits - cur_digits, total=total + digit):
        return True

    return False


def S_subtest(j: int):
    """
    Take in j which is a multiple of 9,
        and check if j**2 is an S-number
        and also if (j+1)**2 is an S-number.

    Args:
        j (int): A multiple of 9 guiding the checking as described above.

    Returns:
        list: At most length 2 (if both j**2 and (j+1)**2 are S-numbers), but may be length 1 or 0.
            Will return the square numbers, the actual S-numbers themselves.
    """
    return [
        isq
        for i in (j, j + 1)
        if canpartition(i, n=(isq := i**2), orig_n=isq)
    ]


def S_generator(n: int):
    """Generate all of the S-numbers <= to n"""
    with Pool() as tp:
        for res in tp.imap_unordered(S_subtest, range(9, isqrt(n) + 1, 9), chunksize=10**3):
            for i in res:
                if i <= n:
                    yield i


def T(N):
    return sum(s for s in S_generator(N))


def solve(n=10**12):
    """
    Any S-number must be 0 or 1 mod 9.
        Also because a number's value mod 9 doesn't change when squared or square-rooted,
            the square-root number of all S-numbers must also be 0 or 1 mod 9.

    Initially I solved this by partitioning and it took over 2.5 minutes to solve with multiprocessing.
        canpartition is the recursive optimization I came up with to avoid building lists with actual partitions...

    Multiprocessing is still required but runtime is below 1m now so goal accomplished.
    """
    return T(n)


solve.answer = 128088830547982

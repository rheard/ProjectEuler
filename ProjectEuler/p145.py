"""
Some positive integers n have the property that the sum [n + reverse(n)] consists entirely of odd (decimal) digits.
    For instance, 36 + 63 = 99 and 409 + 904 = 1313.
    We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
    Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10**9)?
"""

from multiprocessing import Pool, cpu_count


def reversible(start, end):
    count = 0
    for n in range(start, end):
        reverse_n = str(n)[::-1]
        if reverse_n[0] == '0':
            # 90 is not a reversible number by problem definition even though 90 + 9 = 99
            continue

        this_sum = str(n + int(reverse_n))
        for c in this_sum:
            if c in '02468':
                break
        else:
            count += 1
    return count


def solve(n=10**9):
    """No strategy here. Bruteforce."""
    num_chunks = cpu_count()

    chunk_size = n // num_chunks
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_chunks)]

    # Ensure the last chunk includes any remaining numbers
    if ranges:
        ranges[-1] = (ranges[-1][0], n)

    with Pool(processes=num_chunks) as pool:
        results = pool.starmap(reversible, ranges)

    return sum(results)


solve.answer = 608720

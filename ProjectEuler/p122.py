"""
The most naive way of computing n**15 requires fourteen multiplications:

n * n * ... * n = n**15

But using a "binary" method you can compute it in six multiplications:

n * n = n**2
n**2 * n**2 = n**4
n**4 * n**4 = n**8
n**8 * n**4 = n**12
n**12 * n**2 = n**14
n**14 * n = n**15

However it is yet possible to compute it in only five multiplications:

n * n = n**2
n**2 * n = n**3
n**3 * n**3 = n**6
n**6 * n**6 = n**12
n**12 * n**3 = n**15

We shall define m(k) to be the minimum number of multiplications to compute n**k;
    for example m(15) = 5.

For 1 <= k <= 200, find sum(m(k)).
"""

from collections import deque
from math import log2
from multiprocessing import Pool


# Precompute 9/log2(71)
nine_over_log2_71 = 9 / log2(71)


def l_star(n):
    # The chains found. List of tuples, with the tuples being:
    #   First element: Set of numbers found so far.
    #   Second element: The last number found so far.
    if n <= 1:
        return 0

    found_chains = deque([({1}, 1)])
    limit = log2(n) * nine_over_log2_71

    while True:
        new_found_chains = deque()

        for previous_numbers, last_number in found_chains:
            for previous_number in previous_numbers:
                new_last_number = previous_number + last_number

                if new_last_number < n:
                    if len(previous_numbers) + 1 <= limit:
                        new_found_chains.append((previous_numbers | {new_last_number}, new_last_number))
                elif new_last_number == n:
                    return len(previous_numbers)

        found_chains = new_found_chains


def solve(min_k=1, max_k=200):
    """
    This question of finding the minimal number of multiplications is equivalent to finding
        the minimal number of additions. Looking at the above example, finding the
        minimum number of multiplications to form n**15 is equivalent to finding
        the minimum number of additions to form 15:
        1 + 1 = 2
        2 + 1 = 3
        3 + 3 = 6
        6 + 6 = 12
        12 + 3 = 15

    It is thought (but not proven) that finding the shortest addition chain is NP-complete.
        A generalized version is NP-complete.

    If the shortest addition chain is defined as l(n), then we can define a Brauer chain as
        l*(n) where for each a_k in the chain, a_k = a_k-1 + a_j for some j < k. Stated in
        plain english, this means that for each step in the chain the newest element is
        defined as the immediate previous element + some other previous element.

    For n <= 2500, l*(n) == l(n). This is sufficient for this problem.

    However it still needs to be optmized. Multiprocessing can help with that, but for
        n = 197 (the worst case) execution still takes 5-10 seconds or so and upwards of
        6GB of memory.

        By looking at A003313 we are greeted with 2 limits on the length of the addition chain:
        l(n) <= 9/log_2(71) * log_2(n)
        l(n) <= (4/3) * floor(log_2(n)) + 2

        For k <= 214 (which is our area of interest), the first limit produces the smallest
            limit. Most importantly, it is faster to compute.

    Using this limit + multiprocessing on an 8-core Xeon at 3.4GHz, the solution is found in
        less than 35 seconds. The worst case (n=197) only uses 3GB of memory now.
    """
    with Pool(8) as tp:
        return sum(tp.map(l_star, reversed(range(min_k, max_k + 1))))


solve.answer = 1582

"""
The proper divisors of a number are all the divisors excluding the number itself.
    For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
    As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
    forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

import os

from itertools import count

from sympy import divisors

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(n=10**6, k=500):
    """We can solve this method using a similar caching mechanism to previous chain problems."""
    d_vals = list(map(lambda x: sum(divisors(x)[:-1]), range(1, n)))

    def get_chain_length(l):
        l_orig = l
        for i in count(1):
            l = d_vals[l - 1]

            if l == l_orig:
                break

            if l >= n or i >= k:
                return -1

        return i

    chain_lengths = [get_chain_length(x) for x in range(1, n)]
    max_length = max(chain_lengths)
    target_chain = [i + 1 for i, d_val in enumerate(d_vals) if chain_lengths[i] == max_length]
    return min(target_chain)


solve.answer = 14316


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

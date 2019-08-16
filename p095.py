'''
The proper divisors of a number are all the divisors excluding the number itself.
    For example, the proper divisors of 28 are 1, 2, 4, 7, and 14.
    As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
    forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

from __future__ import print_function
from sympy import divisors
from itertools import count


def solve(n=10**6, k=500):
    d_vals = list(map(lambda x: sum(divisors(x)[:-1]), range(1, n)))

    def get_chain_length(l, l_orig=None, chain_length=0):
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


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p095_ans.txt', 'w') as wb:
        wb.write(str(answer))
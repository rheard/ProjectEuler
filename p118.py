"""
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers,
    different sets can be formed. Interestingly with the set {2,5,47,89,631},
    all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once
    contain only prime elements?
"""

from __future__ import print_function
from sympy.utilities.iterables import kbins
from sympy import isprime
from itertools import permutations, product

"""
I took a very simple approach to this problem.

First take the list of all digits converted to strings. Then take the partitions of them.
    Each partition in a partitioning is converted to an integer, and if each partition's
    integer is prime, then this is a valid partitioning. Converted to a sorted tuple,
    and add it to the set, so we can eliminate any duplicates.

A slight speed-up can be given by limiting the number of possible partitions.

For the lower limit, there are no pandigital primes. That is there are no primes which
    have all of the digits 1 through 9 exactly once, so our lower limit is 2 partitions.

For the upper limit, it can be seen that our maximum number of partitions is 6.
    To show this, we can start with a list of the digits:
    1 2 3 4 5 6 7 8 9
    We need to form only primes, so we can rearrange them in a group of primes and a group of
    non-primes:
    2 3 5 7     1 4 6 8 9

    Now the non-primes need to be joined together, or joined to other primes.
    Lets join 8 and 9 next to produce the prime 89:
    2 3 5 7 89      1 4 6

    We could join 1 to one of the others to produce the primes 41 or 61, however
    the remaining number will not be prime. So we must join all 3 together:
    2 3 5 7 641 89

    Thus the maximum number of partitions is 6.

The final speed up is as follows. Instead of generating all of the ordered=1 kbins, and
    eliminating all of the duplicates, we can generate all of the ordered=0 kbins and
    get the product of the permutations of all of the bins with a length greater than 2.
    This will produce 0 duplicates.
"""

def solve():
    cnt = 0

    for i in range(2, 7):
        for groups in kbins([str(x) for x in range(1, 10)], i, ordered=0):
            other_groups = [group for group in groups if len(group) == 1]
            other_nums = [int("".join(group)) for group in other_groups]
            for perm_groups in product(*[permutations(group) for group in groups if len(group) > 1]): 
                perm_nums = [int("".join(group)) for group in perm_groups]
                nums = other_nums + perm_nums
                works = True
                for num in nums:
                    if not isprime(num):
                        works = False
                        break
                if works:
                    cnt += 1

    return cnt


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p118_ans.txt', 'w') as wb:
        wb.write(str(answer))

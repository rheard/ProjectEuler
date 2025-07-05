"""
Let S(A) represent the sum of elements in set A of size n. We shall call it
    a special sum set if for any two non-empty disjoint subsets, B and C,
    the following properties are true:

    1. S(B) != S(C); that is, sums of subsets cannot be equal.
    2. If B contains more elements than C then S(B) > S(C).

For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because
    65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158}
    satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt, a 4K text file with one-hundred sets containing seven to twelve elements
    (the two examples given above are the first two sets in the file), identify all the
    special sum sets, A_1, A_2, ..., A_k, and find the value of S(A_1) + S(A_2) + ... + S(A_k).

NOTE: This problem is related to Problem 103 and Problem 106.
"""

from multiprocessing import Pool

from ProjectEuler.p103 import special_sum_set

with open('ProjectEuler/p105_sets.txt', 'r') as rb:
    __SETS = [tuple(int(x) for x in line.split(',')) for line in rb.readlines()]


def _wrapper(combo):
    if special_sum_set(combo):
        return sum(combo)
    return 0


def solve(sets=None):
    """We simply bruteforce this problem using the code from problem 103."""
    with Pool(6) as tp:
        ans = tp.map(_wrapper, sets or __SETS)

    return sum(ans)


solve.answer = 73702

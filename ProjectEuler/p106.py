"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two
    non-empty disjoint subsets, B and C, the following properties are true:

    i. S(B) != S(C); that is, sums of subsets cannot be equal.
    ii. If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies
    the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4,
    only 1 of these pairs need to be tested for equality (first rule).
    Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.
"""

from itertools import combinations

from sympy.utilities.iterables import kbins


def solve(n=12):
    """
    This was a nightmare of a problem for the simple fact of how vague it is. For instance,
        "need to be tested" can mean different things and no examples are given to clarify.

    Generating the sets as in problem 103 produces the correct number of possible subset pairs,
        so that is easy.

    We are told that a given set contains n strictly increasing elements. This means that any set
        will work to test this provided all of the elements are increasing, so I will use the set
        (1, 2, 3, ..., n)

    We are also told we can assume the set satisfies the second rule. Therefor we are only concerned
        with subsets who have the same number of elements, because if they didn't then they wouldn't
        be equal already according to the second rule.

    Subset pairs where the length of the subsets is 1 do not need to be checked, since the sum of
        one set is always greater the other, because they are disjoint subsets of increasing elements.

    Now we are left with a small portion of the original number of pairs of subsets. For n = 4,
        we are left with 3 pairs left (listed below) and n = 7 we have 175 pairs left.
    (1, 2) (3, 4)
    (1, 3) (2, 4)
    (1, 4) (2, 3)

    Now we have to determine the ones that "need to be tested". After much reading and testing,
        I have determined this to the following meaning, although there are other properties
        that can furthur eliminate options:

        For the first pair listed there, 1<3 and 2<4, so it does not need to be tested.
        For the second pair, 1<2 and 3<4, so it does not need to be tested.
        For the third pair, 1<2 but 4>3, so it needs to be tested.

    At first i thought this to mean that max(B) > x > min(B) for x in C, however this is not the
        case. Instead it should be taken to mean that, for an element x at index i in B,
        the corresponding element y at index i in C is greater than x.

    NOTE: After solving this problem, for n in range(4, 10) we get 1, 5, 20, 70, 231, 735.
        OEIS has this sequence, but fails for the next item. Googling shows other ProjectEuler
        solutions that use an equation with Catalan numbers. However all these equations
        seem to be pulled out of thin air with little to no logical explanation. This performs
        in under 30 seconds and is good enough.
    """
    def generate_pairs(A):
        for item_len in range(2, len(A) + 1):
            for sub_A in combinations(A, item_len):
                for B, C in kbins(sub_A, 2, 0):
                    yield B, C

    return sum(
        1 for B, C in generate_pairs(tuple(range(1, n + 1))) \
        if len(B) == len(C) \
        and len(B) != 1 \
        and not all(x < y for x, y in zip(B, C))
    )


solve.answer = 21384

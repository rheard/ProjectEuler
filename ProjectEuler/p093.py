"""
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations
    (+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
    and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n,
    can be obtained, giving your answer as a string: abcd.
"""

import operator

from itertools import combinations, product, count

from sympy.utilities.iterables import kbins


# This will generate all binary trees with the given leaves.
def generate_trees(leaves):
    # Iterate over all possible groups of 2 bins.
    for these_bins in kbins(leaves, 2, ordered=0):
        # If any of the bins have length greater than 2, then that bin must be broken up into bins
        if any(len(kbin) > 2 for kbin in these_bins):
            single = [x for x in these_bins if len(x) == 1][0][0]
            multiple = [x for x in these_bins if len(x) != 1][0]

            # All possible groups of 2 bins of the child bin.
            for new_bins in generate_trees(multiple):
                yield [single, new_bins]
        else:
            # For all the bins with length 1, extract the singular leaf.
            yield [x[0] if len(x) == 1 else x for x in these_bins]


# This will take in a binary tree of values and a list of operators to apply at the nodes
def compute_tree_value(operators, values):
    this_op = operators[0]
    operators = operators[1:]
    left_val = values[0]
    right_val = values[1]

    if type(left_val) is not float:
        left_vals = list(compute_tree_value(operators, left_val))
    else:
        left_vals = [left_val]

    if type(right_val) is not float:
        right_vals = list(compute_tree_value(operators, right_val))
    else:
        right_vals = [right_val]

    for right_val in right_vals:
        for left_val in left_vals:
            if not (this_op == operator.truediv and right_val == 0):
                yield this_op(left_val, right_val)

            if not (this_op == operator.truediv and left_val == 0) and this_op in [operator.sub, operator.truediv]:
                yield this_op(right_val, left_val)


# This will take in a list of values and possible operators, and compute all the possible expressions with them.
def generate_expression_tree_values(operators, values):
    for tree in generate_trees(values):
        for operator_perm in product(operators, repeat=3):
            for value in compute_tree_value(operator_perm, tree):
                yield value


def solve():
    """
    To start with, since we are looking at digits, we are only concerned with the numbers 0 to 9. Also since
        a < b < c < d, we only care about the combinations and not the permutations of these.

    For each combination of a,b,c,d we generate all possible trees. For example,
        operator
    operator operator
    a      b c      d

    Then we generate all possible groups of operators. By filling in the operators and computing the tree,
        we get all values. This allows us to not worry about parenthesis as any parenthesis would just create
        a different tree which will also be computed. We just have to careful to swap child values if the operator
        is / or -, since order for these matters.
    """
    longest_chain_n = 0
    longest_chain_cat = ''
    for val_perm in combinations([float(x) for x in range(1, 10)], 4):
        values_expressed = {}
        for val in generate_expression_tree_values(
                [operator.add, operator.sub, operator.mul, operator.truediv], val_perm):
            if not val.is_integer() or val <= 0:
                continue

            values_expressed[val] = None

        for i in count(1):
            if i not in values_expressed:
                break

        n = i - 1

        if n > longest_chain_n:
            longest_chain_n = n
            longest_chain_cat = ''.join(str(int(x)) for x in val_perm)

    return longest_chain_cat


solve.answer = 1258

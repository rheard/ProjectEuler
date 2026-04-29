"""
In England the currency is made up of pound, E, and pence, p,
    and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1*E1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can E2 be made using any number of coins?
"""

from copy import copy


def count_possible_currency_in_tree(chosen_currency, currency_left):
    running_sum = sum(chosen_currency)

    # If we are at 200, then this is a combination.
    if running_sum == 200:
        return 1

    # Pop off the next denomination to use in descending order
    current_denomination = currency_left.pop()
    if current_denomination == 1:
        # If we get down to the 1p, then there is only 1 combination possible, that of an extra 1p * (200 - running_sum)
        return 1
    else:
        # Maximum number of coins of this denomination we can still add
        max_i = (200 - running_sum) // current_denomination

        # While we can, add this denomination to the list and continue to the next denomination.
        branch_count = 0
        for i in range(max_i + 1):
            branch_count += count_possible_currency_in_tree(chosen_currency + [current_denomination] * i,
                                                            copy(currency_left))  # Create a copy

    return branch_count


def solve():
    """
    Think of this as working as a tree. For the first denomination (200p),
       You can have 0 or 1. Since for 0, the sum is less than 200 (it's 0),
       we continue to the next denomination; for 100 you can have 0, 1, 2 etc...
       all the way down the tree finding all 200p leaves.
    """
    currency = sorted([1, 2, 5, 10, 20, 50, 100, 200])
    return count_possible_currency_in_tree([], currency)


solve.answer = 73682

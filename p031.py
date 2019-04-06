'''
In England the currency is made up of pound, E, and pence, p,
    and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p).
It is possible to make E2 in the following way:

1*E1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can E2 be made using any number of coins?
'''

from __future__ import print_function


# Think of this as working as a tree. For the first denomination (200p),
#   You can have 0 or 1. Since for 0, the sum is less than 200 (it's 0),
#   we continue to the next denomination; for 100 you can have 0, 1, 2 etc...
#   all the way down the tree finding all 200p leaves.
def count_possible_currency_in_tree(chosen_currency, currency_left):
    running_sum = sum(chosen_currency)

    # If we are at 200, then this is a combination.
    if running_sum == 200:
        return 1

    # Pop off the next denomination to use in descending order
    current_denomination = currency_left.pop()
    if current_denomination == 1:  # If we get down to the 1p, then there is only 1 combination possible, that of an extra 1p * (200 - running_sum)
        return 1
    else:
        # While we can, add this denomincation to the list and continue to the next denomination.
        i = 0
        branch_count = 0
        while running_sum + i * current_denomination <= 200:
            branch_count += count_possible_currency_in_tree(chosen_currency + [current_denomination] * i, [x for x in currency_left])
            i += 1

    return branch_count


def solve():
    currency = sorted([1, 2, 5, 10, 20, 50, 100, 200])
    return count_possible_currency_in_tree([], currency)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p031_ans.txt', 'w') as wb:
        wb.write(str(answer))

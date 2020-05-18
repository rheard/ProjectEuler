"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube.
    By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers
    below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and
    {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like
    {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed;
    otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both
    represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

import os

from itertools import combinations

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def valid_dice():
    for die in combinations(range(10), 6):
        die = set(die)
        die_truths = [x in die for x in range(10)]
        six_or_nine = die_truths[6] or die_truths[9]

        if (die_truths[1] or die_truths[8]) \
                and (die_truths[2] or die_truths[5]) \
                and (die_truths[1] or six_or_nine) \
                and (die_truths[3] or six_or_nine) \
                and (die_truths[4] or six_or_nine) \
                and (die_truths[0] or (die_truths[1] and die_truths[4] and six_or_nine)):
            yield die_truths


def solve():
    """
    The search space for this problem can be reduced by realizing that not all possible dice are valid.
        For instance, in order to represent 25, it is fair to say each die in a pair must have one of each of the
            following:
        0 or 1
        0 or 4
        0 or 9
        1 or 6
        2 or 5
        3 or 6
        4 or 9
        6 or 4
        8 or 1

    Since 6 and 9 can represent each other, each instance of one can be the other. For instance, instead of needing
        1 or 6, a die actually needs 1 or 6 or 9. This makes 4 or 9 and 6 or 4 equivalent. By expanding each
        operation this way and "and"ing them all together, then simplifying we get that each die must have:
        (1 or 8) and (2 or 5) and (1 or 6 or 9) and (3 or 6 or 9) and (4 or 6 or 9) and (0 or (1 and 4 and (6 or 9)))
    """
    dice_combos = 0

    for dice in combinations(valid_dice(), 2):
        six_or_nine = [die[6] or die[9] for die in dice]
        if (dice[0][0] and dice[1][1] or dice[1][0] and dice[0][1]) \
                and (dice[0][0] and dice[1][4] or dice[0][4] and dice[1][0]) \
                and (dice[0][0] and six_or_nine[1] or dice[1][0] and six_or_nine[0]) \
                and (dice[0][1] and six_or_nine[1] or dice[1][1] and six_or_nine[0]) \
                and (dice[0][2] and dice[1][5] or dice[1][2] and dice[0][5]) \
                and (dice[0][3] and six_or_nine[1] or dice[1][3] and six_or_nine[0]) \
                and (dice[0][4] and six_or_nine[1] or dice[1][4] and six_or_nine[0]) \
                and (dice[0][8] and dice[1][1] or dice[0][1] and dice[1][8]):
            dice_combos += 1

    return dice_combos


solve.answer = 1217


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

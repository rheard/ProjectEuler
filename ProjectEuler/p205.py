"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1,2,3,4.
Colin has six six-sided (cubic) dice, each with faces numbered 1,2,3,4,5,6.

Peter and Colin roll their dice and compare totals: the highest total wins.
    The result is a draw if the totals are equal.

What is the probability that Pyramidal Peter beats Cubic Colin?
    Give your answer rounded to seven decimal places in the form 0.abcdefg.
"""

from collections import defaultdict
from itertools import product


def solve():
    """
    Well... I'm not good with probabilities.

    The first thing that comes to mind though is to calculate the odds of Colin rolling each of the
        numbers its possible for him to roll.

        Then for each of the numbers its possible for Peter to roll, I just need to add up the odds he beats Colin.

    The real difficult part of this problem that I spent probably 45 minutes on:
        the 0. should be INCLUDED in the text box.
    """
    colins_odds = defaultdict(int)
    colins_total = 0

    for roll in product(range(1, 6 + 1), repeat=6):
        colins_odds[sum(roll)] += 1
        colins_total += 1

    colins_odds = {k: v / colins_total for k, v in colins_odds.items()}
    peters_wins = 0
    peters_rolls = 0

    for roll in product(range(1, 4 + 1), repeat=9):
        peters_rolls += 1
        this_roll = sum(roll)
        peters_wins += sum(v for k, v in colins_odds.items() if k < this_roll)

    return round(peters_wins / peters_rolls, 7)


solve.answer = 0.5731441

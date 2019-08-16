'''
A bag contains one red disc and one blue disc. In a game of chance a
    player takes a disc at random and its colour is noted. After each
    turn the disc is returned to the bag, an extra red disc is added,
    and another disc is taken at random.

The player pays $1 to play and wins if they have taken more blue discs
    than red discs at the end of the game.

If the game is played for four turns, the probability of a player winning
    is exactly 11/120, and so the maximum prize fund the banker should
    allocate for winning in this game would be $10 before they would
    expect to incur a loss. Note that any payout will be a whole number
    of pounds and also includes the original $1 paid to play the game,
    so in the example given the player actually wins $9.

Find the maximum prize fund that should be allocated to a single game
    in which fifteen turns are played.
'''

from __future__ import print_function
from fractions import Fraction
from math import ceil, floor
from itertools import combinations

from lib import prod

'''
This is a relatively easy problem, but here is my approach.

After looking at the game tree, it can be seen that any path where more
    than n/2 number of blue discs have been drawn will win. The odds of a 
    disc being drawn for the kth draw is 1/k for blue discs and 
    (k - 1)/k for red discs. Thus this question is, find the sum of products
    of the form
    1/2 * 1/3 * 1/4 * ... where at most n/2 are allowed to take the form
    (k - 1)/k instead of 1/k.

Looking at it this way, finding the odds is a simple combinatorics problem.
    Lastly to get the capital required, we inverted the odds and round down.
'''


def odds(draws):
    max_red_draws = ceil(draws / 2) - 1
    running_sum = Fraction(0, 1)
    for red_draw_cnt in range(max_red_draws + 1):
        for red_draws in combinations(range(draws), red_draw_cnt):
            running_sum += prod(Fraction(draw + 1, draw + 2) if draw in red_draws else Fraction(1, draw + 2) for draw in range(draws))
    return running_sum


def solve(draws=15):
    return floor(1/odds(draws))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p121_ans.txt', 'w') as wb:
        wb.write(str(answer))

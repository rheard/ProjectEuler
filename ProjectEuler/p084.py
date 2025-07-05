# TODO: Return to this problem with probabilities instead of randomness

"""
In the game, Monopoly, the standard board is set up in the following way:

GO  A1  CC1 A2  T1  R1  B1  CH1 B2  B3  JAIL
H2                                      C1
T2                                      U1
H1                                      C2
CH3                                     C3
R4                                      R2
G3                                      D1
CC3                                     CC2
G2                                      D2
G1                                      D3
G2J F3  U2  F2  F1  R3  E3  E2  CH2 E1  FP
A player starts on the GO square and adds the scores on two 6-sided dice to determine
    the number of squares they advance in a clockwise direction. Without any further rules
    we would expect to visit each square with equal probability: 2.5%.
    However, landing on G2J (Go To Jail), CC (community chest), and CH (chance)
    changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail,
    if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll.
    Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH
    they take a card from the top of the respective pile and, after following the instructions,
    it is returned to the bottom of the pile. There are sixteen cards in each pile,
    but for the purpose of this problem we are only concerned with cards that order a movement;
    any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
    1. Advance to GO
    2. Go to JAIL

Chance (10/16 cards):
    1. Advance to GO
    2. Go to JAIL
    3. Go to C1
    4. Go to E3
    5. Go to H2
    6. Go to R1
    7. Go to next R (railway company)
    8. Go to next R
    9. Go to next U (utility company)
    10. Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is,
    the probability of finishing at that square after a roll. For this reason it should be clear that,
    with the exception of G2J for which the probability of finishing on it is zero,
    the CH squares will have the lowest probabilities, as 5/8 request a movement to another square,
    and it is the final square that the player finishes at on each roll that we are interested in.
    We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore
    the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers
    to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
    E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the
    six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""

import os

from random import sample, choice
from collections import deque
from math import ceil


def solve(sides=4, rolls=10**6):
    """No strategy here. Just play the game a bunch until we get an idea of the value."""
    possible_rolls = [(i + j, i, j) for i in range(1, sides + 1) for j in range(1, sides + 1)]
    board_lands = [0] * 40
    board_lands[0] += 1

    CC_locations = [2, 17, 33]
    CH_locations = [7, 22, 36]

    CC_cards = [lambda x: 0,
                lambda x: 10] + \
               [lambda x: x] * 14

    CH_cards = [lambda x: 0,
                lambda x: 10,
                lambda x: 11,
                lambda x: 24,
                lambda x: 39,
                lambda x: 5] + \
               [lambda x: (int(ceil((x - 4.0) / 10)) * 10 + 5) % 40] * 2 + \
               [lambda x: 28 if 12 <= x < 28 else 12,
                lambda x: x - 3] + \
               [lambda x: x] * 6

    CC_deck = deque(sample(range(16), k=16))
    CH_deck = deque(sample(range(16), k=16))
    doubles_count = 0
    location = 0

    for roll_i in (choice(possible_rolls) for _ in range(rolls)):
        if roll_i[1] == roll_i[2]:
            doubles_count += 1

            if doubles_count >= 3:
                location = 10
                doubles_count = 0
                board_lands[location] += 1
                continue
        else:
            doubles_count = 0

        location = (location + roll_i[0]) % 40

        if location in CC_locations:
            # Comunity Chest
            location = CC_cards[CC_deck[0]](location)
            CC_deck.rotate(-1)
        elif location in CH_locations:
            # Chance
            location = CH_cards[CH_deck[0]](location)
            CH_deck.rotate(-1)
        elif location == 30:
            location = 10

        board_lands[location] += 1

    odds = sorted([(i, float(x) / sum(board_lands)) for i, x in enumerate(board_lands)], key=lambda x: x[1], reverse=True)

    return ''.join(str(x[0]) for x in odds[:3])


solve.answer = 101524

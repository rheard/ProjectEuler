"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example,
    a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example,
    both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
    if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD      2C 3S 8S 8D TD  Player 2
        Pair of fives       Pair of Eights

2       5D 8C 9S JS AC      2C 5C 7D 8S QH  Player 1
        Highest card Ace    Highest card Queen

3       2D 9C AS AH AC      3D 6D 7D TD QD  Player 2
        Three Aces          Flush with Diamonds

4       4D 6S 9H QH QC      3D 6D 7H QD QS  Player 1
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven

5       2H 2D 4C 4D 4S      3C 3D 3S 9S 9D  Player 1
        Full House          Full House
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
    Each line of the file contains ten cards (separated by a single space):
    the first five are Player 1's cards and the last five are Player 2's cards.
    You can assume that all hands are valid (no invalid characters or repeated cards),
    each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from itertools import chain


_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

with open('ProjectEuler/p054_poker.txt', 'r') as rb:
    # This dealset will be structured as:
    #     [deal for deal in set]
    # where a deal is defined as
    #     [hand for hand in deal]
    # where a hand consists of 5 cards having the format
    #     (index in the array above, char with the suit)
    __DEAL_SET = [
        [sorted(x[:5], reverse=True), sorted(x[5:], reverse=True)]
        for x in (
            [(_values.index(y[0]), y[1]) for y in z.strip().split(' ')]
            for z in rb.readlines()
        )
    ]


# Input is a list of hands, output is the index of the winner
def winner(deal):
    # We should sort here, but, we sort when we build the list above. Its ok to assume the input should be sorted.
    # deal is a list of players, where players are dictionaries. The dictionaries hold the dealt hand, but will also
    #   hold results of analysis, for instance whether or not the player has a flush, etc.
    deal = list({'index': i, 'hand': x, '3kind': (-1, -1)} for i, x in enumerate(deal))

    for player in deal:
        player['flush'] = [card[0] for card in player['hand']] \
            if len(set(card[1] for card in player['hand'])) == 1 \
            else []

        player['straight'] = player['hand'][0][0] \
            if all(player['hand'][0][0] - i == player['hand'][i][0] for i in range(1, 5)) \
            else -1

        player['straight_flush'] = player['straight'] if len(player['flush']) != 0 and player['straight'] != -1 else -1

    max_straight_flush_val = max(player['straight_flush'] for player in deal)
    deal = [player for player in deal if player['straight_flush'] == max_straight_flush_val]

    if len(deal) == 1:
        return deal[0]['index']

    for player in deal:
        player['card_counts'] = [0 for _ in _values]
        for card in player['hand']:
            player['card_counts'][card[0]] += 1

        player['4kind'] = -1 if 4 not in player['card_counts'] else player['card_counts'].index(4)
        player['3kind'] = -1 if 3 not in player['card_counts'] else player['card_counts'].index(3)
        player['2kind'] = sorted([i for i, x in enumerate(player['card_counts']) if x == 2], reverse=True)
        player['full_house'] = (-1, -1) \
            if player['3kind'] == -1 or len(player['2kind']) == 0 \
            else (player['3kind'], player['2kind'][0])

    max_4kind_val = max(player['4kind'] for player in deal)
    deal = [player for player in deal if player['4kind'] == max_4kind_val]

    if len(deal) == 1:
        return deal[0]['index']

    for i in range(2):
        max_full_house_val = max(player['full_house'][i] for player in deal)
        deal = [player for player in deal if player['full_house'][i] == max_full_house_val]

        if len(deal) == 1:
            return deal[0]['index']

    if any(len(player['flush']) != 0 for player in deal):
        deal = [player for player in deal if len(player['flush']) != 0]

        if len(deal) == 1:
            return deal[0]['index']

        for i in range(5):
            max_flush_val = max(chain(player['flush'] for player in deal))
            deal = [player for player in deal if player['flush'][i] == max_flush_val]

            if len(deal) == 1:
                return deal[0]['index']

    max_straight_val = max(player['straight'] for player in deal)
    deal = [player for player in deal if player['straight'] == max_straight_val]

    if len(deal) == 1:
        return deal[0]['index']

    max_3kind_val = max(player['3kind'] for player in deal)
    deal = [player for player in deal if player['3kind'] == max_3kind_val]

    if len(deal) == 1:
        return deal[0]['index']

    max_2kind_count = max(len(player['2kind']) for player in deal)
    deal = [player for player in deal if len(player['2kind']) == max_2kind_count]

    if len(deal) == 1:
        return deal[0]['index']

    for i in range(max_2kind_count):
        max_2kind_val = max(player['2kind'][i] for player in deal)
        deal = [player for player in deal if player['2kind'][i] == max_2kind_val]

        if len(deal) == 1:
            return deal[0]['index']

    for i in range(5):
        max_val = max(player['hand'][i][0] for player in deal)
        deal = [player for player in deal if player['hand'][i][0] == max_val]

        if len(deal) == 1:
            return deal[0]['index']


def solve(deal_set=None):
    """
    There isn't really a strategy here. There is no math that will provide a nice answer here.
        We just have to emulate poker.
    """
    win_count = [0, 0]
    for deal in (deal_set or __DEAL_SET):
        win_count[winner(deal)] += 1

    return win_count[0]


solve.answer = 376

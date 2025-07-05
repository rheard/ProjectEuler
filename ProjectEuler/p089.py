"""
For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
    Even though the rules allow some numbers to be expressed in more than one way there is always a
    "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
    efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
    but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

with open(r'ProjectEuler\p089_roman.txt', 'r') as rb:
    __NUMERALS = [x.strip() for x in rb.readlines()]


def minimize_numerals(numerals):
    numerals = numerals.replace('IIIII', 'V')
    numerals = numerals.replace('VIIII', 'IX')
    numerals = numerals.replace('IIII', 'IV')
    numerals = numerals.replace('XXXXX', 'L')
    numerals = numerals.replace('LXXXX', 'XC')
    numerals = numerals.replace('XXXX', 'XL')
    numerals = numerals.replace('CCCCC', 'D')
    numerals = numerals.replace('DCCCC', 'CM')
    numerals = numerals.replace('CCCC', 'CD')
    return numerals


def solve(numerals=None):
    """This problem can be solved quite simply with a series of replace calls."""
    numerals = numerals or __NUMERALS
    return sum(len(numeral) - len(minimize_numerals(numeral)) for numeral in numerals)


solve.answer = 743

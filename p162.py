"""
In the hexadecimal number system numbers are represented using different digits:

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.

The hexadecimal number AF when written in the decimal number system equals 10 * 16 + 15 = 175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0, 1 and A are all present.
    Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits
    exist with all of the digits 0, 1, and A present at least once?

Give your answer as a hexadecimal number.

(A, B, C, D, E and F in upper case, without any leading or trailing code that marks the number as hexadecimal
    and without leading zeroes, e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
"""

import os

from itertools import combinations, permutations

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def digit_count(r):
    """
    This method solves the problem for a single target length.

    This is relatively straight forward and the simplest way I could think to solve the problem.

    Basically to start just get all combinations of SPOTs to put our 3 numbers,
        then all OPTIONs for each target digit in those 3 spots.

    From there each remaining digit is VARIABLE and can be permuted to find the solution.
    """
    output = 0
    for c in combinations(list(range(r)), r=3):  # Choose where to place our 3 digits
        for o in permutations(['1', '0', 'A']):  # Choose which digits go where
            if c[0] == 0 and o[0] == '0':
                continue  # Don't count numbers with a leading 0

            # Not an actual number, but will represent the map of digits which can still be permuted
            number = ['X'] * r

            # Put the chosen options in the chosen spots in the variable map
            for i, v in zip(c, o):
                number[i] = v

            choices_this_number = 1
            seen_numbers = set()
            # For each remaining variable, find the number of possible choices of digits for that spot:
            for i, digit in enumerate(number):
                if digit != 'X':
                    # The only real "trick" here is to exclude the chosen options to the left of the current variable
                    #   as a choice for the current variable.
                    # This is because there will be a later permutations of options and spots
                    #   to represent the current variable, and counting it here will count that actual number twice
                    seen_numbers.add(digit)
                    continue

                # Choices for a hexadecimal digit, excluding duplicates, and remove 0 if this is a leading variable
                choices = {hex(x)[2:].upper() for x in range(0, 16)}
                choices -= seen_numbers

                if i == 0:
                    choices.remove('0')  # No leading 0

                choices_this_number *= len(choices)  # Permutations for this spot/options choices

            output += choices_this_number

    return output



def solve(max_r=16):
    """Relatively straight forward. Solve for each length of number, then sum up all the lengths below our target"""
    return hex(sum(digit_count(r) for r in range(3, max_r + 1)))[2:].upper()


solve.answer = '3D58725572C62302'


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
    For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
        the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the
    shortest possible secret passcode of unknown length.
"""


def solve():
    """
    Since keylog.txt does not contain hundreds of lines, it is possible to solve this by hand as so:
        (Format follows {entered_key: updated working solution})

    319: 319
    680: 680 or 319
    180: 3 (6 or 1) (80 or 9)
    690: 3 (6 or 1) (8 or 9) 0
    129: 3 (6 or 1) 2 (8 or 9) 0
    620: 3 (6 or 1) 2 (8 or 9) 0
    762: (3 or 7) (6 or 1) 2 (8 or 9) 0
    689: (3 or 7) (6 or 1) 2890
    762: (3 or 7) (6 or 1) 2890
    318: (3 or 7) (6 or 1) 2890
    368: (3 or 7) (6 or 1) 2890
    710: (3 or 7) (6 or 1) 2890
    720: (3 or 7) (6 or 1) 2890
    710: (3 or 7) (6 or 1) 2890
    629: (3 or 7) (6 or 1) 2890
    168: (3 or 7) 162890
    160: (3 or 7) 162890
    689: (3 or 7) 162890
    716: (3 or 7) 162890
    731: 73162890

    All following combinations will math for 73162890.
    """
    return 73162890


solve.answer = 73162890

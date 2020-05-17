"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

from __future__ import print_function

import os
import string

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


with open('ProjectEuler/names.txt', 'r') as rb:
    _NAME_LIST = [x.strip('"') for x in rb.read().split(',')]


def namescore(i, name):
    name = name.upper()
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in name) * i


def solve(name_list=None):
    """No strategy here. Bruteforce."""
    name_list = sorted(name_list or _NAME_LIST)
    return sum((namescore(i + 1, name) for i, name in enumerate(name_list)))


solve.answer = 871198282


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

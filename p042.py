"""
The nth term of the sequence of triangle numbers is given by,
    t_n = 0.5 * n * (n + 1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
    and adding these values we form a word value. For example, the word value for SKY is
    19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
    common English words, how many are triangle words?
"""

from __future__ import print_function

import os

try:
    from .utils import output_answer, triangle
except ImportError:
    from utils import output_answer, triangle


with open('ProjectEuler/words.txt', 'r') as rb:
    __WORDS = [x.strip('"') for x in rb.read().split(',')]


def solve(words=None):
    """No strategy here. Bruteforce."""
    triangle_numbers = set(triangle(n) for n in range(1, 100))

    def get_word_value(word):
        return sum(ord(x) - 0x60 for x in word.lower())

    def triangle_word(word):
        return get_word_value(word) in triangle_numbers

    triangle_words = [x for x in (words or __WORDS) if triangle_word(x)]

    return len(triangle_words)


solve.answer = 162


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

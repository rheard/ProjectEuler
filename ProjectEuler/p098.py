"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively,
    we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions,
    the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE)
    a square anagram word pair and specify further that leading zeroes are not permitted,
    neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
    common English words, find all the square anagram word pairs
    (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

from collections import defaultdict
from itertools import count

with open('ProjectEuler/p042_words.txt', 'r') as rb:
    __WORDS = [x.strip('"') for x in rb.read().split(',')]


def create_mapping(x, y):
    """
    Creates a mapping that map x to y.

    Returns:
        A tuple of integers, that maps the index in x to the integer index in y.
    """
    mapping = []
    for char in x:
        char_index = y.index(char)
        mapping.append(char_index)
        y = y[:char_index] + '_' + y[char_index + 1:]

    return tuple(mapping)


def solve(words=None):
    """
    Here are the steps I thought of to solve this problem:
    1) Sort the words based on length. Only words that have the same length can be anagrams.
    2) Group the words based on character makeup. eg ('N', 'O') is the character makeup for 'NO' and 'ON'.
        Only words that contain the exact same characters can be anagrams.
    3) Remove words that do not have other words with identical charcter makeups.
    4) Sort and group squares based on digit length and digit makeup, similar to how words were just done.
        We only care about squares that have an identical length to words that are still left.
    5) Group words by the mapping between each other instead of by their character makeup.
    6) Find the mapping between squares, find word-pairs with the exact same mapping, and check that they
        work with the rules given the current square-pair. If everything checks out, see if the square-pair
        contains a new largest square and capture it.

    By the end of this, the last captured square is the largest square of interest.
    """
    # First, sort all the words by their length. No use trying to map words of different lengths.
    sorted_words = defaultdict(list)
    words = words or __WORDS

    for word in words:
        sorted_words[len(word)].append(word)

    # Next, group words together that are made up of the same letters.
    grouped_words = defaultdict(lambda: defaultdict(list))
    for word_len, words in sorted_words.items():
        for word in words:
            grouped_words[word_len][tuple(sorted(word))].append(word)

    del sorted_words

    # Lets get rid of word groupings that only consist of 1 word. They won't be matched against anything.
    for word_len, hashed_words in list(grouped_words.items()):
        for word_hash, words in list(hashed_words.items()):
            if len(words) <= 1:
                del hashed_words[word_hash]
        if len(hashed_words) <= 1:
            del grouped_words[word_len]

    # We only care about words that have a length of possible word lengths.
    max_word_len = max(grouped_words)

    # Next, we sort the possible squares by their length.
    sorted_squares = defaultdict(list)
    for i in count(1):
        str_i_sq = str(i**2)
        if len(str_i_sq) in grouped_words:
            sorted_squares[len(str_i_sq)].append(str_i_sq)
        elif len(str_i_sq) > max_word_len:
            break

    # Now, group squares together that are made up of the same digits.
    grouped_squares = defaultdict(lambda: defaultdict(list))
    for square_len, squares in sorted_squares.items():
        for square in squares:
            grouped_squares[square_len][tuple(sorted(square))].append(square)

    del sorted_squares

    # Similar to word groupings, remove groups that consist of only 1 square.
    for square_len, hashed_squares in list(grouped_squares.items()):
        for square_hash, squares in list(hashed_squares.items()):
            if len(squares) <= 1:
                del hashed_squares[square_hash]
        if len(hashed_squares) <= 1:
            del grouped_squares[square_len]

    mapped_words = defaultdict(lambda: defaultdict(list))

    # Group words by mappings. So for each group of words that consist of only the same letters,
    #   create the mapping that goes from word1 to word2, and group the pairs of words by their mappings.
    #   Both ways (word1 -> word2 and word2 -> word1) must be done for either squares or words. Since there
    #   are more squares than words, lets do it for words.
    for word_len, hashed_words in grouped_words.items():
        for word_hash, words in hashed_words.items():
            for i, word in enumerate(words):
                for other_word in words[i + 1:]:
                    mapped_words[word_len][create_mapping(word, other_word)].append((word, other_word))
                    mapped_words[word_len][create_mapping(other_word, word)].append((other_word, word))

    del grouped_words
    largest_square = 0

    # Finally, lets map the squares to each other and then match the word mappings to the square mappings.
    for square_len, hashed_squares in grouped_squares.items():
        for square_hash, squares in hashed_squares.items():
            for i, square in enumerate(squares):
                for other_square in squares[i + 1:]:
                    mapping = create_mapping(square, other_square)
                    if mapping in mapped_words[square_len]:
                        for word1, word2 in mapped_words[square_len][mapping]:
                            # Check the character -> number mappings.
                            # A character cannot map to more than 1 value.
                            # Multiple characters cannot map to the same value.
                            char_mapping = {}

                            for i, char in enumerate(word1):
                                if char not in char_mapping:
                                    char_mapping[char] = square[i]
                                if char_mapping[char] != square[i] or list(char_mapping.values()).count(square[i]) > 1:
                                    break
                            else:
                                # We found a compatible mapping.
                                largest_square = max(largest_square, int(square))
                                largest_square = max(largest_square, int(other_square))

    return largest_square


solve.answer = 18769

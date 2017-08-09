'''
The nth term of the sequence of triangle numbers is given by,
    t_n = 0.5 * n * (n + 1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position
    and adding these values we form a word value. For example, the word value for SKY is
    19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand
    common English words, how many are triangle words?
'''


def solve():
    triangle_numbers = set(0.5 * n * (n + 1) for n in range(1, 100))

    word_list = None
    with open('ProjectEuler/words.txt', 'r') as rb:
        word_list = [x.strip('"') for x in rb.read().split(',')]

    def get_word_value(word):
        return sum([ord(x) - 0x60 for x in word.lower()])

    def triangle_word(word):
        return get_word_value(word) in triangle_numbers

    triangle_words = [x for x in word_list if triangle_word(x)]

    return len(triangle_words)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p042_ans.txt', 'w') as wb:
        wb.write(str(answer))

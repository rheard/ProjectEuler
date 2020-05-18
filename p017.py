"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
    115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage.
"""

import os

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

ones_place_wordlen = [
    len("zero"),
    len("one"),
    len("two"),
    len("three"),
    len("four"),
    len("five"),
    len("six"),
    len("seven"),
    len("eight"),
    len("nine"),
    len("ten"),
    len("eleven"),
    len("twelve"),
    len("thirteen"),
    len("fourteen"),
    len("fifteen"),
    len("sixteen"),
    len("seventeen"),
    len("eighteen"),
    len("nineteen"),
]

tens_place_wordlen = [
    None,
    None,
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety"),
]


# This is only built for 0 <= n <= 1000
def num_wordlen(n):
    """
    Convert a number to its English word representation.

    Notes:
        Only works for numbers 0 <= n <= 1000
    """
    if n < 20:
        return ones_place_wordlen[n]
    elif n == 1000:
        return len("OneThousand")  # One Thousand (don't count the space)
    else:
        str_n = str(n)
        while len(str_n) < 3:
            str_n = '0' + str_n

        running_sum = 0
        last_two_val = int(str_n[-2:])
        hundreds_place = int(str_n[-3])
        if last_two_val >= 20:
            ones_place = int(str_n[-1])
            if ones_place != 0:
                running_sum += ones_place_wordlen[ones_place]

            tens_place = int(str_n[-2])
            if tens_place != 0:
                running_sum += tens_place_wordlen[tens_place]
        elif last_two_val != 0:
            running_sum += num_wordlen(last_two_val)

        if (last_two_val != 0) and hundreds_place != 0:
            running_sum += 3  # 'and'

        if hundreds_place != 0:
            running_sum += ones_place_wordlen[hundreds_place] + 7

        return running_sum


def solve():
    """No strategy here. Bruteforce."""
    return sum(num_wordlen(x) for x in range(1, 1001))


solve.answer = 21124


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

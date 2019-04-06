'''
Comparing two numbers written in index form like 2**11 and 3**7 is not difficult,
    as any calculator would confirm that 2**11 = 2048 < 3**7 = 2187.

However, confirming that 632382**518061 > 519432**525806 would be much more difficult,
    as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines
    with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''

from __future__ import print_function, division

with open('ProjectEuler/base_exp.txt', 'r') as rb:
    global _num_exponents
    _num_exponents = [list(int(i) for i in x.strip().split(',')) for x in rb.readlines()]


def solve(num_exponents=_num_exponents):
    minimum_exponent = min(x for x in num_exponents[1])
    for number in num_exponents:
        number[1] /= minimum_exponent

    numbers = [x[0] ** x[1] for x in num_exponents]

    return numbers.index(max(numbers)) + 1


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p099_ans.txt', 'w') as wb:
        wb.write(str(answer))

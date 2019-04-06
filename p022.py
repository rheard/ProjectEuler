'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

from __future__ import print_function

_name_list = []
with open('ProjectEuler/names.txt', 'r') as rb:
    _name_list = [x.strip('"') for x in rb.read().split(',')]


def namescore(i, name):
    name = name.upper()
    alphabet = [chr(0x41 + j) for j in range(26)]

    return sum(alphabet.index(letter) + 1 for letter in name) * i


def solve(name_list=_name_list):
    name_list = sorted(name_list)
    return sum((namescore(i + 1, name) for i, name in enumerate(name_list)))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p022_ans.txt', 'w') as wb:
        wb.write(str(answer))

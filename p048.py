'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

from __future__ import print_function


def solve(n=1000):
    return str(sum(x**x for x in range(1, n + 1)))[-10:]


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p048_ans.txt', 'w') as wb:
        wb.write(str(answer))

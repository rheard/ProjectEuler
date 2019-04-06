'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from __future__ import print_function
from sympy import primefactors


def solve(n=600851475143):
    answer = max(primefactors(n))
    return answer


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p003_ans.txt', 'w') as wb:
        wb.write(str(answer))

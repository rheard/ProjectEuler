'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

from math import factorial


def solve(n=100):
    return sum(int(x) for x in str(factorial(n)))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p020_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from __future__ import print_function


def solve(n=1000):
    target_sum = 0
    for num in range(3, n, 3):
        target_sum += num

    for num in range(5, n, 5):
        if num % 3 != 0:
            target_sum += num

    return target_sum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p001_ans.txt', 'w') as wb:
        wb.write(str(answer))

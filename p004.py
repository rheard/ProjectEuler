'''
A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from __future__ import print_function


def is_palindromic(n):
    n = str(n)
    return n == n[::-1]


def solve(n=3):
    largest_ans = 0
    min_number = 10**(n - 1) - 1
    for i in range(10**n - 1, min_number, -1):
        for j in range(i, min_number, -1):
            target_num = i * j
            if is_palindromic(target_num) and target_num > largest_ans:
                largest_ans = target_num

    return largest_ans


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p004_ans.txt', 'w') as wb:
        wb.write(str(answer))

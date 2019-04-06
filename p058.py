'''
Starting with 1 and spiralling anticlockwise in the following way,
    a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
    but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
    that is, a ratio of 8/13 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
    If this process is continued, what is the side length of the square spiral for which the ratio of primes
    along both diagonals first falls below 10%?
'''

from __future__ import print_function
from sympy import isprime


def right_lower_diag(n):
    return n**2


def right_upper_diag(n):
    return (4 * n**2) - 10 * n + 7


def left_upper_diag(n):
    return 4 * n**2 + 1


def left_lower_diag(n):
    return (4 * n**2) - 6 * n + 3


def solve(n=0.1):
    prime_count = 0.0
    number_count = 1
    half_side_length = 0

    while True:
        half_side_length += 1
        number_count += 4

        corners = [left_lower_diag(half_side_length + 1),
                   left_upper_diag(half_side_length),
                   right_upper_diag(half_side_length + 1)]

        for number in corners:
            if isprime(number):
                prime_count += 1

        if prime_count / number_count < n:
            break

    return half_side_length * 2 + 1


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p058_ans.txt', 'w') as wb:
        wb.write(str(answer))

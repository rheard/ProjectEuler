'''
Let r be the remainder when (a-1)**n + (a+1)**n is divided by a**2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 which is 42 mod 49.
    And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 <= a <= 1000, find sum(r_max).
'''

from __future__ import print_function

'''
By making a function to look for r_max with n between 1 and 1000, 
    and a between 5 and 10, we are given the sequence:
    20, 24, 42, 48, 72, ...

By plugging this into OEIS, we are greeted with A159469 which
    actually links to this problem. Conveniently we are told that
    r_max of a = a**2 - 2*a if a is even, otherwise a**2 - a.
    or
    r_max of a = a**2 - a*(3 + (-1)**a)/2
    or
    r_max of a = a*(exp(a)*a - sinh(a))

The last causes OverflowError for sinh, since it uses floats.

Of the remaining 2 options, the first is twice as fast, so we'll use that.
'''


def solve(max_n=1000):
    return sum(a**2 - (a if a & 1 else 2*a) for a in range(3, max_n + 1))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p120_ans.txt', 'w') as wb:
        wb.write(str(answer))

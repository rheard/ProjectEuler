"""
A row of five black square tiles is to have a number of its tiles replaced with
    coloured oblong tiles chosen from red (length two), green (length three),
    or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

[x|x| | | ]     [ |x|x| | ]     [ | |x|x| ]     [ | | |x|x]
[x|x|x|x| ]     [x|x| |x|x]     [ |x|x|x|x]

If green tiles are chosen there are three ways.

[x|x|x| | ]     [ |x|x|x| ]     [ | |x|x|x]

And if blue tiles are chosen there are two ways.

[ |x|x|x|x]     [x|x|x|x| ]

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
    replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in
    length be replaced if colours cannot be mixed and at least one coloured
    tile must be used?

NOTE: This is related to Problem 117.
"""

from __future__ import print_function

"""
Problem 116 is a subset of this problem.

It was already observed thaat problem 116 has a strong link
    to the Fibonacci numbers, because for the red blocks of length 2,
    the number of ways to tile them on an n-length grid is equal to the
    nth Fibonacci number - 1.

After writing a script to find the lower values of this problem for n,
    OEIS reveals the answer for this problem also is linked to Fibnocci numbers.
    Specifically, for a grid of length n, the answer is given as the nth
    tetranacci number (with an offset of 3). 

As hard as I tried, I could not transform the equation for problem 116 to
    tetranacci numbers. There must be some underlying mathematical principle
    connecting them.
"""

def tetranacci():
    a_0 = a_1 = a_2 = 0
    a_3 = 1
    yield a_3
    while True:
        a_0, a_1, a_2, a_3 = a_1, a_2, a_3, (a_0 + a_1 + a_2 + a_3)
        yield a_3


def solve(n=50):
    for k, v in enumerate(tetranacci()):
        if k == n:
            return v


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p117_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
The square root of 2 can be written as an infinite continued fraction.

sqrt(2) = 1 + (1/(2 + 1/(2 + 1/(2 + ...))))
The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2) indicates that 2 repeats ad infinitum.
    In a similar way, sqrt(23) = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.
    Let us consider the convergents for sqrt(2).

1 + (1/2) = 3/2

1 + (1/(2 + (1/2)) = 7/5 = 17/12

1 + (1/(2 + (1/(2 + (1/2)))) = 41/29

Hence the sequence of the first ten convergents for sqrt(2) are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''

from __future__ import print_function
from fractions import Fraction
from itertools import count


def continued_fraction_approx(n, gen):
    yield n

    the_dens = [next(gen)]

    while True:
        this_gen = (x for x in reversed(the_dens))
        continued_fraction = Fraction(1, next(this_gen))

        for x in this_gen:
            continued_fraction = Fraction(1, x + continued_fraction)

        this_iter = n + continued_fraction

        yield this_iter

        the_dens.append(next(gen))


def solve(n=100):
    def e_approx_generator():
        for k in count(2, 2):
            yield 1
            yield k
            yield 1

    e_approx = continued_fraction_approx(2, e_approx_generator())
    this_iter = None

    for i in range(n):
        this_iter = next(e_approx)

    return sum(int(x) for x in str(this_iter.numerator))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p065_ans.txt', 'w') as wb:
        wb.write(str(answer))

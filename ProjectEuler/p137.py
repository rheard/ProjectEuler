"""
Consider the infinite polynomial series A_F(x) = x*F_1 + x**2*F_2 + x**3*F_3 + ..., where F_k is the kth term in the
    Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, F_k = F_k−1 + F_k−2, F_1 = 1 and F_2 = 1.

For this problem we shall be interested in values of x for which A_F(x) is a positive integer.

Surprisingly A_F(1/2) = (1/2)*1 + (1/2)**2*1 + (1/2)**3*2 + (1/2)**4*3 + (1/2)**5*5 + ...
  = 1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
  = 2
The corresponding values of x for the first five natural numbers are shown below.

x               AF(x)
sqrt(2)−1       1
1/2             2
(sqrt(13)−2)/3  3
(sqrt(89)−5)/8  4
(sqrt(34)−3)/5  5

We shall call A_F(x) a golden nugget if x is rational, because they become increasingly rarer;
    for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.
"""

from ProjectEuler.utils import fibonacci


def solve(n=15):
    """
    Given the problem statement, I searched OEIS for "2,_,_,_,_,_,_,_,_,74049690" and instantly found the equation
        for this problem: Fibonacci(2*n) * Fibonacci(2*n+1)
    """
    return fibonacci(2*n) * fibonacci(2*n + 1)


solve.answer = 1120149658760

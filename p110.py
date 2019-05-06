"""
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n
It can be verified that when n = 1260 there are 113 distinct solutions
    and this is the least value of n for which the total number of distinct
    solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions
    exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it
    is well beyond the limitations of a brute force approach it requires a
    clever implementation.
"""

from p108 import solve

"""
For the solution walkthough to this problem, go to Problem 108.
"""

if __name__ == '__main__':
    answer = solve(4 * 10**6)
    print(answer)
    with open('p110_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# This problem was solved by solving the series, 2, 6, 20, ...

from math import factorial


def solve(n=20):
    return factorial(2 * n) // (factorial(n)**2)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p015_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
'''


def sum_of_squares(n):
    return sum(x**2 for x in range(1, n + 1))


def square_of_sum(n):
    return sum(range(1, n + 1))**2


def solve(n=100):
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p006_ans.txt', 'w') as wb:
        wb.write(str(answer))

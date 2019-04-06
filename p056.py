'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large:
    one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
'''

from __future__ import print_function


def solve(n=100):
    def digit_sum(n):
        return sum(int(x) for x in str(n))

    current_max = digit_sum((n - 1) ** (n - 1))

    for i in reversed(range(n)):
        # i as both
        iter_max = digit_sum(i ** i)

        # i as exponent for later numbers
        for j in reversed(range(i + 1, n)):
            this_digit_sum = digit_sum(j ** i)

            if this_digit_sum > iter_max:
                iter_max = this_digit_sum

        # i as base for later numbers
        for j in reversed(range(i + 1, n)):
            this_digit_sum = digit_sum(i ** j)

            if this_digit_sum > iter_max:
                iter_max = this_digit_sum

        if iter_max > current_max:
            current_max = iter_max

    return current_max


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p056_ans.txt', 'w') as wb:
        wb.write(str(answer))

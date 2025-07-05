"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large:
    one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""


def solve(n=100):
    """
    Think of a, b as being on a grid. We have to check each cell for the maximum digital sum.

    We start by saying the max is in the cell where a and b are both (n - 1). Then we work our way backwards along the
        diagonal. So we would go to the cell for a and b being 98. We compute 98 ** 98, and work down for both base
        and exponent, so compute 98 ** 97, 97 ** 98, 98 ** 96, 96 ** 98, etc...
    """
    def digit_sum(n_):
        return sum(int(x) for x in str(n_))

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


solve.answer = 972

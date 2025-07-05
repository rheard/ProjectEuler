"""
Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
    so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def solve():
    """
    Instead of finding the proper divisors and summing them,
        we're going to go through each number, and for each multiple in the target range, add to a running sum.
        d will be an array of sums instead of a function.
    """
    def is_amicable(d, limit, n):
        return d[n] != n and d[n] < limit and d[d[n]] == n

    limit = 10000
    d = [0] * limit

    for num in range(1, limit):
        for multiple in range(2 * num, limit, num):
            d[multiple] += num

    return sum(i for i in range(1, limit) if is_amicable(d, limit, i))


solve.answer = 31626

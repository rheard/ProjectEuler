"""
A number where one digit is the sum of the other digits is called a digit sum number or DS-number for short.
    For example, 352, 3003 and 32812 are DS-numbers.

We define S(n) to be the sum of all DS-numbers of n digits or less.

You are given S(3) = 63270 and S(7) = 85499991450.

Find S(2020). Give your answer modulo 10**16.
"""

from math import factorial

from sympy.utilities.iterables import partitions

from ProjectEuler.utils import prod


def S(n=2020, m=None):
    total = 0
    pos_max = m if m else n
    for d_sum in range(1, 10):
        for digits in partitions(d_sum):
            raw_digit_count = sum(digits.values()) + 1

            # This will never happen for n=2020, and was only needed to verify small values of n:
            # if raw_digit_count > n:  # This partitioning with the digit itself would be more than n digits
            #     continue

            digits[d_sum] = digits.get(d_sum, 0) + 1  # Add the digit sum to the number too

            # It is important to include the 0 count as that will affect the number of permutations of the other digits
            zero_count = n - raw_digit_count
            if zero_count > 0:
                digits[0] = zero_count

            position_multiplier = (10**pos_max - 1) // 9

            for d, digit_count in digits.items():
                if d == 0:
                    continue  # minor optimization

                # how many times each digit would appear at each location:
                pos_digit_count = factorial(n - 1) // factorial(digit_count - 1)
                pos_digit_count //= prod(factorial(other_count)
                                         for other_d, other_count in digits.items()
                                         if other_d != d)

                total += position_multiplier * d * pos_digit_count

    return total % 10**m if m else total


def solve(n=2020):
    """
    My first idea is quite straight forward (I think): partition all of the numbers from 1 to 9,
        then count all the unique ways to permute that permutation with the digit itself added in.

    This works however it starts to become apparent around S(12) that this is far too slow.
        I tried using `more_itertools.distinct_permutations`, however it doesn't seem that much faster...
        Switching to sympy's `partitions` method was a nice speed boost here,
            but neither of these solutions will get to S(2020).

    My next idea was to go through each digital position, and count how many times each digit would appear there
        using the partitions. Simple enough, except now the problem becomes: how many times does each digit
            appear at each location?

        I overthought this for months and was off by a factor of 1000 until finally it hit me
            while walking through it with a small example. Lets walk through it
                with the digital sum being 3 and the partitioning being 1+2.

            The DS numbers are:
                123, 132,
                213, 231,
                312, 321.

            Grouping it like this it should be obvious: yes, there is only one 1, and yet it appears in the left-most
                position twice. That is because there are 2 ways to arrange the other digits over the other positions.

        So the number of times a digit appears at a particular position actually deeply depends on the other digits
            and locations!

        It is pretty obvious that the number of times the other digits appear
                in the other n - 1 positions is simply:
            factorial(n - 1) / prod(factorial(other_digit_count) for other_digit, other_digit_count in other_digits)

        keeping in mind that the selected digit would be a part of the other digits if it appears more than once.

    This realization was what I needed to get my algorithm working.
        To get fast enough for n=2020, I just needed to cache factorial and we're done.

    Actually, we're not done... While cleaning up this solution, something I just thought of:
        Since I'm calculating this number as modulo 10**16, and since I'm calculating
            each positional value.... I could just not calculate any of the positions from 17 through 2020?
            I just need to make sure we're still calculating the right number of permutations (using 2020).

    That trick deviates from the definition of S in the problem,
        but it brings the execution time down from 30+ seconds to less than 1 second, and I don't even need to
            cache factorial anymore!

    Yet again while on a walk, I've thought of another optimization:
        I'm going over every position in the number and multiplying by 10**pos, however that is the only time the
            position is used. I'm essentially just multiplying the number by 111...111 of length pos.

        So instead of using a for loop (of length 16), I could just use a repunit?
    """
    return S(n, 16)


solve.answer = 4598797036650685

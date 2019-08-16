'''
The number 512 is interesting because it is equal to the sum of its digits
    raised to some power: 5 + 1 + 2 = 8, and 8**3 = 512.
    Another example of a number with this property is 614656 = 28**4.

We shall define an to be the nth term of this sequence and insist
    that a number must contain at least two digits to have a sum.

You are given that a_2 = 512 and a_10 = 614656.

Find a_30.
'''

from __future__ import print_function
from collections import deque, defaultdict
from itertools import count


'''
Quite simple solution.

power_generator() will generate all powers in order.
a() will take all those and only yield the ones that match the
    problem condition.
solve() will then count those to get to the required n.

Unfortunately, after a lot of optimization, this still takes ~2 minutes
    to run. This isn't completely absurd and I can't figure out how to
    optimize furthur. Everything is sequential, so parallization is off
    the table.
'''


def power_generator():
    def wrapper(val_2, current_max, next_powers):
        for i in count(3):
            pow_i, val_i = current_max[i]
            if val_i < val_2:
                while True:
                    pow_i += 1
                    val_i = i**pow_i
                    next_powers[(val_i, i, pow_i)] = None
                    current_max[i] = (pow_i, val_i)
                    if val_i >= val_2:
                        if pow_i == 2:
                            return
                        break

    next_powers = dict()
    current_max = defaultdict(lambda: (1, 1))
    current_2_power = (2, 4)

    while True:
        pow_2, val_2 = current_2_power
        wrapper(val_2, current_max, next_powers)

        for key in sorted(x for x in next_powers if x[0] < val_2):
            lower_power, base, power = key
            yield base, power, lower_power
            del next_powers[key]

        yield 2, pow_2, val_2
        pow_2 += 1
        current_2_power = (pow_2, 2**pow_2)


def a():
    for base, power, val in power_generator():
        if sum(int(x) for x in str(val)) == base:
            yield val


def solve(n=30):
    n -= 1
    for i, num in enumerate(a()):
        if i == n:
            return num


if __name__ == '__main__':
    answer = solve(25)
    print(answer)
    with open('p119_ans.txt', 'w') as wb:
        wb.write(str(answer))

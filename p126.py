"""
The minimum number of cubes to cover every visible face on a cuboid measuring 3 * 2 * 1 is twenty-two.

If we then add a second layer to this solid it would require forty-six cubes to cover every visible face,
    the third layer would require seventy-eight cubes, and the fourth layer would require
    one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 * 1 * 1 also requires twenty-two cubes;
    similarly the first layer on cuboids measuring 5 * 3 * 1, 7 * 2 * 1, and 11 * 1 * 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers.
    So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
"""

import os

from collections import defaultdict
from itertools import count

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def cuboid_layer_count(x, y, z, layer=1):
    return 2 * (x * y + x * z + y * z) + 4 * (x + y + z + layer - 2) * (layer - 1)


_last_cnts = defaultdict(int)
_last_limit = 0


def solve(n=1000, limit=30000, anustart=True):
    """
    I have tried many solutions to solve this problem, none of which are effective. Giving a limit like this
        and brute forcing a solution is MUCH MUCH MUCH faster than any "smarts" I try to add, such as using
        stars and bars. I am giving up on this... for now.

    Args:
        n (int): The number of shared solutions for i=ab + bc + ac
        limit (int): The max number to search for. Should be quite larger than n. Defaults to 30k
        anustart (bool): Do a new (nu) start? If False, it will use the previous limit and calculations to only
            calculate values between the old limit and the new one. This is for if the solution was not found in
            limit, we don't want to do all that work over again. Defaults to True.

    Returns (int or None):
        The smallest i that has n solutions to i=ab + bc + ac. If no solutions are found within the limit,
        None is returned.
    """
    global _last_cnts
    global _last_limit
    if anustart:
        _last_cnts = defaultdict(int)
        _last_limit = 0

    cnts = _last_cnts
    for x in count(1):
        this_cnt = cuboid_layer_count(x, x, x)
        if this_cnt >= limit:
            break
        if this_cnt < _last_limit:
            continue
        for y in count(x):
            this_cnt = cuboid_layer_count(y, y, x)
            if this_cnt >= limit:
                break
            for z in count(y):
                this_cnt = cuboid_layer_count(x, y, z)
                if this_cnt >= limit:
                    break
                for l in range(1, limit):
                    cnt = cuboid_layer_count(x, y, z, l)
                    if cnt >= limit:
                        break
                    if cnt >= _last_limit:
                        cnts[cnt] += 1

    _last_cnts = cnts
    _last_limit = limit
    for k in sorted(cnts.keys()):
        if k < limit and cnts[k] == n:
            return k

    return None


solve.answer = 18522


if __name__ == '__main__':
    output_answer(solve)

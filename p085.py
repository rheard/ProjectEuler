"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

* * . .     * * * .     * * * *
* * . .     * * * .     * * * *
. . . .     . . . .     . . . .
   6           4           2


* * . .     * * * .     * * * *
* * . .     *   * .     *     *
* * . .     * * * .     * * * *
   3           2           1


Although there exists no rectangular grid that contains exactly two million rectangles,
    find the area of the grid with the nearest solution.
"""

import os

from math import ceil, sqrt

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer


def solve(target_count=2 * 10**6):
    """
    The formula can be derived as follows:

    Start with a 4 x 1 as an example.
    * * . . .       * * * . .       * * * * .       * * * * *
    * * . . .       * * * . .       * * * * .       * * * * *
        4               3               2               1

    So for n x 1, solution is sum(x for x in [1, ..., n]) which is known to be n * (n + 1) / 2

    The same formula can be derived for a 1 x m. By performing the area between these the formulas:
    (n * (n + 1) / 2) * (m * (m + 1) / 2) = n * m * (n + 1) * (m + 1) / 4 = count

    Thus, we want to get as close as possible to
    n * m * (n + 1) * (m + 1) / 4 = target_count
        where target_count = 2 * 10**6

    We can restrict our m and n ranges by doing:
        max_n * min_m * (max_n + 1) * (min_m + 1) = target_count
        Since min_m = 1, it follows:
        max_n = +/- sqrt(8 * target_count + 1) / 2 - 1/2
    """
    closest_count_area = 0
    closest_count_difference = target_count

    max_n = int(ceil((sqrt(8 * target_count + 1) - 1) / 2))
    sum_to_vals = [n * (n + 1) // 2 for n in range(1, max_n + 1)]

    for n in range(1, max_n + 1):
        sum_to_n = sum_to_vals[n - 1]
        for m in range(1, n + 1):
            sum_to_m = sum_to_vals[m - 1]
            this_count = sum_to_n * sum_to_m
            this_difference = abs(target_count - this_count)

            if this_difference < closest_count_difference:
                closest_count_difference = this_difference
                closest_count_area = m * n

    return closest_count_area


solve.answer = 2772


if __name__ == '__main__':
    output_answer(solve)

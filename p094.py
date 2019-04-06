'''
It is easily proved that no equilateral triangle exists with integral length sides and integral area.
    However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the
    third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area
    and whose perimeters do not exceed one billion (1,000,000,000).
'''

from __future__ import print_function
from math import sqrt, floor

'''
Recall from problem 75:
Generating Pythagorean triples:
a = k * (m**2 - n**2)
b = k * 2*m*n
c = k * (m**2 + n**2)
where m, n, k are positive integers
    m > n and m and n are coprime and m and n are not both odd


max_m = (sqrt(2 * max_L + 1) + 1) / 2

We are looking for a triangle where (c + 1) / 2 or (c - 1) / 2 is a or b.
    Through testing it is found that (c + 1) / 2 could equal a and (c - 1) / 2 could equal b,
    but not the other way around

    It can also be found through testing that this only works for fundamental Pythagorean triples,
        eg k will always be 1.

    Another fact gleamed from testing is that this can be a test for Pythagorean triples, eg
        (c + 1) / 2 == a or (c - 1) / 2 == b can only happen if m and n are coprime.
        Since testing for coprime is the most expensive operation here, a significant speed up
        can be gained by doing away with this operation.

    The last fact gleamed from testing is that there is a pattern to the m and n for which this works for.
        This pattern can be seen in the m,n values for the first 5 triangles that this works for:
        m    n
        2    1
        4    1
        7    4
        15   4
        26   15

    so n is the same for 2 triangles, then it's new value is the last m value. This is a major speed improvement,
        by a factor of 500 for max_L=10**7.
'''


def solve(max_L=10**9):
    running_sum = 0
    max_m = int(floor(sqrt(2 * max_L + 1) - 1)) // 2
    n = 1
    n_sq = n**2
    second_time = False

    for m in range(2, max_m + 1):
        m_sq = m**2
        base_a = m_sq - n_sq
        base_b = 2 * m * n
        base_c = m_sq + n_sq
        base = base_a if (base_c + 1) // 2 == base_a else (base_b if (base_c - 1) // 2 == base_b else None)

        if base:
            p = 2 * (base_c + base)

            if p <= max_L:
                running_sum += p

            if second_time:
                n = m
                n_sq = m_sq

            second_time = not second_time

    return running_sum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p094_ans.txt', 'w') as wb:
        wb.write(str(answer))

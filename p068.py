'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

  4
   \
    3
   / \
  1 - 2 - 6
 /
5

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example),
    each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total   Solution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
    What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

from __future__ import print_function
from itertools import permutations

_wrap_ring = lambda inside, i: inside[i % len(inside)]


def working_ring(outside, inside):
    first_summation = outside[0] + inside[0] + inside[1]

    for i, start_val in enumerate(outside):
        if start_val + inside[i] + _wrap_ring(inside, i + 1) != first_summation:
            return False

    return True


def concatenate_solution(solution):
    outside, inside = solution
    concatenated = ''

    for i, start_val in enumerate(outside):
        concatenated += str(start_val)
        concatenated += str(inside[i])
        concatenated += str(_wrap_ring(inside, i + 1))

    return concatenated


def solve(n=5):
    # The following 2 assumptions depend on 2 facts:
    #   We want to maximize the concatenated string
    #   We only want 2 digit numbers once

    # The outside must consist of the number n + 1 through 2 * n
    ordered_outside = list(range(n + 1, 2 * n + 1))

    # The inside must consist of the number 1 through n
    ordered_inside = list(range(1, n + 1))

    # By the ordering, the smallest value must go first on the outside
    possible_outsides = [ordered_outside[:1] + list(x) for x in permutations(ordered_outside[1:])]
    possible_insides = [list(x) for x in permutations(ordered_inside)]

    working_rings = [(possible_outside, possible_inside) for possible_inside in possible_insides
                                                         for possible_outside in possible_outsides
                                                         if working_ring(possible_outside, possible_inside)]

    return max(int(concatenate_solution(solution)) for solution in working_rings)


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p068_ans.txt', 'w') as wb:
        wb.write(str(answer))

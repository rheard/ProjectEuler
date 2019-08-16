'''
Looking at the table below, it is easy to verify that the maximum possible
    sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal)
    is 16 (= 8 + 7 + 1).

-2  5   3   2
9   -6  5   1
3   2   7   3
-1  8   -4  8

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known
    as a "Lagged Fibonacci Generator":

For 1 <= k <= 55, sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000) - 500000.
For 56 <= k <= 4000000, sk = [s_(k-24) + s_(k-55) + 1000000] (modulo 1000000) - 500000.

Thus, s_10 = -393027 and s_100 = 86613.

The terms of s are then arranged in a 2000*2000 table, using the first 2000 numbers to fill the first row
    (sequentially), the next 2000 numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction
    (horizontal, vertical, diagonal or anti-diagonal).
'''

from __future__ import print_function

'''
This problem is pretty straight forward and I would've gotten the solution 10x faster than I did
    if not for this key part of the problem: "find the greatest sum of *(any number of)* adjacent entries."

So for instance, if we were just looking at columns, it isn't "find the greatest sum of any column", instead
    the question is "find the greatest subsequence sum of any column", which changes the problem quite a bit.

    I was going to implement a method to find the greatest subsequence sum, but Google reveals the optimal
    algorithm for the greatest subsequence sum is Kadane's algorithm. Wikipedia is nice enough to give
    a method for this algorithm in Python.
'''


def max_subarray(A):
    '''Credit to Wikipedia, as this was basically copied from there.'''
    A = list(A)
    max_ending_here = max_so_far = A[0]

    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def solve(dimension_size=2000):
    sequence = [None] * dimension_size**2

    for k_sub, _ in enumerate(sequence):
        k = k_sub + 1

        if 1 <= k <= 55:
            sequence[k_sub] = ((100003 - 200003 * k + 300007 * k**3) % 10**6) - 500000
        else:
            sequence[k_sub] = ((sequence[k_sub - 24] + sequence[k_sub - 55] + 10**6) % 10**6) - 500000

    maximum = 0

    # Check horizontals
    for line_number in range(dimension_size):
        maximum = max(maximum, max_subarray(sequence[line_number * dimension_size:(line_number + 1) * dimension_size]))

    # Check verts
    for column_number in range(dimension_size):
        maximum = max(maximum, max_subarray(sequence[column_number + line_number * dimension_size] for line_number in range(dimension_size)))

    # Check diagonal
    for anti in [(lambda x: x), (lambda x: (x // dimension_size) * dimension_size + (dimension_size - (x % dimension_size) - 1))]:
        # Step 1, diagonal along top row
        for top_number in reversed(range(dimension_size)):
            maximum = max(maximum, max_subarray(sequence[anti((dimension_size + 1) * i + top_number)] for i in range(dimension_size - top_number)))

        # Step 2, diagonals along left column.
        for left_number in range(1, dimension_size):
            maximum = max(maximum, max_subarray(sequence[anti((dimension_size * left_number) + i * (dimension_size + 1))] for i in range(dimension_size - left_number)))

    return maximum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p149_ans.txt', 'w') as wb:
        wb.write(str(answer))

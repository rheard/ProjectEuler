"""
A positive integer N is stealthy, if there exist positive integers a, b, c, d
    such that ab = cd = N and a + b = c + d + 1.

For example, 36 = 4 * 9 = 6 * 6 is stealthy.

You are also given that there are 2851 stealthy numbers not exceeding 10**6.

How many stealthy numbers are there that don't exceed 10**14?
"""

from ProjectEuler.utils import triangle_generator


def solve(N_max=10**14):
    """
    This was quite easy to solve for smaller values of N_max by simply creating a datastructure
        along the lines of dict[product, dict[sum, list[tuple]]]

    Then I could simply go over all the pairs of numbers and the product and sums they produce, and then just
        find any sums in the same product that differ by one.

    That was fast enough to solve the problem for 10**6, and it also led me to A072389, which led to two revelations:
        Firstly is that these are called bipronic, and secondly that is because they have the form
            x * (x + 1) * y * (y + 1)

        A pronic would be a number of the form x * (x + 1).
            Therefor stealthy numbers are simply the product of two pronic numbers.

    So I was able to speed up about 20x using this definition and just generating all of the pronic numbers,
        and then multiplying them together to create a set of stealthy numbers.

    Looking at that definition more, I was struck by how pronic numbers were eerily similar to triangle numbers.
        By switching to using my standard triangle number generator,
            and keeping a growing list of all the triangle numbers,
        I was able to get another 4.5x speed boost which was just enough to get below the 60s runtime requirement!
    """
    triangles = list()
    found = set()

    N_max_2 = N_max // 2

    for i in triangle_generator():
        if i >= N_max_2:
            break

        triangles.append(i)  # Append i to the list before going over it, so that we get bipronic numbers where x == y
        for old_triangle in triangles:
            new_stealthy = 4 * i * old_triangle
            if new_stealthy >= N_max:
                break

            found.add(new_stealthy)

    return len(found)

solve.answer = 75737353

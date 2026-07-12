"""
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses
    vertical and horizontal symmetry. For example, using exactly thirty-two square tiles we can form
    two different square laminae:

https://projecteuler.net/resources/images/0173_square_laminas.gif

With one-hundred tiles, and not necessarily using all of the tiles at one time,
    it is possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
"""


def solve(tiles=1_000_000):
    """
    This is a rather easy problem. The important thing to remember is that the squares themselves can be sized
        tiles // 4

    because they are essentially the perimeter of the square, while the holes are always the area within, therefor are
        always the square of their side length. Oh also the holes and squares must obviously have the same parity.

    Keeping that in mind, all one needs to do is for each possible square side, start with the maximal size hole inside,
        and decrease it until we run out of tiles. This is fast enough to solve the problem.
    """
    max_square_side = (tiles // 4) + 1
    output = 0

    for square_side in range(3, max_square_side + 1):
        for hole_side in range(square_side - 2, 0, -2):
            if square_side**2 - hole_side**2 > tiles:
                break
            output += 1

    return output


solve.answer = 1572729

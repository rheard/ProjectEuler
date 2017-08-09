'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def solve():
    is_pythagorean_triplet = lambda a, b, c: a**2 + b**2 == c**2

    product = 0
    for a in range(1, 999):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if is_pythagorean_triplet(a, b, c):
                product = a * b * c

    return product


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p009_ans.txt', 'w') as wb:
        wb.write(str(answer))

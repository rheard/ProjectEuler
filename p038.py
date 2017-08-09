'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product of
    9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
    concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def solve():
    maximum = 0
    all_numbers = [str(x) for x in range(1, 10)]
    for n in range(1, 10000):
        concatenated_products = ''
        i = 1
        while len(concatenated_products) < 9:
            concatenated_products += str(n * i)
            i += 1

        if len(concatenated_products) == 9 and all_numbers == sorted(concatenated_products) and int(concatenated_products) > maximum:
            maximum = int(concatenated_products)

    return maximum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p038_ans.txt', 'w') as wb:
        wb.write(str(answer))
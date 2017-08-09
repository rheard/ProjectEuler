'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits
    0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d_2*d_3*d_4=406 is divisible by 2
d_3*d_4*d_5=063 is divisible by 3
d_4*d_5*d_6=635 is divisible by 5
d_5*d_6*d_7=357 is divisible by 7
d_6*d_7*d_8=572 is divisible by 11
d_7*d_8*d_9=728 is divisible by 13
d_8*d_9*d_10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

# I was trying to avoid using a series of nested for loops for this problem, while keeping the speed up. This is what I came up with.


def numbers_of_interest():
    primes = [2, 3, 5, 7, 11, 13, 17]
    possibilities = [x for x in (str(x) for x in range(102, 988, 2)) if x.count(max(x, key=lambda i: x.count(i))) == 1]

    while len(possibilities) != 0:
        possibility = possibilities.pop()
        prime = primes[len(possibility) - 2]
        minimum_search = int(possibility[-2:] + '0')
        for i in range(minimum_search, minimum_search + 10):
            if i % prime == 0:
                new_char = str(i % 10)
                if new_char not in possibility:
                    new_possibility = possibility + new_char

                    if len(new_possibility) == 9:
                        yield int(new_possibility)
                    else:
                        possibilities.append(new_possibility)


def solve():
    return sum(numbers_of_interest())


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p043_ans.txt', 'w') as wb:
        wb.write(str(answer))

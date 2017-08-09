'''
Surprisingly there are only three numbers that can be written
    as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum
    of fifth powers of their digits.
'''


def solve(n=5):
    maximum = n * 9**n + 1
    running_sum = 0
    for possible_num in range(10, maximum):
        if possible_num == sum(int(x)**n for x in str(possible_num)):
            running_sum += possible_num

    return running_sum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p030_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''


def solve(n=1000):
    return sum(int(x) for x in str(2**n))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p016_ans.txt', 'w') as wb:
        wb.write(str(answer))

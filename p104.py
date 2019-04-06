from lib import fib_generator


def solve():
    pandigital_set = set(str(x) for x in range(1, 10))
    for n, fib in enumerate(fib_generator()):
        fib_str = str(fib)
        if set(fib_str[:10]) == pandigital_set and set(fib_str[-9:]) == pandigital_set:
            return n + 1


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p104_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
'''

from ProjectEuler.lib import fib_generator


def solve(n=4 * 10**6):
    target_sum = 0
    fib_sequence = fib_generator()
    for num in fib_sequence:
        if num >= n:
            break

        if num % 2 == 0:
            target_sum += num

    return target_sum


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p002_ans.txt', 'w') as wb:
        wb.write(str(answer))
'''
The Fibonacci sequence is defined by the recurrence relation:

F.n = F.n−1 + F.n−2, where F.1 = 1 and F.2 = 1.
Hence the first 12 terms will be:

F.1 = 1
F.2 = 1
F.3 = 2
F.4 = 3
F.5 = 5
F.6 = 8
F.7 = 13
F.8 = 21
F.9 = 34
F.10 = 55
F.11 = 89
F.12 = 144
The 12th term, F.12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

from ProjectEuler.lib import fib_generator
from math import log


def solve(n=1000):
    log_10 = log(10)
    for i, fib_num in enumerate(fib_generator()):
        if int(round(log(fib_num) / log_10, 10) + 1) == n:
            return i + 1, fib_num


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p025_ans.txt', 'w') as wb:
        wb.write(str(answer))

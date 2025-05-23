"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
"""

import os

try:
    from utils import fibonacci_generator, output_answer
except ImportError:
    from .utils import fibonacci_generator, output_answer


def solve(n=4 * 10**6):
    """No strategy here. Bruteforce."""
    target_sum = 0
    fib_sequence = fibonacci_generator()
    for num in fib_sequence:
        if num >= n:
            break

        if num % 2 == 0:
            target_sum += num

    return target_sum


solve.answer = 4613732


if __name__ == '__main__':
    output_answer(solve)

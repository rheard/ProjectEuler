import operator
import functools
import fractions

prod = lambda x: functools.reduce(operator.mul, x, 1)


# Generator to cycle through all Fibonacci numbers cleanly
def fib_generator():
    a = 1
    b = 1

    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


# Generator to cycle through all triangle numbers cleanly
def tri_generator():
    running_sum = 0
    i = 1
    while True:
        running_sum += i
        yield running_sum
        i += 1


def gcd(*numbers):
    return functools.reduce(fractions.gcd, numbers)


def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return functools.reduce(lcm, numbers, 1)

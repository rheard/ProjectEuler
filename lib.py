from __future__ import division
from math import factorial
import operator
import functools
import fractions
import math

prod = lambda x: functools.reduce(operator.mul, x, 1)
phi = (1 + math.sqrt(5)) / 2


# Generator to cycle through all Fibonacci numbers cleanly
def fib_generator(a=1, b=1):
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b


def fib(n):
    """Get the nth fibonacci number"""
    return int(round((phi**n - (-phi)**-n) / math.sqrt(5), 0))


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


def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
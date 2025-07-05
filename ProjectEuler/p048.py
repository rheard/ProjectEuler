"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""


def solve(n=1000):
    """No strategy here. Bruteforce."""
    return str(sum(x**x for x in range(1, n + 1)))[-10:]


solve.answer = 9110846700

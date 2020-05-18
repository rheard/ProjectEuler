import os
import time
import multiprocessing

from multiprocessing.pool import Pool

try:
    from .utils import output_answer
except ImportError:
    from utils import output_answer

count = 0


def inc_count(x):
    global count
    if x:
        count += 1


def reversible(n):
    this_sum = str(n + int(str(n)[::-1]))
    for c in this_sum:
        if c in '02468':
            return False
    return True


def solve(n=10**9):
    """No strategy here. Bruteforce."""
    global count
    with Pool(multiprocessing.cpu_count() - 2) as tp:
        add_more = True
        for i in range(1, n):
            while True:
                if tp._taskqueue.qsize() < 1000000:
                    add_more = True
                if tp._taskqueue.qsize() > 2000000:
                    add_more = False
                if not add_more:
                    time.sleep(5)
                    continue
                a = tp.apply_async(reversible, args=[i], callback=inc_count)
                break
    return count


solve.answer = 608720


if __name__ == '__main__':
    output_answer(os.path.splitext(__file__)[0], solve)

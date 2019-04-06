from multiprocessing import Pool
from sympy import sieve
from itertools import count
from math import log10, ceil


def is_prime_pair(p1, p2):
    str_p1 = str(p1)
    log10_p1 = ceil(log10(p1))
    for multiple in count(2*p2, p2):
        if str(multiple % 10**log10_p1).endswith(str_p1):
            return multiple


def solve(min_p1=5, max_p1=10**6):
    sieve.extend(max_p1)
    sieve.extend_to_no(len(sieve._list) + 1)
    with Pool(8) as tp:
        return sum(tp.starmap(is_prime_pair, (x for x in zip(sieve._list, sieve._list[1:]) if min_p1 <= x[0] <= max_p1)))


if __name__ == '__main__':
    ans = solve()
    print(ans)
    with open('p134_ans.txt', 'w') as wb:
        wb.write(str(ans))

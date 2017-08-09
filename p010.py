'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from ProjectEuler.lib import segmented_sieve


def solve(n=2 * 10**6):
    return sum(segmented_sieve(n))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p010_ans.txt', 'w') as wb:
        wb.write(str(answer))

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from ProjectEuler.lib import prime_factors


def solve(n=600851475143):
    answer = max(prime_factors(n))
    return answer


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p003_ans.txt', 'w') as wb:
        wb.write(str(answer))

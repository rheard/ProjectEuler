'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

from decimal import Decimal


def solve(n=1000):
    solution_count = [0] * (n + 1)
    for a in range(1, n - 2):
        for b in range(a, n - 1):
            c = Decimal(a**2 + b**2).sqrt()
            if c % 1 == 0:
                p = int(a + b + c)
                if p <= n:
                    solution_count[p] += 1

    return max(range(n + 1), key=lambda x: solution_count[x])


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p039_ans.txt', 'w') as wb:
        wb.write(str(answer))

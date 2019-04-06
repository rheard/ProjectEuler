from __future__ import print_function

def solve(k=28433, n=7830457, m=10**10):
    '''
    A Proth prime is a prime number of the form k * 2**n + 1.
    A Sierpinski number is a k value that will never produce a prime for all n.

    It is conjectured that 78557 is the smallest Sierpinski number,
        although there were smaller values for which no known prime existed.

    In late 2016, the Proth prime 10223 * 2**31172165 + 1 was found. It was the 7th largest
        prime ever found and currently is the largest known Proth prime.

    This function will return the Proth number k * 2**n + 1 mod m.
    '''
    return (k * pow(2, n, m) + 1) % m


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p097_ans.txt', 'w') as wb:
        wb.write(str(answer))

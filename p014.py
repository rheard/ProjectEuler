'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def collatz_op(n):
    return n / 2 if n % 2 == 0 else 3 * n + 1


def collatz_generator(n):
    yield n
    while n != 1:
        n = collatz_op(n)
        yield n


def solve(n=10**6):
    longest_chain = 0
    longest_chain_i = 0
    found_lengths = {}
    for i in range(1, n):
        chain_length = 0
        for number in collatz_generator(i):
            if number in found_lengths:
                chain_length += found_lengths[number]
                break

            chain_length += 1

        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_chain_i = i

    return longest_chain_i


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p014_ans.txt', 'w') as wb:
        wb.write(str(answer))

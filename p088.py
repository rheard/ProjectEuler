'''
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers,
    {a_1, a_2, ... , a_k} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 * a_2 * ... * a_k.

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
    The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2<=k<=6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30;
    note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2<=k<=12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2<=k<=12000?
'''

from __future__ import print_function
from sympy.utilities.iterables import kbins
from sympy import factorint
from itertools import count

from lib import prod

'''
The key to solving this problem is that any product of a number can be turned into a sum of that number by
    adding 1's to the product. For instance, 8 = 2 * 4 = 1 * 1 * 2 * 4. The second product also has a sum of 8.

From this if we generate a product of divisors of a number n, it can be converted to a k value by doing
    k = i - sum(divisors for product) + len(divisors for product)

Now to generate all possible k's for a number n we need to find all the possible products. These are the
    multiplicative partitions of n. With a list of prime factors of n, kbins will create all the possible
    unique partitions of the list.
'''


def solve(max_k=12000, min_k=2):
    float_inf = float('inf')
    min_ps_numbers = [float_inf] * (max_k - min_k + 1)

    for i in count(1):
        # I would like a better way of looking for the max than just checking to see that all values are
        #   not inf, however this is only a minor portion of the runtime.
        if float_inf not in min_ps_numbers:
            break

        composite_factoring = factorint(i, multiple=True)
        for prod_len in range(2, len(composite_factoring) + 1):
            for multiplicative_partition in kbins(composite_factoring, prod_len, 0):
                multiplicative_partition = [prod(x) for x in multiplicative_partition]
                multiplicative_partition_sum = sum(multiplicative_partition)
                one_count = i - multiplicative_partition_sum
                k = one_count + len(multiplicative_partition)
                array_k = k - min_k
                if array_k < len(min_ps_numbers) and min_ps_numbers[array_k] > i:
                    min_ps_numbers[array_k] = i

    return sum(set(min_ps_numbers))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p088_ans.txt', 'w') as wb:
        wb.write(str(answer))

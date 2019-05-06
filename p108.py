"""
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n
For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4
What is the least value of n for which the number of distinct solutions
    exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110;
    it is strongly advised that you solve this one first.
"""


from __future__ import print_function, division
from sympy import factorint, sieve
from math import ceil, log
from lib import prod


"""
To start with, a few facts about this equation. It is a special case of
    the equation in Fermat's last theorem, with an exponent of -1. It is
    also called the optic equation for it's use in optics. It is stated
    that for the equation

1/a + 1/b = 1/c

then all solutions have the form
a = k*m*(m + n)
b = k*n*(m + n)
c = k*m*n
where m and n are coprime.

I started by brute forcing this for the first few numbers. First
    we get all the possible values of k from the divisors. Then we get
    the possible values of m from the divisors of c / k. Lastly we can
    calculate n by c / k / m. If m > n, then we're repeating a previous
    equality.

This worked well however it was still too slow for this problem. Though
    it was possible to use this function on all numbers in the range(1, 20).
    Using OEIS, it is shown that this sequence is given as A018892 which
    is described as exactly this problem: "Number of ways to write 1/n as
    a sum of exactly 2 unit fractions."

Other than the OEIS sequence, nothing before this was used to solve the problem.

OEIS gives an equation for these. Given a value n which is made of
    primes as such:

    f = (p_1**a_1) * (p_2**a_2) * ... * (p_t**a_t)

    Then the number of solutions to this equation is given as:

    s(f) = ((2*a_1 + 1) * (2*a_2 + 1) * ... * (2*a_t + 1) + 1) / 2

    Which is especially interesting because it shows that the number of
    solutions is dependant not on the primes that make up c, but only
    their exponents.

Problem 110 is also solved using this solve, and more optimizations had
    to be introduced to deal with that. Here is a walkthrough of this
    algorithm.

    To start with we need to understand that we are looking for the exponents
    that minimize the f above, but still produce a value for the
    s(f) above the given n. That can be done by putting found exponents for
    the second equation in reverse order, and assign them to increasing primes.
    eg, for n = 100, the solution is 1260 which is factored
    {2: 2, 3: 2, 5: 1, 7: 1}

    So the primes are sequential and the exponents are in reverse order, great.

But what is the maximum prime possible? Lets manipulate the second equation above:
    n < ((2*a_1 + 1) * (2*a_2 + 1) * ... * (2*a_t + 1) + 1) / 2
    n*2 - 1 < (2*a_1 + 1) * (2*a_2 + 1) * ... * (2*a_t + 1)
    If we assume each exponent (a value) was 1, then we get
    n*2 - 1 < 3 * 3 * ... * 3
    n*2 - 1 < 3**k
    where k is the index of the maximum prime.
    k = ceil(log_3(n / 1 - 1))

So now we know our number will be made of primes less than or equal to
    the kth prime. Lets build a number factoring such as
    f = {2: 0, 3: 0, ..., prime(k): 0}

Now we will increase the exponent on 2 untill the value of s(f) > n.
    Then we will increase the exponent on 3, set the exponent for 2 to that,
    and repeat. Once we get to the last exponent with a value of 2, we know
    we are done.
"""


def optic_equation_solution_count(c):
    if not isinstance(c, dict):
        c = factorint(c)
    # An integer division is acceptable here. The inner values in the prod
    #   are of the form 2*a + 1 so they are always odd. A product of odd
    #   numbers is odd, then + 1 makes it even so it is always divisible
    #   by 2.
    return (prod(2*a + 1 for a in c.values()) + 1) // 2


def solve(n=1000):
    max_num_prime_factors = int(ceil(log(n // 2 - 1) / log(3)))
    sieve.extend_to_no(max_num_prime_factors)
    prime_fact = {sieve._list[i]: 0 for i in range(max_num_prime_factors)}
    minimum = float('inf')

    while True:
        for _ in range(2):
            # Loop this twice. We want to check the count before and after
            #   updating the exponent on 2. The count on the second time
            #   through will always be greater than n thanks to math.
            if optic_equation_solution_count(prime_fact) > n:
                this_num = prod(i**j for i, j in prime_fact.items())
                if this_num < minimum:
                    minimum = this_num
                break

            # Find the exponent for 2 that will get the count over n.
            temp_n = (n + 1) * 2 - 1
            for other_prime in sorted(x for x in prime_fact if x != 2):
                temp_n /= 2*prime_fact[other_prime] + 1
            temp_n -= 1
            temp_n /= 2
            prime_fact[2] = ceil(temp_n)

        # Find the next lowest exponent, increase it....
        start_val = prime_fact[2]
        for target_prime in sorted(x for x in prime_fact if x != 2):
            if prime_fact[target_prime] < start_val:
                prime_fact[target_prime] += 1
                break

        # ... then set all previous exponents to that exponent.
        for prime in sorted(x for x in prime_fact if x < target_prime):
            if prime_fact[prime] >= start_val:
                prime_fact[prime] = prime_fact[target_prime]
            else:
                break

        # If the minimum exponent is 2, we're definitely done.
        min_val = min(prime_fact.values())
        if min_val == 2:
            break

    return minimum 


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p108_ans.txt', 'w') as wb:
        wb.write(str(answer))

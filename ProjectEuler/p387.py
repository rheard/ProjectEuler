"""
A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit,
    always results in a Harshad number a right truncatable Harshad number.

Also:
201/3 = 67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10**14.
"""

from collections import deque

from sympy import isprime

from ProjectEuler.utils import digital_sum


def solve(n=10**14):
    """
    This was a very classic problem, in that I just needed to get a working solution, slowly optimize it,
        and before I know it the code that I thought was un-improvable is now running 10x faster, then 100x faster...

    I started by just going up from 1 to n, and finding all the numbers that satisfy the Harshad definition,
        then going over all the Harshad numbers, truncating them,
            and checking if the result is still in the Harshad set.
        Then with the new set of right-truncatable Harshad numbers, check which ones divide to be prime,
            then going over the primes to see which ones truncate to be in
            that set of strong right-truncatable Harshad numbers.

    This is basically exactly what the problem says to do, nothing smart.
        It was fast enough to verify 10000, but quickly started to lose steam at higher values...

    An interesting note: A001101 defines the Moran numbers, which are the numbers k such that
        k / sum(digits of k) is prime.

        Obviously these are a subset of Harshad numbers, and that matches
            what has been defined as "strong Harshad numbers" in the problem.

    A major speed improvement came on the later parts (Moran check) by building a list of Moran numbers
        when I'm checking for Harshad numbers, since I need to divide anyway, and then instead of building
            the list of strong right-truncatable Harshad numbers,
            I just need to merge the sets of Moran numbers and right-truncatable Harshad numbers.

        Yet another moderate speed improvement came on the front-end (building the Harshad numbers) by implementing the
            digital_sum method (moved to utils because it is very useful) and avoiding `str`/`int` conversions.
        Additionally only looking for Harshad numbers up to n // 10 was an easy 10x speed gain on the front-end.

    However these only got me to about 10**8... clearly I need to do something smarter.
        One idea I had for the backend (where the memory size of the prime sieve worried me for larger numbers),
            was instead of going over all the primes, truncating,
                and checking if it is a strong right-truncatable Harshad number;
            instead go over the strong right-truncatable Harshad numbers, append 1,3,5 or 7,
                and check if that is prime.

        While that was significantly faster for the final step, doing some analysis revealed the final step was already
            a minor bit of the execution time.

        The slowest part of this algorithm was step 1: creating sets of Harshad and Moran numbers.

    So, my final idea was to bring this idea of building up numbers forward to the process of building the Harshad
        numbers themselves.

    Since we're building a list of right-truncatable Harshad numbers, it should be obvious we don't actually
        need to go over every number and build a list of all the Harshad numbers, because we don't actually care about
            ALL of the Harshad numbers.

        Instead we can just start with the single-digits (1, 2, 3, etc),
            and append numbers to a deque to build up all the right-truncatable Harshad numbers,
            and we can also store any Moran numbers found along the way since we're checking divisibility anyway.

    This drastically reduces the algorithms space from checking all numbers, to very selectively building up
        the right-truncatable Harshad numbers and exactly finding the strong ones.

    That completely replaced steps 1 through 3 in my original process (which were the most time consuming).
        This new algorithm scales via O(log n) instead of O(n) as well
            and was enough to reach 10**14 in under 0.5 seconds.
    """
    max_harshad = n // 10

    # region Step 1
    #   Using a deque of growing right-truncatable Harshad numbers,
    #       find all of the strong right-truncatable Harshad numbers.
    input_harshad_numbers = deque(list(range(1, 10)))
    srth_numbers = set()

    while input_harshad_numbers:
        harshad_number = input_harshad_numbers.pop()

        # Multiply by 10 and append digits...
        h10 = harshad_number * 10
        if h10 >= max_harshad:
            continue

        for i in range(10):
            new_harshad_number = h10 + i
            d, m = divmod(new_harshad_number, digital_sum(new_harshad_number))
            if m == 0:
                # Found a new right-truncatable Harshad number, add it to the processing queue
                input_harshad_numbers.append(new_harshad_number)

                if isprime(d):
                    # ...and its strong! Add it to the list of Moran numbers
                    srth_numbers.add(new_harshad_number)
    # endregion

    # region Step 2
    #   Build up the strong, right-truncatable Harshad primes from
    #   the list of strong, right-truncatable Harshad numbers.
    srth_primes = set()
    for s in srth_numbers:
        s10 = s * 10

        for possible_s in [s10 + 1,
                           s10 + 3,
                           s10 + 7,
                           s10 + 9]:
            if isprime(possible_s):
                srth_primes.add(possible_s)
    # endregion

    return sum(srth_primes)


solve.answer = 696067597313468

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

# We only need to compute each one of these once.
_basic_factorials = [factorial(i) for i in range(10)]


def is_factorion(n):
    return sum(_basic_factorials[int(digit)] for digit in str(n)) == n


# Establishing an upper bound (Not gunna lie, Wikipedia helped, but I would not use the information without understanding it)
#   Starting with a number n with d digits
#   1. The bound is obviously 10**(d - 1) <= n <- 9!*d. The lower bound because that is the smallest d digit number
#                               The upper bound because if all digits are 9.
#       Note: If d >= 8, then 10**8 > 9! * 8, so the maximum digits is 7.
#   2. Inputting 7 into the above equation we get an upper bound of 2,540,160
#   3. Since the max is that, the maximum for the first digit is 2, so our new max is 2! + 9! * 6 = 2,177,282
#   4. Note due to the new max, if 2 is the first digit then the second is either 0 or 1. If we recacluate then
#       2! + 1! + 9! * 5 = 1,814,403 is our new max. Thus 2 can not be the first digit.  Therefor the newest max is 1999999.
#   5. Next assume that our number is of the form 1abcdef and that a-f is at least 5. A factorial of at least 5 will always
#       end in 0 since it has 5 and 2 as factors. Therefor the sum of our number will end in 1, from the 1! at the beginning.
#       This contradicts the assumption that f is at least 5. Therefor one of a-f must be less than 4, giving us a new maximum
#       of 1! + 4! + 9! * 5 = 1,814,425.
#   6. Repeating the logic in 4, if the first digit in a 7 digit number is 1, then the second digit is at max 8. Since the
#       second digit is at most 8, then one of the other digits has to be less than 5 as previously discussed. This gives a
#       new max of 1! + 8! + 4! + 9! * 4 = 1,491,865. Therefor the second digit is at most 4, satisfying that one of the
#       digits a-f is less than 4. Therefor the maximum is 1,499,999
def solve():
    return sum(x for x in range(3, 1499999) if is_factorion(x))


if __name__ == '__main__':
    answer = solve()
    print(answer)
    with open('p034_ans.txt', 'w') as wb:
        wb.write(str(answer))

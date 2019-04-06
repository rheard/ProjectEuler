from __future__ import print_function


def bouncy(n):
    str_n = str(n)
    list_n = list(str_n)
    reverse_n = list(reversed(list_n))
    return sorted(str_n, reverse=True) != list(str_n) \
        and sorted(str_n) != reverse_n

999 998 997 996 995 994 993 992 991 990
    988 987 986 985 984 983 982 981 980
        977 976 975 974 973 972 971 970






def solve(n=0.99):
    bouncy_count = 0
    number_count = 99
    for num in count(100):
        number_count += 1
        if bouncy(num):
            bouncy_count
        if bouncy_count / number_count >= n:
            break
    return num
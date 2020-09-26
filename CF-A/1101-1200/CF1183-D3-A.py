# https://codeforces.com/problemset/problem/1183/A

n = int(input())


def find_sum(number):
    s = 0
    while number != 0:
        s += (number % 10)
        number = number // 10
    return s


while find_sum(n) % 4 != 0:
    n += 1

print(n)

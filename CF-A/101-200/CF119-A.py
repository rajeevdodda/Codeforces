# https://codeforces.com/problemset/problem/119/A


def gcd(x, y):
    while y:
        x, y = y, x % y

    return x


a, b, n = map(int, input().split())

while True:
    a_stones = gcd(a, n)
    if a_stones > n:
        print(1)
        break
    n -= a_stones

    b_stones = gcd(b, n)
    if b_stones > n:
        print(0)
        break
    n -= b_stones

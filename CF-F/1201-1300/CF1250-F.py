# https://codeforces.com/problemset/problem/1250/F

n = int(input())

for i in range(int(n ** 0.5), 0, -1):
    if n % i == 0:
        print(2 * ((n // i) + i))
        break



# https://codeforces.com/contest/791/problem/A

a, b = map(int, input().split())
x = 1
while True:
    if a * (3 ** x) > b * (2 ** x):
        print(x)
        break
    else:
        x += 1

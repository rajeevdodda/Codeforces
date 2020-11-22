# https://codeforces.com/problemset/problem/673/A

n = int(input())

minutes = map(int, input().split())

first = 0
total = 0

for i in minutes:
    if i - first > 15:
        print(first + 15)
        break
    else:
        first = i
        total = i + 15
else:

    print(min(total, 90))

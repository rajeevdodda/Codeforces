# https://codeforces.com/contest/112/problem/A
first = input().lower()
second = input().lower()

for i, j in zip(first, second):
    if i < j:
        print(-1)
        break
    elif i > j:
        print(1)
        break
else:
    print(0)
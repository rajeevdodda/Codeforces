# https://codeforces.com/problemset/problem/1328/A

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    temp = a % b

    if temp == 0:
        print(0)
    else:
        if a > b:
            print(b - temp)
        else:
            print(b - a)
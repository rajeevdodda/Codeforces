# https://codeforces.com/problemset/problem/1300/A

for _ in range(int(input())):
    n = int(input())
    total = 0
    zeros = 0

    for i in map(int, input().split()):
        if i == 0:
            zeros += 1
        else:
            total += i

    if total + zeros == 0:
        print(zeros + 1)
    else:
        print(zeros)
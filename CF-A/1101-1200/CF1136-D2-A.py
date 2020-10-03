# https://codeforces.com/problemset/problem/1136/A

n = int(input())
chapters = list()
for i in range(n):
    chapters.append(tuple(map(int, input().split())))

k = int(input())

ans = 0
l = 1
for i in chapters:
    if i[0] <= k <= i[1]:
        ans = l
        break
    l += 1

print(n - ans + 1)
# https://codeforces.com/problemset/problem/609/A

n = int(input())
m = int(input())

l = list()
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
total = 0

for i in range(n):
    total += l[i]
    if total >= m:
        print(i+1)
        break


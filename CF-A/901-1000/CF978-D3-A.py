# https://codeforces.com/problemset/problem/978/A

n = int(input())

a = tuple(input().split())
s = set()
ans = list()

for i in a[::-1]:
    if i not in s:
        ans.append(i)
        s.add(i)

print(len(ans))

print(*ans[::-1])

# https://codeforces.com/contest/365/problem/A

n, k = map(int, input().split())
ans = 0
k_set = set(range(k + 1))

for i in range(n):
    a = int(input())
    temp_set = set()
    while a != 0:
        temp = a % 10
        if temp in k_set:
            temp_set.add(temp)
        a = a // 10
    else:
        if k_set == temp_set:
            ans += 1

print(ans)

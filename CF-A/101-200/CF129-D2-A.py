# https://codeforces.com/contest/129/problem/A

n = int(input())

cookies = map(int, input().split())

even = odd = total = 0
for i in cookies:
    total += i
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

if total % 2 == 0:
    print(even)
else:
    print(odd)

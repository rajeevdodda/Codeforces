# https://codeforces.com/contest/540/problem/A
n = int(input())
first = int(input())
second = int(input())
ans = 0
i = n
while i > 0:
    f = first % 10
    s = second % 10
    ans += min((abs(f - s)), abs(10 - abs(f-s)))
    first = first // 10
    second = second // 10
    i -= 1

print(ans)

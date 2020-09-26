# https://codeforces.com/problemset/problem/1095/A

n = int(input())

string = input()

a = 0

ans = ""
i = 0
while a < n:
    ans += string[a]
    i += 1
    a += i


print(ans)
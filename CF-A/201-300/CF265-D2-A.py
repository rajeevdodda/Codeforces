# https://codeforces.com/contest/265/problem/A
s = input()
t = input()
i = j = 0
while i < len(t):
    if t[i] == s[j]:
        j += 1
    i += 1

print(j + 1)

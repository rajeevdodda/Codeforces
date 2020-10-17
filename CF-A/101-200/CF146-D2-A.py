# https://codeforces.com/problemset/problem/146/A

n = int(input())
s = input()

first = 0
second = 0

i, j = 0, n // 2

while i < n // 2 and j < n:

    if s[i] == '7' or s[i] == '4':
        first += int(s[i])

    else:
        print("NO")
        break

    if s[j] == '7' or s[j] == '4':
        second += int(s[j])

    else:
        print("NO")
        break

    i += 1
    j += 1
else:
    if first != second:
        print("NO")

    else:
        print("YES")


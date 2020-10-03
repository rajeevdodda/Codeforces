# https://codeforces.com/problemset/problem/867/A

n = int(input())

s_f = f_s = 0

string = input()

for i in range(1, n):
    if string[i - 1] == "S" and string[i] == "F":
        s_f += 1

    if string[i - 1] == "F" and string[i] == "S":
        f_s += 1

if s_f > f_s:
    print("YES")
else:
    print("NO")
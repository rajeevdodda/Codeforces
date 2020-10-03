# https://codeforces.com/problemset/problem/1139/A

n = int(input())

string = input()
total = 0
for i in range(n):
    if int(string[i]) % 2 == 0:
        total += i + 1

print(total)

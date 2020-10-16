# https://codeforces.com/problemset/problem/946/A

_ = input()
total = 0
for i in map(int, input().split()):
    if i > 0:
        total += i
    else:
        total -= i

print(total)

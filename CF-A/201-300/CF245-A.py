# https://codeforces.com/problemset/problem/245/A

a_count = 0
a_ping = 0
b_ping = 0
n = int(input())

for _ in range(n):
    server, x, y = map(int, input().split())
    if server == 1:
        a_count += 1
        a_ping += x
    else:
        b_ping += x

if a_count * 5 <= a_ping:
    print("LIVE")
else:
    print("DEAD")
if (n - a_count) * 5 <= b_ping:
    print("LIVE")
else:
    print("DEAD")

# https://codeforces.com/contest/344/problem/A
n = int(input())
previous = input()
ans = 1
for i in range(1, n):
    magnet = input()
    if previous != magnet:
        ans += 1
        previous = magnet
print(ans)

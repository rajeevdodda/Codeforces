# https://codeforces.com/contest/699/problem/A
n = int(input())

particles = input()

positions = map(int, input().split())

temp = None
ans = float('inf')
for p, x in zip(particles, positions):
    if temp is None:
        if p == "R":
            temp = x
    else:
        if p == "R":
            temp = x
        if p == "L":
            if abs(temp - x) < ans:
                ans = abs(temp - x)
if ans == float('inf'):
    print(-1)
else:
    print(ans//2)

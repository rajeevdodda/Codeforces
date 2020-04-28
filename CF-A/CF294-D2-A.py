# https://codeforces.com/contest/294/problem/A
n = int(input())
birds = list(map(int, input().split()))

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    if n == 1:
        birds[0] = 0
        break

    if x == 0:
        birds[x + 1] = birds[x + 1] + (birds[x] - y)
        birds[x] = 0
    elif x == n - 1:
        birds[x - 1] += (y - 1)
        birds[x] = 0
    else:
        birds[x - 1] = birds[x - 1] + (y - 1)
        birds[x + 1] = birds[x + 1] + (birds[x] - y)
        birds[x] = 0

for i in birds:
    print(i)

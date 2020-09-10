# https://codeforces.com/contest/415/problem/A

n, m = map(int, input().split())

lights = [None] * n

pushed_buttons = tuple(map(int, input().split()))

for i in pushed_buttons:

    temp = i - 1
    while temp < n and lights[temp] is None:
        lights[temp] = i
        temp += 1

print(*lights)

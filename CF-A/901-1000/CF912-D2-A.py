# https://codeforces.com/problemset/problem/912/A

a, b = map(int, input().split())

y, g, blue = map(int, input().split())

yellow_needed = (2 * y) + g
blue_needed = (3 * blue) + g

ans = 0

if yellow_needed > a:
    ans += (yellow_needed - a)

if blue_needed > b:
    ans += (blue_needed - b)
print(ans)

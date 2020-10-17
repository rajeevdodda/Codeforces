# https://codeforces.com/problemset/problem/900/A

left = 0
right = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 0:
        left += 1
    if x > 0:
        right += 1

    if left > 1 and right > 1:
        print("NO")
        break

else:
    print("YES")

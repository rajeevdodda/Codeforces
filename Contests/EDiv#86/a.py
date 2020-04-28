t = int(input())

for i in range(t):
    ans = 0
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if b / a < 2:
        ans += min(x, y) * b
        ans += abs(x - y) * a
    else:
        ans = (x + y) * a

    print(ans)

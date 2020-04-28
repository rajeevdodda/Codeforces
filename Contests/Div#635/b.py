t = int(input())

for i in range(t):
    x, n, m = map(int, input().split())
    if 10 * m >= x:
        print("YES")
        continue
    for j in range(n):
        x = (x // 2) + 10
        if 10 * m >= x:
            print("YES")
            break
    else:
        print("NO")

t = int(input())
for i in range(t):
    ans = list()
    a, b, q = map(int, input().split())
    for _ in range(q):
        x, y = map(int, input().split())
        if max(x, y) < min(a, b):
            ans.append(0)
        else:
            temp = 0
            for j in range(x, y + 1):
                if (j % a) % b != (j % b) % a:

                    temp += 1
                else:
                    print(j)
            ans.append(temp)
    print(*ans)

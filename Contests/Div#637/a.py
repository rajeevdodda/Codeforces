t = int(input())

for i in range(t):
    n, a, b, c, d = map(int, input().split())
    if (a - b) <= (c + d) / n <= (a + b):
        print("Yes")
    elif (a - b) <= (c - d) / n <= (a + b):
        print("Yes")
    else:
        print("No")


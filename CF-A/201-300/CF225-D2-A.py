# https://codeforces.com/contest/225/problem/A

n = int(input())
top = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a1, b1 = 7 - a, 7 - b
    if a1 == top or b == top or a == top or b1 == top:
        print("NO")
        break
    else:
        top = 7 - top

else:
    print("YES")
# https://codeforces.com/contest/47/problem/A
n = int(input())
if (((1 + 8 * n) ** (0.5) - 1)/2) % 1 == 0:
    print("YES")
else:
    print("NO")

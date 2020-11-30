# https://codeforces.com/problemset/problem/818/A# https://codeforces.com/problemset/problem/818/A

n, k = map(int, input().split())
# winners = cert + diploma
# cert = k * diploma
# winners <= n//2  and winners an be 0

# print diploma, cert, not winners


d = (n // 2) // (k + 1)

print(d, d * k, n - (k + 1) * d)
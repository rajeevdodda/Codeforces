# https://codeforces.com/problemset/problem/658/A

n, c = map(int, input().split())
p = tuple(map(int, input().split()))
t = list(map(int, input().split()))

limak_t = 0
radewoosh_t = 0

limak = 0
radewoosh = 0
for i in range(n):
    limak_t += t[i]
    radewoosh_t += t[n - i - 1]
    limak += max(0, p[i] - c * limak_t)
    radewoosh += max(0, p[n - i - 1] - c * radewoosh_t)

if limak > radewoosh:
    print("Limak")
elif limak < radewoosh:
    print("Radewoosh")
else:
    print("Tie")

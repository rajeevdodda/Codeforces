# https://codeforces.com/problemset/problem/1207/A

for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    b_half = b // 2
    total = 0
    if b_half == 0:
        print(total)
    else:
        if h > c:
            if b_half > p:
                total = p * h + min(b_half - p, f) * c
            else:
                total = b_half * h
        else:

            if b_half > f:
                total = f * c + min(b_half - f, p) * h
            else:
                total = b_half * c
        print(total)

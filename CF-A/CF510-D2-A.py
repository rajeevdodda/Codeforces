# https://codeforces.com/contest/510/problem/A
n, m = map(int, input().split())

edge = True
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    else:
        if edge:
            print("." * (m - 1) + "#")
            edge = False
        else:
            print("#" + "." * (m - 1))
            edge = True

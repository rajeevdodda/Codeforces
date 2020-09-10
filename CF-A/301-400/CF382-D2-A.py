# https://codeforces.com/contest/382/problem/A

l, r = input().split("|")
x = input()
temp = len(l + x + r) / 2
if len(l + x + r) % 2 == 0:
    for i in x:
        if len(l) <= len(r):
            l += i
        else:
            r += i
    if len(l) == len(r):
        print(l + "|" + r)
    else:
        print("Impossible")
else:
    print("Impossible")

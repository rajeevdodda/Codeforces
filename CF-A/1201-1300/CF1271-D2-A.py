# https://codeforces.com/problemset/problem/1271/A

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


if f > e:
    b_suit = min(b, c, d)
    print(b_suit * f + min(a, d - b_suit) * e)
else:
    a_suit = min(a, d)
    print(a_suit * e + min(b, c, d - a_suit) * f)

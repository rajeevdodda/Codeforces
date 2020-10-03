# https://codeforces.com/problemset/problem/1108/A

for _ in range(int(input())):
    l1, r1, l2, r2 = input().split()
    if l1 != r2:
        print(l1, r2)
    else:
        print(l1, l2)
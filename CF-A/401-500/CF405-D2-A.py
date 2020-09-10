# https://codeforces.com/contest/405/problem/A
n = input()
a = list(map(int, input().split()))
a.sort()
for i in a:
    print(i, end=" ")

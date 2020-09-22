# https://codeforces.com/problemset/problem/1283/A


for i in range(int(input())):
    h, m = map(int, input().split())
    print((23-h)*60 + (60-m))

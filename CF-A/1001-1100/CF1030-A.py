# https://codeforces.com/problemset/problem/1030/A

n = input()

ans = input().split()

for i in ans:
    if i == "1":
        print("HARD")
        break
else:
    print("EASY")
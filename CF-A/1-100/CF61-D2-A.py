# https://codeforces.com/contest/61/problem/A
a = input()
b = input()

for i, j in zip(a,b):
    if i != j:
        print("1", end="")
    else:
        print("0", end="")
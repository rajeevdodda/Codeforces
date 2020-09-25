# https://codeforces.com/problemset/problem/1220/A

_ = input()

string = input()

n = z = 0
for i in string:
    if i == 'n':
        n += 1
    if i == 'z':
        z += 1

for i in range(n):
    print("1", end=" ")
for i in range(z):
    print("0", end=" ")
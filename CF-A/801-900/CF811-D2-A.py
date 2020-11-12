# https://codeforces.com/problemset/problem/811/A

a, b = map(int, input().split())

i = 1
j = 2

while True:
    if i <= a:
        a -= i
        i += 2
    else:
        print("Vladik")
        break

    if j <= b:
        b -= j
        j += 2
    else:
        print("Valera")
        break
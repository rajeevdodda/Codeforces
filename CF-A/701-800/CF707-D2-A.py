# https://codeforces.com/contest/707/problem/A

n, m = map(int, input().split())
result = False
for i in range(n):
    colours = input().split()
    for c in colours:
        if c not in "BWG":
            print("#Color")
            result = True
            break
    if result:
        break
else:
    print("#Black&White")


# https://codeforces.com/problemset/problem/855/A

n = input()

s = set()

for i in range(int(n)):
    a = input()
    if a in s:
        print("YES")
    else:
        s.add(a)
        print("NO")

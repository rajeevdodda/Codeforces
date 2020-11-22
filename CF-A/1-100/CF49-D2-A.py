# https://codeforces.com/problemset/problem/49/A

s = input()

for i in s[::-1]:
    if i.isalpha():
        if i.lower() in 'aeiouy':
            print("YES")
        else:
            print("NO")

        break

# https://codeforces.com/problemset/problem/12/A

one = input()
two = input()
three = input()

if one != three[::-1]:
    print("NO")
else:
    if two != two[::-1]:
        print("NO")
    else:
        print("YES")
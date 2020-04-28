# https://codeforces.com/contest/520/problem/A

n = int(input())
string = input().lower().replace(" ", "")

if n < 26:
    print("NO")
else:
    if len(set(string)) == 26:
        print("YES")
    else:
        print("NO")



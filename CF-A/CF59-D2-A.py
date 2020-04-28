# https://codeforces.com/contest/59/problem/A
string = input()
upper, lower = 0, 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if lower >= upper:
    print(string.lower())
else:
    print(string.upper())
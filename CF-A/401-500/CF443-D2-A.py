# https://codeforces.com/contest/443/problem/A

string = input()
s = set()
for i in string:
    if i.isalpha():
        if i not in s:
            s.add(i)
print(len(s))
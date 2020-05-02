# https://codeforces.com/contest/118/problem/A

string = input()

for i in string:
    if i.lower() in "aoyeui":
        continue
    else:
        print("."+ i.lower(), end="")
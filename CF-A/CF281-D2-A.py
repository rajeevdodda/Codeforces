# https://codeforces.com/contest/281/problem/A

string = input()

if string[0].isupper():
    print(string)
else:
    print(string[0].upper()+string[1:])
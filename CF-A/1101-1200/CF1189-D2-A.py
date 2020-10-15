# https://codeforces.com/problemset/problem/1189/A

n = int(input())

zeros = ones = 0
string = input()
for i in string:
    if i == "0":
        zeros += 1
    else:
        ones += 1

if ones == zeros:
    print(2)
    print(string[0], string[1:])
else:
    print(1)
    print(string)

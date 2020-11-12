# https://codeforces.com/problemset/problem/1159/A

n = int(input())
temp = 0
for i in input():

    if i == '-':
        temp -= 1
        if temp < 0:
            temp = 0
    if i == '+':
        temp += 1

print(temp)
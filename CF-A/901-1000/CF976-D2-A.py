# https://codeforces.com/problemset/problem/976/A

n = int(input())

s = input()
total = 0

if n == 1:
    print(s)
else:
    for i in s:
        if i == '0':
            total += 1

    print('1' + '0' * total)

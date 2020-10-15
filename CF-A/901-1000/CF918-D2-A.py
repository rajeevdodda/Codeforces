# https://codeforces.com/problemset/problem/918/A


n = int(input())

a, b = 1, 2
s = set()

while a <= n+1:
    s.add(a)
    a, b = b, a+b


for i in range(1, n+1):
    if i in s:
        print("O", end='')
    else:
        print('o', end="")




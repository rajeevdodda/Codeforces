# https://codeforces.com/problemset/problem/1385/A

from sys import stdin, stdout

t = int(stdin.readline())

for _ in range(t):
    array = sorted(map(int, stdin.readline().split()))
    if array[1] != array[2]:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
        stdout.write(str(array[0]) + " " + str(array[0]) + " " + str(array[2])+"\n")

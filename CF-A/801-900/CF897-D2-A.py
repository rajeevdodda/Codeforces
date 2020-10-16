# https://codeforces.com/problemset/problem/897/A
n, m = map(int, input().split())

string = list(input())

for _ in range(m):
    l, r, c1, c2 = input().split()

    for i in range(int(l) - 1, int(r)):
        if string[i] == c1:
            string[i] = c2

print("".join(string))

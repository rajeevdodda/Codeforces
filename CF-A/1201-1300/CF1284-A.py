# https://codeforces.com/problemset/problem/1284/A

n, m = map(int, input().split())

n_strings = tuple(input().split())
m_strings = tuple(input().split())

for _ in range(int(input())):
    x = int(input())
    print(n_strings[x % n - 1] + m_strings[x % m - 1])

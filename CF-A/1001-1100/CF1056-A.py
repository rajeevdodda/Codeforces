# https://codeforces.com/problemset/problem/1056/A

n = int(input())

new_set = set(tuple(map(int, input().split()))[1:])
for i in range(n - 1):
    new_set = new_set.intersection(set(tuple(map(int, input().split()))[1:]))

print(*new_set)
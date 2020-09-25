# https://codeforces.com/problemset/problem/1397/A

for _ in range(int(input())):
    hash_map = dict()
    n = int(input())
    for i in range(n):
        for k in input():
            hash_map[k] = hash_map.get(k, 0) + 1

    for values in hash_map.values():
        if values % n != 0:
            print("NO")
            break
    else:
        print("YES")


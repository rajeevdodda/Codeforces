# https://codeforces.com/problemset/problem/1270/A

for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    first_max = max(map(int, input().split()))
    second_max = max(map(int, input().split()))

    if first_max > second_max:
        print("YES")
    else:
        print("NO")
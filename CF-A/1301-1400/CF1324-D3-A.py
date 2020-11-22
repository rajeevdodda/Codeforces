# https://codeforces.com/problemset/problem/1324/A

for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))

    if a[0] % 2 == 0:
        for i in a[1:]:
            if i % 2 != 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        for i in a[1:]:
            if i % 2 == 0:
                print("NO")
                break
        else:
            print("YES")

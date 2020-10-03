# https://codeforces.com/problemset/problem/1323/A

for _ in range(int(input())):
    n = int(input())
    odd_count = list()
    k = 1
    for i in map(int, input().split()):
        if i % 2 == 0:
            print(1)
            print(k)
            break
        if i % 2 == 1:
            odd_count.append(k)
            if len(odd_count) == 2:
                print(2)
                print(*odd_count)
                break
        k += 1
    else:
        print(-1)

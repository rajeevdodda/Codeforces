# https://codeforces.com/problemset/problem/1249/A

for _ in range(int(input())):
    n = int(input())
    array = sorted(map(int, input().split()))
    for i in range(1, n):
        if array[i] - array[i-1] == 1:
            print(2)
            break
    else:
        print(1)
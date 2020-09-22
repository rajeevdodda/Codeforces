# https://codeforces.com/problemset/problem/1360/B

t = int(input())

for i in range(t):
    n = int(input())
    array = sorted(map(int, input().split()))
    min_value = float('inf')
    for k in range(1, n):
        if array[k] - array[k - 1] < min_value:
            min_value = array[k] - array[k - 1]
            if min_value == 0:
                print(0)
                break
    else:
        print(min_value)
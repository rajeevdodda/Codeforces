# https://codeforces.com/problemset/problem/1360/A

t = int(input())

for i in range(t):

    a, b = map(int, input().split())
    
    min_value = min(a, b)
    max_value = max(a, b)

    if 2 * min_value >= max_value:
        print((min_value*2) ** 2)
    else:
        print(max_value ** 2)
    
# https://codeforces.com/contest/22/problem/A

n = int(input())
first_min = float('inf')
second_min = float('inf')

for i in map(int, input().split()):
    if i < first_min:
        first_min, second_min = i, first_min
    elif first_min < i < second_min:
        second_min = i

if second_min == float('inf'):
    print("NO")
else:
    print(second_min)

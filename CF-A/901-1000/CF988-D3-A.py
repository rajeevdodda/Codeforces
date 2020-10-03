# https://codeforces.com/problemset/problem/988/A

n, k = map(int, input().split())
array = tuple(map(int, input().split()))

s = set()
ans = 0
new_list = list()
for i in range(n):
    if array[i] not in s:
        s.add(array[i])
        new_list.append(i+1)
        ans += 1
        if ans == k:
            print("YES")
            print(*new_list)
            break
else:
    print("NO")
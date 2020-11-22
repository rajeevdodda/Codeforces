# https://codeforces.com/problemset/problem/426/A

n, s = map(int, input().split())

arr = sorted(map(int, input().split()))

if sum(arr[0:n-1]) <= s:
    print("YES")
else:
    print("NO")
# https://codeforces.com/problemset/problem/688/A

n, d = map(int, input().split())

ans = temp = 0

for _ in range(d):

    for i in input():
        if i == '0':
            temp += 1
            ans = max(temp, ans)
            break
    else:
        temp = 0
print(ans)

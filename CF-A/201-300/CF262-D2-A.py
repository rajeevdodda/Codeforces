# https://codeforces.com/contest/262/problem/A

n, k = map(int, input().split())

ans = 0

digits = input().split()

for i in digits:
    temp = 0
    for j in i:
        if j == "4" or j == "7":
            temp += 1
            if temp > k:
                break
    else:
        if temp <= k:
            ans += 1

print(ans)




# https://codeforces.com/problemset/problem/978/B

n = int(input())

ans = 0

string = input()
temp = 0
for i in range(0, n):
    if string[i] == 'x':
        temp += 1
        if temp > 2:
            ans += 1
    else:
        temp = 0


print(ans)
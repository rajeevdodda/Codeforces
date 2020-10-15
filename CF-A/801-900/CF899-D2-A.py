# https://codeforces.com/problemset/problem/899/A

two = 0
one = 0

n = input()

for i in input().split():
    if i == '1':
        one += 1
    else:
        two += 1


if one == 0:
    print(0)
else:
    ans = min(two, one)
    ans += ((one - ans) // 3)
    print(ans)
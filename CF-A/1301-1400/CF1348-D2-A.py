# https://codeforces.com/problemset/problem/1348/A

t = int(input())

for i in range(t):
    coins = int(input())
    ans = 2 ** coins
    k = 1
    while k + 1 <= coins / 2:
        ans += 2 ** k
        k += 1

    k = coins // 2
    while k < coins:
        ans -= 2 ** k
        k += 1

    
    print(abs(ans))
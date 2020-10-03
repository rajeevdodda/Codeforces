# https://codeforces.com/problemset/problem/1176/A

for _ in range(int(input())):

    n = int(input())
    if n == 1:
        print(0)
    else:
        ans = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                ans += 1
            elif n % 3 == 0:
                n = 2 * (n // 3)
                ans += 1
            elif n % 5 == 0:
                n = 4 * (n // 5)
                ans += 1
            else:
                print(-1)
                break
        else:
            print(ans)

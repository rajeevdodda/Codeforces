# https://codeforces.com/problemset/problem/1433/A

for _ in range(int(input())):

    n = input()
    l = len(n)

    number = int(n) % 10
    ans = 0
    for i in range(1, number):
        ans += 10
    total = 0
    for i in range(1, l+1):
        total += i

    ans += total
    print(ans)

# https://codeforces.com/problemset/problem/1399/B

t = int(input())

for i in range(t):
    n = int(input())

    candies = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    min_candy = min(candies)
    min_orange = min(oranges)
    ans = 0

    for l in range(n):
        ans += max((candies[l] - min_candy), (oranges[l] - min_orange))

    print(ans)

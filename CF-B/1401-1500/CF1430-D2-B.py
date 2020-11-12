# https://codeforces.com/problemset/problem/1430/B

for _ in range(int(input())):
    n, k = map(int, input().split())
    barrels = sorted(map(int, input().split()), reverse=True)
    print(sum(barrels[0:k+1]))


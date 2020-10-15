# https://codeforces.com/problemset/problem/1417/A


for _ in range(int(input())):
    n, k = map(int, input().split())
    piles = tuple(map(int, input().split()))
    min_pile = piles[0]
    min_index = 0

    for i in range(1, n):
        if piles[i] < min_pile:
            min_index, min_pile = i, piles[i]
    ans = 0

    if min_pile > k:
        print(0)
    else:
        for i in range(n):
            if i == min_index:
                pass
            else:
                if min_pile <= piles[i] <= k:
                    ans += (k - piles[i]) // min_pile

        print(ans)

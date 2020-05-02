# https://codeforces.com/contest/158/problem/A

n, k = map(int, input().split())
places = tuple(map(int, input().split()))
kth_place_score = places[k - 1]

ans = 0
for i in places:
    if i == 0:
        break
    else:
        if i >= kth_place_score:
            ans += 1
        else:
            break

print(ans)


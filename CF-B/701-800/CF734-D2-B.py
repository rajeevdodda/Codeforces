# https://codeforces.com/problemset/problem/734/B


k2, k3, k5, k6 = map(int, input().split())

min_value = min(k2, k5, k6)
another_min = min(k3, k2 - min_value)

print(256 * min_value + 32 * another_min)

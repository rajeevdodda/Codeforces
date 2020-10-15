# https://codeforces.com/contest/215/problem/B

r_outer = max(map(int, input().split()))

_, *p_outer = map(int, input().split())

p_outer_max = max(p_outer)

_, *p_inner = map(int, input().split())

p_inner_min = min(p_inner)

a, b = map(int, input().split())

r = ((r_outer * r_outer)/(1 + ((a/b)*(p_inner_min/p_outer_max))))**0.5
print(r)

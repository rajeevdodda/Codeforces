# https://codeforces.com/problemset/problem/1015/A

n, m = map(int, input().split())

m_array = [i for i in range(1, m + 1)]

for i in range(n):
    l, r = map(int, input().split())
    while l <= r:
        if m_array[l - 1] != 0:
            m_array[l - 1] = 0
            m -= 1
        l += 1

print(m)
for i in m_array:
    if i != 0:
        print(i, end=" ")

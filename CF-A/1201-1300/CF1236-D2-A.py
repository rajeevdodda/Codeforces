# https://codeforces.com/problemset/problem/1236/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    b_stones = min(c // 2, b)
    a_stones = min((b - b_stones) // 2, a)
    print((a_stones + b_stones) * 3)

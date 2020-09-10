# https://codeforces.com/contest/378/problem/A
a, b = map(int, input().split())
a_wins = draw = b_wins = 0

for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        a_wins += 1
    elif abs(a - i) == abs(b - i):
        draw += 1
    else:
        b_wins += 1

print(a_wins, draw, b_wins)
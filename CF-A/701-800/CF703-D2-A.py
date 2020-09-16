# https://codeforces.com/problemset/problem/703/A

n = int(input())

m_wins = 0
c_wins = 0

for i in range(n):
    m, c = map(int, input().split())

    if m > c :
        m_wins += 1
    elif m == c:
        m_wins += 1
        c_wins += 1
    else:
        c_wins += 1

if m_wins > c_wins:
    print("Mishka")
elif c_wins > m_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")
    
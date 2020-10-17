# https://codeforces.com/problemset/problem/1150/A

n, m, r = map(int, input().split())

n_integers = min(map(int, input().split()))
m_integers = max(map(int, input().split()))

if n_integers >= m_integers:
    print(r)
else:
    print(r % n_integers + ((r // n_integers) * m_integers))

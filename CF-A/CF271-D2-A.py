# https://codeforces.com/contest/271/problem/A

n = input()

while True:
    n = str(int(n) + 1)
    if len(set(n)) == 4:
        print(n)
        break


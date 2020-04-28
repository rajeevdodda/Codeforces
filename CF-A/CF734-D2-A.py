# https://codeforces.com/contest/734/problem/A
n = int(input())
s = input()
a_wins = 0
s_wins = 0
for i in s:
    if i == "A":
        a_wins += 1
        if a_wins > n // 2:
            print("Anton")
            break
    else:
        s_wins += 1
        if s_wins > n // 2:
            print("Danik")
            break

if a_wins == s_wins:
    print("Friendship")

# https://codeforces.com/contest/43/problem/A

n = int(input())
team_dict = dict()
for i in range(n):
    team = input()
    team_dict[team] = team_dict.get(team, 0) + 1

print(max(team_dict, key=team_dict.get))
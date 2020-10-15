# https://codeforces.com/problemset/problem/987/A

s = {
    'green': 'Time',
    'yellow': 'Mind',
    'orange': 'Soul',
    'purple': 'Power',
    'red': 'Reality',
    'blue': 'Space',
}
for _ in range(int(input())):
    del s[input()]

print(len(s))
for i in s.values():
    print(i)

# https://codeforces.com/contest/469/problem/A

n = int(input())

_, *x = map(int, input().split())
_, *y = map(int, input().split())
ans = set()

for i in x:
    ans.add(i)
for i in y:
    ans.add(i)

if ans == set(range(1,n+1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

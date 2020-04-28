# https://codeforces.com/contest/807/problem/A
n = int(input())
rating = list()
ans = True

for i in range(n):
    a, b = map(int, input().split())
    rating.append(b)
    if a != b:
        print("rated")
        break
else:
    temp = float('inf')
    for j in rating:
        if j <= temp:
            temp = j
        else:
            print("unrated")
            break
    else:
        print("maybe")

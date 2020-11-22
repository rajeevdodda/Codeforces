# https://codeforces.com/problemset/problem/837/A

n = int(input())

ans = 0

for word in input().split():
    temp = 0
    for letter in word:
        if letter.isupper():
            temp += 1

    ans = max(temp, ans)
print(ans)
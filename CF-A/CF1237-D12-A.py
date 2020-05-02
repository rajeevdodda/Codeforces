# https://codeforces.com/contest/1237/problem/A

n = int(input())

round_down = True

for i in range(n):
    temp = int(input())
    if temp % 2 == 0:
        print(temp//2)
    else:
        if round_down:
            print(temp//2)
            round_down = False
        else:
            print(temp//2 + 1)
            round_down = True


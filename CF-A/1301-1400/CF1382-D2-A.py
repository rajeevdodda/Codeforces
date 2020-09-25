# https://codeforces.com/problemset/problem/1382/A

for _ in range(int(input())):
    n, m = input().split()
    a_seq = input().split()
    b_seq = set(input().split())

    for a in a_seq:
        if a in b_seq:
            print("YES")
            print(1, a)
            break
    else:
        print("NO")

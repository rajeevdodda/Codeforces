# https://codeforces.com/problemset/problem/1385/B

n = int(input())

for i in range(n):
    l = input()
    ans = list()
    ans_set = set()
    array = map(int, input().split())

    for k in array:
        if k not in ans_set:
            ans_set.add(k)
            ans.append(k)

    print(*ans)
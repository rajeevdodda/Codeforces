# https://codeforces.com/problemset/problem/1316/A


for i in range(int(input())):
    n, m = map(int, input().split())
    scores_array = tuple(map(int, input().split()))
    my_score = scores_array[0]
    for k in scores_array[1:]:
        my_score += k
        if my_score > m:
            print(m)
            break
    else:
        print(my_score)


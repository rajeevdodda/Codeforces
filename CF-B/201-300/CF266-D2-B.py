# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split())

queue = list(input())


for i in range(t):
    j = 0
    while j < n - 1:
        if queue[j] == "B" and queue[j+1] == "G":
            queue[j], queue[j+1]  = "G", "B"
            j += 1
        j +=1

print(''.join(queue))

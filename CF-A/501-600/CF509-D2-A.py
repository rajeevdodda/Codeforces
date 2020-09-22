# https://codeforces.com/problemset/problem/509/A

from collections import deque

n = int(input())

if n == 1:
    print(1)
else:
    q = deque(maxlen=n)

    for i in range(n - 1):
        q.append(1)

    for i in range(n - 1):
        temp = 1
        for k in range(n - 1):
            temp += q.popleft()
            q.append(temp)

    print(q.pop())

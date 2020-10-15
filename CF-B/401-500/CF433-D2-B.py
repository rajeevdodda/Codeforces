# https://codeforces.com/contest/433/problem/B

n = int(input())

question1 = list(map(int, input().split()))

question2 = sorted(question1)


for i in range(1, n):
    question1[i] += question1[i - 1]
    question2[i] += question2[i - 1]
question2 = [0] + question2
question1 = [0] + question1

for i in range(int(input())):
    t, l, r = map(int, input().split())
    if t == 2:
        print(question2[r] - question2[l - 1])
    else:
        print(question1[r] - question1[l - 1])

# https://codeforces.com/contest/701/problem/A

n = int(input())

cards = map(int, input().split())
vector_list = list()
for i, j in enumerate(cards, start=1):
    vector_list.append((i, j))

vector_list.sort(key= lambda x : x[1])
i, j = 0, n-1
while i <=j:
    print(vector_list[i][0], vector_list[j][0])
    i += 1
    j -= 1


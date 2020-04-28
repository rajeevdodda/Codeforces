# https://codeforces.com/contest/490/problem/A

n = int(input())
min_count = float('inf')
talent_dict = {
    1: [],
    2: [],
    3: []
}
talent_list = map(int, input().split())
j = 1
for i in talent_list:
    talent_dict[i].append(j)
    j += 1
for key, values in talent_dict.items():
    if len(values) < min_count:
        min_count = len(values)
print(min_count)

for i in range(min_count):
    for key, values in talent_dict.items():
        print(values[i], end=" ")
    print()

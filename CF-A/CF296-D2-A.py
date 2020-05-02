n = int(input())
numbers = (map(int, input().split()))
two_count = 0

ans_dict = dict()

for i in numbers:
    ans_dict[i] = ans_dict.get(i, 0) + 1

for k, v in ans_dict.items():
    if v > (n +1)/2:
        print("NO")
        break
else:
    print("YES")


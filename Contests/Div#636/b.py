t = int(input())

for i in range(t):
    n = int(input())
    if (n // 2) % 2 == 1:
        print("NO")
    else:
        print("YES")
        even_list = list(range(2, n + 1, 2))
        odd_list = list(range(1, n - 1, 2))
        odd_list.append(sum(even_list) - sum(odd_list))
        print(" ".join(str(x) for x in even_list+odd_list))

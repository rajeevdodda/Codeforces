t = int(input())
for i in range(t):
    for j in range(9):
        k = list(input())
        if j in [1, 4, 7]:
            k[1], k[4], k[7] = k[0], k[3], k[6]
        print("".join(k))


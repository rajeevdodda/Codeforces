n = int(input())
i, j = 0, n - 1

cards = list(map(int, input().split()))
sreeja, dima = 0, 0
turn = True

while i <= j:
    if cards[i] > cards[j]:
        temp = cards[i]
        i += 1
    else:
        temp = cards[j]
        j -= 1

    if turn:
        sreeja += temp
        turn = False
    else:
        dima += temp
        turn = True
print(sreeja, dima)

# https://codeforces.com/problemset/problem/1097/A

table_card = list(input())

cards = input().split()


for card in cards:

    if card[0] == table_card[0] or card[1] == table_card[1]:
        print("YES")
        break
else:
    print("NO")
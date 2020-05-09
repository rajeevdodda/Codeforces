def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


t = single_integer()

for i in range(t):
    candy = single_integer()
    candies_list = tuple(multi_integer())
    alice_list = [0]
    bob_list = [0]

    alice = 0
    bob = candy - 1
    moves = 0

    while alice < bob:
        temp = 0
        while bob_list[-1] > temp and alice < bob:
            alice += 1
            temp += candies_list[alice]

        if bob_list[-1] == temp and alice < bob:
            alice += 1
            temp += candies_list[alice]
        moves += 1
        alice_list.append(temp)

        temp = 0
        while alice_list[-1] > temp and alice < bob:
            bob -= 1
            temp += candies_list[bob]

        if alice_list[-1] == temp and alice < bob:
            bob -= 1
            temp += candies_list[bob]

        moves += 1
        bob_list.append(temp)
    print(moves, sum(alice_list), sum(bob_list))

# https://codeforces.com/contest/141/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


guest = string()
host = string()
both = string()

guest_host_dict = dict()
both_dict = dict()

if len(guest) + len(host) != len(both):
    print("NO")
else:
    for i in guest:
        guest_host_dict[i] = guest_host_dict.get(i, 0) + 1

    for i in host:
        guest_host_dict[i] = guest_host_dict.get(i, 0) + 1

    for i in both:
        both_dict[i] = both_dict.get(i, 0) + 1

    for i in both_dict.keys():
        if i in guest_host_dict:
            if both_dict[i] != guest_host_dict[i]:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("YES")

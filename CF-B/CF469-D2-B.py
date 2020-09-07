# https://codeforces.com/contest/469/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


p, q, l, r = multi_integer()

x_timings = list()
y_timings = list()

for i in range(p):
    x_timings.append(tuple(multi_integer()))

for j in range(q):
    y_timings.append(tuple(multi_integer()))

ans = 0
moments = set()

# for i in x_timings:
#     for j in y_timings:
#         print(i, j)
#         temp = l
#         while temp <= r:
#             if i[0] <= j[0] + temp <= i[1]:
#                 moments.add((j[0], temp))
#             if i[0] <= j[1] + temp <= i[1]:
#                 # print(i[0], j[0] + temp, i[1], " and", i[0], j[1] + temp, i[1], " and", temp)
#                 moments.add((j[1], temp))
#             temp += 1

while l <= r:
    ans_found = False
    for x in x_timings:
        for y in y_timings:
            if x[0] <= y[0] + l <= x[1] or x[0] <= y[1] + l <= x[1]:
                ans += 1

                ans_fount = True
                break

        if ans_found:
            break
    l += 1
    pass

print(ans)

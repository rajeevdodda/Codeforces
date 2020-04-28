t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    elif n == 2:
        print(1)
        continue
    elif n == 3:
        print(1)
        continue

    sample_dict = dict()
    max_key = 0
    max_value = 0
    for j in a:

        sample_dict[j] = sample_dict.get(j, 0) + 1
        if sample_dict[j] > max_value:
            max_key, max_value = j, sample_dict[j]

    # distinct_keys = 0
    # keys = 0
    # for l in sample_dict.values():
    #     keys += 1
    #     if l == 1:
    #         distinct_keys += 1
    if len(sample_dict) > max_value:
        print(max_value)
    elif len(sample_dict) == max_value:
        print(max_value - 1)
    elif len(sample_dict) < max_value:
        print(len(sample_dict))

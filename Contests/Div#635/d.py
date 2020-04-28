t = int(input())

for i in range(t):
    nr, ng, nb = map(int, input().split())
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l, m = 0, ng - 1
    r_value, g_value = r[0], g[-1]
    min_r_g = float('inf')
    r_g_list = list()
    while l < nr and m > -1:
        temp_sum = abs(r[0] - g[m])
        if temp_sum < min_r_g:
            min_r_g = temp_sum
            r_value, g_value = r[l], g[m]

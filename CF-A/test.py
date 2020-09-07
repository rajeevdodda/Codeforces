import math


def numPoints(points, r):
    ans = 0
    for p in points:
        temp = 0
        for q in points:
            if math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) <= 2 * r:
                print(p, q)
                temp += 1

        if temp > ans:
            print(p)
            ans = temp
    print(ans)


#numPoints(points=[[-2, 0], [2, 0], [0, 2], [0, -2]], r=2)
numPoints(points=[[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], r=5)

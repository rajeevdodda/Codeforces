# https://codeforces.com/contest/456/problem/A


n = int(input())

price, quality = map(int, input().split())

high_quality_laptop = low_price_laptop = high_price_laptop = low_quality_laptop = (price, quality)

for i in range(n - 1):
    price, quality = map(int, input().split())
    if price > low_price_laptop[0] and quality < low_price_laptop[1]:
        print("Happy Alex")
        break
    else:
        if price < low_price_laptop[0]:
            low_price_laptop = price, quality
    if price > high_quality_laptop[0] and quality < high_quality_laptop[1]:
        print("Happy Alex")
        break
    else:
        if quality > high_quality_laptop[1]:
            high_quality_laptop = price, quality
    if price < high_price_laptop[0] and quality > high_price_laptop[1]:
        print("Happy Alex")
        break
    else:
        if price > high_price_laptop[0]:
            high_price_laptop = price, quality

    if price < low_quality_laptop[0] and quality > low_quality_laptop[1]:
        print("Happy Alex")
        break
    else:
        if quality > low_quality_laptop[1]:
            low_quality_laptop = price, quality
else:
    print("Poor Alex")

while True:
    price = int(input("상품의 가격 = "))
    if price != 0:
        if price > 20000:
            cost = 0
        elif price > 10000:
            cost = 1500
        else:
            cost = 3000
        print("배송비 = ", cost)
    else:
        break
print("bye")
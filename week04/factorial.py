import random, turtle

def factorial():
    n = int(input("숫자 : "))
    f=1
    for i in range(1, n+1):
        f = f*i
    print(f)

# 역 factorial
def factorialReverse():
    n = int(input("숫자 : "))
    for i in range(n-1, 0, -1):
        n = n*i
    print(n)

def gugu():
    n = int(input("숫자 : "))
    print(f"{n}의 구구단")
    for i in range(1, 10):
        print(f"{n}X{i} = {n * i}")

def randomMath():
    a = random.randint(1, 101)
    count = 0
    while True:
        b = int(input("숫자 : "))
        count += 1
        if(b > a):
            print("큼")
        elif(b < a):
            print("너무 작음")
        elif(b == a):
            print("정답")
            print(f"count = {count}")
            break

def randomTur():
    t = turtle.Turtle()
    while True:
        forward = random.randint(1, 91)
        way = random.randint(0, 2)
        angle = random.randint(1, 91)

        t.forward(forward)
        if(way == 0):
            t.left(angle)
        elif(way == 1):
            t.right(angle)
    turtle.mainloop()
    turtle.bye()


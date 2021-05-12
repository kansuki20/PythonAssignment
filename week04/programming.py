import turtle, random

# 전부 함수로 처리

# 연습문제 2번
def practice2():
    myList = [11, 22, 23, 99, 81, 93, 35]
    a = 0
    for i in range(len(myList)): # myList의 길이만큼 반복
        a += myList[i]
    print(a)

# 연습문제 5번
def practice5():
    a = int(input("정수를 입력하시오 : "))
    for i in range(0, a): # 세로의 길이
        for j in range(0, i): # 가로의 길이
            print(j+1, end=" ")
        print(i+1)

# 연습문제 9번
def practice9():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i * j, end=" ")
        print()

# 연습문제 18번
def practice18():
    t = turtle.Turtle()
    for i in range(10):
        # r, x, y 전부 난수 처리
        r = random.randint(1, 100)
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        t.up() # 거북이가 이동하는 동안에는 선을 긋지 않음
        t.goto(x, y)
        t.down() # 거북이가 원을 그리는 동안에는 선을 긋게 함
        t.circle(r)
    turtle.mainloop()
    turtle.bye()
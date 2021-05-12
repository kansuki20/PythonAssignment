#과제 01
def display(count, msg="Welcome"):
    for i in range(count):
        print(msg)

#과제 02
def display2(count, **msg):
    for i in range(count):
        print(msg)

#교재 p246 03
def calc():
    x = int(input("첫 번째 정수를 입력하시오: "))
    y = int(input("두 번째 정수를 입력하시오: "))
    print(f"{x+y}, {x-y}, {x*y}, {x/y}이 반환되었습니다.")

#교재 p246 04
def getGrade():
    score = int(input("점수를 입력하세요: "))
    grade = 0
    if(score >= 90):
        grade = "A"
    elif(score >= 80):
        grade = "B"
    elif(score >= 70):
        grade = "C"
    elif(score >= 60):
        grade = "D"
    else:
        grade = "F"
    print(f"성적은 {grade}입니다.")

#교재 p249 15
def drawTurtle():
    import turtle
    size = int(input("사이즈를 입력하시오 : "))
    t = turtle.Turtle()
    while True:
        t.forward(size)
        t.left(90)
        size += 5
    turtle.mainloop()
    turtle.bye()

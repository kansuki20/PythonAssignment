import turtle

t = turtle.Turtle()
t.shape("turtle")
def turtleMoveLeft(tur, rad, move):
    tur.left(rad)
    tur.forward(move)
def turtleMoveRight(tur, rad, move):
    tur.right(rad)
    tur.forward(move)

while True:
    command = input("l=왼쪽 r=오른쪽 q=끝 : ")
    if command == "q":
        print("끝")
        break
    rad = int(input("회전할 각도 : "))
    dis = int(input("이동할 거리 : "))
    if command == "l":
        turtleMoveLeft(t, rad, dis)
    elif command == "r":
        turtleMoveRight(t, rad, dis)
turtle.mainloop()
turtle.bye()
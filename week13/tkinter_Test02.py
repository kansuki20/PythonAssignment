from tkinter import *

window = Tk()

counter = 0

def clicked():
    global counter
    counter += 1
    label['text'] = '버튼 클릭 횟수:' + str(counter)

def init(): #initialization
    global counter
    label['text'] = '초기화됨'
    counter = 0

label = Label(window, text="아직 눌려지지 않음")
label.pack()
button = Button(window, text="증가", command=clicked).pack()
buttonInit = Button(window, text="초기화", command=init).pack()


window.mainloop()

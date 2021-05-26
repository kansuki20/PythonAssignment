from tkinter import *

window = Tk()

window.geometry("800x600") # width x heightst
window.title("tkinter test")

l1 = Label(window, text="Hello tkinter")

l2 = Label(window, text="이름")

l3 = Label(window, text="電話番号")

l4 = Label(window, text="住所")

l5 = Label(window, text="e-mail")


b1 = Button(window, text="검색", bg='orange', fg='blue', width=10, height=2)
b2 = Button(window, text="추가", bg='orange', fg='blue', width=10, height=2)
b3 = Button(window, text="삭제", bg='orange', fg='blue', width=10, height=2)
b4 = Button(window, text="수정", bg='orange', fg='blue', width=10, height=2)
b5 = Button(window, text="종료", bg='orange', fg='blue', width=10, height=2)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)

e1 = Entry(window)
# e1.pack()

window.mainloop()

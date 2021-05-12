list = []
def x(y):
    return(y)
list.append(1)
list.append(3)
list.append("slsl")
list.append(x)
list.append(False)
print(type(list[4]))
print(list)
print("False의 위치", list.index(False))

# list 값 변경
print("변경전 list 3 :", list[3])
list[3] = "s"
print("list 3 :", list[3])
# list 값 삭제
print("삭제전 list 1 :", list[1])
list.remove(3)
print("list 1 :", list[1])
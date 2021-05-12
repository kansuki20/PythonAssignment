x, y, z = eval(input("3개의 정수를 입력하시오 : "))

def xyz(a, b, c):
    if(x > y):
        if(y > z):
            return z
        else:
            return y
    else:
        if(x > z):
            return z
        else:
            return x

print(xyz(x, y, z))
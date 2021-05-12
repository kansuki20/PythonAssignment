
def chkEvenOdd(n): # 변수를 n에 받으면 홀수인지 짝수인지 구분
    if n%2 == 0:
        print(f"{n} = 짝수")
    else:
        print(f"{n} = 홀수")

while True: # 입력받는 값이 0000이 아닌동안 무한반복
    x = int(input("홀수 짝수 구분 : "))
    if x != 0000:
        chkEvenOdd(x)
    else:
        print("끝")
        break
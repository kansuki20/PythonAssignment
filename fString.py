import random

score = 0
count = 0

while count < 5: #count가 5가 될때까지
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    #format
    answer = int(input('{} + {} = '.format(x, y))) # answer = int(input('{} + {} = '.format(x, y)))
    flag = (answer == (x+y)) #bool 변수에 결과를 저장하고 출력
    if(flag == True):
        print(True)
        score += 20
    else:
        print(False)
    count += 1

print(f"총점 = {score}")
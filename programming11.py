weight = int(input("무게(킬로그램) : "))
height = float(input("키(미터) : "))
BMI = weight/height**2
print(f"당신의 BMI : {BMI}")
if(BMI > 30):
    print("비만입니다.")
elif(BMI >= 25 or BMI < 30):
    print("과체중입니다.")
elif(BMI >= 20 or BMI < 25):
    print("정상입니다.")
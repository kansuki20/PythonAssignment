list01 = []
student = 5
count = 0
for i in range (student):
    list01.append(int(input("점수를 입력하시오 : ")))
    if(list01[i] >= 80):
        count += 1

print(f"성적 평균 = {sum(list01)/5}")
print(f"최대 점수 = {max(list01)}")
print(f"최소 점수 = {min(list01)}")
print(f"80점 이상인 과목 수 = {count}")
print("sorting : ", sorted(list01))
import pickle

def main():
    address_book = {}  # 공백 딕셔너리를 생성한다.
    # 주소록 파일 불러오기
    try:
        infile = open("./addressData.txt", "r")
        while True:
            lineR = infile.readline().split(", ")
            if len(lineR) == 1: #공백인 readline()은 길이 1의 배열로 넘어옴
                break
            address_book[lineR[0]] = [lineR[1].strip("\'"), lineR[2].strip("\'"), lineR[3].rstrip().strip("\'")]
        for key, value in address_book.items():
            print(f"{key} : {value}")
        infile.close()
        print("--------------------------------------")
    except:
        print("파일없음")
        print("--------------------------------------")

    while True:
        user = display_menu()
        if user == 1:  # 연락처 추가
            name, number, address, email = get_contact()
            address_book[name] = [number, address, email]  # key에 name과 value에 number, address, email을 추가한다.
        elif user == 2:  # 연락처 삭제
            name = input("이름 : ")
            address_book.pop(name)  # name을 키로 가지고 항목을 삭제한다.
        elif user == 3:  # 연락처 검색
            name = input("이름 : ")
            if (address_book.get(name)):
                print(f"{name}의 연락처 : {address_book[name]}")
            else:
                print(f"({name}) 딕셔너리에 없음")
            print("--------------------------------------")
            # 검색 : 도전 문제 참조
        elif user == 4:  # 연락처 출력
            print("--------------------------------------")
            for key in sorted(address_book):
                print(key, "의 전화번호:", address_book[key])
            print("--------------------------------------")
        else:  # 파일 저장하기
            infile = open("./addressData.txt", "w")
            for key in address_book:
                infile.write(key + ", " + str(address_book[key]).strip("[").strip("]") + "\n")
            print("파일이 저장되었습니다!")
            infile.close()
            break

        # elif user == 6:  # 파일 불러오기
        # with open("./addressData.bin", "rb") as f:
        #  address_book = pickle.load(f)
        #  print(address_book)

# 이름과 전화번호를 입력받아서 반환한다.
def get_contact():
    name = input("이름: ")
    number = input("전화번호: ")
    address = input("주소: ")
    email = input("이메일: ")
    return [name, number, address, email]


# 메뉴를 화면에 출력한다.
def display_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 저장 및 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

# __main__은 프로그램의 시작점
if __name__ == '__main__':
    main()

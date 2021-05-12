def get_rect_area(w, h):
    return w*h


def main():
    w = int(input("넓이 : "))
    h = int(input("높이 : "))
    print("사각형의 면적은", get_rect_area(w, h))

main()
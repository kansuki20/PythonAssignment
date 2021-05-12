infile = open("./input.txt", "w")
line = {}

def get_contact():
    name = input("이름: ")
    number = input("전화번호: ")
    address = input("주소: ")
    email = input("이메일: ")
    return [name, number, address, email]

while True:
    name, number, address, email = get_contact()
    if(name == "q"):
        break
    else:
        line[name] = [number, address, email]

for key in line:
    infile.write(key + ", " + str(line[key]).strip("[").strip("]") + "\n")

infile.close()

infile = open("./input.txt", "r")

while True:
    lineR = infile.readline().split(", ")
    if len(lineR) == 1:
        break
    line[lineR[0]] = [lineR[1].strip("\'"), lineR[2].strip("\'"), lineR[3].rstrip().strip("\'")]

print(line["w"])

infile.close()


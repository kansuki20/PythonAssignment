import csv

file = open('output.csv', 'w', encoding='utf-8', newline='')
dic = {'sl':"hi", 'sll':'hii'}
wr = csv.writer(file)
for key in dic:
    wr.writerow([key, dic[key]])
file.close()



dic1 = {}
ls = 0

file = open('output.csv', 'r', encoding='utf-8')
lines = csv.reader(file)

for line in lines:
    print(line)

file.close()
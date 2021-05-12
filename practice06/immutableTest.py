meter_list = [3, 7, 9, 10]
centi_meter_list = [100*i for i in meter_list if i%2 != 0]
print(centi_meter_list)

result = [x * y for x in range(1, 10) for y in range(1, 10)]


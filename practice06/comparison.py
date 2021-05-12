name = ['a', 'b']
value = [1, 2]
for n, v in name, value:
    print(n, v)
print("--------")
for n, v in zip(name, value):
    print(n, v)

stack = []

for i in range(3):
    f = input("과일을 입력하시오:")
    stack.append(f)

print(stack)
print(stack.pop())
print("----------------")
for i in range(len(stack)):
    print(stack.pop())

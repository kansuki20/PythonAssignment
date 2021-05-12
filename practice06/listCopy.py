t = [1, 3, 5, 6, 10]
v = t
v.append(5)
print("v =", v)
print("t =", t)
print("-----------------")
x = list(t) # x = list(t) 와 x = t[:]와 같음
t.append(20)
print("t =", t)
print("x =", x)
print("-----------------")
print("x =", x[:: -1])

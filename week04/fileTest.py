# f = open('out.txt', 'w')
# print("print!!", file=f)
# f.close()
#
# print(open('out.txt').read())
def d():
    data = 123
    print('%04d' %data)
    print('%d, %x, %o' %(data, data, data))

def f():
    data = 125.45
    print('%f' %data)
    print('%10.1f' %data)
    print('%-10.3f' %data)

def s():
    data = "Python"
    print('%s' %data)
    print('%08s' %data)

print(r"\n\\\lsiel\.\]\-")
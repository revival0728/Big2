def t1():
    print(1)
def t2():
    print(2)
def t3():
    print(3)
def t4():
    print(4)

testList = [tuple([t1, t2]), tuple([t3, t4])]

for i in testList:
    for j in i:
        j()

a = 100
#print(a)

def testA():
    print(a)

def testB():
    #如果直接修改 此时的a是局部变量a
    a = 300
    print(a)

def testC():
    print(a)

testA()
testB()
testC()
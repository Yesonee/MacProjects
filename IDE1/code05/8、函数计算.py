#三个数求和
def sum_num(a,b,c):
    return  a+b+c

result = sum_num(1,2,3)
print(result)

#2、任意三个数求平均值
def average_num(e,d,f):
    #先求和 再除以平均值
    sumResult = sum_num(e,d,f)
    return  sumResult / 3
result1 = average_num(1,2,3)

print(result1)
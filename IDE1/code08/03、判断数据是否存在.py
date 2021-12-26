str1 = 'abcd'
list1 = [10,20,30,40]
t1 = ('name' , 'python','age' )

# in 和 not in
#1、字符a是否存在
print('a' in str1)
print('a' not in str1)

#2、数据10是否存在
print(10 in list1)
print(10 not in list1)

#3、100是否存在
print(100 in list1)
print(100 not in list1)

#3、name是否存在
print('name' in t1)
print('name' not in t1)
print('name' not in t1.keys())
print('name' not in t1.values())
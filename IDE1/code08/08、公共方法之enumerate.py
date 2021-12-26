list1 = ['a','b','c','d','e']

#用法：：enumerate（可遍历对象，start=0）
#enumerate 返回结果是元组，元组第一个数据是原是迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
# for i in enumerate(list1):
#     print(i)


#原始坐标重2开始
for i in enumerate(list1,start=2):
    print(i)
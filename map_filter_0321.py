# -*-coding:utf-8-*-

#map
it = [1, 3, 5, 7, 9]

def add(num):
    return num + 2

rs = map(add,it)
print(list(rs))      #需要用list进行转换

rs2 = map(lambda x:x * x,[1,2,3,4,5])
print(list(rs2))

#filter filter（）函数包括两个参数，分别是function和list。
# 该函数根据function参数返回的结果是否为真来过滤list参数中的项，最后返回一个新列表

li = [2,5,8,4,6,0]
print(list(filter(lambda x:x>3,li)))

#如果filter参数值为None，就使用identity（）函数，list参数中所有为假的元素都将被删除。
b = filter(None,li)
print(list(b))

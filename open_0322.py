# -*-coding:utf-8-*-

"""
文件操作
"""
# r  读取一次就默认关闭了
f = open('test.txt','r')
print(f.readlines())
f.close()

#w     只写不可读，不存在则创建，存在则报错
f2 = open('test2.txt','w')
f2.write('i love python')
f2.close()

# a 追加模式  不存在则创建，存在则追加
f3 = open('test2.txt','a')
f3.write('\nlove you')
f3.close()

# rb wb ab 以二进制进行读写加    r+ ，w+ ，x+ ,a+ ,能读能写
f4 = open('test2.txt','ab')
f4.write(bytes('\n深圳',encoding='utf-8')) #"深圳"是字符串。需要用bytes转换成字节
f4.close()
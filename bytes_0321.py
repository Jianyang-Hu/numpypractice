#-*-coding:utf-8-*-

# name = 'laogaoyang'
# nameBytes = name.encode('utf-8')   # 字节
# nameStr = nameBytes.decode('utf-8')# 字符串
# print(name)
# print(nameBytes)
# print(nameStr)

"""
bytearray和bytes不一样的地方在于，bytearray是可变的。

"""
a = bytes("loveyouverymuch深圳",encoding='utf-8')
print(a)

b = bytearray("love you 深圳",encoding='utf-8')
print(b)

"""
一个汉字用utf-8的话是用了3个字节，GBK的话是用了两个
{>>> '汉'.encode('utf-8')
b'\xe6\xb1\x89'
>>> '汉'.encode('GBK')
b'\xba\xba'}
"""

b[:6] = bytearray('广州'.encode())
print(b.decode())
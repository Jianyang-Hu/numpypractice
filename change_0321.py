#-*-coding:utf-8-*-
"""
十进制转换

"""

#转换成十进制 int
a = 0Xba5
print(int(a))

b = int('a5',base=16)
print(b)

#十六进制 表示法0xaf   hex()
c = hex(1234)
print(c)

d = 0o11
print(hex(d))

#八进制0o(第一个0是数字0，第二个是字母0)  oct()
e = 0o11227
print(oct(e))

f = 11227
print(oct(f))
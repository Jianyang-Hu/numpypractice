# -*- coding: utf-8 -*-

"""
re.match       从头开始匹配

re.search       浏览全部字符串，匹配第一个符合规则的字符串

re.findall       将匹配到的所有内容都放置在一个列表中

re.finditer

re.split

re.sub

"""


import re


"""
Python通过re模块提供对正则表达式的支持。
使用re的一般步骤是先使用re.compile()函数，
将正则表达式的字符串形式编译为Pattern实例，
然后使用Pattern实例处理文本并获得匹配结果（一个Match实例），
最后使用Match实例获得信息，进行其他的操作。
"""
s = "hello World!"

regex = re.compile("hello world!", re.I)
print (regex.match(s).group())

s2 = "adfad asdfasdf asdfas asdfawef asd adsfas"
reObj1=re.findall('((\w+)\s+\w+)',s2)
print(reObj1)

"""
I    IGNORECASE， 忽略大小写的匹配模式

一般，m.group(N) 返回第N组括号匹配的字符。
而m.group() == m.group(0) == 所有匹配的字符，与括号无关，这个是API规定的。
m.groups() 返回所有括号匹配的字符，以tuple格式。
m.groups() == (m.group(0), m.group(1), ...)
"""

s3 = 'hello World!'

regex = re.compile("hELlo world!", re.I)
print (regex.match(s3).group())

"""
M    MULTILINE，多行模式, 改变 ^ 和 $ 的行为
"""
s4 = '''first line
second line
third line'''

regex_start_m = re.compile("^\w+", re.M)
print (regex_start_m.findall(s4))

"""
S  　DOTALL，此模式下 '.' 的匹配不受限制，可匹配任何字符，包括换行符
"""
regex_dotall = re.compile(".+", re.S)
print (regex_dotall.findall(s4))

"""
search(pattern, string, flags=0)函数类似于 match,
不同之处在于不限制正则表达式的开始匹配位置
"""
s5 = '''first line
second line
third line'''

print (re.match('i\w+', s5))
print (re.search('i\w+', s5))
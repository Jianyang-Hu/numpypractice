# -*-coding:utf-8-*-
"""
动态参数
参数前一个“*”：在函数中会把传的参数转成一个元组。
“**args”的参数：函数中被转成一个字典。
"""


def func(*args, **kwargs):  # one * write args,two ** kwargs
    print("%s----%s" % (args, kwargs))

func(1, 3, 5, 7, a=1, b=2)

# 需要交代类型
list = (9, 8, 7, 6)
dic = {'k1': 2, 'k2': 5, 'k3': 10}
func(*list, **dic)

# 不加*就整体当一个元素
func(list)
func(*list)

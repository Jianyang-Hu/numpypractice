# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/4/10 21:24
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : with_0410.py
# @Software: PyCharm

# somefile = open(r'test.txt')
#
# try:
#     for line in somefile:   #按行读取文件
#         print (line)
#         # ...more code
# finally:
#     somefile.close()

"""
     with 语句执行过程

    1.执行 context_expression，生成上下文管理器 context_manager
    2.调用上下文管理器的 __enter__() 方法；如果使用了 as 子句，则将 __enter__() 方法的返回值赋值给 as 子句中的 target(s)
    3.执行语句体 with-body
    4.不管是否执行过程中是否发生了异常，执行上下文管理器的 __exit__() 方法，__exit__() 方法负责执行“清理”工作，
    如释放资源等。如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，
    则以 None 作为参数调用 __exit__(None, None, None) ；如果执行过程中出现异常，
    则使用 sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)
    5.出现异常时，如果 __exit__(type, value, traceback) 返回 False，则会重新抛出异常，
    让with 之外的语句逻辑来处理异常，这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理

"""

import sys,contextlib

with open(r'test.txt') as context_manager:
    exit = type(context_manager).__exit__
    value = type(context_manager).__enter__(context_manager)
    exc = True  # True 表示正常执行，即便有异常也忽略；False 表示重新抛出异常，需要对异常进行处理
    try:
        try:
            target = value  # 如果使用了 as 子句
            for line in context_manager:
                    print (line)
                    # 执行 with-body
        except:
            # 执行过程中有异常发生
            exc = False
            # 如果 __exit__ 返回 True，则异常被忽略；如果返回 False，则重新抛出异常
            # 由外层代码对异常进行处理
            if not exit(context_manager, *sys.exc_info()):
                raise
    finally:
        # 正常退出，或者通过 statement-body 中的 break/continue/return 语句退出
        # 或者忽略异常退出
        if exc:
            exit(context_manager, None, None, None)
            # 缺省返回 None，None 在布尔上下文中看做是 False

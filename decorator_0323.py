# -*- coding: utf-8 -*-
import re
import logging

# 不带参数
# def use_logging(func):
#     def wrapper(*args, **kwargs):
#         logging.warn("%s is running" % func.__name__)
#         return func(*args)
#
#     return wrapper
#
# @use_logging
# def foo():
#     print("i am foo")
#
# foo()
#
# @use_logging
# def bar():
#     print("i am bar")
#
# bar()


#带参数
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#
#     return decorator
#
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
#
# foo()

#执行顺序
# def foo():
#     print('3')
#     print("foo")
#     print(4)
#
# def bar(func):
#     print('1')
#     func()
#     print(2)
#
# bar(foo)

#
# def use_logging(func):
#
#     def wrapper():
#             print('1')
#             logging.warn("%s is running" % func.__name__)
#             print('2')
#             return func()     # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
#             print('3')
#     print('6')
#     return wrapper
#     print('7')
#
# def foo():
#     print('4')
#     print('i am foo')
#     print('5')
#
# foo = use_logging(foo)     # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
# foo()                       # 执行foo()就相当于执行 wrapper()



def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running1" % func.__name__)
            elif level == "info":
                logging.info("%s is running2" % func.__name__)
            return func(*args)

        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)
    print("i am really %s" % name)


foo()

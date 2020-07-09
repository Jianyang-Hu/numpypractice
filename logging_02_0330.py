# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/30 11:19
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : logging_02_0330.py
# @Software: PyCharm

import logging
#  http://www.tuicool.com/articles/QveiAbq
"""
logging.basicConfig():用默认Formatter为日志系统建立一个StreamHandler，
设置基础配置并加到root logger中
"""
logging.basicConfig(level=logging.INFO,
                     format='%(asctime)s %(name)s %(levelname)s %(message)s',
                     datefmt='%m-%d %H:%M',
                     filename='log2.log',
                    filemode='w')

"""
 logging.StreamHandler

使用这个Handler可以向类似与sys.stdout或者sys.stderr的
任何文件对象(file object)输出信息。它的构造函数是：

StreamHandler([strm])

其中strm参数是一个文件对象。默认是sys.stderr
"""
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
"""
在 python 中，变量 __name__ 的名称就是当前模块的名称。比如，
在模块 “foo.bar.my_module” 中调用 logger.getLogger(__name__) 等价于
调用logger.getLogger(“foo.bar.my_module”) 。
"""
logging.getLogger('').addHandler(console)

logging.info("hello world!")
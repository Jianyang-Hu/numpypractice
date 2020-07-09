# -*- coding: utf-8 -*-
# @version : Python3.6
# @Time    : 2017/3/30 10:12
# @Author  : Jianyang-Hu
# @contact : jianyang1993@163.com
# @File    : logging_0330.py
# @Software: PyCharm
"""
Logging模块构成主要分为四个部分：

    Loggers：提供应用程序直接使用的接口
    Handlers：将Loggers产生的日志传到指定位置
    Filters：对输出日志进行过滤
    Formatters：控制输出格式

场景 	                                        适合使用的方法
在终端输出程序或脚本的使用方法 	print
报告一个事件的发生（例如状态的修改） 	logging.info()或logging.debug()
发生了一个特定的警告性的事件 	logging.warn()
发生了一个特定的错误性的事件 	raise
发生了一个特定的错误性的事件，
但是又不想因为此错误导致程序退出
（例如程序是一个守护进程） 	logging.error(),logging.exception(),logging.critical()

"""
import logging

#logging.basicConfig():用默认Formatter为日志系统建立一个StreamHandler，设置基础配置并加到root logger中
logging.basicConfig(filename = 'log.log',
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(message)s',
                    datefmt='%Y - %a - %d %H:%H:%S %p',
                    level=logging.INFO
                    )

logging.critical('c')
logging.fatal('f')
logging.error('e')
logging.warning('w')
logging.debug('d')
logging.log(logging.INFO,'333')
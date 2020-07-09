# -*- coding: utf-8 -*-
# @version : ??
# @Time    : 2017/3/29 17:31
# @Author  : Aries
# @Site    : 
# @File    : shutil_0329.py
# @Software: PyCharm

import zipfile
"""
压缩 解压 .zip包
"""
# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('test.txt')
z.write('test2.xml')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()


import tarfile
"""
压缩 解压 .tar包
"""

# 压缩
tar = tarfile.open('two.tar', 'w')
tar.add('E:\Python3.6\practice', arcname='demo02.xml')
tar.add('E:\Python3.6\practice', arcname='test.txt')
tar.close()

# 解压
tar = tarfile.open('two.tar', 'r')
tar.extractall()  # 可设置解压地址
tar.close()
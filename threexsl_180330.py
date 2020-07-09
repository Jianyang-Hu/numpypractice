#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd		# 读取模块
from xlutils.copy import copy	# 写入模块

# 读取表格
rb = xlrd.open_workbook('F:\\汇总统计表 - 副本.xlsx')
wb = copy(rb)
sheets = rb.sheets()
table_en = sheets[0]  # 英文统计表
table_cn = sheets[1]  # 中文统计表
table_data1 = sheets[2]  # 原始数据表（电话，邮箱）
table_data_en = sheets[3]  # 原始数据表（英文）
table_data_cn = sheets[4]  # 原始数据表（中文）

# 遍历英文统计表，查询电话和主题
n_of_rows = table_en.nrows  # 行数
ws = wb.get_sheet(0)
for i in range(1, n_of_rows):
    # 跳过表示国家(即第二列为空)的单元格
    if table_en.cell(i, 3).value:
        name = table_en.cell(i, 2).value
        print('姓名：%s' % name)
        info = {'name': name, 'row': i}  # 名称与位置、电话、标题的字典
        # 查询电话
        n2 = table_data1.nrows
        for j in range(1, n2):
            if name in table_data1.cell(j, 0).value:
                tel = table_data1.cell(j, 2).value
                info['tel'] = tel
                print('电话：%s' % tel)
                break
        # 查询演讲主题
        n3 = table_data_en.nrows
        for j in range(1, n3):
            if name in table_data_en.cell(j, 2).value:
                theme = table_data_en.cell(j, 7).value
                if theme:
                    info['theme'] = theme
                    print('演讲主题：%s\n' % theme)
                    break
        # 写入信息
        if 'tel' in info:
            ws.write(i, 5, info['tel'])
        if 'theme' in info:
            ws.write(i, 7, info['theme'])
            
# 遍历中文统计表，查询电话和主题
n_of_rows = table_cn.nrows  # 行数
ws = wb.get_sheet(1)
for i in range(1, n_of_rows):
    # 跳过表示国家(即第二列为空)的单元格
    if table_cn.cell(i, 1).value:
        name = table_cn.cell(i, 0).value
        print('姓名：%s' % name)
        info = {'name': name, 'row': i}  # 名称与位置、电话、标题的字典
        # 查询电话
        n2 = table_data1.nrows
        for j in range(1, n2):
            if name in table_data1.cell(j, 0).value:
                tel = table_data1.cell(j, 2).value
                info['tel'] = tel
                print('电话：%s' % tel)
                break
        # 查询演讲主题
        n3 = table_data_cn.nrows
        for j in range(1, n3):
            if name in table_data_cn.cell(j, 0).value:
                theme = table_data_cn.cell(j, 5).value
                if theme:
                    info['theme'] = theme
                    print('演讲主题：%s\n' % theme)
                    break
        # 写入信息
        if 'tel' in info:
            ws.write(i, 3, info['tel'])
        if 'theme' in info:
            ws.write(i, 5, info['theme'])
wb.save('F:\\汇总统计表2.xls')

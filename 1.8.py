#coding: utf-8
import os
import json
import xlwt
# 存放文件的目录
filepath = 'D:'
os.chdir(filepath)
# 读取文件内容
with open('student.txt') as f:
    content = f.read()
# 转为json
d = json.loads(content)
file = xlwt.Workbook()
# 添加sheet
table = file.add_sheet('test')
for row, i in enumerate(list(d)):
    table.write(row, 0, i)
    for col, j in enumerate(d[i]):
        table.write(row, col + 1, j)
file.save('student.xls')

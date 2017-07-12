#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author : yemilice_lau
import xlrd
import xlwt
from datetime import datetime,date
data = xlrd.open_workbook('test_data/data.xls')
table = data.sheet_by_name(u'Sheet1')
nrows = table.nrows   #行数
ncols = table.ncols   #列数
cell_A1 = table.cell(1,0).value
print cell_A1
for i in range(nrows):
    print table.row_values(i) #循环列表数据

def read_excel():
    workbook = xlrd.open_workbook('test_data/data.xls')





if __name__ == '__main__':
    print 'test'







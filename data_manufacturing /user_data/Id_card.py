#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author : yemilice_lau
import random
import string
import os
from datetime import date,timedelta
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = BASE_DIR + "districtcode.txt"

# 随机生成手机号码
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

# 随机生成身份证号
# 身份证号生成策略：
# 前1、2位数字表示：所在省份的代码,第3、4位数字表示：所在城市的代码,第5、6位数字表示：所在区县的代码,第7~14位数字表示：出生年、月、日
# 第15~17位数字是顺序码,顺序码的奇数分配给男性,偶数分配给女性,第18位数字是校检码：用来检验身份证的正确性
def getdistrictcode():
    with open('districtcode.txt') as file:
        data = file.read()
        districtlist = data.split('\n')
    for node in districtlist:
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            # print code
            codelist.append({"state": state, "city": city, "district": district, "code": code})


def gennerator():
    global codelist
    codelist = []
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
    id = id + str(random.randint(1930, 2017))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id

#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author : yemilice_lau
import random

def generate_bankcard_num():
    check_code = random.randint(10000,20000)
    bank_card = '567889933678889' + str(check_code)
    return bank_card







#
# if __name__ == '__main__':
#     print 'test'
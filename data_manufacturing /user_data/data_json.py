#-*- coding:UTF-8 -*-
import urllib,urllib2
import threading
import time
import requests,httplib
import re
import json
import Id_card
import chinesename
import bank_card
import random
import cProfile
import sys
method = "post"
# url = "http://114.55.125.148:8006/collection/import_collection_info"
url = "http://127.0.0.1:8006/collection/import_collection_info"
def postRequest(threadNum):
    repayment_id = random.randint(30000,40000)
    bank_number = bank_card.generate_bankcard_num()
    phone_number = Id_card.createPhone()
    card_number = Id_card.gennerator()
    name = chinesename.run()
    data = {
        "actual_collection_data":[
            {
                "card_info":{
                    "bank_type":"xxxx",
                    "card_number":bank_number,
                    "card_type":"3",
                    "phone_no":phone_number
                },
                "id_card":{
                    "back_pic":"",
                    "front_pic":"",
                    "handle_pic":""
                },
                "repayment_info":{
                    "accounts_receivable":100,
                    "actual_amount":1000,
                    "amount":1100,
                    "apply_time":"2016-05-02 17:46:05",
                    "installment_count":1,
                    "installment_day":14,
                    "installment_id":0,
                    "installment_info":[
                        {
                            "exact_pay_amount":0,
                            "installment_id":1,
                            "installment_number":1,
                            "installment_status":2,
                            "overdue_amount":7340,
                            "overdue_days":367,
                            "should_pay_amount":1100,
                            "should_repay_time":"2016-05-16 00:00:00"
                        }
                    ],
                    "pay_time":"2016-05-02 17:46:05",
                    "penalty":20,
                    "repay_amount":1100,
                    "repayment_id":repayment_id,
                    "rest_amount":1100
                },
                "user_info":{
                    "channel":"wechat",
                    "contact_list":[
                        {
                            "name":"张张张1",
                            "phone_no":"18521030270",
                            "relationship":"同学"
                        },
                        {
                            "name":"测试",
                            "phone_no":"17602150413",
                            "relationship":"朋友"
                        }
                    ],
                    "email":"",
                    "gender":"男",
                    "home_address":"河南省周口地区周口地区",
                    "id_no":card_number,
                    "mariage":0,
                    "name":name,
                    "phone_no":phone_number,
                    "postcode":"级别：A，芝麻分:599，备注：null",
                    "register_time":"",
                    "work_address":"",
                    "work_name":"",
                    "work_number":""
                }
            }
        ],
        "all_collection_data_length":1,
        "org_account":"lld",
        "org_token":"58ea49418e89ef17dffadac9182ef1556c1a0bde8bd0dcbe163dc1dcb908c529"
    }
    postdata = json.dumps(data)
    header = {"content-type": "application/json"}
    r = requests.post(url=url,data=postdata,headers = header)
    # if response.status in range(200, 300):
    #     print u"线程" + str(threadNum) + u"状态码：" + str(response.status)
    # conn.close()


def run(threadNum, internTime, duration):
    # 创建数组存放线程
    threads = []
    try:
        # 创建线程
        for i in range(1, threadNum):
            # 针对函数创建线程
            t = threading.Thread(target=postRequest, args=(i,))
            # 把创建的线程加入线程组
            threads.append(t)
    except Exception, e:
        print e

    try:
        # 启动线程
        for thread in threads:
            thread.setDaemon(True)
            thread.start()
            time.sleep(internTime)

            # 等待所有线程结束
        for thread in threads:
            thread.join(duration)
    except Exception, e:
        print e


if __name__ == '__main__':
    startime = time.strftime("%Y%m%d%H%M%S")

    now = time.strftime("%Y%m%d%H%M%S")
    duratiion = raw_input(u"输入持续运行时间:")
    while (startime + str(duratiion)) != now:
        run(10, 1, int(duratiion))
        now = time.strftime("%Y%m%d%H%M%S")

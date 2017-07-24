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
url = "http://114.55.125.148:8006/collection/import_collection_info"

repayment_id = random.randint(30000,40000)
bank_number = bank_card.generate_bankcard_num()
phone_number = Id_card.createPhone()
card_number = Id_card.gennerator()
print bank_number
print phone_number
print repayment_id
print chinesename.run()
print card_number
name = chinesename.run()
data = {
    "actual_collection_data":[
        {
            "card_info":{
                "bank_type":"xxxx",
                "card_number":"",
                "card_type":"3",
                "phone_no":phone_number
            },
            "id_ca  rd":{
                "back_pic":"",
                "front_pic":"",
                "handle_pic":""
            },
            "repayment_info":{
                "accounts_receivable":"0",
                "actual_amount":"1000",
                "amount":"1100",
                "apply_time":"2016-05-02 17:46:05",
                "installment_count":"1",
                "installment_day":"14",
                "installment_id":"0",
                "installment_info":[
                    {
                        "exact_pay_amount":"0",
                        "installment_id":"1",
                        "installment_number":1,
                        "installment_status":"2",
                        "overdue_amount":"7340",
                        "overdue_days":"367",
                        "should_pay_amount":"1100",
                        "should_repay_time":"2016-05-16 00:00:00"
                    }
                ],
                "pay_time":"2016-05-02 17:46:05",
                "penalty":"20",
                "repay_amount":"1100",
                "repayment_id":repayment_id,
                "rest_amount":"1100"
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
                "mariage":"",
                "name":name,
                "phone_no":phone_number,
                "postcode":"级别：A，芝麻分:599，备注：null",
                "register_time":"",
                "work_address":"",
                "work_name":"",
                "work_number":""
            }
        },
    ],

    "all_collection_data_length":1,
    "org_account":"wd",
    "org_token":"58ea49418e89ef17dffadac9182ef1556c1a0bde8bd0dcbe163dc1dcb908c529"
}
postdata = json.dumps(data)
header = {"content-type": "application/json"}
r = requests.post(url=url,data=postdata,headers = header)

    # if response.status in range(200, 300):
#-*- coding:UTF-8 -*-
import urllib,urllib2
import threading
import time
import requests
import re
import json
method = "post"
url = "http://114.55.125.148:8006/collection/update_collection_info"
# url = "http://127.0.0.1:8003/collection/update_collection_info"
data = {
	"actual_collection_data":[
		{
			"repayment_info":{
				"amount":1300,
				"apply_time":"2017-04-17 10:21:13",
				"installment_count":1,
				"installment_id":1,
				"installment_info":[
					{
						"exact_pay_amount":0,
						"installment_id":1,
						"installment_number":1,
						"installment_status":2,
						"overdue_amount":400,
						"overdue_days":20,
						"should_pay_amount":1300
					}
				],
				"pay_time":"2017-04-17 10:21:13",
				"repay_amount":0,
				"repayment_id":"2536615",
				"rest_amount":0
			},
			"user_info":{
				"channel":"",
				"contact_list":[],
				"email":"",
				"gender":"",
				"home_address":"",
				"id_no":"422325198204025710",
				"mariage":0,
				"name":"廖维辉",
				"phone_no":"15872828796",
				"postcode":"",
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
data = json.dumps(data)
print data
#线程数
thread_num = 20
#线程循环次数
one_work_num = 2
#请求时间间隔
loop_sleep = 1
#平均响应时间列表
response_time = []
#错误信息列表
error = []

class CreateThread:
    def __init__(self):
        pass

    @classmethod
    def thread_api(cls):
        global results
        try:
            if method == "post":
                results = requests.post(url,data)
            if method == "get":
                results = requests.get(url,data)
            return results
        except requests.ConnectionError:
            return results

    #获取响应时间
    @classmethod
    def thread_response(cls):
        responsetime = float(CreateThread.thread_api().elapsed.microseconds) / 1000
        return responsetime

    #获取平均响应时间
    @classmethod
    def thread_response_avg(cls):
        avg = 0.000
        l = len(response_time)
        for num in response_time:
            avg += 1.000 * num / 1
        return avg

    #获取当前时间格式
    @classmethod
    def thread_time(cls):
        return time.asctime(time.localtime(time.time()))

    #获取错误的返回状态码
    @classmethod
    def thread_error(cls):
        try:
            pa = u"个人信息"
            pattern = re.compile(pa)
            match = pattern.search(CreateThread.thread_api().text)
            if CreateThread.thread_api().status_code == 0:
                pass
                if match.group() == pa:
                    pass
            else:
                error.append(CreateThread.thread_api().status_code)
        except AttributeError:
            error.append("登录失败")

    @classmethod
    def thread_work(cls):
        threadname = threading.currentThread().getName()
        print "[", threadname, "] Sub Thread Begin"
        for i in range(one_work_num):
            CreateThread.thread_api()
            print "接口请求时间： ", CreateThread.thread_time()
            response_time.append(CreateThread.thread_response())
            CreateThread.thread_error()
            time.sleep(loop_sleep)
        print "[", threadname, "] Sub Thread End"

    # 工作线程循环

    @classmethod
    def thread_main(cls):
        start = time.time()
        threads = []
        for i in range(thread_num):
            t = threading.Thread(target=CreateThread.thread_work())
            t.setDaemon(True)
            threads.append(t)
        for t in threads:
            t.start()
        # 启动所有线程
        for t in threads:
            t.join()
        # 主线程中等待所有子线程退出
        end = time.time()

        print "========================================================================"
        print "接口性能测试开始时间：", time.asctime(time.localtime(start))
        print "接口性能测试结束时间：", time.asctime(time.localtime(end))
        print "接口地址：", url
        print "接口类型：", method
        print "线程数：", thread_num
        print "每个线程循环次数：", one_work_num
        print "每次请求时间间隔：", loop_sleep
        print "总请求数：", thread_num * one_work_num
        print "错误请求数：", len(error)
        print "总耗时（秒）：", end - start
        print "每次请求耗时（秒）：", (end - start) / (thread_num * one_work_num)
        print "每秒承载请求数（TPS)：", (thread_num * one_work_num) / (end - start)
        print "平均响应时间（毫秒）：", CreateThread.thread_response_avg()


if __name__ == '__main__':
    CreateThread.thread_main()



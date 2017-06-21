# -*- coding: utf-8 -*-
__author__ = "Yemilice_lau"

import time
import urllib2
import threading
from Queue import Queue
from time import sleep

# 性能测试页面
PERF_TEST_URL = "http://localhost:8080/perf.jsp"

# 配置:压力测试
# THREAD_NUM = 10            # 并发线程总数
# ONE_WORKER_NUM = 500       # 每个线程的循环次数
# LOOP_SLEEP = 0.01      # 每次请求时间间隔(秒)

# 配置:模拟运行状态
THREAD_NUM = 100  # 并发线程总数
ONE_WORKER_NUM = 10000  # 每个线程的循环次数
LOOP_SLEEP = 0.5  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0


# 具体的处理函数，负责处理单个任务
def doWork(index):
    t = threading.currentThread()
    # print "["+t.name+" "+str(index)+"] "+PERF_TEST_URL

    try:
        html = urllib2.urlopen(PERF_TEST_URL).read()
    except urllib2.URLError, e:
        print "[" + t.name + " " + str(index) + "] "
        print e
        global ERROR_NUM
        ERROR_NUM += 1


        # 这个是工作进程，www.linuxidc.com负责不断从队列取数据并处理


def working():
    t = threading.currentThread()
    print "[" + t.name + "] Sub Thread Begin"

    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
        sleep(LOOP_SLEEP)

    print "[" + t.name + "] Sub Thread End"


def main():
    # doWork(0)
    # return

    t1 = time.time()

    Threads = []

    # 创建线程
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    print "main thread end"

    t2 = time.time()
    print "========================================"
    print "URL:", PERF_TEST_URL
    print "任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM
    print "总耗时(秒):", t2 - t1
    print "每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)
    print "每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print "错误数量:", ERROR_NUM


if __name__ == "__main__": main()  
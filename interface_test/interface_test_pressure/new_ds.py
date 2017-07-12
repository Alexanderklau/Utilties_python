# -*- coding:utf-8 -*
import requests

#自动化接口测试工具

def test():
    url = "http://120.24.239.**:9080/user/app/login.do"  #登录的接口
    headers = {'content-type': 'application/json'}
    r = requests.get(url=url, headers=headers)
    return r.json()

def test_have_session(url):
    cookie = "JSESSIONID=" + "".join(test().get("JSESSIONID"))  #利用登录接口获取JSESSIONID
    headers = {'content-type': 'application/xml', 'Cookie': cookie}
    r = requests.post(url, headers=headers)
    return r.json()

if __name__ == "__main__":
    url = ""    #测试的接口url
    test_have_session(url)
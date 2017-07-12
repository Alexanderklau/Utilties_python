#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author : yemilice_lau
# -*- coding: utf-8 -*-
"""
出问题了立马发送邮件给我，不管什么时候
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from datetime import datetime
from_addr = '13281101982@163.com'
password = 'lwb13689963881'
to_addr = 'liuwenbo@rongshutong.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))
def send_email():
    msg = MIMEText('ERROR:今天的案件没有分配！','plain', 'utf-8')
    msg['From'] = _format_addr(u'刘文博 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(u'<%s>错误邮件' % datetime.now().strftime('%b-%d-%y %H:%M:%S'), 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


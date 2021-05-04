import requests
import time
# -*- coding:utf-8 -*-
#课程数据
kecheng = 126567
endkecheng = 126686
###基础数据
http = 'http://'
host = 'hubei.ouchn.cn'
studyurl = '/mod/page/view.php?id='

headers = {}
headers['Host'] = 'hubei.ouchn.cn'
headers['Connection'] = 'keep-alive'
headers['Upgrade-Insecure-Requests'] = '1'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3012.0 Safari/537.36'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate, sdch'
headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
headers['Cookie'] = 'MoodleSession=v0g60lsfn8kpbe8l0naveoajig; username=2042001200492; UserName=2042001200492'

###开始访问

while kecheng <= endkecheng :
    tt = requests.get(http + host + studyurl + str(kecheng),headers = headers)
    print('课程ID'+str(kecheng)+'已读')
    kecheng += 1
    time.sleep(4)

print('结束')
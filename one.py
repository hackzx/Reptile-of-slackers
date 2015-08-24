import os
import sys
import ConfigParser
import requests
import json

reload(sys)
sys.setdefaultencoding('utf8')

#首先我们来定义个创建session函数
def create_session():
	global session
	global cookies
	cf = ConfigParser.ConfigParser()
	cf.read("config.ini")
	cookies = cf._sections['cookies']

	email = cf.get("info","email") #获取email通过get(option,item)
	password = cf.get("info","password")
	cookies = dict(cookies)	#根据()里面的内容生成一个｛｝类似列表的东东

	s = requests.session() 	#初始化一个session对象
	login_data = {"email":email, "password": password}	#定义登录的数据
	header = {
		'User-Agent': "Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
		'Host': "www.zhihu.com",
		'Referer': "http://www.zhihu.com/"
		'X-Requested-With': "XMLHttpRequest"
	}	#设置请求的头部字段

	r = s.post('http://www.zhihu.com/login', data=login_data, headers=header) #配置数据，对指定url进行访问
	if r.json()["r"] == 1:
		print "Login Failed, reason is:"
		for m in r.json()["data"]:
			print r.json()["data"][m]
		print "Use cookies"
		has_cookies = False
		for key in cookies:
			if key != '__name__' and cookies[key] != '':
				has_cookies = True
				break
		if has_cookies == False:
			raise ValueError("请填写config.ini文件中的cookies项.")
	session = s

	#感觉好像不对 这样不太好 先停住。。。。



	
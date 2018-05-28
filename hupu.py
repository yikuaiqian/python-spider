import requests
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client.hupu_database
collection = db.hupu


link = "https://bbs.hupu.com/bxj"
headers = {"Host":"bbs.hupu.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0"}

re = requests.get(link,headers = headers)

soup = bs(re.text,"lxml")   
list = soup.find_all("li")
for i in list:
	if(i.find(attrs=({"class":"truetit"}))):
		print("标题："+i.find(attrs=({"class":"truetit"})).text)
		
		list = i.find(attrs=({"class":"author box"}))
		list1 = list.find_all("a")
		a = i.find(attrs=({"class":"ansour box"})).text.split("/")
		
		
		print("作者："+list1[0].text)
		print("时间："+list1[1].text)
		print("回复数："+a[0])
		print("浏览数："+a[1])
		print("最后回复时间："+i.find(attrs=({"class":"endreply box"})).a.text)
		print("最后回复作者："+i.find(attrs=({"class":"endreply box"})).span.text)
		print("##########################################################")
		title = i.find(attrs=({"class":"truetit"})).text
		author = list1[0].text
		time = list1[1].text
		liulan = a[1]
		huifu = a[0]
		huifutime = i.find(attrs=({"class":"endreply box"})).a.text
		huifuauthor = i.find(attrs=({"class":"endreply box"})).span.text
		
		post = {"title" : i.find(attrs=({"class":"truetit"})).text,
				"author" : list1[0].text,
				"time" : list1[1].text,
				"liulan" : a[1],
				"huifu" : a[0],
				"huifutime" : i.find(attrs=({"class":"endreply box"})).a.text,
				"huifuauthor" : i.find(attrs=({"class":"endreply box"})).span.text }
		collection.insert_one(post)
		
		
		
import requests
import datetime
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

link = "http://www.santostang.com/"
headers = {"Host":"www.santostang.com",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0" }

re = requests.get(link ,headers = headers)
# print(re.content)
soup = bs(re.text,"lxml")
# print(soup.prettify())

list = soup.find_all(attrs={"class":"post-title"})
client = MongoClient("localhost",27017)
db = client.blog_database
collection = db.blog
for i in list:
	link = i.a["href"]
	neirong = i.text
	post = {"url":link,
			"data":neirong,
			"date":datetime.datetime.utcnow()}
	collection.insert_one(post)
	
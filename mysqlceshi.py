import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='scraping',charset = 'utf8')
cur = conn.cursor()
cur.execute("insert into urls (url,content) values('www.baidu.com','这是百度！')")

cur.close()
conn.commit()
conn.close()




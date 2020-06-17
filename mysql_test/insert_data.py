#_*_ coding:utf-8 _*_ 
import pymysql
db=pymysql.connect('localhost','root','19880611zh','mysql')
cursor=db.cursor()
sql='insert into test_course (id,name,test_name,score) VALUES ("201907100002","张三","语文","99")'
try:
    cursor.execute(sql)
    db.commit()
    print('插入成功')
except:
    db.rollback()
cursor.close()
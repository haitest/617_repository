#_*_ coding:utf-8 _*_ 
import pymysql
db=pymysql.connect('localhost','root','19880611zh','mysql')
cursor=db.cursor()
sql_one='select name from user_info WHERE age=30'
cursor.execute(sql_one)
result1=cursor.fetchone()
print(result1)
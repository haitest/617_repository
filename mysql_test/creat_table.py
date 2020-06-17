#_*_ coding:utf-8 _*_ 
import pymysql
db=pymysql.connect('localhost','root','19880611zh','mysql')#连接数据库
cursor=db.cursor()#创建游标
cursor.execute('select version()')#执行查询语句
data=cursor.fetchone()#获取一条查询结果
print(data)
sql='''create table test_course (
id int,
name char(20),
test_name char(10),
score float)'''
cursor.execute(sql)
cursor.close()#关闭连接
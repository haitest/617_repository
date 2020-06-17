#_*_ coding:utf-8 _*_ 
import pymysql
import readConfig
localConfig=readConfig.ReadConfig()
host=localConfig.get_db('host')
username=localConfig.get_db('username')
password=localConfig.get_db('password')
database=localConfig.get_db('database')
port=localConfig.get_db('port')
config={'host':str(host),'user':username,'password':password,'port':int(port),'database':database}
db=pymysql.connect(**config)
cur=db.cursor()
print('----------------++++++++++++++++-------------')
sql_select='select * from test_score where user_name="张海"'
sql_update='UPDATE test_score ts SET ts.chinese=10 WHERE ts.user_name="张海"'
try:
    cur.execute(sql_update)
    db.commit()
except:
    db.rollback()
cur.execute(sql_select)
results=cur.fetchall()
for i in results:
    print(i)


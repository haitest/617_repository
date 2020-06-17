#_*_ coding:utf-8 _*_ 
from configparser import ConfigParser
import requests
cf=ConfigParser()#实例化
cf.read('config.ini')#直接读取文件
#获取节点
secs=cf.sections()
print(secs)
#获取节点内的选项
opts=cf.options('DATABASE')
print(opts)
#获取选项的键值对
kvs=cf.items('DATABASE')
print(kvs)
#得到选项的值
host=cf.get('DATABASE','host')
print(host)
print(requests.__version__)



#_*_ coding:utf-8 _*_ 
import os
import codecs
import configparser

# proDir=os.path.split(os.path.realpath(__file__))[0]#获取文件的绝对路径
proDir=os.getcwd()
# print(proDir)
# print(os.path.realpath(__file__))
# print(os.getcwd())
configPath=os.path.join(proDir,'config.ini')
# print(configPath)
class ReadConfig:
    def __init__(self):
        fd=open(configPath)
        data=fd.read()
        fd.close()
        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)
    def get_email(self,name):
        value=self.cf.get('EMAIL',name)
        return value
    def get_http(self,name):
        value=self.cf.get('HTTP',name)
        return value
    def get_db(self,name):
        value=self.cf.get('DATABASE',name)
        # print(value)
        return value



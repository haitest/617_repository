#_*_ coding:utf-8 _*_ 
# import datetime
# time1=datetime.date(2019,1,29)
# time2=datetime.date(2019,7,12)
# days=(time2-time1).days
# seconds=(time2-time1).total_seconds()
# time3=time1+datetime.timedelta(30)
# print(time3)
'''
假设你有无限数量的邮票,面值分别为6角，7角，8角,请问你最大的不可支付邮资是多少元？
'''
a=6
b=7
c=8
t=50
s=[]
for i in range(t+1):
    s1=a*i
    s.append(s1)
    for j in range(t+1):
        s2=a*i+b*j
        s.append(s2)
        for k in range(t+1):
            s3=a*i+b*j+c*k
            s.append(s3)
print(len(s))
s.sort()
news=[]
for i in s:
    if i not in news:
        news.append(i)
print('组合生成的最大数%s'%news[-1])

r=[]
for i in range(6*t):
    if i in news:
        pass
    else:
        r.append(i)
print('组合不能生成的数字是%s'%r)
print(('不能生成的最大数字是%s'%r[-1]))

'''
冒泡排序
'''
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li
li=[1,2,3,14,25,2,0,1,7]
print(bubbleSort(li))



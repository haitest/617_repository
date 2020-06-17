#_*_ coding:utf-8 _*_ 
# flag = False            # 用于控制外层循环的标志
# for i in range(10):
#     if flag:            # 当flag被内层循环设置为True的时候，跳出外层循环
#         break
#     for j in range(10):
#         if j==7:
#             flag = True
#             break
#         print(i,j)
'''推导式
列表推导式
字典推导式
集合推导式
元组推导式
'''
result=[lambda x:x+i for i in range(10)]
print(result[0](10))
result2=[lambda x,i=i:x+i for i in range(10)]
print(result2[0](10))

'''
递归函数
'''
#
# def sum(n):
#     total=0
#     for i in range(n+1):
#         total += i
#     return total
# print(sum(100))
#
# def sum2(n):
#     if n==0:
#         return 0
#     return sum2(n-1)+n
# print(sum2(0))
'''乘法表'''
def nn(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j<=i:
              print("%sx%s=%s " %(i,j,i*j),end=' ')
        print('')

'''冒泡算法'''
def mp(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
nn(10)
list=[1,24,2,66,23,42]
print(mp(list))

def nn2(n):
    for i in range(1,n+1):
        j=1
        while j<=i:
            print('{0}*{1}={2:>2}'.format(j,i,j*i),end='\t')
            j+=1
        print()
nn2(9)

'''闰年'''
import calendar
def runnian(n):
    if n.isdigit()==False:
        print('请输入数字！！！')
    else:
        if calendar.isleap(int(n))==True:
            print('%s年是闰年'%n)
        else:
            print('%s年不是闰年'%n)

# n=input('请输入一个数字：')
# runnian(n)
#_*_ coding:utf-8 _*_
import os
# f=open('test_file.txt','a')
# f.write("This is a test file.\nI'm leaning python\n")
# f.close()
#
# lis=[1,2,3,4]
# for i in lis:
#     # print(i)
#     print('下标为{0}的数是:{1}'.format(i-1,i))
#     print('下标为{0}的数是:{1:.2f}'.format(i-1,i))
#     print('{:25}'.format(i))
#     # print('{:*25}'.format(i))
#     print('{:^10}'.format(i))
#     print('{:*^25}'.format(i))

# a=os.path.split(os.path.realpath(__file__))
# print(os.path.realpath(__file__))
# print(a)
import sys
import time


def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        bar(i, 100)
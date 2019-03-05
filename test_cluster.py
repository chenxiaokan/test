# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:48:58 2018

@author: user
"""


 a = 1540
 print('a =%x'%(a))

 import math 
 print('pi =%f'%(math.pi))

 a = '{}+{}={}'
 print(a)
 print(a.format('7','9','7+9'))	

 c = '{1}+{2}={0}'
 print(c)
 print(c.format(3+4,3,4))



 print('姓名：%r'%('账单之门'))
 #print(repr(姓名：账单之门))	

 a = '{}'
 print(a.format('姓名：账单之门'))

 s1='账单之门'
 s2=99
 s3='male'
 print('姓名：%s 年龄：%d 性别：%r'%(s1,s2,s3))

 s1=5.30
 s2=2.40
 print('%-.2f +%-.2f =%-.2f'%(s1,s2,s1+s2))


 b = '{}+{}={}'
 print(b)
 print(b.format(5.10,2.30,7.40))


 for i in range(1,9):
     for j in range(1,9):
         print(i,'*',j,'=',i*j)
         print('/n')
        

 #==============================================================================
 # 99乘法表
 #==============================================================================
 a = eval(input("please input a number："))
 for i in range(1,a):
     for j in range(1,i+1):
         print(i,'*',j,'=',i*j,end="  ")
     print()



short = {'NTU':'台湾大学','TW':'台湾','112':'资工系','train':'训练班'}
print('%(NTU)s'%short)

string = 'apple is a kind of fruit'
print(string.split())



############ data analysis ######

def pySum():
    a = [0,1,2,3,4]
    b = [5,6,7,8,9]
    c = []
    
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
    
    return c

pySum()

########### save CSV file##########
## np.savetxt ##
## np.loadtxt ##
## np.tofile ##
import numpy as np

a = np.arange(15).reshape(3,5)
a

np.average(a)
np.std(a)

############# 图像处理
## PIL库是一个具有强大的图像处理的第三方库 ##
# 图像是有像素组成的一个二维矩阵，每个元素都是RGB值

from PIL import Image
import numpy as np

a = Image.open("C:/Users/user/Desktop/1.jpg")
a.mode

im = np.array(Image.open("C:/Users/user/Desktop/1.jpg"))
print(a.shape,a.dtype)

b = [2,2,2,2,2]+a

im_new = Image.fromarray(b.astype('int32'))
im_new = im_new.convert('RGB')
im_new.save('C:/Users/user/Desktop/2.jpg')


















--- 
title:  python-将文件夹下的图片名保存到txt中 
tags: []
categories: [] 

---
import os

dir1 = ' '  # 存放图片的路径

txt1 = ‘ ’ #保存的txt路径

f1 = open(txt1, 'a')  # 打开文件流 ， a 追加数据

for filename in os.listdir(dir1):

     # f1.write(filename.rstrip(.jpg))  #去除后缀

     f1.write(filename)

     f1.write('\n')  #换行

f1.close()  # 关闭文件流

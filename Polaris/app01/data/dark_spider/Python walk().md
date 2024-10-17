
--- 
title:  Python walk() 
tags: []
categories: [] 

---
 os.walk() 函数声明：walk(top,topdown=True,οnerrοr=None) 1&gt;参数top表示需要遍历的目录树的路径 2&gt;参数topdown的默认值是"True",表示首先返回目录树下的文件，然后在遍历目录树的子目录.Topdown的值为"False"时，则表示先遍历目录树的子目录，返回子目录下的文件，最后返回根目录下的文件 3&gt;参数onerror的默认值是"None",表示忽略文件遍历时产生的错误.如果不为空，则提供一个自定义函数提示错误信息后继续遍历或抛出异常中止遍历 4&gt;该函数返回一个元组，该元组有3个元素，这3个元素分别表示每次遍历的路径名，目录列表和文件列表 os,walk()实例:   

```
import os
def VisitDir(path):
  for root,dirs,files in os.walk(path):
    for filespath in files:
      print os.path.join(root,filespath)
if __name__=="__main__":
path="/root"
VisitDir(path)
  
os.path.walk()
```

```
import os,os.path
def VisitDir(arg,dirname,names):
  for filespath in name:
    print os.path.join(dirname,filespath)
if __name__=="__main__":
path="/root"
os.path.walk(path,VisitDir,())
```

```
# -*- coding: utf-8 -*-
import os
for root, dirs, files in os.walk('/media/cdrom0'):
open('mycd.cdc', 'a').write("%s %s %s" % (root,dirs,files))
```



 2. 引入了 os 模块；

 3. 使用os.walk() 扫描光盘，并返回三个对象；

 4. 使用open()打开mycd.cdc 文件对象，并声明成追加模式，逐行记录以上三个对象。

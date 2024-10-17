
--- 
title:  用python创建文件夹 
tags: []
categories: [] 

---
在python中没有直接针对文件夹的操作方法，可以借助模块os,os.path和shutil来操作。在新建文件夹时可以创建一级文件，也可以创建多级文件。

## 判断文件夹或者文件是否存在
- 判断文件或者文件夹是否存在，可以使用os.path.exists()函数来判断，其使用方法如下
```
os.path.exists(path) # path是文件夹或者文件的相对路径或者绝对路径

```

示例：

```
import os
path=r'C:\Users\xf\Desktop\测试文件夹'
print(os.path.exists(path))
# 结果 True

```

## 用os模块创建一级文件夹

创建一级文件是指，被创建文件夹的上级文件夹都存在。只创建最后一层文件夹，如果中间某一层文件夹不存在，将报错，可以先使用`os.path.exists()`判断。
- 例如桌面上有一个测试文件夹，要在其中创建一个名为测试文件夹2的文件夹，指令如下：
```
os.mkdir(r'C:\Users\xf\Desktop\测试文件夹\测试文件夹2')

```
- 如果直接在测试文件夹中新建一个‘测试文件夹2’，在‘测试文件夹2’中新建一个‘测试文件夹3’.测试文件夹2是不存在的，此时就会报错
```
os.mkdir(r'C:\Users\xf\Desktop\测试文件夹\测试文件夹2\测试文件夹3')
# FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'C:\\Users\\xf\\Desktop\\测试文件夹\\测试文件夹2\\测试文件夹3'

```

## 用os创建多级文件夹
- 针对上述中间文件夹不存在的情况，需要使用`os.makedirs(path)`指令，即使中间文件夹不存在，也不会报错，而是相应的创建。
```
os.makedirs(r'C:\Users\xf\Desktop\测试文件夹\测试文件夹2\测试文件夹3')

```

大家可以动手实践一下。

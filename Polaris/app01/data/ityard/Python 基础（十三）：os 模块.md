
--- 
title:  Python 基础（十三）：os 模块 
tags: []
categories: [] 

---


#### 目录
- - 


## 1 简介

<img src="https://img-blog.csdnimg.cn/20191226204139760.jpg#pic_center" alt=""> 我们都知道 os 中文就是操作系统的意思，顾名思义，Python 的 os 模块提供了各种操作系统的接口，这些接口主要是用来操作文件和目录。

Python 中所有依赖于操作系统的内置模块统一设计方式为：对于不同操作系统可用的相同功能使用相同的接口，这样大大增加了代码的可移植性；当然，通过 os 模块操作某一系统的扩展功能也是可以的，但这样做会损害代码的可移植性。

## 2 常用函数

**os.getcwd()** 查看当前路径。

```
import os
print(os.getcwd())

```

**os.listdir(path)** 返回指定目录下包含的文件和目录名列表。

```
import os
print(os.listdir('E:/'))

```

**os.path.abspath(path)** 返回路径 path 的绝对路径。

```
import os
# 当前路径（相对路径方式）
print(os.path.abspath('.'))

```

**os.path.split(path)** 将路径 path 拆分为目录和文件两部分，返回结果为元组类型。

```
import os
print(os.path.split('E:/tmp.txt'))

```

**os.path.join(path, *paths)** 将一个或多个 path（文件或目录） 进行拼接。

```
import os
print(os.path.join('E:/', 'tmp.txt'))

```

**os.path.getctime(path)** 返回 path（文件或目录） 在系统中的创建时间。

```
import os
import datetime
print(datetime.datetime.utcfromtimestamp(os.path.getctime('E:/tmp.txt')))

```

**os.path.getmtime(path)** 返回 path（文件或目录）的最后修改时间。

```
import os
import datetime
print(datetime.datetime.utcfromtimestamp(os.path.getmtime('E:/tmp.txt')))

```

**os.path.getatime(path)** 返回 path（文件或目录）的最后访问时间。

```
import os
import datetime
print(datetime.datetime.utcfromtimestamp(os.path.getatime('E:/tmp.txt')))

```

**os.path.exists(path)** 判断 path（文件或目录）是否存在，存在返回 True，否则返回 False。

```
import os
print(os.path.exists('E:/tmp.txt'))

```

**os.path.isdir(path)** 判断 path 是否为目录。

```
import os
print(os.path.isdir('E:/'))

```

**os.path.isfile(path)** 判断 path 是否为文件。

```
import os
print(os.path.isfile('E:/tmp.txt'))

```

**os.path.getsize(path)** 返回 path 的大小，以字节为单位，若 path 是目录则返回 0。

```
import os
print(os.path.getsize('E:/tmp.txt'))
print(os.path.getsize('E:/work'))

```

**os.mkdir()** 创建一个目录。

```
import os
os.mkdir('E:/test')

```

**os.makedirs()** 创建多级目录。

```
import os
os.makedirs('E:/test1/test2')

```

目录 test1、test2 均不存在，此时使用 os.mkdir() 创建会报错，也就是说 os.mkdir() 创建目录时要保证末级目录之前的目录是存在的。

**os.chdir(path)** 将当前工作目录更改为 path。

```
import os
print(os.getcwd())
os.chdir('/test')
print(os.getcwd())

```

**os.system(command)** 调用 shell 脚本。

```
import os
print(os.system('ping www.baidu.com'))

```

如果出现乱码，可以通过修改编码解决，比如：我在 Windows 下 PyCharm 中出现乱码问题，可以将 PyCharm 中编码修改为 GBK 解决。

参考： 

<img src="https://img-blog.csdnimg.cn/20191212073821865.png#pic_center" alt="" width="600">

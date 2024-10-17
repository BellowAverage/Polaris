
--- 
title:  Numpy数据分析csv文件的应用 
tags: []
categories: [] 

---
## 1.数据存取与函数

### 1.1.数据的CSV文件存取

CSV(Comma-Separated Value,逗号分隔值) CSV是一种常见的文件格式，用来存储批量数据

```
 np.savetxt(frame, array, fmt=‘%.18e’, delimiter=None)
复制代码
```

frame : 文件、字符串或产生器，可以是.gz或.bz2的压缩文件

array : 存入文件的数组

fmt : 写入文件的格式，例如：%d %.2f %.18e

delimiter : 分割字符串，默认是任何空格

```
a=np.arange(100).reshape(20,5)
np.savetxt('C:/Users/12079/Desktop/python/CSV/a.csv',a,fmt='%d',delimiter=',')
复制代码
```

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9203bdf82602fb5b0921d5081172a2fb.png">

```
np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)
复制代码
```

frame:文件、字符串或产生器，可以是.gz或.bz2的压缩文件

dtype:数据类型，可选

delimiter:分割字符串，默认是任何空格

unpack:如果True，读入属性将分别写入不同变量



```
b=np.loadtxt('C:/Users/12079/D
```

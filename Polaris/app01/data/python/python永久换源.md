
--- 
title:  python永久换源 
tags: []
categories: [] 

---
Windows下python永久换源方式有两种： ①找到系统的pip.ini文件手动替换文件内容； ②直接命令行（终端）一键换源。

1.手动 系统搜索找打pip.ini的位置（我的电脑是在 C:\Users\lhsmd(用户名)\AppData\Roaming\pip\pip.ini 其他电脑也是在类似的位置），然后用记事本打开，将下面的内容替换掉文件中原有的内容：

```
[global] 
timeout = 6000 
index-url = https://mirrors.aliyun.com/pypi/simple 
trusted-host = pypi.douban.com

```

其中https://mirrors.aliyun.com/pypi/simple为新源地址，常用的国内可用源：

```
# 腾讯
http://mirrors.tencentyun.com/pypi/simple
# 阿里
https://mirrors.aliyun.com/pypi/simple
# 豆瓣
https://pypi.douban.com/simple
# 中科大
https://pypi.mirrors.ustc.edu.cn/simple/
# 清华
https://pypi.tuna.tsinghua.edu.cn/simple

```

2.终端命令替换

```
 pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

```

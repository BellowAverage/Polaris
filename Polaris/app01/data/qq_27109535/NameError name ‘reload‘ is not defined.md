
--- 
title:  NameError: name ‘reload‘ is not defined 
tags: []
categories: [] 

---
问题：NameError: name ‘reload’ is not defined

自己代码：

```
# 处理编码问题
reload(sys)
sys.setdefaultencoding("utf-8")

```

<img src="https://img-blog.csdnimg.cn/5a316b58f4e24397a16ac09ac8ca87bf.png" alt="在这里插入图片描述"> 解决方法如下：

```
#对于 &gt;= Python 3.4：
import importlib
importlib.reload(sys)

```

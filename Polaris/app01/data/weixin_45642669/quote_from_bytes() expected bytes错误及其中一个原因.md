
--- 
title:  quote_from_bytes() expected bytes错误及其中一个原因 
tags: []
categories: [] 

---
使用pymysql的时候，出现了quote_from_bytes()。

后来发现：我自己导入数据的时候使用了yaml，而密码是123456.所以导入的数据的时候无法导入。

这个代码的作用就是把字符串转为字节流失败了，然后函数后面就是失败的原因。

quote_from_bytes需要把字符串转化为字节，只能接受字符串变量。而我给了他一个数字，他解析失败返回expected bytes。

解决方式：指定格式为字符串。

```
# key : 123456
key : "123456"

```

问题就解决了。

反思：对于配置文件需要确定类型。passwd、filename等必须是String类型，不然转化为字节流会出现这个问题。

问题很简单，记录一下

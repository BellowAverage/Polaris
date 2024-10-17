
--- 
title:  yagmail 导入html 前面有空行 
tags: []
categories: [] 

---
#### 问题：

yagmail导入html格式数据以后，有大量空行。 数据越多，空行越多。 <img src="https://img-blog.csdnimg.cn/50206fd07cfc4f2c924fcfc5102f3e10.png" alt="在这里插入图片描述">

#### 解决

通过翻阅邮件源码发现： 数据出现了两次，第一次是text/plain格式，第二次是text/html格式 第一次text格式导致的邮件多出大量的字符。 <img src="https://img-blog.csdnimg.cn/89fda55fefb040788027578dd515566b.png" alt="在这里插入图片描述">

解决方案：使用正则将所有换行符替换为空白字符即可。

```
# html是发送的html格式数据
html = html.repace("\n", "")

```

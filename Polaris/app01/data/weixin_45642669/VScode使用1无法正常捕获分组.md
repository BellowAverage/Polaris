
--- 
title:  VScode使用\1无法正常捕获分组 
tags: []
categories: [] 

---
## 问题描述

vscode里面无法通过\1获取正常的捕获组。

## 问题解决

VS里面使用捕获组的方式是$1而不是\1 可能是协议不统一。



不知道为啥，反正官网上说$才是正经的捕获组

<img src="https://img-blog.csdnimg.cn/direct/42d1de674be94ea7930267d1b9cda5a5.png" alt="在这里插入图片描述"> 测试：

对字符d进行（d）捕获，然后用$1$1进行替换，替换成功 <img src="https://img-blog.csdnimg.cn/direct/8ec7492b821c4352bfb270fb19551c10.png" alt="在这里插入图片描述">

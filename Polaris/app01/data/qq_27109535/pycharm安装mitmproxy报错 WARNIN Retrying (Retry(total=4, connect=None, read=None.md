
--- 
title:  pycharm安装mitmproxy报错 WARNIN: Retrying (Retry(total=4, connect=None, read=None 
tags: []
categories: [] 

---
### 1. 问题：pycharm安装mitmproxy报错

WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘ProxyError(‘Cannot connect to proxy.’, timeout(’_ssl.c:1114: The handshake operation timed out’))': /simple/mitmproxy/

### 2. 分析错误：代理服务器开启状态中需要关闭：

<img src="https://img-blog.csdnimg.cn/cc5a326396484ea69b56a045f1b020ee.png" alt="在这里插入图片描述">

### 3. 再次安装运行结果：

<img src="https://img-blog.csdnimg.cn/c8ed33512ba342ea846568c95eb69c87.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/332b840dcca645f7beec739c505666f5.png" alt="在这里插入图片描述">

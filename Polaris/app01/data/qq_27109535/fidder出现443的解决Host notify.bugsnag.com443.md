
--- 
title:  fidder出现443的解决Host: notify.bugsnag.com:443 
tags: []
categories: [] 

---
fiddler抓取HTTPS数据失败，全部显示tunnel to…443， Host: notify.bugsnag.com:443

<img src="https://img-blog.csdnimg.cn/481971d07b794be2ac5b05235b461500.png" alt="在这里插入图片描述">

### 1. 运行certmgr.msc

```
certmgr.msc

```

<img src="https://img-blog.csdnimg.cn/2de265ef436d44c6bc3d5c956242a664.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/56fa5bf3a40241b0be7e7aadbec72a7d.png" alt="在这里插入图片描述"> 证书删除 <img src="https://img-blog.csdnimg.cn/4e74f15ec2df4c408b7cd618c78f922e.png" alt="在这里插入图片描述">

### 2. 双击FiddlerCertMarker.exe重新打开一个证书

下载一个叫“FiddlerCertMarker.exe”的工具，双击运行即可重新打开一个证书。

<img src="https://img-blog.csdnimg.cn/9276d699854c443d9ff963d6993ba49c.png" alt="在这里插入图片描述">
1. 重新打开fiddler，使用chrome或IE输入“https://www.baidu.com/”，这回可以捕获https的消息并解密成功了。1. 使用原生浏览器访问“https://www.baidu.com/”，fiddler成功抓取到https的数据。1. <img src="https://img-blog.csdnimg.cn/0da7bbb06d8d4390b98dc2b0d5a25bf6.png" alt="使用原生浏览器访问“https://www.baidu.com/”，fiddler成功抓取到https的数据。">
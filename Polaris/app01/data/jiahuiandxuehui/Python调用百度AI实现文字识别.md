
--- 
title:  Python调用百度AI实现文字识别 
tags: []
categories: [] 

---


#### 目录标题

  - 
  - 
  - 
 


## 前沿

今天我们也来高大上一下，玩一把人工智能。那就是免费调用百度AI实现图片上面的文字识别。相对于Python的第三方库，百度人工智能要更强大，毕竟人工智能不是那么容易搞的。要调用，其实很简单，关键的代码只需要三行。但需要先注册百度AI，获得ID和密钥。注册也很简单，百度AI社区有详细说明，高铁直达链接：https://ai.baidu.com/forum/topic/show/867951 。只需走到“1.6 获取密钥”即可。然后记录下自己的APP_ID、API_KEY、SECRET_KEY，就可以开始了。界面如下。每个ID每天可免费识别200次，请珍惜使用哈。

<img src="https://img-blog.csdnimg.cn/3bb2dd1d1ae041c39c543f04fd55371e.png" alt="在这里插入图片描述">

## 实战演示

忘了，还有一步，那就是要安装百度AI库。电脑运行cmd, 输入 “pip install baidu-aip”，然后喝杯茶静待安装完成。随后就可以开始调用啦。

```
from aip import AipOc
```

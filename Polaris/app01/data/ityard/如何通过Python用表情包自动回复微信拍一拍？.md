
--- 
title:  如何通过Python用表情包自动回复微信拍一拍？ 
tags: []
categories: [] 

---
>  
  作者：5pyx5oOf5oG6 
  https://zhuanlan.zhihu.com/p/149912352 
 

前不久微信上线了拍一拍功能，刚推出就被有才的网友玩坏了。

还有更多没有节操的拍法这里就不展示了。

但拍一拍属于弱提示，只有在聊天界面才能感受到。如果不在微信界面，被人拍了没办法及时回应，这里给大家介绍一下如何使用`PyWeChatSpy(https://github.com/veikai/PyWeChatSpy)`来用表情包回应拍一拍。

1、首先我们准备一些表情图，这里我选了沙雕熊猫头

2、安装`2.8.0.133`版本的PC微信客户端`(https://share.weiyun.com/5AwuXRG)`

3、安装`Python3.8.3_x64 32`位系统`(https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe)`的同学可以去官网自行下载32位安装包

4、打开cmd输入`pip install PyWeChatSpy`回车执行

5、这时候需要我们编码了，先新建一个`app.py`文件

先引入PyWeChatSpy模块、正则re模块和随机random模块 re用于匹配消息内容，random用于随机选取回复图片

```
from PyWeChatSpy import WeChatSpy
import random
import re

```

接着定义一个回复处理函数my_parser

```
def my_parser(data):
    pass

```

然后实例化一个WeChatSpy类

```
spy = WeChatSpy(parser=my_parser)

```

最后编写my_parser函数处理逻辑

```
if data["type"] == 5: # 判断是微信消息数据
    for msg in data["data"]: # 遍历微信消息
        if msg["msg_type"] == 10000:  # 判断是微信拍一拍系统提示
            # 因为微信系统消息很多 因此需要用正则匹配消息内容进一步过滤拍一拍提示
            # {'self': 0, 'msg_type': 10000, 'wxid1': '179xxxxxx72@chatroom', 'content': '"Mandy的小脑袋" 拍了拍你'}
            m = re.search('".*" 拍了拍你', msg["content"])
            if m:  # 搜索到了匹配的字符串 判断为拍一拍
                image_path = f"images/{random.randint(1, 7)}.jpg"  # 随机选一张回复用的图片
                spy.send_file(msg["wxid1"], image_path)  # 发送图片

```

运行代码

```
if __name__ == '__main__':
    spy.run()  # 运行代码

```

大功告成，这时候如果再有人拍你，无论是群聊还是私聊都会自动回复设置好的图片。

整体代码如下：

```
from PyWeChatSpy import WeChatSpy
import random
import re


def my_parser(data):
    if data["type"] == 5: # 判断是微信消息数据
        for msg in data["data"]:  # 遍历微信消息
            if msg["msg_type"] == 10000:  # 判断是微信拍一拍系统提示
                # 因为微信系统消息很多 因此需要用正则匹配消息内容进一步过滤拍一拍提示
                # {'self': 0, 'msg_type': 10000, 'wxid1': '179xxxxxx72@chatroom', 'content': '"Mandy的小脑袋" 拍了拍你'}
                m = re.search('".*" 拍了拍你', msg["content"])
                if m:  # 搜索到了匹配的字符串 判断为拍一拍
                    image_path = f"images/{random.randint(1, 7)}.jpg"  # 随机选一张回复用的图片
                    spy.send_file(msg["wxid1"], image_path)  # 发送图片


spy = WeChatSpy(parser=my_parser)  # 实例化WeChatSpy类


if __name__ == '__main__':
    spy.run()  # 运行代码

```

`app.py`存放的地方要和图片文件夹一致，否则无法正确回复，如图片路径`D:\images,app.py`存放路径为`D:\app.py`，暂不支持中文路径。

```
推荐书籍《趣学Python算法100例》本书专为Python算法初学者量身打造，详解100个趣味编程算法实例，内容涵盖Python编程的基础知识和常用算法。

```

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

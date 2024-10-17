
--- 
title:  在PyCharm中直接启动mitmproxy并自动打开&关闭系统代理 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/6c5ea9cc21114f5a80e9c4e463b67252.jpeg#pic_center#pic_center" alt="在这里插入图片描述">

## 前言

在前面的文章中，有几篇是介绍`mitmproxy` 的。 这个`mitmproxy` 的确是个捕获数据的好工具，但在运行时候需要在命令行启动，这是很令人苦恼的。

之前也尝试过脱离命令行去启动`mitmproxy`， 但它是借助Python 中的 `os` 和 `subprocess`模块去执行Windows系统的cmd命令； 总觉得这不是个好方法，遂有此文。

在这篇文章中，我将介绍如何在PyCharm中直接启动`mitmproxy`，让你可以更加方便地使用这个强大的工具。

## 知识点

|模块|作用
|------
||免费和开源的交互式HTTPS代理
||程序在退出时的处理器
|**winproxy**|通过Python模块函数和命令行编程来实现修改系统代理

如何在`PyCharm`中直接启动`mitmproxy`：
- 通过将命令行参数以逗号分隔，依次填写到`mitmdump([])` 里面，可以在PyCharm中直接启动mitmproxy。
如何自动启动和关闭系统代理：
- 通过使用`winproxy`库的`ProxySetting`类，可以方便地在`Windows`系统中启动和关闭系统代理。
如何使用`atexit`模块注册程序退出时的处理函数：
- 通过`atexit.register()`函数，可以在程序退出时自动执行特定的清理操作，如关闭系统代理。
如何编写`mitmproxy`的数据捕获脚本：
- 文章中提供了一个具体的脚本示例，展示了如何捕获和处理特定URL的HTTP响应。
## 实现

### 常规情况

现在项目只有一个`script.py`文件，它的内容为`mitmproxy`数据捕获的脚本。 代码来自于这篇文章，

**script.py**

```
from mitmproxy import http


# 定义一个函数，用于处理每一个响应
def response(flow: http.HTTPFlow) -&gt; None:
    # 判断响应的URL是否是公众号留言的URL
    if "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&amp;scene=0" in flow.request.url:
        # 获取响应的数据包
        response = flow.response
        # 打印出响应的状态码和内容
        print(f"Status: {<!-- -->response.status_code}")
        print(f"Content: {<!-- -->response.content}")
        print(parse(data=response.text))


def parse(data: str):
    """解析留言流量包"""
    _data = defaultdict(list)
    try:
        for item in json.loads(data)['elected_comment']:
            _data['nick_name'].append(item['nick_name'])
            _data['content'].append(item['content'])
            _data['like_num'].append(item['like_num'])
            _data['province_name'].append(item['ip_wording']['province_name'])
    except (KeyError, json.decoder.JSONDecodeError):
        ...
    finally:
        return _data


addons = [response]


```

在这份代码中，一般的运行步骤是去命令行，输入
- `-p 9527 -q` 这些参数可选~
```
mitmdump -s demo.py -p 9527 -q

```

这样一来一回，就不够便捷了。

### 在PyCharm运行

在这里，只需要将命令行参数以逗号分隔，依次填写到`mitmdump([])` 里面即可。

就是这么简单！！！

```
from mitmproxy import http
from mitmproxy.tools.main import mitmdump


if __name__ == "__main__":
    # 运行 Mitmproxy，并传递命令行参数
    mitmdump(['-s', __file__, '-p', '9527', '-q'])

```

这里，需要注意一下的是，作为`mitmproxy`脚本，如果写的是类，则需要添加一行代码，

#### 有class

顺序也很重要，必须要在`if __name__ == '__main__':`之前。

```
from mitmproxy.tools.main import mitmdump

class ListenComment:
    def __init__(self):
        ...
        
    def response(self, flow: mitmproxy.http.HTTPFlow):
        ...


addons = [ListenComment()]


if __name__ == '__main__':
    mitmdump(['-s', __file__, '-q'])

```

### 实际案例

这里结合这一篇文章，

完成一个自动启动与关闭系统代理，且在`PyCharm` 执行的 `mitmproxy` 程序，极简到家了！！！

```
# -*- coding: utf-8 -*-
# Name:         mitm.py
# Author:       小菜
# Date:         2023/11/03 11:30
# Description:

import atexit
import json
from collections import defaultdict

import mitmproxy.http
from mitmproxy.tools.main import mitmdump
from winproxy import ProxySetting

ps = ProxySetting()


def set_proxy():
    """设置系统代理"""
    ps.enable = True
    ps.server = '127.0.0.1:9527'
    ps.registry_write()
    print('代理已经打开!')


def close_proxy():
    """关闭系统代理"""
    ps.enable = False
    ps.registry_write()
    print('代理已经关闭!')


class ListenComment:
    def __init__(self):
        self.map = {<!-- -->
            'liveObjectId': str(),
            'jsons': dict()
        }
        self.set = set()

    # 定义一个函数，用于处理每一个响应
    def response(self, flow: mitmproxy.http.HTTPFlow) -&gt; None:
        # 判断响应的URL是否是公众号留言的URL
        if "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&amp;scene=0" in flow.request.url:
            # 获取响应的数据包
            response = flow.response
            # 打印出响应的状态码和内容
            print(f"Status: {<!-- -->response.status_code}")
            print(f"Content: {<!-- -->response.content}")
            print(self.parse(data=response.text))

    def parse(self, data: str):
        """解析留言流量包"""
        _data = defaultdict(list)
        try:
            for item in json.loads(data)['elected_comment']:
                _data['nick_name'].append(item['nick_name'])
                _data['content'].append(item['content'])
                _data['like_num'].append(item['like_num'])
                _data['province_name'].append(item['ip_wording']['province_name'])
        except (KeyError, json.decoder.JSONDecodeError):
            ...
        finally:
            return _data


addons = [ListenComment()]

if __name__ == '__main__':
    # 打开代理
    set_proxy()
    # 注册清理函数
    atexit.register(close_proxy)
    mitmdump(['-s', __file__, '-p 9527', '-q'])


```

**运行效果如下图所示：**

<img src="https://img-blog.csdnimg.cn/28930d3ea5d14edd8b8af2d58618509f.gif" alt="在这里插入图片描述">

## 总结

在本文中，我详细介绍了如何在`PyCharm`中直接启动`mitmproxy`，以及如何自动启动和关闭系统代理，无需再通过命令行。 这种方法不仅避免了频繁在命令行中输入命令的麻烦，而且通过自动管理系统代理，使得整个过程更加便捷和高效。 我还提供了具体的代码示例，以帮助读者朋友们更好地理解和实践。 希望这篇文章能对大家使用`mitmproxy`进行数据捕获的工作带来帮助，提高工作效率。

## 后话

本次分享到此结束， see you~🎉🎉

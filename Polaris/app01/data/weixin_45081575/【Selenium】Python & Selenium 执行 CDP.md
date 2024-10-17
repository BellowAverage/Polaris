
--- 
title:  【Selenium】Python & Selenium 执行 CDP 
tags: []
categories: [] 

---
## 前言

>  
 这篇文章来吧啦一下由Selenium中用到的cdp（`Chrome DevTools Protocol` 的调用 用作于记录学习所得，无实质性意义。 


以下几篇文章有一点点关系，感兴趣的可以逐一审阅🔎🔎

<th align="left">标题</th>|链接
|------
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/112621581
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/126389273
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/126551260
<td align="left"></td>|https://blog.csdn.net/weixin_45081575/article/details/126556995

本篇文章不讲CDP的原理，只讲它在Python 和 Selenium 中的实现。

## 知识点📖

>  
  允许使用工具来检测、检查、调试和分析 Chromium、Chrome 和其他基于 Blink 的浏览器。 


`Chrome DevTools Protocol`，简称**CDP**

看以下  ，感兴趣的可以深入去学习了解。

<img src="https://img-blog.csdnimg.cn/64f16156984d41618cf531005a56a375.png" alt="在这里插入图片描述">

## Selenium的基础

在Selenium中，执行下面的代码，便可以调用 cdp 命令~

```
# selenium调用 cdp
webdriver.execute_cdp_cmd(command, cmd_args)  

```

翻看一下它的源码，
- 该函数是执行 cdp 命令和 获取返回结果- 参考链接：，使用示例 务必要参考这里使用，因为不用方法的传参不一样- 使用示例：`driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': requestId})`，下面再解释它的意思
**\site-packages\selenium\webdriver\chromium\webdriver.py** <img src="https://img-blog.csdnimg.cn/00909a6e9a124e5a9fda594f97725a3c.png" alt="">

## CDP操作

>  
 下面介绍几种执行 CDP的方法 


### Selenium 执行 CDP

这里指定端口号为 `9527`

```
# -*- coding: utf-8 -*-
# @Time   : 2022-08-28 23:17
# @Name   : selenium_cdp_test.py


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")  # 指定端口为9527
driver = webdriver.Chrome(options=options)  # 启动浏览器
# 显示一个弹框，并输出 hello world
result = driver.execute_cdp_cmd('Runtime.evaluate', {<!-- -->'expression': "alert('hello world')"})
print(result)


```

代码运行效果如下，
- 显示一个弹框，并输出 hello world
<img src="https://img-blog.csdnimg.cn/3306a58e765e4dadb370ccfa6632e5b8.gif" alt=""> 可能会有疑问，这行代码是什么意思？

```
driver.execute_cdp_cmd('Runtime.evaluate', {<!-- -->'expression': "alert('hello world')"})

```

这个时候就需要用到上面的参考网站了，
- 左侧是对应的 域名 的一个大类- `Runtime.evaluate` 是 计算全局对象上的 expression- `expression` 是我们传进入的 js 语句（这里只有`expression` 是必选参数，其它的都是可选的~
<img src="https://img-blog.csdnimg.cn/c6ec9e1766074d6ab4140bd2cf97a85f.png" alt=""> 当然，也还有上面的 `Network.getResponseBody`
- `Network.getResponseBody` 是 为给定 requestId 请求返回内容- `requestId` 是网络请求的唯一标识符
<img src="https://img-blog.csdnimg.cn/e6c6f951c1054f5c8015e64bd9c6d194.png" alt="">

更多的用法，可以通过官方文档学习~

### Python使用 `requests`操作 CDP

这个方法是用过Selenium的源码中找到的，以调试模式执行Selenium，打上断点，一步步跟下去，找到了它发网络请求的地方~

**\site-packages\selenium\webdriver\remote\remote_connection.py** <img src="https://img-blog.csdnimg.cn/491cff70ce5544678c463e079dd16e12.png" alt="">

再看调试的控制台的信息 <img src="https://img-blog.csdnimg.cn/d17438e9da2a4d408c5ce2c50f0a2e3c.png" alt="">

结合两图，总结一下
- method：`POST`- url：`http://localhost:55438`（这里的端口号是随机的- path：`/session/$sessionId/goog/cdp/execute`- `sessionId，service_url`，（每启动Selenium都会有该参数，且唯一
所以可以得出以下规律，
- 请求连接：`{service_url}`/session/`{session_id}`/goog/cdp/execute（其中`{xxx}`为要填充的内容（这里的端口号是随机生成的，上一篇文章中有说~- data：就是我们传进去的表达式，是一个字典，cmd 为指定方法，params 为所需要携带的参数
**你执行以下代码时候，需要替换成自己的 `service_url`和 `session_id`**

```
# -*- coding: utf-8 -*-
# @Time   : 2022-08-27 12:41
# @Name   : selenium_cdp_2.py

import time
import json
import requests

# 'http://127.0.0.1:{port}/session/{session_id}/goog/cdp/execute'
url = 'http://127.0.0.1:55623/session/0ce4027784730e1ffb42b334809ed427/goog/cdp/execute'
# 导航当前页面到给定的URL
data_1 = {<!-- -->"cmd": "Page.navigate", "params": {<!-- -->"url": "https://www.baidu.com"}}

data_2 = {<!-- -->
    "cmd": "Runtime.evaluate",
    "params": {<!-- -->"expression": "alert('hello world')"}  # 出来一个弹框
}
resp = requests.post(url, data=json.dumps(data_1))
print(resp)
print(resp.json())

time.sleep(2)
resp = requests.post(url, data=json.dumps(data_2))
print(resp)
print(resp.json())



```

以上代码执行效果如下所示，
- 先访问了 baidu- 然后 弹出一个 弹窗
<img src="https://img-blog.csdnimg.cn/2596e45495b64053b4b6fd1b9bfc04e5.gif" alt="">

但是这个方法有点麻烦，因为需要以调试模式执行，才能知道当前的 **session_id** 和 **service_url** 。下面有个更好的方法~

### Python连接 `WebSocket` 执行 CDP

这个方法就简单的多了，还记得前面的文章吗？

讲到了这个链接：

看图右边的 **webSocketDebuggerUrl** 参数，这是个 `WebSocket` 的链接，所以使用 `WebSocket` 进行连接后，我们也可以执行 CDP。 <img src="https://img-blog.csdnimg.cn/d438685993224628823f4aab6a2eec5a.png" alt="">

这里值得注意是安装 websocket 模块，要按照这以下顺序
1. pip install webscoket1. pip install websocket-client
```
# 这里插入代码片
# -*- coding: utf-8 -*-
# @Time   : 2022-08-27 12:00
# @Name   : py_cdp.py

import json
import requests
import websocket


def websocket_conn():
    # websocket_conn 连接
    resp = requests.get('http://127.0.0.1:9527/json')  # 有不懂的看上一篇文章
    assert resp.status_code == 200
    ws_url = resp.json()[0].get('webSocketDebuggerUrl')
    return websocket.create_connection(ws_url)


def execute_cdp(conn: websocket, command: dict):
    # 执行  dp
    conn.send(json.dumps(command))
    # 接受websocket的响应，并将字符串转换为 dict()
    return json.loads(conn.recv())


def main():
    conn = websocket_conn()
    # js = "alert('hello world')" # 弹窗 hello world
    # js = "console.log('hello world')" # 控制台打印 hello world
    js = "location.href='https://www.bilibili.com'"  # 页面跳转
    command = {<!-- -->
        'method': 'Runtime.evaluate',  # 处理 传进去的 expression
        'id': int(),	# id需要传一个整型，否则会报错
        'params': {<!-- -->'expression': js}
    }
    resp = execute_cdp(conn, command)
    print(resp)


if __name__ == '__main__':
    main()


```

运行效果看下面动图，js代码中指定页面跳转到 B站。

<img src="https://img-blog.csdnimg.cn/8a8c025d8f56479e9037ce62fb12f902.gif" alt="">

## 后话

本次的执行cdp操作就介绍到这里了， 怎么样，是不是感觉没用的知识又增加了~🎃🎃 see you.

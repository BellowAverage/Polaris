
--- 
title:  【Requests】获取本地的请求IP和域名解析的IP 
tags: []
categories: [] 

---
>  
 此博客仅为我业余记录文章所用，发布到此，仅供网友阅读参考，如有侵权，请通知我，我会删掉。 这篇文章没啥用，请略过。 


## 前言

先来假设两个使用 **Python** 的网络请求库 **`Requests`** 场景：
- 使用代理 **ip** 访问某网站，想查看当前的请求的代理 **ip**- 访问的是域名，但想查看 `域名解析` 后的 **ip**
本篇文章就来介绍以上两种获取 `ip` 的方法。

**`Requests`** 的安装和使用参考  <img src="https://img-blog.csdnimg.cn/8cc6d014f05a47a4bba8732e0e01f0d3.png" alt="">

### 前置知识

#### HTTP请求

>  
 引用这张图是想说，后面会用到 **Socket连接**（有了 Socket连接，就可以获取到本地和远程的 `ip` 了。 


**HTTP请求和响应步骤**
- 图片来自 https://zhuanlan.zhihu.com/p/38240894
<img src="https://img-blog.csdnimg.cn/795aec0245a14eeea4813ab8ac2a1723.png" alt="https://zhuanlan.zhihu.com/p/38240894">

#### Socket

看到  的**Socket**函数介绍，后面会用到这两个**Socket** 函数。
- `socket.getpeername()` 返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。- `socket.getsockname()` 返回套接字自己的地址。通常是一个元组(ipaddr,port)
<img src="https://img-blog.csdnimg.cn/dbd5876925a144f38bdb850d3d81e9ce.png" alt="在这里插入图片描述">

#### DNS查询

网站：https://tool.chinaz.com/dns/?type=1&amp;host=blog.csdn.net

这个网站可以查看该域名 **blog.csdn.net** 所有的 `ip`，看到有多个ip，这就是为什么访问同一个网站时却会是不同的 `ip`。

打个比喻：就近原则，哪个服务器距离当前请求近，就由那个服务器来处理请求。（大致如此） <img src="https://img-blog.csdnimg.cn/62997aa0447c464d96a5da1faf3ffd8f.png" alt="在这里插入图片描述">

### 受害网站

下面请出本次的受害者

### 代码

```
import requests
from requests.models import Response

url = 'https://httpbin.org/get'

resp: Response = requests.get(url, stream=True)
localhost_address = resp.raw._connection.sock.getsockname()
remote_address = resp.raw._connection.sock.getpeername()
print("local_address is  ==&gt; ", localhost_address)
print("remote_address is ==&gt; ", remote_address)


```

请求时候需要设定 **`stream=True`**，官方释义如下：

```
:param stream: (optional) if ``False``, the response content will be immediately downloaded.

```

调试模式，下断点 可以看到 `Requests` 响应值的 **raw._connection.sock**，是一个`Socket连接` <img src="https://img-blog.csdnimg.cn/4643062d734e400ea610d39913ef6599.png" alt="在这里插入图片描述">

### 本地的请求IP

**`socket.getsockname()`**：返回连接套接字的本地地址

这里可以打开`CMD`，然后输入 `ipconfig`，可以看到当前的主机 `ip`地址； 这是没有开启代理的~ <img src="https://img-blog.csdnimg.cn/0437adeacd274164821efb4c7b70343c.png" alt="在这里插入图片描述">

这是开启了代理的~ <img src="https://img-blog.csdnimg.cn/0f14469ef6b04525bfd215d57d434294.png" alt="在这里插入图片描述">

### DNS解析的IP

<img src="https://img-blog.csdnimg.cn/1d417d35bee74e98ad4b8a009c6a930f.png" alt="在这里插入图片描述"> 从上图中可以看到，他们访问的网址不一样，但是他们的返回结果是一样的； 左侧访问的是 ，右侧访问的则是该域名解析后的 `ip` ： 至于为什么会这样，这不是本文章要讨论的内容~

**`socket.getpeername()`**：返回连接套接字的远程地址

至于这个`ip`为啥不和上图的一样，因为它有多个`ip`吖！ <img src="https://img-blog.csdnimg.cn/1754650284924b37900952897cf29c6f.png" alt="在这里插入图片描述">

## 后话

本次的分享到此结束， 如有疑问，请自行解决。

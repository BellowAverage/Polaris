
--- 
title:  Python 爬虫（二）：Requests 库 
tags: []
categories: [] 

---


#### 目录
- <ul><li>- - <ul><li><ul><li>- - - - - 


所谓爬虫就是模拟客户端发送网络请求，获取网络响应，并按照一定的规则解析获取的数据并保存的程序。要说 Python 的爬虫必然绕不过 Requests 库。

### 1 简介

对于 Requests 库，官方文档是这么说的：

>  
 Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用。 警告：非专业使用其他 HTTP 库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。 


这个介绍还是比较生动形象的，便不再多说。安装使用终端命令 `pip install requests` 。

### 2 快速上手

##### 2.1 发送请求

导入 Requests 模块：

```
import requests

```

获取网页：

```
r = requests.get('http://xxx.xxx')

```

此时，我们获取了 Response 对象 r，我们可以通过 r 获取所需信息。Requests 简便的 API 意味着所有 HTTP 请求类型都是显而易见的，我们来看一下使用常见 HTTP 请求类型 `get、post、put、delete` 的示例：

```
r = requests.head('http://xxx.xxx/get')
r = requests.post('http://xxx.xxx/post', data = {<!-- -->'key':'value'})
r = requests.put('http://xxx.xxx/put', data = {<!-- -->'key':'value'})
r = requests.delete('http://xxx.xxx/delete')

```

通常我们会设置请求的超时时间，Requests 使用 `timeout` 参数来设置，单位是秒，示例如下：

```
r = requests.head('http://xxx.xxx/get', timeout=1)

```

##### 2.2 参数传递

在使用 get 方式发送请求时，我们会将键值对形式参数放在 URL 中问号的后面，如：`http://xxx.xxx/get?key=val` ，Requests 通过 params 关键字，以一个字符串字典来提供这些参数。比如要传 `key1=val1` 和 `key2=val2` 到 `http://xxx.xxx/get`，示例如下：

```
pms= {<!-- -->'key1': 'val1', 'key2': 'val2'}
r = requests.get("http://xxx.xxx/get", params=pms)

```

Requests 还允许将一个列表作为值传入：

```
pms= {<!-- -->'key1': 'val1', 'key2': ['val2', 'val3']}

```

`注`：字典里值为 None 的键都不会被添加到 URL 的查询字符串里。

##### 2.3 响应内容

我们来获取一下服务器的响应内容，这里地址 `https://api.github.com` 为例：

```
import requests
r = requests.get('https://api.github.com')
print(r.text)

# 输出结果
# {"current_user_url":"https://api.github.com/user","current_user...

```

当访问 `r.text` 之时，Requests 会使用其推测的文本编码，我们可以使用 `r.encoding` 查看其编码，也可以修改编码，如：`r.encoding = 'GBK'`，当改变了编码，再次访问 `r.text` 时，Request 都将会使用 `r.encoding` 的新值。

1）二进制响应内容 比如当我们要获取一张图片的数据，会以二进制的方式获取响应数据，示例如下：

```
from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(r.content))

```

2）JSON响应内容 Requests 中已经内置了 JSON 解码器，因此我们可以很容易的对 JSON 数据进行解析，示例如下：

```
import requests
r = requests.get('https://api.github.com')
r.json()

```

`注`:成功调用 r.json() 并不一定响应成功，有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节），这时我们就需要查看响应的状态码了 `r.status_code` 或 `r.raise_for_status()`，成功调用时 `r.status_code` 为 200，`r.raise_for_status()` 为 None。

##### 2.4 自定义请求头

当我们要给请求添加 headers 时，只需给 `headers` 参数传递一个字典即可，示例如下：

```
url = 'http://xxx.xxx'
hds= {<!-- -->'user-agent': 'xxx'}
r = requests.get(url, headers=hds)

```

`注`：自定义 headers 优先级是低于一些特定的信息的，如：在 `.netrc` 中设置了用户认证信息，使用 headers 设置的授权就不会生效，而当设置了 `auth` 参数，`.netrc` 的设置会无效。所有的 headers 值必须是 string、bytestring 或者 unicode，通常不建议使用 unicode。

##### 2.5 重定向与历史

默认情况下，Requests 会自动处理除了 HEAD 以外的所有重定向，可以使用响应对象的 `history` 属性来追踪重定向，其返回为响应对象列表，这个列表是按照请求由晚到早进行排序的，看一下示例：

```
import requests
r = requests.get('http://github.com')
print(r.history)
# 输出结果
# [&lt;Response [301]&gt;]

```

如果使用的是 `get、post、put、delete、options、patch` 可以使用 `allow_redirects` 参数禁用重定向。示例如下：

```
r = requests.get('http://xxx.xxx', allow_redirects=False)

```

##### 2.6 错误与异常

当遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出 ConnectionError 异常；在 HTTP 请求返回了不成功的状态码时， Response.raise_for_status() 会抛出 HTTPError 异常；请求超时，会抛出 Timeout 异常；请求超过了设定的最大重定向次数，会抛出 TooManyRedirects 异常。所有 Requests 显式抛出的异常都继承自 requests.exceptions.RequestException。

参考： 

**欢迎关注文末公众号，免费领取海量学习资料！**

<img src="https://img-blog.csdnimg.cn/20191118111747841.jpg#pic_center" alt="" width="600">

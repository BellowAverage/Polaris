
--- 
title:  scrapy专利爬虫（二）——请求相关 
tags: []
categories: [] 

---
## scrapy专利爬虫（二）——请求相关

在这里笔者将会介绍一些关于发送request的相关内容。

### Spider

Spider默认需要填写三个参数：
|name|spider的独立名称，必须唯一
|allowed_domains|允许爬取的范围，以专利爬虫为例，不会超出专利网站的范围，所以只需要填写”pss-system.gov.cn”即可。
|start_urls|起始url，spider会首先请求这个参数里的地址。


### Request和FormRequest

在Spider之后，如果想继续深入爬取，可以使用Requset或FormRequest对象建立新的链接。
- 需要指定Request/FormRequset的callback参数，这是一个含reponse的回调函数，这样当请求完成后，scrapy会自动调用所设定的回调函数处理reponse。- 参数传递，Request和FormRequest都用meta这个参数，这个参数会跟随reponse在callback参数的回调函数中出现。所以可以进行参数传递。- 设定请求的method是get，post等。- 关于FormRequest，这是一个可以用来发送表单数据的请求，有个formData参数，可带tuple格式参数- 其他参数详见
在这里必须要解释的一个python关键字是`yield`，笔者的理解这是一个迭代对象生成器。对于list等可迭代对象，可以用函数的方式生成，只要在函数中使用yield这个关键字，代码在执行的时候会先挂起yield前的所有操作，当对象产生迭代行为，如for循环时才会执行前面的代码。在scrapy中将会经常使用这个关键字，发送请求。

### 下载延时

在settings.py文件中，可以设置请求完成后的文件下载延时DOWNLOAD_DELAY，为了减轻服务器的压力这个延时不能设置得太低。

### 部分中间件
- UserAgentMiddleware
可以用来随机替换程序发送请求请求的User-Agent参数，伪装各种浏览器，不会轻易被服务器发现。

```
class RandomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', HeadersEngine().getRandomUserAgent())
```
- HttpProxyMiddleware
可以用来实现ip代理的功能

```
class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://" + 你的代理ip + : + 你的代理ip的端口号
```
- 如何开启中间件
在settings.py文件中，有这样一段代码：

```
DOWNLOADER_MIDDLEWARES = {
    'PatentCrawler.middlewares.ProxyMiddleware': 543,
    'PatentCrawler.middlewares.RandomUserAgentMiddleware': 542
}
```

需要在花括号内将定义的中间件填写上去，并填写优先级。

### 源码下载
- - <td align="center" colspan="2">赞赏</td>
<td align="center"> <img src="https://img-blog.csdn.net/20170521121423299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="微信支付"> </td><td align="center"> <img src="https://img-blog.csdn.net/20170521131930503?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="支付宝"> </td>
<td align="center">微信</td><td align="center">支付宝</td>

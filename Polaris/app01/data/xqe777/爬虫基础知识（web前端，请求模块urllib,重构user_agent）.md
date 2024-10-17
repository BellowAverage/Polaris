
--- 
title:  爬虫基础知识（web前端，请求模块urllib,重构user_agent） 
tags: []
categories: [] 

---
网络爬虫（又被称作网络蜘蛛，网络机器人，网页追逐者），可以按照一定的规则（网络爬虫的算法）自动浏览或抓取网络中的信息，利用python可以很轻松的编写爬虫程序或者脚本。 

#### 爬虫知识
- - <ul><li>- <ul><li>


## 了解web前端

**HTTP基本原理** HTTP(HpperText Transfer Protocol),即超文本传输协议，是互联网上应用广泛的一种网络协议。HTTP是利用TCP在Web服务器和客户端之间传输信息的协议，客户端使用Web浏览器发起HTTP请求给Web服务器，Web服务器发送被请求的信息给客户端。 <mark>HTTP协议常用的请求方法</mark>

|方法|描述
|------
|GET|请求指定的页面信息，并返回响应内容
|POST|向指定资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求体中。POST请求可能会导致新的资源的建立、或已有资源的修改
|HEAD|类似于GET请求，只不过返回的响应中没有具体的内容，用于获取报文头部信息
|PUT|从客户端像服务器传送的数据取代指定的文档内容
|DELEAE|请求服务器删除指定内容
|OPTIONS|允许客户端查看服务器性能

<mark>HTTP状态码及其含义</mark>

|代码|含义
|------
|1**|信息，请求收到，继续处理
|2**|成功，行为被成功地接受、理解和采纳
|3**|重定向，为了完成请求必须进一步执行的动作
|4**|客户端错误，请求包含语法错误或者请求无法实现
|5**|服务器错误，服务器不能实现一种明显无效的请求

例如：状态码200，表示请求成功完成，状态码404，表示服务器找不到给定的资源。 **浏览器中的请求与响应** 例如使用谷歌浏览器访问百度官网，查看请求和响应的具体步骤如下： <mark>1</mark>在谷歌浏览器输入网址进入百度官网

<mark>2</mark>按下**F12**键（或单击鼠标右键选择”检查“选项），审查页面元素

<mark>3</mark>单击谷歌浏览器调试工具中“Network”选项，按下**F5** 键（或手动刷新页面），单击调试工具中的“Name”栏目下的网址，查看请求与响应信息。

<mark>Geral概述关键信息如下</mark> Request URL:请求的URL网址，也就是服务器的URL网址

Request Method:请求方式为<mark>GET</mark> Status Code:状态码为<mark>200</mark>,即成功返回响应。 Remote Address :服务器IP地址是<mark>39.156.66.14:443</mark>，端口号是<mark>80</mark>

### 请求模块urllib

urllib是python自带模块，该模块提供了一个urlopen()的方法，通过该方法指定URL发送网络请求来获取数据，urllib提供了多个子模块，如下图所示

|模块名称|描述
|------
|urllib.request|用于实现基本HTTP请求的模块
|urllib.error|异常处理模块，如果在发送网络请求时出现错误，可以捕获异常进行异常的有效处理
|urllib.parse|用于解析URL的模块
|urllib.robotparser|用于解析robots.txt文件，判断网站是否可以爬取信息

在使用urlopen()方法实现一个网络请求时，所返回的是一个“&lt;http.client.HTTPResponse object at 0x0000013BA5A47E48&gt;”对象

#### 重构user_agent

User-Agent(简称UA)，记录了操作系统的信息和浏览器的信息 以www.baidu.com为例演示

当不重构ua时，直接访问网址，只会返回百度的部分源码，因为百度识别出来我们是爬虫

这时就需要重构ua,伪装自己是浏览器发起请求 查看浏览器ua的方法：按F12键打开Network，在request headers里面就可以看到浏览器的ua.

创建具有请求头信息的Request对象，然后使用urlopen()方法向“百度”地址发送一个GET请求，利用字典添加请求头信息最常用的用法就是修改User-Agent来伪装浏览器，例如 headers = {“user-agent”: “Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36” }表示伪装成谷歌浏览器进行网络请求，可以获取百度的全部源代码

以上就是爬虫基础知识，如果有改进的建议，欢迎在评论区留言奥~ 觉得不错的话三连支持一下~

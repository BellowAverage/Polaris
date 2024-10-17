
--- 
title:  史上最全！Python爬虫requests库(附案例) 
tags: []
categories: [] 

---
来源：AI算法科研paper

## 1.requests 库简介

Requests 是一个为人类设计的简单而优雅的 HTTP 库。requests 库是一个原生的 HTTP 库，比 urllib3 库更为容易使用。requests 库发送原生的 HTTP 1.1 请求，无需手动为 URL 添加查询串， 也不需要对 POST 数据进行表单编码。相对于 urllib3 库， requests 库拥有完全自动化 Keep-alive 和 HTTP 连接池的功能。requests 库包含的特性如下。

❖ 1Keep-Alive &amp; 连接池

❖ 国际化域名和 URL

❖ 带持久 Cookie 的会话

❖ 浏览器式的 SSL 认证

❖ 自动内容解码

❖ 基本 / 摘要式的身份认证

❖ 优雅的 key/value Cookie

❖ 自动解压

❖ Unicode 响应体

❖ HTTP(S) 代理支持

❖ 文件分块上传

❖ 流下载

❖ 连接超时

❖ 分块请求

❖ 支持 .netrc

### 1.1 Requests 的安装

```
pip install requests
```

### 1.2 Requests 基本使用

代码 1-1: 发送一个 get 请求并查看返回结果

```
import requests
url = 'http://www.tipdm.com/tipdm/index.html' # 生成get请求
rqg = requests.get(url)
# 查看结果类型
print('查看结果类型：', type(rqg))
# 查看状态码
print('状态码：',rqg.status_code)
# 查看编码
print('编码 ：',rqg.encoding)
# 查看响应头
print('响应头：',rqg.headers)
# 打印查看网页内容
print('查看网页内容：',rqg.text)
```

```
查看结果类型：&lt;class ’requests.models.Response’&gt;
状态码：200
编码 ：ISO-8859-1
响应头：{’Date’: ’Mon, 18 Nov 2019 04:45:49 GMT’, ’Server’: ’Apache-Coyote/1.1’, ’
Accept-Ranges’: ’bytes’, ’ETag’: ’W/"15693-1562553126764"’, ’Last-Modified’: ’
Mon, 08 Jul 2019 02:32:06 GMT’, ’Content-Type’: ’text/html’, ’Content-Length’: ’
15693’, ’Keep-Alive’: ’timeout=5, max=100’, ’Connection’: ’Keep-Alive’}
```

### 1.3 Request 基本请求方式

你可以通过 requests 库发送所有的http请求：

```
requests.get("http://httpbin.org/get") #GET请求
requests.post("http://httpbin.org/post") #POST请求
requests.put("http://httpbin.org/put") #PUT请求
requests.delete("http://httpbin.org/delete") #DELETE请求
requests.head("http://httpbin.org/get") #HEAD请求
requests.options("http://httpbin.org/get") #OPTIONS请求
```

## 2.使用Request发送GET请求

HTTP中最常见的请求之一就是GET 请求，下面首先来详细了解一下利用requests构建GET请求的方法。

GET 参数说明：get(url, params=None, **kwargs):

❖ URL: 待请求的网址

❖ params ：（可选）字典，列表为请求的查询字符串发送的元组或字节

❖ **kwargs: 可变长关键字参数

首先，构建一个最简单的 GET 请求，请求的链接为 http://httpbin.org/get ，该网站会判断如果客户端发起的是 GET 请求的话，它返回相应的请求信息，如下就是利用 requests构建一个GET请求

```
import requests
r = requests.get(http://httpbin.org/get)
print(r.text)
{
"args": {},
"headers": {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Host": "httpbin.org",
"User-Agent": "python-requests/2.24.0",
"X-Amzn-Trace-Id": "Root=1-5fb5b166-571d31047bda880d1ec6c311"
},
"origin": "36.44.144.134",
"url": "http://httpbin.org/get"
}
```

可以发现，我们成功发起了 GET 请求，返回结果中包含请求头、URL 、IP 等信息。那么，对于 GET 请求，如果要附加额外的信息，一般怎样添加呢？

### 2.1 发送带 headers 的请求

首先我们尝试请求知乎的首页信息

```
import requests
response = requests.get(’https://www.zhihu.com/explore’)
print(f"当前请求的响应状态码为：{response.status_code}")
print(response.text)
```

当前请求的响应状态码为：400

## 400 Bad Request

这里发现响应的状态码为 400 ，说明我们请求失败了，因为知乎已经发现了我们是一个爬虫，因此需要对浏览器进行伪装，添加对应的 UA 信息。

```
import requests
headers = {"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’}
response = requests.get(’https://www.zhihu.com/explore’, headers=headers)
print(f"当前请求的响应状态码为：{response.status_code}")
# print(response.text)
```

当前请求的响应状态码为：200

&lt;!doctype html&gt;

.......

这里我们加入了 headers 信息，其中包含了 User-Agent 字段信息，也就是浏览器标识信息。很明显我们伪装成功了！这种伪装浏览器的方法是最简单的反反爬措施之一。

GET 参数说明：携带请求头发送请求的方法

requests.get(url, headers=headers)

-headers 参数接收字典形式的请求头

-请求头字段名作为 key ，字段对应的值作为 value

**练习**

请求百度的首页 https://www.baidu.com , 要求携带 headers, 并打印请求的头信息 !

**解**

```
import requests
url = 'https://www.baidu.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 在请求头中带上User-Agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
print(response.content)
# 打印请求头信息
print(response.request.headers)
```

### 2.2 发送带参数的请求

我们在使用百度搜索的时候经常发现 url 地址中会有一个 ‘?‘ ，那么该问号后边的就是请求参数，又叫做查询字符串!

通常情况下我们不会只访问基础网页，特别是爬取动态网页时我们需要传递不同的参数获取 不同的内容；GET 传递参数有两种方法，可以直接在链接中添加参数或者利用 params 添加参数。

#### 2.2.1 在 url 携带参数

直接对含有参数的url发起请求

```
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
url = ’https://www.baidu.com/s?wd=python’
response = requests.get(url, headers=headers)
```

#### 2.2.2 通过 params 携带参数字典

1.构建请求参数字典

2.向接口发送请求的时候带上参数字典，参数字典设置给 params

```
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 这是目标url
# url = ’https://www.baidu.com/s?wd=python’
# 最后有没有问号结果都一样
url = ’https://www.baidu.com/s?’
# 请求参数是一个字典 即wd=python
kw = {’wd’: ’python’}
# 带上请求参数发起请求，获取响应
response = requests.get(url, headers=headers, params=kw)
print(response.content)
```

通过运行结果可以判断，请求的链接自动被构造成了：

http://httpbin.org/get?key2=value2&amp;key1=value1 。

另外，网页的返回类型实际上是str类型，但是它很特殊，是 JSON格式的。所以，如果想直接解析返回结果，得到一个字典格式的话，可以直接调用json() 方法。示例如下：

```
import requests
r = requests.get("http://httpbin.org/get")
print( type(r.text))
print(r.json())
print( type(r. json()))
```

&lt; class ’str’ &gt;

{ ’args’ : {}, ’headers’ : { ’Accept’ : ’*/*’ , ’Accept-Encoding’ : ’gzip, deflate’ , ’Host’

’httpbin.org’ , ’User-Agent’ : ’python-requests/2.24.0’ , ’X-Amzn-Trace-Id’ : ’

Root=1-5fb5b3f9-13f7c2192936ec541bf97841’ }, ’origin’ : ’36.44.144.134’ , ’url’ : ’

http://httpbin.org/get’ }

&lt; class ’dict’ &gt;

可以发现，调用 json() 方法，就可以将返回结果是JSON格式的字符串转化为字典。但需要注意的是，如果返回结果不是 JSON 格式，便会出现解析错误，抛出 json.decoder.JSONDecodeError异常。

补充内容，接收字典字符串都会被自动编码发送到 url ，如下：

```
import requests
headers = {’User-Agent’: ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36’}
wd = ’张三同学’
pn = 1
response = requests.get(’https://www.baidu.com/s’, params={’wd’: wd, ’pn’: pn},
headers=headers)
print(response.url)
```

## # 输出为：https://www.baidu.com/s?wd=%E9%9B%A8%E9%9C%93%E5%90%8

C%E5%AD%A6&amp;pn=1

# 可见 url 已被自动编码

上面代码相当于如下代码，params编码转换本质上是用urlencode

```
import requests
from urllib.parse import urlencode
headers = {’User-Agent’: ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko)
wd = ’张三同学’
encode_res = urlencode({’k’: wd}, encoding=’utf-8’)
keyword = encode_res.split(’=’)[1]
print(keyword)
# 然后拼接成url
url = ’https://www.baidu.com/s?wd=%s&amp;pn=1’ % keyword
response = requests.get(url, headers=headers)
print(response.url)
```

## # 输出为：https://www.baidu.com/s?wd=%E9%9B%A8%E9%9C%93%E5

%90%8C%E5%AD%A6&amp;pn=1

### 2.3 使用 GET 请求抓取网页

上面的请求链接返回的是 JSON 形式的字符串，那么如果请求普通的网页，则肯定能获得相应的内容了!

```
import requests
import re
headers = {"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’}
response = requests.get(’https://www.zhihu.com/explore’, headers=headers)
result = re.findall("(ExploreSpecialCard-contentTitle|ExploreRoundtableCard
questionTitle).*?&gt;(.*?)&lt;/a&gt;", response.text)
print([i[1] for i in result])
```

[ ’ 西安回民街有什么好吃的？’ , ’ 西安有哪些值得逛的宝藏店铺？’ , ’ 西安哪些商圈承载着你的青春？’ , ’ 你有哪些好的驾驶习惯可以分享？’ , ’ 有哪些只有经验丰富的司机才知道的驾驶技巧？’ , ’ 有车的注意了，这些开车知识每个人都要掌握，关键时刻能救命 ’ , ’ 欢迎着陆！知乎宇宙成员招募通告’ , ’ 星球登陆问题：给你十块钱穿越到未来，怎样才能混得风生水起？’ , ’ 星球登陆问题：知乎宇宙中的「超能量」你最希望拥有哪一种？你会如何使用它？’ , ’ 挪威三文鱼，原产地至关重要 ’ , ’ 挪威最吸引人的地方有哪些？’ , ’ 生活在挪威是一种 什么体验？’ , ’ 如何看待京东方 AMOLED 柔性屏量产？未来前景如何？’ , ’ 柔性屏能不能给手机行业带来革命性的影响？’ , ’ 什么是超薄可弯曲柔性电池？会对智能手机的续航产生重大影响吗？’ , ’ 美术零基础怎样才能学好美术，在艺考中取得高分？’ , ’ 清华美院被鄙视吗 ?’ , ’ 艺术生真的很差吗？’ , ’ 人应该怎样过这一生？’ , ’ 人的一生到底该追求什么？’ , ’ 人类知道世界的终极真理后会疯掉吗?’ , ’ 焦虑是因为自己能力不够吗？’ , ’ 社交恐惧症是怎样的一种体验？’ , ’ “忙起来你就没时间抑郁了”这句话有理么？’ ]

这里我们加入了 headers 信息，其中包含了 User-Agent 字段信息，也就是浏览器标识信息。如果不加这个，知乎会禁止抓取。

抓取二进制数据在上面的例子中，我们抓取的是知乎的一个页面，实际上它返回的是一个 HTML 文档。

如果想抓去图片、音频、视频等文件，应该怎么办呢？图片、音频、视频这些文件本质上都是由二进制码组成的，由于有特定的保存格式和对应的解析方式，我们才可以看到这些形形色色的多媒体。

所以，想要抓取它们，就要拿到它们的二进制码。下面以 GitHub的站点图标为例来看一下：

```
import requests
response = requests.get("https://github.com/favicon.ico")
with
open(’github.ico’, ’wb’) as f:
f.write(response.content)
```

Response对象的两个属性，一个是 text, 另一个是 content. 其中前者表示字符串类型文本，后者表示 bytes 类型数据 , 同样地，音频和视频文件也可以用这种方法获取。

### 2.4 在Headers参数中携带cookie

网站经常利用请求头中的 Cookie 字段来做用户访问状态的保持，那么我们可以在 headers 参数中添加 Cookie ，模拟普通用户的请求。

#### 2.4.1 Cookies 的获取

为了能够通过爬虫获取到登录后的页面，或者是解决通过 cookie 的反爬，需要使用 request 来处理 cookie 相关的请求：

```
import requests
url = ’https://www.baidu.com’
req = requests.get(url)
print(req.cookies)
# 响应的cookies
for key, value in req.cookies.items():
print(f"{key} = {value}")
```

&lt;RequestsCookieJar[&lt;Cookie BDORZ=27315 for .baidu.com/&gt;]&gt;

BDORZ = 27315

这里我们首先调用 cookies 属性即可成功得到 Cookies ，可以发现它是 RequestCookieJar 类型。然后用 items() 方法将其转化为元组组成的列表，遍历输出每一个 Cookie 的名称和值，实现 Cookie 的遍历解析。

#### 2.4.2 携带 Cookies 登录

带上 cookie 、 session 的好处 ：能够请求到登录之后的页面。

带上 cookie 、 session 的弊端：一套 cookie 和 session 往往和一个用户对应请求太快，请求次数太多，容易被服务器识别为爬虫。

不需要 cookie 的时候尽量不去使用 cookie 但是为了获取登录之后的页面, 我们必须发送带有 cookies 的请求 我们可以直接用 Cookie 来维持登录状态 , 下面以知乎为例来说明。首先登录知乎，将 Headers 中的 Cookie 内容复制下来。

➢ 从浏览器中复制 User-Agent 和 Cookie

➢ 浏览器中的请求头字段和值与 headers 参数中必须一致

➢ headers 请求参数字典中的 Cookie 键对应的值是字符串

```
import requests
import re
# 构造请求头字典
headers = {
# 从浏览器中复制过来的User-Agent
"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (
KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’,
# 从浏览器中复制过来的Cookie
"cookie": ’xxx这里是复制过来的cookie字符串’}
# 请求头参数字典中携带cookie字符串
response = requests.get(’https://www.zhihu.com/creator’, headers=headers)
data = re.findall(’CreatorHomeAnalyticsDataItem-title.*?&gt;(.*?)&lt;/div&gt;’,response.text)
print(response.status_code)
print(data)
```

当我们不携带 Cookies 进行请求时：

```
import requests
import re
headers = {"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’}
response = requests.get(’https://www.zhihu.com/creator’, headers=headers)
data = re.findall(’CreatorHomeAnalyticsDataItem-title.*?&gt;(.*?)&lt;/div&gt;’,response.text)
print(response.status_code)
print(data)
```

200

[]

在打印的输出结果中为空 , 两者对比 , 则成功利用 headers 参数携带 cookie ，获取登陆后才能访问的页面!

#### 2.4.3 cookies 参数的使用

上一小节我们在headers参数中携带cookie ，也可以使用专门的cookies参数。

❖ 1. cookies 参数的形式：字典

cookies = "cookie 的 name":"cookie 的 value"

➢ 该字典对应请求头中 Cookie 字符串，以分号、空格分割每一对字典键值对

➢ 等号左边的是一个 cookie 的 name ，对应 cookies 字典的 key

➢ 等号右边对应 cookies 字典的 value

❖ 2.cookies 参数的使用方法

response = requests.get(url, cookies)

❖ 3. 将 cookie 字符串转换为 cookies 参数所需的字典：

cookies_dict = { cookie . split ( ’=’ ) [ 0 ]: cookie . split ( ’=’ ) [- 1 ] for cookie in

cookies_str . split ( ’; ’ ) }

❖ 4. 注意：cookie 一般是有过期时间的，一旦过期需要重新获取

```
response = requests.get(url, cookies)
import requests
import re
url = ’https://www.zhihu.com/creator’
cookies_str = ’复制的cookies’
headers = {"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’}
cookies_dict = {cookie.split(’=’, 1)[0]:cookie.split(’=’, 1)[-1] for cookie in
cookies_str.split(’; ’)}
# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=cookies_dict)
data = re.findall(’CreatorHomeAnalyticsDataItem-title.*?&gt;(.*?)&lt;/div&gt;’,resp.text)
print(resp.status_code)
print(data)
```

200

[ ’python 中该怎么把这种 id 不同但是 class 相同的方法写成一个整合呀？’ , ’ 父母没有能力给我买电脑的钱，我该怎么办？’ , ’ 一句话形容一下你现在的生活状态？’ ]

#### 2.4.4 构造RequestsCookieJar对象进行cookies设置

在这里我们还可以通过构造 RequestsCookieJar 对象进行 cookies 设置 , 示例代码如下:

```
import requests
import re
url = ’https://www.zhihu.com/creator’
cookies_str = ’复制的cookies’
headers = {"user-agent": ’Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36’}
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies_str.split(’;’):
key,value = cookie.split(’=’,1)
jar. set(key,value)
# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=jar)
data = re.findall(’CreatorHomeAnalyticsDataItem-title.*?&gt;(.*?)&lt;/div&gt;’,resp.text)
print(resp.status_code)
print(data)
```

200

[ ’python 中该怎么把这种 id 不同但是 class 相同的方法写成一个整合呀？’ , ’ 父母没有能力给我买电脑的钱，我该怎么办？’ , ’ 一句话形容一下你现在的生活状态？’ ]

这里我们首先新建了一个RequestCookieJar对象，然后将复制下来的cookies利用split() 方法分剖，接着利用 set()方法设置好每个Cookie的key和value，然后通过调用 requests的get()方 法并传递给cookies参数即可。

当然，由于知乎本身的限制， headers参数也不能少，只不过不需要在原来的 headers 参数里面设置 cookie 字段了。测试后，发现同样可以正常登录知乎。

#### 2.4.5 cookieJar 对象转换为 cookies 字典的方法

使用 requests 获取的 resposne 对象，具有 cookies 属性。该属性值是一个 cookieJar 类型，包含了对方服务器设置在本地的 cookie 。我们如何将其转换为 cookies 字典呢？

❖ 1. 转换方法

cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)

❖ 2. 其中 response.cookies 返回的就是 cookieJar 类型的对象

❖ 3. requests.utils.dict_from_cookiejar 函数返回 cookies 字典

```
import requests
import re
url = 'https://www.zhihu.com/creator'
cookies_str = '复制的cookies'
headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
cookie_dict = {cookie.split('=', 1)[0]:cookie.split('=', 1)[-1] for cookie in
cookies_str.split('; ')}
# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=cookies_dict)
data = re.findall('CreatorHomeAnalyticsDataItem-title.*?&gt;(.*?)&lt;/div&gt;',resp.text)
print(resp.status_code)
print(data)
# 可以把一个字典转化为一个requests.cookies.RequestsCookieJar对象
cookiejar = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None,
overwrite=True)
type(cookiejar) # requests.cookies.RequestsCookieJar
type(resp.cookies) # requests.cookies.RequestsCookieJar
#构造RequestsCookieJar对象进行cookies设置其中jar的类型也是 requests.cookies.
RequestsCookieJar
#cookiejar转字典
requests.utils.dict_from_cookiejar(cookiejar)
```

### 2.5 Timeout 设置

在平时网上冲浪的过程中，我们经常会遇到网络波动，这个时候，一个请求等了很久可能任 然没有结果。

在爬虫中，一个请求很久没有结果，就会让整个项目的效率变得非常低，这个时候我们就需 要对请求进行强制要求，让他必须在特定的时间内返回结果，否则就报错。

❖ 1. 超时参数 timeout 的使用方法

response = requests.get(url, timeout=3)

❖ 2. timeout=3 表示：发送请求后， 3 秒钟内返回响应，否则就抛出异常

url = 'http://www.tipdm.com/tipdm/index.html'

#设置超时时间为2

print('超时时间为2:',requests.get(url,timeout=2))

## 超时时间过短将会报错

requests.get(url,timeout = 0.1) #备注时间为0.001

超时时间为 2: &lt;Response [200]&gt;

## 3.使用Request发送POST请求

思考：哪些地方我们会用到POST请求？

1.登录注册（在 web 工程师看来 POST 比 GET 更安全， url 地址中不会暴露用户的账号密码等信息）

2.需要传输大文本内容的时候（ POST 请求对数据长度没有要求）

所以同样的，我们的爬虫也需要在这两个地方回去模拟浏览器发送 post 请求其实发送 POST 请求与 GET 方式很相似，只是参数的传递我们需要定义在 data 中即可：

POST参数说明：

post(url, data=None, json=None, **kwargs):

❖ URL: 待请求的网址

❖ data ：( 可选 ) 字典，元组列表，字节或类似文件的对象，以在 Request 的正文中发送

❖ json: ( 可选 )JSON 数据，发送到 Request 类的主体中。

❖ **kwargs: 可变长关键字参数

```
import requests
payload = {’key1’: ’value1’, ’key2’: ’value2’}
req = requests.post("http://httpbin.org/post", data=payload)
print(req.text)
```

### 3.1 POST发送JSON数据

很多时候你想要发送的数据并非编码为表单形式的 , 发现特别在爬取很多java网址中出现这个问题。如果你传递一个 string而不是一个dict ，那么数据会被直接发布出去。我们可以使用json.dumps()是将 dict 转化成str格式 ; 此处除了可以自行对dict进行编码，你还可以使用json参数直接传递，然后它就会被自动编码。

```
import json
import requests
url = ’http://httpbin.org/post’
payload = {’some’: ’data’}
req1 = requests.post(url, data=json.dumps(payload))
req2 = requests.post(url, json=payload)
print(req1.text)
print(req2.text)
```

可以发现，我们成功获得了返回结果，其中 form 部分就是提交的数据，这就证明 POST 请求 成功发送了。

**笔记**

requests 模块发送请求有 data 、 json 、 params 三种携带参数的方法。

params 在 get 请求中使用， data 、 json 在 post 请求中使用。

data 可以接收的参数为：字典，字符串，字节，文件对象。

❖ 使用 json 参数，不管报文是 str 类型，还是 dict 类型，如果不指定 headers 中 content-type 的

类型，默认是：application/json 。

❖ 使用 data 参数，报文是 dict 类型，如果不指定 headers 中 content-type 的类型，默认 application/x

www-form-urlencoded ，相当于普通 form 表单提交的形式，会将表单内的数据转换成键值对，此时数据可以从 request.POST 里面获取，而 request.body 的内容则为 a=1&amp;b=2 的这种键值对形式。

❖ 使用 data 参数，报文是 str 类型，如果不指定 headers 中 content-type 的类型，默认 application/json。

用 data 参数提交数据时， request.body 的内容则为 a=1&amp;b=2 的这种形式，

用 json 参数提交数据时， request.body 的内容则为 ’"a": 1, "b": 2’ 的这种形式

### 3.2 POST 上传文件

如果我们要使用爬虫上传文件，可以使用 fifile 参数：

```
url = 'http://httpbin.org/post'
files = {'file': open('test.xlsx', 'rb')}
req = requests.post(url, files=files)
req.text
```

如果有熟悉 WEB 开发的伙伴应该知道，如果你发送一个非常大的文件作为 multipart/form data 请求，你可能希望将请求做成数据流。默认下 requests 不支持 , 你可以使用 requests-toolbelt 三方库。

### 3.3 使用 POST 请求抓取网页

主要是找到待解析的网页

```
import requests
# 准备翻译的数据
kw =
input("请输入要翻译的词语：")
ps = {"kw": kw}
# 准备伪造请求
headers = {
# User-Agent：首字母大写，表示请求的身份信息；一般直接使用浏览器的身份信息，伪造
爬虫请求
# 让浏览器认为这个请求是由浏览器发起的[隐藏爬虫的信息]
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (
KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
}
# 发送POST请求，附带要翻译的表单数据--以字典的方式进行传递
response = requests.post("https://fanyi.baidu.com/sug", data=ps)
# 打印返回的数据
# print(response.content)
print(response.content.decode("unicode_escape"))
```

## 4.Requests进阶(1)*Session会话维持

在这一部分主要介绍关于 Session 会话维持，以及代理 IP 的使用。

在requests中，如果直接利用get()或post()等方法的确可以做到模拟网页的请求，但是这实际上是相当于不同的会话，也就是说相当于你用了两个浏览器打开了不同的页面。

设想这样一个场景，第一个请求利用post() 方法登录了某个网站，第二次想获取成功登录后的自己的个人信息， 你又用了一次get()方法去请求个人信息页面。实际上，这相当于打开了两个浏览器，这是两个完全不相关的会话，能成功获取个人信息吗？那当然不能。

有小伙伴可能说了，我在两次请求时设置一样的cookies不就行了？可以，但这样做起来显 得很烦琐，我们有更简单的解决方法。

其实解决这个问题的主要方法就是维持同一个会话，也就是相当于打开一个新的浏览器选项 卡而不是新开一个浏览器。但是我又不想每次设置cookies，那该怎么办呢？这时候就有了新的 利器一Session对象。

利用它，我们可以方便地维护一个会话，而且不用担心 cookies 的问题，它 会帮我们自动处理好。

requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的。接下来我们就来学习它。

### 4.1 requests.session 的作用以及应用场景

❖ requests.session 的作用

自动处理 cookie ， 即下一次请求会带上前一次的 cookie

❖ requests.session 的应用场景

自动处理连续的多次请求过程中产生的cookie

### 4.2 requests.session 使用方法

session 实例在请求了一个网站后，对方服务器设置在本地的 cookie 会保存在 session 中，下 一次再使用 session 请求对方服务器的时候，会带上前一次的 cookie。

session = requests . session () # 实 例 化 session 对 象

response = session . get ( url , headers , ...)

response = session . post ( url , data , ...)

session 对象发送 get 或 post 请求的参数，与 requests 模块发送请求的参数完全一致。

### 4.3 使用Session维持github登录信息

❖ 对 github 登陆以及访问登陆后才能访问的页面的整个完成过程进行抓包

❖ 确定登陆请求的 url 地址、请求方法和所需的请求参数

-部分请求参数在别的 url 对应的响应内容中，可以使用 re 模块获取

❖ 确定登陆后才能访问的页面的的 url 地址和请求方法

❖ 利用 requests.session 完成代码

```
import requests
import re
# 构造请求头字典
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (
KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',}
# 实例化session对象
session = requests.session()
# 访问登陆页获取登陆请求所需参数
response = session.get(https://github.com/login, headers=headers)
authenticity_token = re.search('name="authenticity_token" value="(.*?)" /&gt;',
response.text).group(1) # 使用正则获取登陆请求所需参数
# 构造登陆请求参数字典
data = {
'commit': 'Sign in', # 固定值
'utf8': ' ', # 固定值
'authenticity_token': authenticity_token, # 该参数在登陆页的响应内容中
'login':
input('输入github账号：'),
'password':
input('输入github账号：')}
# 发送登陆请求（无需关注本次请求的响应）
session.post(https://github.com/session, headers=headers, data=data)
# 打印需要登陆后才能访问的页面
response = session.get(https://github.com/settings/profile, headers=headers)
print(response.text)
```

可以使用文本对比工具进行校对 !

## 5.Requests进阶(2)*代理的使用

对于某些网站，在测试的时候请求几次，能正常获取内容。但是一旦开始大规模爬取，对于 大规模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，更甚者可能会直接封禁客户端的 IP ，导致一定时间段内无法访问。

那么，为了防止这种情况发生，我们需要设置代理来解决这个问题，这就需要用到 proxies 参数。可以用这样的方式设置：

proxy代理参数通过指定代理ip ，让代理ip对应的正向代理服务器转发我们发送的请求，那么我们首先来了解一下代理ip以及代理服务器。

### 5.1 使用代理的过程

1.代理 ip 是一个 ip ，指向的是一个代理服务器

2.代理服务器能够帮我们向目标服务器转发请求

### 5.2 正向代理和反向代理

前边提到 proxy 参数指定的代理 ip 指向的是正向的代理服务器，那么相应的就有反向服务器；现在来了解一下正向代理服务器和反向代理服务器的区别。

❖ 从发送请求的一方的角度，来区分正向或反向代理

❖ 为浏览器或客户端（发送请求的一方）转发请求的，叫做正向代理

-浏览器知道最终处理请求的服务器的真实 ip 地址，例如 VPN

❖ 不为浏览器或客户端（发送请求的一方）转发请求、而是为最终处理请求的服务器转发请求的，叫做反向代理

-浏览器不知道服务器的真实地址，例如nginx。

### 5.3 代理 ip(代理服务器）的分类

❖ 根据代理 ip 的匿名程度，代理 IP 可以分为下面三类：

➢ 透明代理 (Transparent Proxy) ：透明代理虽然可以直接“隐藏”你的 IP 地址，但是还是可以查到你是谁。

目标服务器接收到的请求头如下：

REMOTE_ADDR = Proxy IP

HTTP_VIA = Proxy IP

HTTP_X_FORWARDED_FOR = Your IP

➢ 匿名代理 (Anonymous Proxy) ：使用匿名代理，别人只能知道你用了代理，无法知道你是谁。

目标服务器接收到的请求头如下：

REMOTE_ADDR = proxy IP

HTTP_VIA = proxy IP

HTTP_X_FORWARDED_FOR = proxy IP

➢ 高匿代理 (Elite proxy 或 High Anonymity Proxy) ：高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。** 毫无疑问使用高匿代理效果最好 ** 。

目标服务器接收到的请求头如下：

REMOTE_ADDR = Proxy IP

HTTP_VIA = not determined

HTTP_X_FORWARDED_FOR = not determined

❖ 根据网站所使用的协议不同，需要使用相应协议的代理服务。

从代理服务请求使用的协议可以分为：

➢ http 代理：目标 url 为 http 协议

➢ https 代理：目标 url 为 https 协议

➢ socks 隧道代理（例如 socks5 代理）等：

✾ 1. socks 代理只是简单地传递数据包，不关心是何种应用协议（ FTP 、 HTTP 和HTTPS 等）。

✾ 2. socks 代理比 http 、 https 代理耗时少。

✾ 3. socks 代理可以转发 http 和 https 的请求

### 5.4 proxies 代理参数的使用

为了让服务器以为不是同一个客户端在请求；为了防止频繁向一个域名发送请求被封 ip ，所以我们需要使用代理 ip ；那么我们接下来要学习 requests 模块是如何使用代理 ip 的基本用法。

```
response = requests . get ( url , proxies = proxies )
proxies 的形式：字典
proxies = {
" http ": " http :// 12.34.56.79: 9527 ",
" https ": " https :// 12.34.56.79: 9527 ",
}
```

注意：如果 proxies 字典中包含有多个键值对，发送请求时将按照 url 地址的协议来选择使用相应的代理ip

```
import requests
proxies = {
"http": "http://124.236.111.11:80",
"https": "https:183.220.145.3:8080"}
req = requests.get(’http://www.baidu.com’,proxies =proxies)
req.status_code
```

## 6.Requests进阶(3)*SSL证书验证

此外， requests还提供了证书验证的功能。当发送HTTP请求的时候，它会检查SSL证书，我 们可以使用verify参数控制是否检查此证书。其实如果不加verify参数的话，默认是True，会向动验证。

现在我们用 requests 来测试一下：

```
import requests
url = 'https://cas.xijing.edu.cn/xjtyrz/login'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
req = requests.get(url,headers=headers)
```

SSLError: HTTPSConnectionPool(host= ’cas.xijing.edu.cn’ , port=443): Max retries

exceeded with url: /xjtyrz/login (Caused by SSLError(SSLCertVerificationError(1,

’[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get

local issuer certificate (_ssl.c:1123)’ )))

这里提示一个错误 SSL Error ，表示证书验证错误。所以，如果请求一个 HTTPS 站点，但是证书验证错误的页面时，就会报这样的错误，那么如何避免这个错误呢？很简单，把 verify 参数设置为 False 即可。

相关代码如下：

```
import requests
url = 'https://www.jci.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
req = requests.get(url,headers=headers,verify=False)
req.status_code
```

200

找不到需要做 SSL 验证的网页了，好气哦 !

不过我们发现报了一个警告它建议我们给它指定证书。我们可以通过设置忽略警告的方式来屏蔽这个警告：

```
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
url = 'https://www.jci.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
req = requests.get(url,headers=headers,verify=False)
req.status_code
```

200

或者通过捕获警告到日志的方式忽略警告：

```
import logging
import requests
logging.captureWarnings(True)
url = 'https://www.jci.edu.cn/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
req = requests.get(url,headers=headers,verify=False)
req.status_code
```

200

当然，我们也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：

```
import requests
response = requests.get(https://www.12306.cn’,cert=(’./path/server.crt’,’/path/key
))
print(response.status_code)
```

200

当然，上面的代码是演示实例，我们需要有 crt 和 ke y 文件，并且指定它们的路径。注意，本地私有证书的 key 必须是解密状态，加密状态的 key 是不支持的。现在都很少有这种了网址了 !

## 7.Requests库其他内容

### 7.1 查看响应内容

发送请求后，得到的自然就是响应。在上面的实例中，我们使用 text 和 content 获取了响应的内容。此外，还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、Cookies 等。

示例如下：

```
import requests
url = 'https://www.baidu.com'
req = requests.get(url)
print(req.status_code)
# 响应状态码
print(req.text)
# 响应的文本内容
print(req.content)
# 响应的二进制内容
print(req.cookies)
# 响应的cookies
print(req.encoding)
# 响应的编码
print(req.headers)
# 响应的头部信息
print(req.url)
# 响应的网址
print(req.history)
# 响应的历史
```

### 7.2 查看状态码与编码

使用 rqg.status_code 的形式可查看服务器返回的状态码，而使用 rqg.encoding 的形式可通过 服务器返回的 HTTP 头部信息进行网页编码。需要注意的是，当 Requests 库猜测错误的时候，需 要手动指定 encoding 编码，避免返回的网页内容出现乱码。

### 7.3 发送get请求，并手动指定编码

代码 1-2: 发送 get 请求，并手动指定编码

```
url = 'http://www.tipdm.com/tipdm/index.html'
rqg = requests.get(url)
print('状态码 ',rqg.status_code)
print('编码 ',rqg.encoding)
rqg.encoding = 'utf-8' #手动指定编码
print('修改后的编码 ',rqg.encoding)
# print(rqg.text)
```

状态码

200

编码

ISO-8859-1

修改后的编码

utf-8

**笔记**

手动指定的方法并不灵活，无法自适应爬取过程中的不同的网页编码，而使用chardet库的方法比较简便灵活。chardet 库是一个非常优秀的字符串 / 文件编码检测模块

### 7.4 chardet 库的使用

chartdet 库的 detect 方法可以检测给定字符串的编码，其语法格式如下。

chartdet.detect(byte_str)

detect 方法常用参数及其说明

byte_str ：接收 string 。表示需要检测编码的字符串。无默认值

### 7.5 使用detect方法检测编码并指定

代码 1-3: 使用 detect 方法检测编码并指定编码

```
import chardet
url = 'http://www.tipdm.com/tipdm/index.html'
rqg = requests.get(url)
print(rqg.encoding)
print(chardet.detect(rqg.content))
rqg.encoding = chardet.detect(rqg.content)['encoding']
# 访问字典元素
print(rqg.encoding)
```

ISO-8859-1

{ ’encoding’ : ’utf-8’ , ’confidence’ : 0.99, ’language’ : ’’ }

utf-8

### 7.6 requests 库综合测试

向网站 ’http://www.tipdm.com/tipdm/index.html’ 发送一个完整GET的请求 , 该请求包含链接、 请求头、响应头、超时时间和状态码, 并且编码正确设置。

代码 1-6: 生成完整的HTTP请求。

```
# 导入相关的库
import requests
import chardet
# 设置url
url = 'http://www.tipdm.com/tipdm/index.html'
# 设置请求头
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit
/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
# 生成GET请求，并设置延时为2
rqg = requests.get(url,headers=headers,timeout = 2)
# 查看状态码
print("状态码 ",rqg.status_code)
# 检测编码(查看编码)
print('编码 ',rqg.encoding)
# 使用chardet库的detect方法修正编码
rqg.encoding = chardet.detect(rqg.content)['encoding']
# 检测修正后的编码
print('修正后的编码: ',rqg.encoding)
#查看响应头
print('响应头：',rqg.headers)
# 查看网页内容
#print(rqg.text)
```

状态码

200

编码

ISO-8859-1

修正后的编码 : utf-8

响应头：{ ’Date’ : ’Mon, 18 Nov 2019 06:28:56 GMT’ , ’Server’ : ’Apache-Coyote/1.1’ , ’

Accept-Ranges’ : ’bytes’ , ’ETag’ : ’W/"15693-1562553126764"’ , ’Last-Modified’ : ’

Mon, 08 Jul 2019 02:32:06 GMT’ , ’Content-Type’ : ’text/html’ , ’Content-Length’ : ’

15693’ , ’Keep-Alive’ : ’timeout=5, max=100’ , ’Connection’ : ’Keep-Alive’ }
- - - - - 
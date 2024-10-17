
--- 
title:  如何用 Python 提取韦小宝身份证信息 
tags: []
categories: [] 

---
记得以前有个广告词叫：“学好数理化，走遍天下都不怕”，感觉应该再加一句：“带上身份证”，本文我们看一下如何使用 Python 提取身份证信息。

### 实现方式

实现方式大致可以分为两种：
-  自己造轮子，如：使用 OpenCV 等自己编码实现，该方式所有功能都需自己来实现，比较耗时耗力，优点是更灵活一些 -  使用现成的轮子，如：百度云，平台已经实现好了核心功能，并对外提供了 API 接口，我们直接调用接口即可，该方式省时省力，但灵活性可能差一些 
### 实现过程

因为我们要实现的功能也比较简单，这里就用第二种方式来演示一下，下面简单看一下实现过程。

#### SDK 安装

百度云 SDK 对多种语言提供了支持，这里我们安装 Python 版的 SDK，使用 `pip install baidu-aip` 命令即可，SDK 目录结构如下：

```
├── README.md
├── aip                   // SDK 目录
│   ├── __init__.py       // 导出类
│   ├── base.py           // aip 基类
│   ├── http.py           // http 请求
│   └── ocr.py //OCR
└── setup.py              // setuptools 安装

```

#### 创建应用

SDK 安装好后，我们接着需要创建应用了，这里需要一个百度账号或百度云账号，如果没有的话自己注册一个即可，登录及注册地址为：`https://login.bce.baidu.com/?redirect=http%3A%2F%2Fcloud.baidu.com%2Fcampaign%2Fcampus-2018%2Findex.html`，具体过程与基本类似，如果不清楚的话，可以看一下车牌识别这篇文章。

#### 具体实现

我们先找一张身份证图片，如图所示： <img src="https://img-blog.csdnimg.cn/img_convert/f33abc58d266e0a601d14742bcbcc9b5.png" alt=""> 接着看一下代码实现，首先创建 AipOcr，AipOcr 是 OCR 的 Python SDK 客户端，代码实现如下：

```
# 自己的 APPID AK SK
APP_ID = '自己的 App ID'
API_KEY = '自己的 Api Key'
SECRET_KEY = '自己的 Secret Key'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

```

上面三个参数也可以参照中的介绍。

信息的提取有普通和高精度两种模式，普通模式代码实现如下：

```
# 打开并读取文件内容
fp = open("card.jpg", "rb").read()
res = client.basicGeneral(fp) # 普通
# 遍历结果
for tex in res["words_result"]:
    row = tex["words"]
    print(row)

```

输出结果如下：

```
姓名韦小宝
性别男民族汉
出生1654年12月20日
住址北京市东城区景山前街4号
紫禁城敬事房
公民身份证号码112441654122日2438

```

再来试一下高精度模式，代码实现如下：

```
# 打开并读取文件内容
fp = open("card.jpg", "rb").read()
res = client.basicAccurate(fp) # 高精度
# 遍历结果
for tex in res["words_result"]:
    row = tex["words"]
    print(row)

```

输出结果如下：

```
姓名韦小宝
性别男民族汉
出生1654年12月20日
住址北京市东城区景山前街4号
紫禁城敬事房
公民身份证号码11204416541220243X

```

通过输入结果我们可以看到：高精度模式提取了正确的身份证号码，普通模式提取的身份证号码是有一些误差的。

### 总结

本文我们使用 Python 结合百度云接口几行代码就提取了身份证信息，其实除了身份证信息也可以提取其他卡片信息，比如银行卡信息等，有兴趣的可以试一下。

源码在公众号 **Python小二** 后台回复 **201216** 获取。

>  
 本文非首发于个人号 


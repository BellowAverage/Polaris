
--- 
title:  python requests模拟登陆带验证码的网站 
tags: []
categories: [] 

---
作为之前专利爬虫的续篇，本篇准备描述如何通过python的requests模块登录。

### 环境准备
- python 3.6- requests
### chrome尝试

首先，我们使用chrome尝试登录专利网站，并通过network分析各个请求的相关信息。  <img src="https://img-blog.csdn.net/20170812162151182?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

<img src="https://img-blog.csdn.net/20170812160738336?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="Network" title="">

通过分析network，我们可以看到，一次登录操作，有以上相关请求。特别注意的是，以为登录成功后页面会刷新，我们需要将Network工具栏上的Preserve log勾选上，才能保证network不被刷新掉。

由此我们可以发现，checkLoginTimes-check.shtml和wee_security_check这两次请求像是发送登录校验请求。

经过比对后我们发现wee_security_check才是想要的结果。

<img src="https://img-blog.csdn.net/20170812162553814?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">  注：以上图片中，笔者账号密码是瞎填的，但是j_username和j_password显示的内容和笔者写的内容不一致，是因为网站在前端使用了Base64进行加密，这一点笔者是从网站发送的请求中有base64.js这个文件发现的，于是尝试过后确实是base64加密。

### cookies

#### 查看cookies

做过web的朋友可能知道，账号密码验证码登录的时候，经常会使用cookie作为同一用户的标志。于是我们查看一下刚才请求的cookies。  <img src="https://img-blog.csdn.net/20170812163026538?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

#### 为什么要cookies

经验较少的朋友可能乍一看会以为IS_LOGIN是cookies的关键，其实不然。  我们先要简单了解一下cookies是个啥东西，有经验的朋友可以略过。

>  
 “Cookie”是小量信息，由网络服务器发送出来以存储在网络浏览器上，从而下次这位独一无二的访客又回到该网络服务器时，可从该浏览器读回此信息。这是很有用的，让浏览器记住这位访客的特定信息，如上次访问的位置、花费的时间或用户首选项（如样式表）。Cookie 是个存储在浏览器目录的文本文件，当浏览器运行时，存储在 RAM 中。一旦你从该网站或网络服务器退出，Cookie 也可存储在计算机的硬驱上。当访客结束其浏览器对话时，即终止的所有 Cookie。(百度百科） 


我们知道登录有个麻烦事就是验证码，这个对于后台来说其实也是个小麻烦，请求大家都发，后台怎么知道哪个验证码对应哪个浏览器发的请求？答案就是通过cookies。前端请求验证码的时候后台先用Set-Cookie的 response header将一个标识符带个前端浏览器，浏览器储存后下次发送登录请求的时候带上之前后台发过来的cookies，后台就知道是对应验证码的结果对不对了。

#### 明确cookie

那么哪个cookie是我们需要的呢，我可以说通过肉眼观察得知吗~WEE_SID就是我们想要的cookie。好吧，管他是哪个呢，不管三七二十一全部带上就好了。。。。。

### 开发

requests发送管理cookie有两种方式，一种是手动携带，放在get,post等请求的参数带上去即可。另一种使用requests.Session()自动管理cookies，我们不需要操心。但是第二种笔者测试完之后发现好像只有一个cookie的情况下是正常的，当有多个cookie的情况。比如说这个网站，就不行了。不知道是什么原因，如有知道的朋友请告知。  这里我们就只介绍第一种方式。

#### 登录流程
- 第一步获取验证码和相应cookies，  验证码的地址通过观察network获得，这里不再赘述。
```
codeurl = 'http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml'
valcode = requests.get(codeurl)
```

此处cookies已经保存在valcode.cookies中，接下来我们需要将valcode保存为图片。

```
    f = open('valcode.png', 'wb')
    # 将response的二进制内容写入到文件中
    f.write(valcode.content)
    # 关闭文件流对象
    f.close()
```

保存图片之后，鉴于技术问题暂时还没有做机器识别，只能用人眼识别了。得知验证码结果后我们Input进来。

```
    code = input('请输入验证码：')
    data["j_validation_code"] = str(code)
```
- 第二步发送登录请求  通过观察network我们发现登录请求所带的参数格式如下：
```
data = {
        "j_loginsuccess_url": "",
        "j_validation_code": "",
        "j_username": base64Name,
        "j_password": base64Pass
    }
```

这里用户名和密码已经通过base64加密，python中有现成的base64解码编码模块，直接import进来用就可以，笔者不再赘述。

```
checkUrl = 'http://www.pss-system.gov.cn/sipopublicsearch/wee/platform/wee_security_check'
resp = requests.post(checkUrl, headers = checkHeader, cookies = requests.utils.dict_from_cookiejar(valcode.cookies), data=data)
```

发送过后，我们可以从结果看到已经登录成功。  <img src="https://img-blog.csdn.net/20170812173254644?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" title="">

代码资源：
<td align="center" colspan="2">赞赏</td>
<td align="center"> <img src="https://img-blog.csdn.net/20170521121423299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="微信支付"> </td><td align="center"> <img src="https://img-blog.csdn.net/20170521131930503?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="支付宝"> </td>
<td align="center">微信</td><td align="center">支付宝</td>

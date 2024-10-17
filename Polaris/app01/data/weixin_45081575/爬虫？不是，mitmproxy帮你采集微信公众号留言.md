
--- 
title:  爬虫？不是，mitmproxy帮你采集微信公众号留言 
tags: []
categories: [] 

---
## 前言

>  
 有位朋友需要收集公司微信公众号的文章的留言，但苦于微信公众平台没有提供留言的`API`，所以朋友需要在每一篇文章下面去手动复制粘贴，朋友觉得很麻烦，于是来找到我！遂有此文。 


下一篇，将结合`uiautomation`，实现全自动化收集微信公众号留言

值得注意的是：借助`mitmproxy`，我们可以拦截感兴趣的流量，但在这里充其量就是节省了我们手动复制的麻烦，`mitmproxy`在这里的角色就是`拷贝忍者`。

## 知识点📖📖

关于`mitmproxy`，还需要安装配置。参考下面链接： 

本文主要使用的是 `mitmproxy`，关于它的使用，可以
- 看官方文档：- 看我录制的视频：
## 实现

>  
 本文的重点在于定位到留言的流量（即留言的数据包 


打开 `charles` 抓包工具，看看留言的流量，因为比较简单，一眼就找到了对应流量包。 现在知道了留言的流量包，复制它的`URL`，接下来使用`mitmproxy`去拦截它，然后再做保存就可以了。

<img src="https://img-blog.csdnimg.cn/7e1560d39a4045f1a8d1af1c4cae5f8a.png" alt="在这里插入图片描述">

现在去 `chatGPT` 问问强大的它，代码该怎么写。

**mitmproxy监听微信公众号留言的代码**

<img src="https://img-blog.csdnimg.cn/53d6dbe6882846cc8e4ec8ac8f6f3a2e.png" alt="在这里插入图片描述">

看到上图，强大的`chatGPT`连代码都给我们写出来了。 我们关心的是响应，所以取上面的`response`函数，然后替换里面的`URL`即可，如下所示：

<img src="https://img-blog.csdnimg.cn/e1aeaa2a6fc44e26aa29922c8923d52b.png" alt="在这里插入图片描述">

然后在控制台窗口运行它（记得打开电脑代理：
- 参数不做解释
```
mitmdump -s listen_comment.py -q

```

可以看到以下内容，拦截成功。那接下来的工作就只剩下数据解析了。

<img src="https://img-blog.csdnimg.cn/1521e4b60c4445d9adc3d330abf94c8e.png" alt="在这里插入图片描述">

代码的解析很简单，这里就不再做介绍了。

## 代码

>  
 下面的代码还没能保存数据！还需调用一下`parse`函数噢！！！ 


在命令行窗口输入：`mitmdump -s listen_comment.py -q`，即可运行本程序

```
# listen_comment.py

# 导入必要的库
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

## 后话

本次分享到这里结束了， 善于利用工具，就可以实现包括但不限于本文之类的操作啦！ see you~🐱‍🏍🐱‍🏍

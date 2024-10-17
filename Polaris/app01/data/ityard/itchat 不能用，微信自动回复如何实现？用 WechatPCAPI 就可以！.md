
--- 
title:  itchat 不能用，微信自动回复如何实现？用 WechatPCAPI 就可以！ 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200523131719785.PNG#pic_center" alt=""> 在之前的文章  中，我们使用 WechatPCAPI 做了获取微信好友信息以及查看撤回消息，本文我们再使用 WechatPCAPI 来实现微信自动回复的功能。

实现自动回复的功能，我们需要用到图灵机器人，网址为：`http://www.turingapi.com`，我们在浏览器中输入上述网址打开，之后点击`注册/登录`按钮，如下图所示： <img src="https://img-blog.csdnimg.cn/20200523131753697.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 打开后如下图所示： <img src="https://img-blog.csdnimg.cn/2020052313181261.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们接着点击`立即注册`，就跳转到了注册页，如下图所示： <img src="https://img-blog.csdnimg.cn/20200523131829219.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们先填写必填信息，填写完之后点击`注册`按钮即可，注册成功之后便跳到了机器人管理页面，如下所示： <img src="https://img-blog.csdnimg.cn/20200523131846501.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们点击`创建机器人`按钮跳转到如下页面： <img src="https://img-blog.csdnimg.cn/20200523131900289.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们填写完相应信息之后点`创建`按钮，之后会跳转到机器人设置页面，如下图所示： <img src="https://img-blog.csdnimg.cn/2020052313191689.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们需要记录下 `apikey`。

有了 `apikey`，我们就可以实现自动回复功能了，实现代码如下所示：

```
import time, logging, random, requests
from queue import Queue
from WechatPCAPI import WechatPCAPI

logging.basicConfig(level=logging.INFO)
queue_recved_event = Queue()

def on_message(msg):
    queue_recved_event.put(msg)

# 机器人返回消息
def reply_msg(receive_msg):
    apikey = '自己的apikey'
    apiurl = 'http://www.tuling123.com/openapi/api?key=%s&amp;info=%s' % (apikey, receive_msg)
    result = requests.get(apiurl)
    result.encoding = 'utf-8'
    data = result.json()
    return data['text']

def login():
    pre_msg = ''
    # 初始化微信实例
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    # 启动微信
    wx_inst.start_wechat(block=True)
    # 等待登陆成功，此时需要人为扫码登录微信
    while not wx_inst.get_myself():
        time.sleep(5)
    print('登陆成功')
    while True:
        msg = queue_recved_event.get()
        if 'msg::single' in msg.get('type'):
            data = msg.get('data')
            if data.get('is_recv', False):
                msgfrominfo = data.get('msgfrominfo')
                if msgfrominfo is not None:
                    wx_id = msgfrominfo.get('wx_id')
                    if wx_id != 'weixin':
                        receive_msg =str(data.get('msgcontent'))
                        reply = reply_msg(receive_msg)
                        wx_inst.send_text(to_user=wx_id, msg=reply)

```

看一下实现效果： <img src="https://img-blog.csdnimg.cn/20200523131938956.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt="">

>  
 作者：程序员野客 公号：Python小二 链接： 


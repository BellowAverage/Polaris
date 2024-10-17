
--- 
title:  不止短信！教你用 Python 发送告警通知到微信 
tags: []
categories: [] 

---
常见的告警方式有：邮件，电话，短信，微信。

短信和电话，通常是收费的（若你有不收费的，可以评论分享一下），而邮件又不是那么及时，因此最后我选择微信通知。

这里说的微信，是企业微信，而我之前用注册过个体户的执照，因此可以很轻松就可以注册自己的企业微信。

### # 1. 新建应用

登陆网页版企业微信 (https://work.weixin.qq.com/)，点击 **应用管理** -&gt; **应用** -&gt; **创建应用**

上传应用的 logo，输入应用名称，再选择可见范围，成功创建一个告警应用

### # 2. 获取Secret

使用 Python 发送告警请求，其实就只使用到两个接口
- **获取 Token **：https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&amp;corpsecret={secret}- **发送请求**：https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}
可以看到，最重要的是 corpid 和 secret:
- corpid：唯一标识你的企业- secret：应用级的密钥，有了它程序才知道你要发送该企业的哪个应用
corpid 可以通过 **我的企业** -&gt; **企业信息** 获取

而 secret 获取相对麻烦一点，点击前面创建应用，点击 查看 secret

然后再点击发送就会发送到你的企业微信上

最后将 corpid 和 secret 填入下面的常量中。

```
import json
import datetime
import requests

CORP_ID = ""
SECRET = ""

class WeChatPub:
    s = requests.session()

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={CORP_ID}&amp;corpsecret={SECRET}"
        rep = self.s.get(url)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)['access_token']


    def send_msg(self, content):
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
        header = {
            "Content-Type": "application/json"
        }
        form_data = {
            "touser": "@all",
            "toparty": " PartyID1 | PartyID2 ",
            "totag": " TagID1 | TagID2 ",
            "msgtype": "textcard",
            "agentid": 1000002,
            "textcard": {
                "title": "服务异常告警",
                "description": content,
                "url": "URL",
                "btntxt": "更多"
            },
            "safe": 0
        }
        rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
        if rep.status_code != 200:
            print("request failed.")
            return
        return json.loads(rep.content)
```

然后就可以通过 send_msg 函数发送消息了。

```
wechat = WeChatPub()
now = datetime.datetime.now()
timenow = now.strftime('%Y年%m月%d日 %H:%M:%S')
wechat.send_msg(f"&lt;div class=\"gray\"&gt;{timenow}&lt;/div&gt; &lt;div class=\"normal\"&gt;阿里云 cookie 已失效&lt;/div&gt;&lt;div class=\"highlight\"&gt;请尽快更换新的 cookie&lt;/div&gt;")
```

只要你的企业微信没有关闭通知的权限，那你的手机立马就会弹出这个告警信息。

简单几步就对接了企业微信，实现了手机的实时告警功能，推荐有企业微信的同学使用。

当然一定有更多，更好用的实现方法，我只是我选择了其中一种。

**<strong>往期回顾：**</strong>
- - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/a3dc3d48c060d372c2846c54ff544ed2.gif" alt="a3dc3d48c060d372c2846c54ff544ed2.gif">

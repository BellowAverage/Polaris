
--- 
title:  yagmail无法发送邮件，提示连接失败 
tags: []
categories: [] 

---
#### 问题描述

用其他工具能够连接，但是yagmail无法连接。  

#### 排查

以为是pop3而不是SMTP，发现不是。 网络服务通畅，能够连接服务器 密码正确  

#### 解决

查看配置的时候才发现：有一个参数

```
    def __init__(
        self,
        user=None,
        password=None,
        host="smtp.gmail.com",
        port=None,
        smtp_starttls=None,
        smtp_ssl=True,
        smtp_set_debuglevel=0,
        smtp_skip_login=False,
        encoding="utf-8",
        oauth2_file=None,
        soft_email_validation=True,
        dkim=None,
        **kwargs

```

其中有个参数是smtp_ssl=True，默认使用ssl证书连接。 修改为smtp_ssl=False，成功连接。

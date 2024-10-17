
--- 
title:  Python学习笔记第二十二天(SMTP发送邮件) 
tags: []
categories: [] 

---


#### Python学习笔记第二十二天
- - <ul><li>- 


## Python SMTP发送邮件

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

Python创建 SMTP 对象语法如下：

```
import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

```

参数说明：
- host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。- port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。- local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。
Python SMTP 对象使用 sendmail 方法发送邮件，语法如下：

```
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])

```

参数说明：
- from_addr: 邮件发送者地址。- to_addrs: 字符串列表，邮件发送地址。- msg: 发送消息
这里要注意一下第三个参数，msg 是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。这个格式就是 smtp 协议中定义的格式。

### SMTP 的服务

以下执行实例需要你本机已安装了支持 SMTP 的服务，如：sendmail。

以下是一个使用 Python 发送邮件简单的实例：

```
# 实例 1
import smtplib 
from email.mime.text import MIMEText 
from email.header import Header 
sender = 'from@XXX.com' 
receivers = ['XXXXXX@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8') # 发送者 
message['To'] = Header("测试", 'utf-8') # 接收者 

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8') 
try: 
    smtpObj = smtplib.SMTP('localhost') 
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    print("邮件发送成功")
except smtplib.SMTPException: 
    print("Error: 无法发送邮件")

```

我们使用三个引号来设置邮件信息，标准邮件需要三个头部信息： **From**, **To**, 和 **Subject** ，每个信息直接使用空行分割。

我们通过实例化 smtplib 模块的 SMTP 对象 **smtpObj** 来连接到 SMTP 访问，并使用 **sendmail** 方法来发送信息。

执行以上程序，如果你本机安装 **sendmail（邮件传输代理程序）**，就会输出：

```
$ python test.py 
邮件发送成功

```

### 邮件服务商的 SMTP 访问

如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。

```
# 实例 2
import smtplib 
from email.mime.text import MIMEText 
from email.header import Header 
# 第三方 SMTP 服务 
mail_host="smtp.XXX.com" #设置服务器 
mail_user="XXXX" #用户名 
mail_pass="XXXXXX" #口令 

sender = 'from@XX.com'
receivers = ['XXXXXX@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8') 
message['From'] = Header("百度", 'utf-8') 
message['To'] = Header("测试", 'utf-8') 

subject = 'Python SMTP 邮件测试' 
message['Subject'] = Header(subject, 'utf-8') 
try: 
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25) # 25 为 SMTP 端口号 
    smtpObj.login(mail_user,mail_pass) 
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    print("邮件发送成功")
except smtplib.SMTPException: 
    print("Error: 无法发送邮件")

```

今天学习的是Python发送邮件学会了吗。 今天学习内容总结一下：
1. SMTP 的服务1. 邮件服务商的 SMTP 访问
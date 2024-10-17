
--- 
title:  Python 进阶（三）：邮件的发送与收取 
tags: []
categories: [] 

---


#### 目录
- - 


## 1. 发送邮件

SMTP 全称 Simple Mail Transfer Protocol，中文译为简单邮件传输协议，它能跨越网络传输邮件，可实现相同网络处理进程之间的邮件传输，也可通过中继器或网关实现进程与其他网络之间的邮件传输。

Python 的 smtplib 模块对 SMTP 做了封装，可以很方便的实现邮件的发送，同时提供了 email 模块来构造邮件。

**smtplib.SMTP(host=’’, port=0, local_hostname=None, [timeout, ]source_address=None)**

用于创建 SMTP 对象。参数说明如下：
-  host：SMTP 服务器主机。 -  port：端口号。 -  local_hostname：如果 SMTP 在本机，只需指定服务器地址为 localhost 即可。 -  timeout：指定超时时间，可选。 -  source_address：该参数允许绑定到具有多个网络接口的计算机中的某些特定源地址或某些特定源 TCP 端口。 
**SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())**

发送邮件。参数说明如下：
-  from_addr：邮件发送者地址。 -  to_addrs：邮件接收者地址。 -  msg：邮件内容。 
以 QQ 邮箱为例，我们先用发送者账号登录 QQ 邮箱，登录后依次点击“设置”、“账户”，找到如下所示位置： <img src="https://img-blog.csdnimg.cn/20200212203305968.PNG" alt=""> 开启“POP3/SMTP服务”，并将授权码记录下来，如果之前已经开启了服务，但忘记了授权码，可以点击“生成授权码”，看一下具体示例。

**发送简单邮件**

先看一下如何发送简单的文本内容。

```
import smtplib
from email.mime.text import MIMEText

# 发送者邮箱地址
senderMail = 'xxxxxx@qq.com'
# 发送者 QQ 邮箱授权码
authCode = 'xxxxxxxxx'
# 接收者邮箱地址
receiverMail = 'xxxxxx@qq.com'
# 邮件主题
subject = '简单邮件'
# 邮件内容
content = 'hello email'
msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = senderMail
msg['To'] = receiverMail
try:
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
    server.login(senderMail, authCode)
    print('成功登录邮箱')
    server.sendmail(senderMail, receiverMail, msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()

```

**发送复杂邮件**

我们知道有时候邮件内容，除了文本，还会有附件、图片等。

```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 发送者邮箱地址
senderMail = 'xxxxxx@qq.com'
# 发送者 QQ 邮箱授权码
authCode = 'xxxxxxxxx'
# 接收者邮箱地址
receiverMail = 'xxxxxx@qq.com'
# 邮件主题
subject = '复杂邮件测试'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = senderMail
msgRoot['To'] = receiverMail
msgAtv = MIMEMultipart('alternative')
msgRoot.attach(msgAtv)
# html
html_content = '''
&lt;p&gt;我的博客地址：&lt;/p&gt;
&lt;p&gt;&lt;a href='https://blog.csdn.net/ityard'&gt;点击进入我的CSDN&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;我的公众号二维码：&lt;/p&gt;
&lt;p&gt;&lt;img src="cid:image"&gt;&lt;/p&gt;
'''
html = MIMEText(html_content, 'html', 'utf-8')
msgAtv.attach(html)
f = open('qrcode.jpg', 'rb')
msgImage = MIMEImage(f.read())
f.close()
msgImage.add_header('Content-ID', '&lt;image&gt;')
msgRoot.attach(msgImage)
# 附件
annex = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
annex['Content-Type'] = 'application/octet-stream'
annex['Content-Disposition'] = 'attachment; filename="test.txt"'
msgRoot.attach(annex)
try:
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
    server.login(senderMail, authCode)
    print('成功登录邮箱')
    server.sendmail(senderMail, receiverMail, msgRoot.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()

```

登录接收者账号看一下发送情况，如下所示：

<img src="https://img-blog.csdnimg.cn/2020021220484687.PNG#pic" alt="" width="300">

## 2. 收取邮件

POP3 全称 Post Office Protocol - Version 3，3 是版本号，中文译为邮局协议，该协议可以实现邮件的收取，Python 的 poplib 模块实现了该协议。

**poplib.POP3(host, port=POP3_PORT[, timeout])**

实现 POP3 的类。参数说明如下：
-  host：主机。 -  port：端口号。 -  timeout：可选参数，超时时间。 
**poplib.POP3_SSL(host, port=POP3_SSL_PORT, keyfile=None, certfile=None, timeout=None, context=None)**

POP3 通过 SSL 加密套接字连接到服务器的子类。自版本 3.6 起不推荐使用 keyfile 和 certfile，而推荐使用 context。

看一下邮件获取及解析示例。

```
import poplib
from email.parser import Parser
from email.header import decode_header,Header
from email.utils import parseaddr

def print_email(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s &lt;%s&gt;' % (name, addr)
        print('%s: %s' % (header, value))
    # 获取邮件主体信息
    attachment_files = []
    for part in msg.walk():
        # 获取附件名称类型
        file_name = part.get_filename()
        # 获取数据类型
        contentType = part.get_content_type()
        # 获取编码格式
        mycode = part.get_content_charset()
        if file_name:
            h = Header(file_name)
            # 对附件名称进行解码
            dh = decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                # 将附件名称可读化
                filename = decode_str(str(filename, dh[0][1]))
            attachment_files.append(filename)
            # 下载附件
            data = part.get_payload(decode=True)
            # 在当前目录下创建文件
            with open(filename, 'wb') as f:
                # 保存附件
                f.write(data)
        elif contentType == 'text/plain':
            data = part.get_payload(decode=True)
            content = data.decode(mycode)
            print('正文：',content)
        elif contentType == 'text/html':
            data = part.get_payload(decode=True)
            content = data.decode(mycode)
            print('正文：', content)
    print('附件名列表：', attachment_files)

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 接收者邮箱地址
receiverMail = 'xxxxxx@qq.com'
# 接收者 QQ 邮箱授权码
authCode = 'xxxxxxxxx'
pop3_server = 'pop.qq.com'
# 连接到 POP3 服务器
server = poplib.POP3_SSL(pop3_server, 995)
# 身份认证
server.user(receiverMail)
server.pass_(authCode)
# stat() 返回邮件数量和占用空间
print('邮件数量:%s  占用空间:%s' % server.stat())
# list() 返回所有邮件的编号，lines 存储了邮件的原始文本的每一行
resp, mails, octets = server.list()
index = len(mails)
# 获取最新一封邮件
resp, lines, octets = server.retr(index)
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 解析邮件
msg = Parser().parsestr(msg_content)
print_email(msg)
# 根据邮件索引号直接从服务器删除邮件
# server.dele(1)
# 关闭连接
server.quit()

```

<img src="https://img-blog.csdnimg.cn/20200212224139622.png#pic_center" alt="" width="500">

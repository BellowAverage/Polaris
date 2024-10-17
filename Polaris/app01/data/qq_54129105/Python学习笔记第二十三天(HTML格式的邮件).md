
--- 
title:  Python学习笔记第二十三天(HTML格式的邮件) 
tags: []
categories: [] 

---


#### Python学习笔记第二十三天
- - - 


## Python发送HTML格式的邮件

Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html。

```
# 实例 1
import smtplib 
from email.mime.text import MIMEText 
from email.header import Header 
sender = 'from@XX.com' 
receivers = ['XXXXXX@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 
mail_msg = """ &lt;p&gt;Python 邮件发送测试...&lt;/p&gt; &lt;p&gt;&lt;a href="http://www.baidu.com"&gt;这是一个链接&lt;/a&gt;&lt;/p&gt; """ 
message = MIMEText(mail_msg, 'html', 'utf-8') 
message['From'] = Header("baidu", 'utf-8')
message['To'] = Header("测试", 'utf-8') 
subject = 'Python SMTP 邮件测试' 
message['Subject'] = Header(subject, 'utf-8') 
try: 
    smtpObj = smtplib.SMTP('localhost') 
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")


```

## Python发送带附件的邮件

发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。

```
# 实例 2
import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.header import Header 
sender = 'from@XX.com' 
receivers = ['XXXXXX@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 
#创建一个带附件的实例 
message = MIMEMultipart() 
message['From'] = Header("百度", 'utf-8')
message['To'] = Header("测试", 'utf-8') 
subject = 'Python SMTP 邮件测试' 
message['Subject'] = Header(subject, 'utf-8')
#邮件正文内容 
message.attach(MIMEText('这是Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件 
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8') 
att1["Content-Type"] = 'application/octet-stream' 
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字 
att1["Content-Disposition"] = 'attachment; filename="test.txt"' 
message.attach(att1) 
# 构造附件2，传送当前目录下的 baidu.txt 文件 
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8') 
att2["Content-Type"] = 'application/octet-stream' 
att2["Content-Disposition"] = 'attachment; filename="baidu.txt"' 
message.attach(att2) 
try: 
    smtpObj = smtplib.SMTP('localhost') 
    smtpObj.sendmail(sender, receivers, message.as_string()) 
    print("邮件发送成功" )
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

```

## HTML文本中添加图片

邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加图片

```
import smtplib 
from email.mime.image import MIMEImage 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.header import Header 
sender = 'from@XX.com' 
receivers = ['XXXXXX@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("百度", 'utf-8') 
msgRoot['To'] = Header("测试", 'utf-8') 
subject = 'Python SMTP 邮件测试' 
msgRoot['Subject'] = Header(subject, 'utf-8') 
msgAlternative = MIMEMultipart('alternative') 
msgRoot.attach(msgAlternative)
mail_msg = """ &lt;p&gt;Python 邮件发送测试...&lt;/p&gt; &lt;p&gt;&lt;a href="http://www.runoob.com"&gt;菜鸟教程链接&lt;/a&gt;&lt;/p&gt; &lt;p&gt;图片演示：&lt;/p&gt; &lt;p&gt;&lt;img src="cid:image1"&gt;&lt;/p&gt; """ 
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8')) # 指定图片为当前目录 
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read()) fp.close() # 定义图片 ID，在 HTML 文本中引用 msgImage.add_header('Content-ID', '&lt;image1&gt;') 
msgRoot.attach(msgImage) 
try: 
    smtpObj = smtplib.SMTP('localhost') 
    smtpObj.sendmail(sender, receivers, msgRoot.as_string()) 
    print("邮件发送成功" except) 
smtplib.SMTPException: 
    print("Error: 无法发送邮件")


```

今天学习的是Python发送邮件学会了吗。 今天学习内容总结一下：
1. Python发送HTML格式的邮件1. Python发送带附件的邮件1. HTML文本中添加图片
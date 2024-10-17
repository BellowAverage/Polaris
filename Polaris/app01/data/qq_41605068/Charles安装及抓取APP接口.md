
--- 
title:  Charles安装及抓取APP接口 
tags: []
categories: [] 

---
## 一、Charles使用

Charles是一款，通过过将自己设置成系统（电脑或者浏览器）的网络访问代理服务器，然后截取请求和请求结果达到分析抓包的目的。该软件是用Java写的，能够在Windows，Mac，Linux上使用。安装Charles的时候要先装好Java环境。

Charles的主要功能：

（1）截取Http 和 Https 网络封包。

（2）支持重发网络请求，方便后端调试。

（3）支持修改网络请求参数。

（4）支持网络请求的截获并动态修改。

（5）支持模拟慢速网络。

## 二、下载

地址：<img alt="" height="323" src="https://img-blog.csdnimg.cn/be5f2c0e0f164bd0a860a5e72c7eb256.png" width="1004">

##  三、安装

<img alt="" height="436" src="https://img-blog.csdnimg.cn/dcc68b46958e40469ab577b2f5a18157.png" width="987">

##  四、激活

地址：

<img alt="" height="413" src="https://img-blog.csdnimg.cn/e0dbe2a291074eda82f7b4ecba6e043c.png" width="1200">

<img alt="" height="402" src="https://img-blog.csdnimg.cn/6125b47642734f73a54ee43bfbd8ebab.png" width="955">

 <img alt="" height="229" src="https://img-blog.csdnimg.cn/668213b93c084c1dac0ba8e0457b0e39.png" width="174">

 填写：

<img alt="" height="532" src="https://img-blog.csdnimg.cn/7183220ddb224f67b94cf07270c0ea01.png" width="898">

##  五、PC抓包

由于charles会自动配置浏览器和工具的代理设置，所以说打开工具直接就已经是抓包状态了。直接打开网页就可以了。

注意：

（1）Charles支持抓去http、https协议的请求，不支持socket。

（网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket）

（2）防火墙关掉

点击上方的代理—windows代理

<img alt="" height="821" src="https://img-blog.csdnimg.cn/6498f7025ce14c69b13d1fceb46162fa.png" width="672">

###  5.1下载SSL证书

<img alt="" height="625" src="https://img-blog.csdnimg.cn/a181f9c583c94b4abfad6be01215ba52.png" width="1019">

###  5.2安装证书

<img alt="" height="578" src="https://img-blog.csdnimg.cn/7a843edfe0d5405bb65d0bded559febc.png" width="1164">

## 6.APP抓包 

 使手机和电脑在一个局域网内，不一定非要是一个ip段，只要是同一个路由器下就可以了。

### 6.1配置代理服务器

<img alt="" height="1050" src="https://img-blog.csdnimg.cn/dda2a65b666e49d9b2e28b2130c88388.png" width="1200">

### 6.2查看本地IP

 <img alt="" height="817" src="https://img-blog.csdnimg.cn/67518d6ec1d04b85b2a18c8a88627219.png" width="1200">

###  6.3手机端的wifi代理设置那里去进行相关的配置设置。

 <img alt="" height="1010" src="https://img-blog.csdnimg.cn/3f70cbc114f14edbb09cb638e0fc5363.png" width="500">

###  6.4配置完成

配置完成，会看到一个charles与手机端的连接提示弹窗，选择allo即可。

<img alt="" height="226" src="https://img-blog.csdnimg.cn/5d24754a8a55419182e6f113404afb98.png" width="801">

###  6.5抓包https

由于https协议的特殊性，所以要求电脑端和手机端都需要安装下证书，否则会看到返回的数据都是乱码。

>  
 注意：同一个手机对应不同电脑上的Charles都要分别下载证书进行认证，因为手机的证书是和电脑端的Charles一一配对的。 


#### 6.5.1电脑端下载

<img alt="" height="588" src="https://img-blog.csdnimg.cn/7e7200da73264e27a0ab30ebf0abc2a8.png" width="954">

### 6.5.2手机端下载

 浏览器输入：http://www.charlesproxy.com/getssl 

## 7.问题

### 7.1**抓取的包全部出现unknow的解决方法**

<img alt="" height="666" src="https://img-blog.csdnimg.cn/6cb3c17fe4c04295ba1b611b35c52ca2.png" width="831">

###  7.2当前设备不支持安装证书

选择从存储器安装证书，点击 搜索，点击安装即可

## 8.设置

### 8.1模拟慢网速

方法一：点击 上方的乌龟标志，模拟网络延迟；

方法二：点击Proxy——Throttle Settings——勾选Enable Throttling——再勾选Only for selected hosts——点击Add,设置指定的域名——OK；（针对指定的域名模拟弱网）

<img alt="" height="588" src="https://img-blog.csdnimg.cn/a4d1906e4d264c25b6d16204a5392e8b.png" width="924">

### 8.2断点

 在会话列表中找到请求的数据包后，点击右键—Breakpoints,对某个请求数据包进行断点设置（**而不是对整个域名进行断点设置哦**）

#### 8.2.1在charles中对 百度搜索：大熊猫整个请求数据包进行断点设置，如下图

<img alt="" height="775" src="https://img-blog.csdnimg.cn/4d74e850ba484a5491d60e7d36f1880f.png" width="949">

#### 8.2.2在刷新（发送）一次 搜索：大熊猫的请求，charles 对该请求数据包进行了拦截，并修改大熊猫为大雁，再点击Execute 。如下图

 <img alt="" height="681" src="https://img-blog.csdnimg.cn/29f95c5311f34dabad2cd9745b28ecc6.png" width="930">

 **注：（该方式只针对请求数据包的某个<strong>资源进行断点设置，故放行后，服务器返回的数据不会被拦截了**）</strong>


--- 
title:  Windows终端远程管理linux和windows主机 
tags: []
categories: [] 

---
## 一、前言

  Window系统使用rdp远程桌面的方式实现远程登录和管理，linux系统使用shell终端进行登录和管理，这是大家习惯和常用的管理方式。windows使用自带的远程桌面工具管理windows，需要使用第三方终端工具管理linux。那windows能否直接ssh管理linux呢？有没有一个工具既可以远程管理windows又可以远程管理linux的呢？答案马上为你揭晓。

## 二、windows直接远程管理

### 1、windows远程管理windows
-  运行栏输入mstsc.exe后回车，启动远程桌面工具。 <img src="https://img-blog.csdnimg.cn/c8fbf67328a740ebb20d3bc9209e1adf.png" alt="在这里插入图片描述"> -  输入IP地址和用户名后点击连接。 <img src="https://img-blog.csdnimg.cn/4ca9479dfee142fda4a61935a1ca2c23.png" alt="在这里插入图片描述"> -  弹窗后输入账户密码，点击确定完成登录。 <img src="https://img-blog.csdnimg.cn/b1dc54d93d1248a7a99cf514264c96fa.png" alt="在这里插入图片描述"> 
### 2、windows远程管理linux

  windows可以试验powershell连接linux远程主机，其中win10及以上版本的powershell已经自带ssh命令，如果是win7系统则还需要自行安装ssh命令后才可以使用。
- 打开powershell <img src="https://img-blog.csdnimg.cn/e61fa8e8d5874bf2901056e084dc2075.png" alt="在这里插入图片描述">- 使用ssh user@ip:port的命令格式远程连接linux主机，如果是默认的22端口可以省略。如果是首次登陆该主机则会提示是否需要保存主机公钥，选择yes继续完成登录即可。 <img src="https://img-blog.csdnimg.cn/aae53bbcac224049a3921c0074ccc2c2.png" alt="在这里插入图片描述">
### 3、第三方工具远程管理linux终端

  使用第三方工具远程管理linux终端，可以参考。

## 三、FinalShell远程管理

  FinalShell是一款开源免费的运维工具，还是一款国产化软件。FinalShell工具window版本既支持ssh连接管理linux，也支持远程桌面管理windows，一个工具搞定。未来Linux版本也将支持双类型管理。

### 0、FinalShell安装

  登录官网http://www.hostbuf.com/t/988.html选择window版本进行下载，下载完成后双击exe程序按照提示完成安装即可。

### 1、FinalShell远程管理Linux

  FinalShell是一块运维管理工具，既可以管理使用ssh连接管理linux，也可以使用远程桌面管理windows，其中ssh连接管理linux目前linux版本也是支持的，windows版本的使用方式是一样的，可以参考。

### 2、FinalShell远程管理windows

  
- 新建远程桌面连接 <img src="https://img-blog.csdnimg.cn/71bf5344d5754d4bae22d29160848cef.png" alt="在这里插入图片描述">- 配置连接主机信息 <img src="https://img-blog.csdnimg.cn/39817d4dc2864d768091f0fb1625792d.png" alt="在这里插入图片描述">- 双击发起连接 <img src="https://img-blog.csdnimg.cn/56f67099af9d44448a827d2775949ea8.png" alt="在这里插入图片描述">- 远程连接成功 <img src="https://img-blog.csdnimg.cn/a3e1a30132a94f02b34f0c1335676448.png" alt="在这里插入图片描述">
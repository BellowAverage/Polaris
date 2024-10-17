
--- 
title:  Linux之iNodeclient客户端定制和安装 
tags: []
categories: [] 

---
## 一、前言

  因工作需要客户给了一个iNodeclient客户端，通过sslvpn连接到客户测试环境进行系统调测。客户给的是一个window版本，自行从网上找了个linux版本的iNodeclient客户端。近期客户环境进行了版本升级，升级后的iNodeclient客户端连接报错，提示网关参数查询失败导致连接失败。客户联系人反馈他们只有window版本，没有linux版，系统经过开发调试后已经部署测试环境了，而测试环境我们是部署在linux环境下的。为了实现测试环境系统联调测试目的只能我们自己想办法了。iNodeclient是H3C的SSL VPN客户端，这么大公司肯定是有linux版本的，只是客户不知道而已。 <img src="https://img-blog.csdnimg.cn/f9df7dbf40c34b859b8f75e045dcb9c3.png" alt="在这里插入图片描述">

## 二、iNodeManager下载及安装

### 1、知了社区提问

  百度了一番和在H3C官网都没有直接搜索到iNodeclient下载的链接，关于H3C产品不清楚的我们都可以去知了社区提问。 <img src="https://img-blog.csdnimg.cn/18899f5b2e3c4345b36b2dac9537af17.png" alt="在这里插入图片描述">

### 2、H3C官网下载

  知了社区提问后很快就有热心的工程师解答了疑问，还提供了iNode PC客户端下载的连接和账号（H3C有些软件下载需要合作伙伴账户）。打开链接我们发现当前最新版本是iNode 7.3 E0585。 <img src="https://img-blog.csdnimg.cn/749f006f94ba477ebfc756ddc316e8a9.png" alt="在这里插入图片描述">

### 3、下载iNode_PC7.3最新版

  。如果需要下载的网友可以可以私信我哦。点击下载链接，然后输入账号，接受软件许可协议即可下载。 <img src="https://img-blog.csdnimg.cn/347eb3e9ebe6429e8129a16e6c7eaeaa.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ae1b1d9078184981af57db42299be132.png" alt="在这里插入图片描述">

### 4、解压软件包

  解压软件包，里面包括iNodeManager的linux、macOS、windows版本及安装配置手册等。linux版本又包括x86,x64,ARM等不同CPU架构版本。我们将x64版本上传到linux服务器。 <img src="https://img-blog.csdnimg.cn/0258af7e32e642bf88ea96a6fe6878a1.png" alt="在这里插入图片描述">

### 5、解压并添加执行权限

  将软件包解压，修改属主为待安装的用户，然后将目录移动到/home目录下，给install64.sh脚本添加执行权限。

>  
 [root@s146 tmp]# tar -zxvf iNodeManager_H3C_Linux64_7.30(E0585).tar.gz … [root@s146 tmp]# chown -R wuhs.wuhs iNodeManager [root@s146 tmp]# mv iNodeManager /home/ [root@s146 tmp]# cd /home/iNodeManager/ [root@s146 iNodeManager]# chmod u+x install64.sh 


### 6、执行安装脚本

  执行install64.sh脚本，其实安装脚本执行动作很简单就是解压lib64.tar.gz，然后给iNodeManager添加执行权限。

>  
 [root@s146 iNodeManager]# sh install64.sh lib64/ lib64/libQt5DBus.so.5.1.1 lib64/libQt5DBus.so.5.1 lib64/libQt5DBus.so.5 lib64/libicudata.so.51.1 lib64/libicudata.so.51 lib64/libicui18n.so.51.1 lib64/libicui18n.so.51 lib64/libQt5Core.so.5.1.1 lib64/libQt5Core.so.5.1 lib64/libQt5Core.so.5 lib64/libQt5Gui.so.5.1.1 lib64/libQt5Xml.so.5.1.1 lib64/libQt5Xml.so.5.1 lib64/libQt5Xml.so.5 lib64/libicuuc.so.51.1 lib64/libicuuc.so.51 lib64/libQt5Network.so.5 lib64/libQt5Gui.so.5.1 lib64/libQt5Gui.so.5 lib64/libQt5Widgets.so.5.1.1 lib64/libQt5Network.so.5.1.1 lib64/libQt5Widgets.so.5.1 lib64/libQt5Widgets.so.5 lib64/libQt5Network.so.5.1 


### 7、启动iNodeManager

  进入安装目录启动iNodeManager，界面如下。 <img src="https://img-blog.csdnimg.cn/b979535186534abb8f45180f6459e9a4.png" alt="在这里插入图片描述">

## 三、iNodeClient定制及安装

### 1、客户端定制

  在iNode管理中心，点击客户端定制，勾选SSL VPN，点击高级定制，设置定制版本信息。 <img src="https://img-blog.csdnimg.cn/529e085a153a48e68f400e65dac9c160.png" alt="在这里插入图片描述">

### 2、高级定制

  我们这里使用的是iNodeclient的 SSL VPN功能，点击SSL VPN配置项，添加添加网关，配置网关地址和端口信息，端口默认是443，如果使用的是非默认端口记得修改。当然，除了这些还可以配置连接次数，重连次数，认证方式，超时时间等网关参数信息。 <img src="https://img-blog.csdnimg.cn/238ad7db9a6041428ea4cb56182c0c7a.png" alt="在这里插入图片描述">

### 3、设置定制客户端软件包类型

  弹窗输入定制客户端的版本管理信息，此处纯粹就是定制版本历史信息记录使用，与客户端原始版本没有关系。我们设置生成定制的客户端安装程序，即完成的安装程序。 <img src="https://img-blog.csdnimg.cn/5beece78b0f543e8ba75df862f650479.png" alt="在这里插入图片描述">

### 4、查看定制结果

  定制完成后会弹窗告知客户端软件包存储路径，存储在/home/iNodeManager/iNodeSetup目录下，会生产两个软件包，一个32位的安装包，一个64位的安装包。 <img src="https://img-blog.csdnimg.cn/0d9fe00efff0442fa65c8ac3a76fdba4.png" alt="在这里插入图片描述">

### 5、卸载原版本

  如果是版本更新，我需要先卸载旧的iNodeClient软件包，卸载方式很简单，执行uninstall.sh脚本即可。

>  
 [root@s146 home]# cd /home/iNode/iNodeClient/ [root@s146 iNodeClient]# sh uninstall.sh Stopping AuthenMngService: OK Nothing special for 


### 6、解压并安装

  将iNodeclient软件包上传或者拷贝到/home/iNode目录下，解压后执行安装脚本install_64.sh。

>  
 [root@s146 iNode]# cp /home/iNodeManager/iNodeSetup/iNodeClient_Linux64_7.3\ (E0585).tar.gz ./ [root@s146 iNode]# tar -zxvf iNodeClient_Linux64_7.3\ (E0585).tar.gz iNodeClient/ iNodeClient/iNodeClient.png … [root@s146 iNode]# cd iNodeClient/ [root@s146 iNodeClient]# sh install_64.sh Starting AuthenMngService: OK 


### 7、启动iNodeClient客户端

  通过桌面进入/home/iNode/iNodeClient/.iNode目录，因为iNodeClient是需要依赖图形化界面的，所以如果是新装客户端软件，记得要安装图形化桌面。 <img src="https://img-blog.csdnimg.cn/a8ad0492aac544cd8466e4e9e80c4d86.png" alt="在这里插入图片描述">

### 8、新建连接

  点击新建连接，创建一个SSL VPN协议的连接，因为是定制版本网关参数我们已经不需要填写，下拉选择即可。如果是有多个VPN的，我们定制的时候配置多个，这里下拉选择对应的即可。 <img src="https://img-blog.csdnimg.cn/5f69591faf0f4e018af6008ba590a80e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/4a88d6c9cdea4dbab02a7d7ccdc34555.png" alt="在这里插入图片描述">

### 9、拨号连接

  配置完成后点击向上箭头进行拨号连接，这次没有报错，提示查询网关参数成功，成功获取VPN ip地址，拨号也成功了。 <img src="https://img-blog.csdnimg.cn/51549d09711b4fd6a05fcf23b5ab89be.png" alt="在这里插入图片描述">

## 四、总结
- 遇到软件问题如果百度不到的，最佳的求助方式是就是官网、官方论坛这些官方渠道；- 办法总比困难多，只要你愿意去尝试一定可以解决问题的；- 愿意分享，愿意帮助他人的人很多，社会还是好人多。
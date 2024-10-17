
--- 
title:  爬虫免费Charles使用教程 
tags: []
categories: [] 

---
爬虫免费Charles使用教程

### 一、Charles破解

下载安装及破解方法：

1.下载charles并安装 

2.安装后先打开Charles一次（Windows版可以忽略此步骤）

3.下载破解文件 charles.jar 网盘下载地址](https://pan.baidu.com/s/1Pub5dVrNVRr6tW1-nuyeUA#list/path=/)

4.替换掉原文件夹里的charles.jar Windows替换路径: C:\Program Files\Charles\lib\charles.jar Mac替换路径: /Applications/Charles.app/Contents/Java/charles.jar

### 二、配置电脑

在电脑上，我们首先需要安装证书，点击help，如图：

<img src="https://img-blog.csdnimg.cn/a9ec42d12e464f3a94760465163f8b48.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/f3f80f106d894c0a92e61db9edc2b8ee.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/325552e6840f4fb7932431315ff4bd91.png" alt="在这里插入图片描述">

### 三、移动设备配置

在移动设备上安装证书，首先点击proxy—&gt;proxy settings…端口修改为8888，如下图所示：

<img src="https://img-blog.csdnimg.cn/bb54c1363b1e44b2964d323025111f7b.png" alt="在这里插入图片描述">

然后我们查看ip地址，这样在手机上才可以添加ip地址和端口号.点击help——local ip addresses，如下图所示：

<img src="https://img-blog.csdnimg.cn/5de6c55fc7ac493382c99034074699e4.png" alt="在这里插入图片描述">

点击手机连接的WIFI，设置手动http代理，设置完成后要检查是否正确

以上设置完成后，就可以捕捉到手机请求啦，连接成功后 打开你要测试的APP，进行刷新动作，然后Charles会弹出确认提示框，这时候选择‘Allow’即可，如下图所示：

<img src="https://img-blog.csdnimg.cn/f05696e9905d4b9cb6bdcc36acccb7fe.png" alt="在这里插入图片描述">

### 四、安装移动设备的证书

这个时候虽然可以抓包了，但是https的还抓取不到，因为上面我们安装的证书是电脑本地的证书，接下来我们安装移动设备的证书。

首先点击help——SSL proxying ——，如下图所示：

<img src="https://img-blog.csdnimg.cn/6fb7f814e0274563b7e66288aa0b5928.png" alt="在这里插入图片描述">

打开手机浏览器，输入下方网址，如下图所示：

<img src="https://img-blog.csdnimg.cn/a23a615f0b0d49338139521a4cfee2a3.png" alt="在这里插入图片描述">

接下来弹出证书安装提示：页面和提示为英文是因为当前设备设置的语言为英文，如下图所示：

<img src="https://img-blog.csdnimg.cn/6990bbfb07b44ca0b4023003de473c61.png" alt="在这里插入图片描述">

选择‘确认’后进行安装 点击‘下载’ ，如下图所示：

<img src="https://img-blog.csdnimg.cn/fae7e6f461894cc9a77608b2df76dedd.png" alt="在这里插入图片描述">

此时已经安装成功，还差最后一步，信任该证书，点击设置——通用——关于——拉到底部——勾选信任该证书

最后一步，启动HTTPS捕捉 点击proxy——SSL proxying settings——设置通配符 * *，如下图所示：

<img src="https://img-blog.csdnimg.cn/776db5c56e364e6795bc4c84e3a84cbf.png" alt="在这里插入图片描述">

通过以上配置，此时手机和电脑设置完毕，我们可以截取https的网络封包。

### 五、使用charles进行抓包

1.看发出的请求

<img src="https://img-blog.csdnimg.cn/b803cff60b094ac3b06f1a1873f098a3.png" alt="在这里插入图片描述">

2.定位问题 server端的问题 客户端的问题 3.能帮咱们模拟一下服务端返回的异常情况 4.拦截请求并修改请求及返回值，通过设置断点来拦截，下面以598同城为例 　4.1 左侧选中bj.58.com，右侧点击response–HTML查看返回结果

<img src="https://img-blog.csdnimg.cn/ceb16acb208a4e58864706a2046c02f3.png" alt="在这里插入图片描述">

4.2将bj.58.com设置为断点，右键“bj.58.com”–“breakpoints”，然后点击垃圾桶，清空请求列表

<img src="https://img-blog.csdnimg.cn/e7b154827f504f0da7aef8537c3a86e4.png" alt="在这里插入图片描述">

4.3刷新58首页，修改请求 <img src="https://img-blog.csdnimg.cn/8a60b8a30dfc48188216033dec9d504e.png" alt="在这里插入图片描述">

4.4修改完后点击“Execute”，这时可修改返回值

<img src="https://img-blog.csdnimg.cn/6c89b73ab5aa492c9b9b5481901c1134.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/64703e00472741dd96d95cdaa037d9c4.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e065903e09404cafa9d64cc1e7014a45.png" alt="在这里插入图片描述">

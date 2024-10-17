
--- 
title:  SRC漏洞挖掘信息收集与挖掘技巧 
tags: []
categories: [] 

---
### **子****收集**

#### **暴力破解**

本地工具，Layer的子域名挖掘机等工具。

优点：能够枚举到很多通过证书查询查不到的子域名。

缺点：速度慢，靠字典。

<img src="https://img-blog.csdnimg.cn/img_convert/1606df9b9d4b3a86bea76e3dc6d47970.jpeg" alt="img">

#### **搜索引擎搜索**

Google、百度、360、bing、搜狗等主流搜索引擎，通过搜索语法进行搜索。

优点：发现域名时往往会同时发现一些敏感的页面。

缺点：收录有限。

<img src="https://img-blog.csdnimg.cn/img_convert/0e1e0b764dcb037a4e6b255b47a05041.jpeg" alt="img">

#### **证书查询**

常用证书查询的站点: censys.io crt.sh 等等。

优点：可以发现暴力破解无法爆破出来的子域，例如：test-xxxxx-xxxx.baidu.com

缺点：收录有限。

<img src="https://img-blog.csdnimg.cn/img_convert/f0ff90244c39ab1c5ca8db18e4559c3d.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/928ab2a83d5b955de6c29e4b982072ed.jpeg" alt="img">

#### **利用IP进行反查域名**

常用的站点:ip138、微步在线 VIRUSTOTAL等等

优点：能够发现很多通过搜索引擎、证书查询、暴力破解都无法发现的子域名。

缺点：微步需要积分进行查询，其他平台相对微步数据不是那么全面。

VIRUSTOTAL查询写了一个小脚本 供大家参考。

<img src="https://img-blog.csdnimg.cn/img_convert/abccdcdc69fc07c7f89dfcf24e67310f.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/a3955535391f39599368e22060c4493b.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/520d2ea07c7fb4c7b55ffa810a799656.jpeg" alt="img">

#### **IP地址块收集**

常用的站点: CNNIC

收集IP地址块对IP地址进行反查域名能够发现很多资产。

<img src="https://img-blog.csdnimg.cn/img_convert/4bb9988ea25143ba7b3d2baa208dbff1.jpeg" alt="img">

#### **主机端口探测**

常用的工具有:nmap、masscan等等

<img src="https://img-blog.csdnimg.cn/img_convert/77f15acfedcff11f3140c127a92c5d42.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/3d61a86710a01a43bcd5868d71627e65.jpeg" alt="img">

#### **微信公众号、**

微信是日常生活中用的最多的软件之一，通过微信公众号、小程序可以获得部分域名或ip地址。

<img src="https://img-blog.csdnimg.cn/img_convert/a3c8ac0237aac8563b147e537c19a4c6.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/139d34853aa381f7bdab25c3c01d852c.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/db4639f16531532a8f04ba19c4ab7275.jpeg" alt="img">

#### **APP收集**

通过对APP流量的抓取也可以获取到部分子域名或者ip。

<img src="https://img-blog.csdnimg.cn/img_convert/b7281bdf6ab86baabf69687d64fbd2c6.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/fe1dce4f00bb466c73608f98980355de.jpeg" alt="img">

#### **其他方面信息收集**

通过百家号、微博、抖音、快手、哔哩哔哩等媒体公众号，可以收集到员工的账号。或是不小心泄露出来的一些web服务。当收集到qq群这种信息时还可以”潜伏”到qq群，qq群文件可能会包含一些敏感的信息。这方面的信息收集能够帮助我们在漏洞利用时构造一些参数值或是进行暴力破解等等。

### **漏洞挖掘小技巧**

#### **F12、查看源文件大法**

<img src="https://img-blog.csdnimg.cn/img_convert/6296f23f2090388cf15541a2fcfd729e.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/6d3d86da67d727f4fb41c1cd94750044.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/f291815959ffbab5e995555dce9b1a58.jpeg" alt="img">

在漏洞挖掘时可以多多查看“源文件”，越来越多的站点使用webpack进行打包会导致接口暴露等信息暴露，看似比较乱的js通过js格式化就能很好的进行阅读发现问题。

F12大法可以发现页面在打开时有没有请求一些接口，访问接口路径构造敏感页面进行漏洞探测。

例如：添加swagger-ui.html 可以访问到swagger服务。如果服务端对swagger-ui.html这个页面进行了限制可以通过/v2/api-docs 来获取API

<img src="https://img-blog.csdnimg.cn/img_convert/9f37d26bc3469a298bc5358dcc35e78d.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/3e713899cd9dabacdc09c25854f334ff.jpeg" alt="img">

<img src="https://img-blog.csdnimg.cn/img_convert/4d254dea6cb3733e8bb58ff47423fe42.jpeg" alt="img">

### **总结**

502943)]

[外链图片转存中…(img-YiMm0sjm-1706757502943)]

[外链图片转存中…(img-SmaUzr8Z-1706757502943)]

### **总结**

>  
 1.挖掘SRC漏洞时，对于子域名的收集至关重要，子域名的多少决定了漏洞的产出。 2.在进行信息收集时尽可能的做到全面，这样能最大限度上获取到子域名。 3.进行漏洞挖掘时要细心，JS中蕴藏着宝藏。 


#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

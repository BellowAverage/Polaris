
--- 
title:  [ 红队知识库 ] 常见防火墙(WAF)拦截页面 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 


测试过程中经常会碰到WAF拦截，经常需要绕WAF，这里收集了一些常见的WAF拦截页面，不全，但基本上够用了。 严禁用于非授权测试，否则后果自负。



#### 文章目录
- - - <ul><li>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


## 一、云WAF

>  
 云WAF主要利用DNS技术，通过移交域名解析权来实现安全防护，用户的请求首先发送到云端节点进行检测，如存在异常请求则进行拦截否则将请求转发至真实服务器。 


### 1、阿里云盾

```
http://aliyunyd.com/

```

<img src="https://img-blog.csdnimg.cn/a281357a5d724346a628e58d02ef8f38.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/fd39f863db2c4514a4b3c6b5d655c913.png" alt="在这里插入图片描述">

### 2、腾讯T-Sec Wb 应用防火墙

```
https://cloud.tencent.com/product/waf

```

<img src="https://img-blog.csdnimg.cn/5f17deae7f52412ea8c51b823802fbd8.png" alt="在这里插入图片描述">

### 3、华为Web应用防火墙 WAF

```
https://www.huaweicloud.com/product/waf.html

```

<img src="https://img-blog.csdnimg.cn/50f5e27be0fd4bcf84bcbbbe657c2ad9.png" alt="在这里插入图片描述">

### 4、安恒云-Web应用防火墙（玄武盾）平台

```
https://www.dbappsecurity.com.cn/product/cloud119.html

```

<img src="https://img-blog.csdnimg.cn/737228a855194f7a9a031d830de2a611.png" alt="在这里插入图片描述">

### 6、百度云应用防火墙 WAF

```
https://cloud.baidu.com/product/waf.html

```

<img src="https://img-blog.csdnimg.cn/d944a339128540d3966ce0c4ec0609aa.png" alt="在这里插入图片描述">

### 7、华为云-云防火墙 CFW

```
https://www.huaweicloud.com/product/cfw.html

```

<img src="https://img-blog.csdnimg.cn/b80004db00e04577ad7de34b0b48b30b.png" alt="在这里插入图片描述">

### 8、安全狗云御WEB应用防护系统

```
https://www.safedog.cn/index/wafIndex.html

```

<img src="https://img-blog.csdnimg.cn/97f66ffb99814566b80404541b0e973f.png" alt="在这里插入图片描述">

### 9、知道创宇-创宇盾Web应用防火墙

```
https://defense.yunaq.com/cyd/

```

<img src="https://img-blog.csdnimg.cn/9ff55cce7a3a49d38bc31eadd9fef2cc.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b5672bc15ff94df1b26bea33a3ff8873.png" alt="在这里插入图片描述">

### 10、F5 分布式云 WAF

```
https://www.f5.com.cn/cloud/products/distributed-cloud-waf

```

<img src="https://img-blog.csdnimg.cn/c6ee65d86aa242b98b2e3bb480be0d83.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/907830b2c2e14a6caf7f468673a6afc5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/404f4a3f552d45b1872371178d704b72.png" alt="在这里插入图片描述">

### 11、奇安信网站卫士

```
https://wangzhan.qianxin.com/

```

<img src="https://img-blog.csdnimg.cn/aea0ab6e713045178d6b5cbbfac85eeb.png" alt="在这里插入图片描述">

### 12、360磐云

```
https://wangzhan.360.cn/panyun

```

<img src="https://img-blog.csdnimg.cn/47eeddad1cba4ff281b58f3fb8e5682f.png" alt="在这里插入图片描述">

### 13、网宿Web应用防火墙

```
https://www.wangsu.com/product/52

```

<img src="https://img-blog.csdnimg.cn/d8351e7b3d794134a9f780a37b334b0c.png" alt="在这里插入图片描述">

### 14、奇安信网神WEB应用安全云防护系统（安域）

```
https://www.qianxin.com/product/detail/pid/400

```

<img src="https://img-blog.csdnimg.cn/a5352977eb7a48f1abf2c94b200566aa.png" alt="在这里插入图片描述">

### 15、腾讯云WAF

<img src="https://img-blog.csdnimg.cn/59fb3e9c86aa4a9987a3f4bd86c51e98.png" alt="在这里插入图片描述">

### 16、腾讯门神

<img src="https://img-blog.csdnimg.cn/6d35346f5de241edbb1f2f975fa749a2.png" alt="在这里插入图片描述">

### 17、绿盟网站云防护

```
https://www.nsfocus.com.cn/html/2020/458_0107/108.html

```

### 18、启明星辰虚拟化WAF

```
https://www.venustech.com.cn/new_type/xnWAF/

```

### 19、深信服云Web应用防火墙云WAF

```
https://www.sangfor.com.cn/product-and-solution/sangfor-security/yun-web

```

### 20、瑞数动态Web应用防火墙（River Safeplus）

```
https://www.riversecurity.com/product-Safeplus.shtml

```

## 二、硬件WAF

>  
 硬件WAF通常部署在Web服务器之前，过滤所有外部访问流量，并对请求包进行解析，通过安全规则库的攻击规则进行匹配，识别异常并进行请求阻断。 常见产品： 


### 1、安恒明御Web应用防火墙

```
https://www.dbappsecurity.com.cn/product/cloud150.html

```

<img src="https://img-blog.csdnimg.cn/2ea76be6dbe74b8e8675c24a41709a8d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/006696fdd5024802b893403599de08d7.png" alt="在这里插入图片描述">

### 2、长亭雷池(SafeLine)下一 代Web应用防火墙

```
https://www.chaitin.cn/zh/safeline

```

<img src="https://img-blog.csdnimg.cn/0bb5eda683054546ade89dc3f6d47225.png" alt="在这里插入图片描述">

### 3、铱迅Web应用防护系统

```
https://www.yxlink.com/index_product_index.html

```

<img src="https://img-blog.csdnimg.cn/c27bd884317444ce9710b4aae6d2b04a.png" alt="在这里插入图片描述">

### 4、绿盟Web应用防护系统

```
https://www.nsfocus.com.cn/html/2019/206_0911/6.html

```

### 5、远江盛邦Web应用防护系统(RayWAF)

```
https://www.webray.com.cn/channel/RayWAF.html

```

### 6、天融信Web应用安全防护系统(TopWAF)

```
https://www.topsec.com.cn/product/25.html

```

### 7、深信服Web应用防火墙WAF

```
https://www.sangfor.com.cn/product-and-solution/sangfor-security/waf

```

### 8、启明天清Web应用安全网关

```
https://www.venustech.com.cn/new_type/Webyyfhq/

```

### 9、E5 Advanced WAF (API安全-新一代WAF)

```
https://www.f5.com.cn/products/security/advanced-waf

```

## 三、软件WAF

>  
 软件WAF安装在需要防护的服务器上，通过监听端口或以Web容器扩展方式进行请求检测和阻断。 


### 1、网站安全狗

```
https://www.safedog.cn/

```

<img src="https://img-blog.csdnimg.cn/36b792725b0e4a46aa3e7a7351a42568.png" alt="在这里插入图片描述">

### 2、云锁

```
https://yunsuo.qianxin.com/

```

<img src="https://img-blog.csdnimg.cn/acc0bf034ec24a078886f44fd6dc1761.png" alt="在这里插入图片描述">

### 3、D盾

```
https://d99net.net/

```

<img src="https://img-blog.csdnimg.cn/154ca0276ed64b65a72f7fc210c8f8d3.png" alt="在这里插入图片描述">

### 4、网防G01

```
https://www.gov110.cn/

```

<img src="https://img-blog.csdnimg.cn/61183bf6e3bc492c856ec7d0480ff15c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/33bb991f404e41ee9a70e9aaf196e2f0.png" alt="在这里插入图片描述">

### 5、护卫神

```
https://www.hws.com/

```

<img src="https://img-blog.csdnimg.cn/56dc2c48bf8147aaa3a93bb23513227c.png" alt="在这里插入图片描述">

### 6、智创

```
https://www.zcnt.com/

```

<img src="https://img-blog.csdnimg.cn/242601bd6fa64a869b9b5b4001e0b05f.png" alt="在这里插入图片描述">

### 7、UPUPW

```
https://www.upupw.net/versions/

```

<img src="https://img-blog.csdnimg.cn/0da75017dd26484b8bee6768158dff0c.png" alt="在这里插入图片描述">

### 8、宝塔网站防火墙

```
https://www.bt.cn/

```

<img src="https://img-blog.csdnimg.cn/b44ecd27371345d0828243c87a67c363.png" alt="在这里插入图片描述">

### 9、360网站卫视

<img src="https://img-blog.csdnimg.cn/9a895acff51c4beaa1d36d414afe7470.png" alt="在这里插入图片描述">

### 10、悬镜

```
https://www.xmirror.cn/

```

### 11、安骑士

```
https://help.aliyun.com/product/28449.html

```

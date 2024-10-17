
--- 
title:  [ 靶场环境片 ] kali-linux采用Docker 搭建 pikachu（特别详细） 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - <ul><li>- - - - - - - - - - - - 


## 一、pikachu介绍

### 1.Pikachu简介

>  
 Pikachu是一个带有漏洞的Web应用系统，在这里包含了常见的web安全漏洞。 如果你是一个Web渗透测试学习人员且正发愁没有合适的靶场进行练习，那么Pikachu可能正合你意。 Pikachu管理工具里面提供了一个简易的xss管理后台,供你测试钓鱼和获取cookie,每类漏洞根据不同的情况又分别设计了不同的子类，在Pikachu平台上为每个漏洞都设计了一些小的场景,点击漏洞页面右上角的"提示"可以查看到帮助信息。 


### 2.Pikachu上的漏洞类型列表

```
Burt Force(暴力破解漏洞)
XSS(跨站脚本漏洞)
CSRF(跨站请求伪造)
SQL-Inject(SQL注入漏洞)
RCE(远程命令/代码执行)
Files Inclusion(文件包含漏洞)
Unsafe file downloads(不安全的文件下载)
Unsafe file uploads(不安全的文件上传)
Over Permisson(越权漏洞)
../../../(目录遍历)
I can see your ABC(敏感信息泄露)
PHP反序列化漏洞
XXE(XML External Entity attack)
不安全的URL重定向
SSRF(Server-Side Request Forgery)
······

```

## 二、windows搭建pikachu



## 三、Docker 搭建 pikachu

### 1.下载pikachu镜像

>  
 利用docker拉取皮卡出镜像 


```
docker pull area39/pikachu

```

<img src="https://img-blog.csdnimg.cn/803a0d7d307f47cdaa7cfdc637131e20.png" alt="在这里插入图片描述">

### 2.遇到拉取慢的情况下可以使用docker的国内镜像加速

>  
 修改 Docker 镜像服务器，即修改 /etc/docker/daemon.json文件。 可供参考：  


### 3.启动pikachu容器

```
docker run -itd -p 80:80 -p 3306:3306 --name pikachu area39/pikachu
简单解释：
-p 80:80 		将本机的80端口映射到容器中的80端口
-p 3306:3306	将本机的3306端口映射到容器中的3306端口

```

<img src="https://img-blog.csdnimg.cn/4813d8829c1849a6a6d6257a572b6c00.png" alt="在这里插入图片描述">

### 4.访问pikachu，验证启动成功

>  
 打开网页 


```
http://10.10.9.215:80/

```

<img src="https://img-blog.csdnimg.cn/832682df00694c35915e399dac76fae2.png" alt="在这里插入图片描述">

### 5.安装/初始化

>  
 点击上图中红色部分 请提前安装“mysql+php+中间件”的环境; 请根据实际环境修改inc/config.inc.php文件里面的参数; 点击“安装/初始化”按钮; 


<img src="https://img-blog.csdnimg.cn/3c15cf2c9ba04c739c68968bbbf314ac.png" alt="在这里插入图片描述">

>  
 直接点击安装/初始化按钮，环境就搭建成功了。 


<img src="https://img-blog.csdnimg.cn/0f64ecd58e9647039fba9d92a73cc468.png" alt="在这里插入图片描述">

>  
 如果初始化失败，很可能是数据库连接不上，需要我们修改pikachu的配置文件 当然也有可能就是缺少环境，需要我们安装各种环境 下面来介绍一个docker修改pikachu配置文件（kali 搭建需要的环境都有） 


## 四、docker修改pikachu配置文件

>  
 只需要根据实际环境修改inc/config.inc.php文件里面的参数 


### 1.进入pikachu容器

>  
 1、查看容器ID 


```
docker ps

```

<img src="https://img-blog.csdnimg.cn/8a703ad67acd43648b4f1728c5187ac8.png" alt="在这里插入图片描述">

>  
 2、进入容器 


```
docker exec -it 容器ID bash

```

<img src="https://img-blog.csdnimg.cn/535d190f35464041a16e5f67fdaa14f3.png" alt="在这里插入图片描述">

### 2.有关数据库的设置

>  
 1、进入inc目录 


```
cd app/inc

```

<img src="https://img-blog.csdnimg.cn/4d8e66f0fd1a40f7b8463ec6589ede08.png" alt="在这里插入图片描述">

>  
 2.打开config.inc.php 


```
vim config.inc.php

```

<img src="https://img-blog.csdnimg.cn/705019a9a47d4453b09a71a9b1af32b1.png" alt="在这里插入图片描述">

>  
 3、设置数据库 进入pikachu容器修改配置文件，连接mysql数据库的密码等设置 我们在配置文件中看到密码处为空，我们设置我们的mysql密码就ok，当然如果你的数据库名字、用户名、端口啥的有过改动那就改成自己的就行了 


<img src="https://img-blog.csdnimg.cn/cc0973bec54749c38f2d0eb047af9ea9.png" alt="在这里插入图片描述">

### 3.有关pkxss配置文件的修改

```
cd app/pkxss/inc 
vim config.inc.php

```

<img src="https://img-blog.csdnimg.cn/7f4faa1382e942e6990dafafc2e3cf15.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/8f079dd86d7c4cb8889fbe65edfb86b8.png" alt="在这里插入图片描述">

### 4.修改完配置文件，重启pikachu容器

```
docker restart 容器ID

```

<img src="https://img-blog.csdnimg.cn/8bb5c1db45284a7db3e8ae1304e5eb59.png" alt="在这里插入图片描述">

## 五、设置pikachu自启动

>  
 这里我搭建靶场环境，我想让他卡机自启动 我只需要在自启动文件中加入启动命令即可 


### 1.法一：直接写入内容

>  
 1、直接执行如下命令 


```
cat &gt; /etc/rc.local &lt;&lt;-'__EOF__'
#!/bin/bash
docker run -itd -p 80:80 -p 3306:3306 area39/pikachu
exit 0
__EOF__

```

>  
 2、加权限等操作 


```
chmod +x /etc/rc.local
systemctl daemon-reload
systemctl enable rc-local

```

<img src="https://img-blog.csdnimg.cn/345ce478d1bf43bbae76279bc947fa69.png" alt="在这里插入图片描述">

### 2.法二：采用vim写入内容

>  
 1、进入/etc/rc.local文件 


```
vim /etc/rc.local

```

<img src="https://img-blog.csdnimg.cn/ad95b9ac118d4c4a85d11190b6dc2815.png" alt="在这里插入图片描述">

>  
 2、写入如下内容 


```
#!/bin/bash
docker run -itd -p 80:80 -p 3306:3306 area39/pikachu
exit 0

```

<img src="https://img-blog.csdnimg.cn/db8fff12873b48eaa246a16a55d74376.png" alt="在这里插入图片描述">

>  
 3、加权限等操作 


```
chmod +x /etc/rc.local
systemctl daemon-reload
systemctl enable rc-local

```

<img src="https://img-blog.csdnimg.cn/a58c3ea0040e4128a0e5d5d3681ceb19.png" alt="在这里插入图片描述">

## 六、相关资源

  


--- 
title:  centos7安装 nacos-server-2.0.3.zip 
tags: []
categories: [] 

---
### centos7安装 nacos-server-2.0.3.zip
1. 下载nacos：  <img src="https://img-blog.csdnimg.cn/535ba31aed1a433e94ce94641ba5265a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">1. 上传至centos7 上，方式很多种，小编用的是 rz -e , 然后解压 <img src="https://img-blog.csdnimg.cn/ddf2cff0ae46473689d6b00ad11228aa.png" alt="在这里插入图片描述">1. 进入 bin 目录
```
cd  nacos/bin

```

<img src="https://img-blog.csdnimg.cn/9d2301f8c1a94081932406653847086d.png" alt="在这里插入图片描述"> 4. 修改 startup.sh：

```
 vim  startup.sh

```

更改java 的安装目录和 export MODE=“standalone” <img src="https://img-blog.csdnimg.cn/bd1c1353033b414ca66ef472e55a09f2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 5. 配置nacos 的数据库连接信息

```
cd  ../conf

```

修改 application.properties 文件

```
vim application.properties

```

<img src="https://img-blog.csdnimg.cn/ee892cb270a74aa5a182cffba89db007.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 请根据自己数据库的情况进行修改, 下面是小编的数据库连接情况

```
# db mysql
spring.datasource.platform=mysql
db.num=1
db.url.0=jdbc:mysql://localhost:3306/xxxx?characterEncoding=utf8&amp;connectTimeout=1000&amp;socketTimeout=3000&amp;autoReconnect=true&amp;useUnicode=true&amp;useSSL=false&amp;serverTimezone=UTC
db.user=root
db.password=password

```
1. 进入 bin 目录，启动程序: ./startup.sh
```
cd ../bin/

```

```
./startup.sh

```

<img src="https://img-blog.csdnimg.cn/890910106afd472781114dd8a39feb87.png" alt="在这里插入图片描述"> 7. 访问 nacos: http://192.168.8.132:8848/nacos/#/ <img src="https://img-blog.csdnimg.cn/7df11a90be4741a682d60241fe4c5aa8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

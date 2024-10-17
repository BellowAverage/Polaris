
--- 
title:  Java 配置log4J2 
tags: []
categories: [] 

---
这个东西很基础，只是记录一下。

## 日志门面

实际工作中，使用Slf4j等日志门面来解决问题，而不是直接导入包。  
- 在Maven里面加入Log4J2的依赖和Slf4j的日志门面- 创建Slf4j配置文件，并调整日志参数- 在类上面加入@Slf4j注解使用logger即可。
## 单独配置

个人认为说的最好的文章是这个： https://www.cnblogs.com/hafiz/p/6170702.html

log4j2的官网为： https://logging.apache.org/log4j/2.x/

### 需要安装需要的log4J2包。官网里面有下载的路径。

或者看我的： https://blog.csdn.net/weixin_45642669/article/details/122148736

### 配置log4j2.xml文件。

说的是：默认路径在： 文件默认路径为log4j2.yaml 或者其他格式 <img src="https://img-blog.csdnimg.cn/e11e2ffaa1e9402798e5608772e0321e.png" alt="在这里插入图片描述"> xml文件这么配置： <img src="https://img-blog.csdnimg.cn/cf8a4da4a4904aa8a7541b0e32102b54.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 就可以打出warn 的日志。

在进程里面加一个logger。 如果使用slf4j的话，直接假如注解即可。 <img src="https://img-blog.csdnimg.cn/d92e98329f79421a8128e88471d92694.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 就可以打印出日志了。

<img src="https://img-blog.csdnimg.cn/0a636ab606d241d38643d7f8fe8eeca8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 代码先跑起来，细节啥的慢慢调吧。

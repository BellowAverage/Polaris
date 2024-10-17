
--- 
title:  Java IDEA MAVEN的配置 
tags: []
categories: [] 

---
前两天配置了一个maven。

他的作用类似于yum，一个依赖包管理程序。 IDEA默认是安装了的，所以直接搜索maven即可。

<img src="https://img-blog.csdnimg.cn/880c421185d44098a44f5a1e1e997c7f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 然后，我测试了一下，发现在cmd下无法运行Maven，会报错JAVA_PATH不存在。 控制面板写入 <img src="https://img-blog.csdnimg.cn/7c21569485744253a24aeb00f0446bc9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 不知道缺啥，都写了： <img src="https://img-blog.csdnimg.cn/55916a6061f74a7b97e9d0b6bdb44142.png" alt="在这里插入图片描述"> path也写了： <img src="https://img-blog.csdnimg.cn/67be8aefc71649819186029853593af2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f5675f7fa9b340c18f5be9920ccf834d.png" alt="在这里插入图片描述"> 于是：还是不好使。

一个小时也搞不定，吐血了。于是关机休息，第二天起来一看：好了。 给大家一个建议：win10需要重启才能配置Maven。

Maven的配置文件在： <img src="https://img-blog.csdnimg.cn/08944ea4bb1a404e8e0b698567033b15.png" alt="在这里插入图片描述"> 这个需要问其他开发人员要XML文件，导入即可。

如果不存在，那么会安装到：<img src="https://img-blog.csdnimg.cn/0270307d55554135bdba3af5bef23beb.png" alt="在这里插入图片描述"> 这个路径里面。

了解。

如果你的电脑里面从来没有过Maven，那么需要执行： <img src="https://img-blog.csdnimg.cn/b68a5b181a3d4bd3a767ab7680903e59.png" alt="在这里插入图片描述"> 系统会安装Maven的依赖环境，完全不需要你关心。 <img src="https://img-blog.csdnimg.cn/1ad56f52de184970aa0b91d087fa6512.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 总的来说，用IDE还是……比较轻松的（吐血）

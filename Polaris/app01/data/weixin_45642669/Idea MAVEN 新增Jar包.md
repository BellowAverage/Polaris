
--- 
title:  Idea MAVEN 新增Jar包 
tags: []
categories: [] 

---
入门Java配置Maven，对我来说有点苦手。花了3个小时搞定了。

第一步，新建一个Maven Java项目。 <img src="https://img-blog.csdnimg.cn/fb0f61c2e75b4d269e4059602ef7fc17.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">Maven项目有一个pom.xml文件。他的作用是：整理依赖关系。 个人用了很多网上的文件配置maven，都不如官方ide提供的pom好用。

给maven改个名字。比如我配个域名啥的都行。 上面是默认的maven仓库啥的，下面是JDK版本。 <img src="https://img-blog.csdnimg.cn/dc70382e323f468aa270ec65c4ccfbde.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 然后去官方文档里面找，我用的是log4J2这个模块举例。 <img src="https://img-blog.csdnimg.cn/e6da572e7204462a946913946d69db99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 把这个依赖写入到pom.xml里面。 <img src="https://img-blog.csdnimg.cn/3716caf7822d4d3fb0d4b39777c9560a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">写入了以后，系统会提示：找不到这个模块，系统无法运行。 这时候，刷新一下依赖： <img src="https://img-blog.csdnimg.cn/e87d41a7798743e8bfcaaa9b42b16b3a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

这样，maven就会自动下载你需要的log4j2了。

查看一下： <img src="https://img-blog.csdnimg.cn/8c92a44149d84d50b4d19153f435ad9b.png" alt="在这里插入图片描述"> 有了。 即可开心的使用这个插件。

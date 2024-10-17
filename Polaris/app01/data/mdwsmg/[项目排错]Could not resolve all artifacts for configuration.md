
--- 
title:  [项目排错]Could not resolve all artifacts for configuration 
tags: []
categories: [] 

---
Could not resolve all artifacts for configuration ：xxxxxx Could not find spring-boot-gradle-plugin-2.1.13.RELEASE.jar

###### 前情提要

git上拉取了一个JavaWeb项目最新的代码，按照惯例刷新一下 <img src="https://img-blog.csdnimg.cn/20210112153734467.png" alt="在这里插入图片描述"> 然后一堆的 Could not find spring-boot-gradle-plugin-2.1.13.RELEASE.jar 诸如此类的“插件找不到”

###### 问题解决

重新下载/更换 Gradle。不一定要如下操作。 <img src="https://img-blog.csdnimg.cn/20210112154113895.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21kd3NtZw==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

PS:会出现这样的情况有很多，我的这种仅供参考

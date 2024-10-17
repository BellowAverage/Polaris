
--- 
title:  java获取项目运行根目录 
tags: []
categories: [] 

---
System.out.println(类名.class.getResource("").getPath());

System.out.println(类名.class.getResource("/").getPath());

**加不加斜杠好像有点差别，如果在tomcate里面运行的话输出的是tomcate里面的项目路径** 



<img src="https://img-blog.csdn.net/20160309124320451?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

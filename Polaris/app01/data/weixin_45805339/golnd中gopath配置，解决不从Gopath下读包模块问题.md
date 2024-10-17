
--- 
title:  golnd中gopath配置，解决不从Gopath下读包模块问题 
tags: []
categories: [] 

---
相信很多初学者，在首次使用goland编辑器时，用gopath管理包模块的时候会遇到这样的问题，特别是从git远程仓库下git pull下来的工程代码，goland上调试的时候会发现，它只会从goroot路径下去寻找包，并不会去Goland配置的gopath路径。 gopath 配置： <img src="https://img-blog.csdnimg.cn/b7cc34549e324b08a6742af7ebc65e8f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6Ziz5YWJX-S9oOWlvQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 明明已经配置了gopath,但是为什么不起作用呢。那是因为用gopath管理包时，需要讲GoModules下Enable Go modules intergration 去掉勾选，这样就OK了 <img src="https://img-blog.csdnimg.cn/aaacde6819e94036841cabbd0b2e81bd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA6Ziz5YWJX-S9oOWlvQ==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

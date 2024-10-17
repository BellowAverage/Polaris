
--- 
title:  [ docker相关知识 ] 删除 docker 拉取的镜像 -- 释放内存 
tags: []
categories: [] 

---
>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - - - <ul><li>- - - - - 


>  
 kali内存满了，释放一下内存 


## 一、查看本地镜像

```
docker image ls

```

<img src="https://img-blog.csdnimg.cn/58820cbdde1540448dee8440a789056b.png" alt="在这里插入图片描述">

## 二、删除本地镜像

```
docker image rm 镜像id
docker image rm be5b3b208cbf

```

<img src="https://img-blog.csdnimg.cn/605981e863dc4372b3e955af6a084f46.png" alt="在这里插入图片描述">

## 三、docker image ls详解

### 1、作用：

```
docker image ls命令用于列出所有映像。

```

### 2、使用方法：

```
docker image ls [选项参数] [REPOSITORY[:TAG]]

```

### 3、参数：

```
--all（简写：-a） 					列出本地所有的镜像 （包含中间镜像层） 
--quiet（简写：-q） 				只展示镜像的ID 
--filter filter（简写：-f） 			根据提供的条件过滤输出 
--digests 							展示镜像的摘要信息 
--no-trunc 						显示完整的镜像信息 
--format string 					使用Go模板打印漂亮的镜像

```

## 四、docker image rm详解

### 1、作用：

```
docker image rm命令用于删除一个或多个镜像。

```

### 2、使用方法：

```
docker image rm [OPTIONS] IMAGE [IMAGE...]

```

### 3、参数：

```
--force（简写：-f） 		强制删除映像（默认：false） 
--no-prune 		 		不要删除未标记的父映像 （默认：false） 

```

## 五、docker image所有命令介绍

```
docker image build 		从Docker文件构建映像 
docker image history 		显示映像的历史记录 
docker image import 		从tarball导入内容以创建文件系统映像 
docker image inspect 		显示一个或多个映像的详细信息 
docker image load 			从tar存档或STDIN加载映像 
docker image ls 			列出映像 
docker image prune 		删除未使用的映像 
docker image pull 			从注册表中拉出映像或存储库 
docker image push 		将映像或存储库推送到注册表 
docker image rm 			删除一个或多个映像 
docker image save 			将一个或多个映像保存到tar存档(默认情况下流式传输到STDOUT) 
docker image tag 			创建引用SOURCE_IMAGE的标签TARGET_IMAGE 

```

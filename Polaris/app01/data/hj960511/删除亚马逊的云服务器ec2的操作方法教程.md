
--- 
title:  删除亚马逊的云服务器ec2的操作方法教程 
tags: []
categories: [] 

---
>  
 本篇文章主要间接如何删除亚马逊服务器的操作和疑难困惑解答 作者：任聪聪 日期：2023年6月2日 


### 疑惑解答

1.亚马逊的服务器只能终止，不能删除，终止后卷（存储、硬盘会自动关闭，如果没有快照不可恢复）

2.终止的服务器会存在你的列表一段时间后自动消失。（大概在3个小时左右） <img src="https://img-blog.csdnimg.cn/cd1312f63aa8438eb898ce4d7ae4af55.png" alt="在这里插入图片描述"> 3.停止服务器是会继续收费的，但是终止服务器是不会再继续收费的。

### 操作指南

步骤一、进入到实例的列表，路径服务找到计算找到ec2，点击正在运行的实例，邮件实例弹出菜单界面。 <img src="https://img-blog.csdnimg.cn/c607243cd2464b4693665f1e252739c8.png" alt="在这里插入图片描述"> 步骤二、点击实例设置，找到更改关闭操作 <img src="https://img-blog.csdnimg.cn/feb2c48f4f624ef4b65447c0f21e9317.png" alt="在这里插入图片描述">

步骤三、选择终止，点击确定即可完成（注意如果是重要的服务器建议先备份数据，不建议直接终止，因为终止了就再也找不回来数据了）

<img src="https://img-blog.csdnimg.cn/7601e0a2aacc41abb26764b80f68bfb9.png" alt="在这里插入图片描述"> end：终止完毕！

<img src="https://img-blog.csdnimg.cn/66d2217cd0f341f1becc3c32108cb415.png" alt="在这里插入图片描述">

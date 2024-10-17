
--- 
title:  1panel中的sftpgo webadmin 更新修改docker容器文件的配置教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解1panel中的sftpgo webadmin 更新修改docker容器文件的配置教程，适合sftpgo webadmin和1panel系统用户配置时使用。 作者：任聪聪 rccblogs.com 日期：2024年1月8日 


sftpgo是无法直接直接更改容器内部的网站目录的，但是可以通过挂载本地目录，配置容器目录实现操作，无论是1panel还是自搭建的docker环境均是这样的思路。

### 配置说明

#### 步骤一、进入面板找到容器，并点击sftpgo webadmin的容器的更多菜单

<img src="https://img-blog.csdnimg.cn/direct/51b49077680140e4a6d2e9a2add71e50.png" alt="在这里插入图片描述">

点击更多找到编辑 <img src="https://img-blog.csdnimg.cn/direct/0f6407b66edf4d1ea1946cd199694fb3.png" alt="在这里插入图片描述">

#### 步骤二、进入到容器编辑界面，添加新的挂载，并设置一个容器目录如下：

<img src="https://img-blog.csdnimg.cn/direct/43edf8ad803e46f1bc23b001ba279e81.png#pic_center" alt="在这里插入图片描述"> 保存并重启这个容器

#### 步骤三、回到sftpgo webadmin管理系统中，使用admin管理员账户登录创建一个test账户如下：

<img src="https://img-blog.csdnimg.cn/direct/56be4b2047774e2abc67f44beea8efa1.png#pic_center" alt="在这里插入图片描述"> 注意：设置的目录可以/www/sites/your website path/。默认就可以直接到这个用户当前的网站目录中了。

最后点击保存，即可完成test用户的创建。

### 使用说明：

这里我们使用的是flashFxp进行的ftp的链接，默认sftpgo的链接端口是2121，配置信息大致如下。 <img src="https://img-blog.csdnimg.cn/direct/d6a1d540f0f44a5aab98eaca10602dce.png" alt="在这里插入图片描述"> 点击连接，如果密码和端口等配置正确，我们将会直接进入到网站的目录中，如下。 <img src="https://img-blog.csdnimg.cn/direct/939a9d30fb6d4b5fa778694867fb083a.png" alt="在这里插入图片描述"> 至此，sftpgo webadmin的目录配置教程完毕~

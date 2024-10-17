
--- 
title:  获取并安装AWS CLI应用程序 
tags: []
categories: [] 

---
## 获取并安装AWS CLI应用程序

### Download and Install AWS CLI Application

#### 1. 获取AWS CLI

##### 1) 访问亚马逊云科技官网链接：



##### 2) 下滑页面，找到下载部分，点击下载CLI安装程序- MSI文件。

<img src="https://img-blog.csdnimg.cn/6fa13c6ac1b74da3b3c383869afd90cb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/58739a3bbe6848f5a88e9a371dc1ad7b.png" alt="在这里插入图片描述">

##### 3) 在Install or update the AWS CLI小节（如上图），点击第1.节的链接，下载AWSCLIV2.msi安装文件；

##### 4) 下载完毕，双击该文件开始安装，如下图：

<img src="https://img-blog.csdnimg.cn/50fafa67a3b94a75a75a96f103bcd504.png" alt="在这里插入图片描述"> 点击**Next**进入下一步。

<img src="https://img-blog.csdnimg.cn/f6436a100cf945ce9acadcd10225f715.png" alt="在这里插入图片描述"> 勾选**I accept the terms in the License Agreement**, 并点击**Next**进行下一步。 <img src="https://img-blog.csdnimg.cn/b26a131547314d7ea07d9466701aa1b0.png" alt="在这里插入图片描述"> 按默认选项，点击**Next**进行下一步。 <img src="https://img-blog.csdnimg.cn/aaad48872261428eaa019d934f0beb22.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0357b1d5b661407fb3710eaebf5e4c69.png" alt="在这里插入图片描述"> 点击**Finish**完成安装。

##### 5) 如果不使用安装向导，也可以使用msiexec命令来完成安装：

```
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi 

```

##### 6) 安装结束，可验证安装完毕的CLI版本

打开**cmd**命令行窗口，输入以下命令：

```
aws --version

```

得到相应版本号，如下图所示： <img src="https://img-blog.csdnimg.cn/e734965951af48a6b415a56be1b57d90.png" alt="在这里插入图片描述"> 至此，AWS CLI应用程序安装完毕，可以直接使用了！

欢迎关注和点赞！技术好文会陆续推出。😊

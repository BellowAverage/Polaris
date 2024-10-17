
--- 
title:  宝塔面板使用Supervisor进程守护插件，配置守护Mysql的操作教程。 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，在宝塔面板中使用Supervisor进程守护插件，配置守护Mysql的操作教程。 作者：任聪聪 日期：2023年11月5日 


## 一、安装守护进程插件

### 安装插件一、进程守护插件

安装说明：在软件商店中搜索“进程守护”，找到如下插件应用并安装 <img src="https://img-blog.csdnimg.cn/d37b094c156d4ae1af0d201b14f490b6.png" alt="在这里插入图片描述">

### 安装插件二、任务管理器

<img src="https://img-blog.csdnimg.cn/c056a8a8d99b4facb5c7d9e8e23cf443.png" alt="在这里插入图片描述">

## 二、配置mysql的进程守护操作

### 步骤一、打开我们安装好的任务管理器，并找到mysql服务。

#### step1：点击设置打开应用

<img src="https://img-blog.csdnimg.cn/d1f2fc1a3f3c441c85aa9cee1ca35f64.png" alt="在这里插入图片描述">

#### step2：找到mysql服务并点击打开

<img src="https://img-blog.csdnimg.cn/22991cd86f65469287c0c96b6fa2f88c.png" alt="在这里插入图片描述">

### 步骤二、点击mysql服务进入到详细的进程页面，并找到启动命令

#### 通过插件的形式找：只需要打开详情页就可以找到启动命令这栏

<img src="https://img-blog.csdnimg.cn/4e0d9a62e5e849338c1284d4462a9f66.png" alt="在这里插入图片描述">

#### 通过ps -aux 查看详细的进程信息，如下图方式：

```
ps -aux

```

<img src="https://img-blog.csdnimg.cn/d0f6dedd95004406baabcfc3c28effa7.png" alt="在这里插入图片描述"> 提示：上述只是一个说明，具体的进程并不是这张图中的，mysql的进程是以mysql开头。这里红框内是系统相关组件的启动命令。

### 步骤三、打开我们的进程守护插件应用

#### step1：点击设置即可打开

<img src="https://img-blog.csdnimg.cn/20b9d8c8074c41559a11e47ebd0b8ff3.png" alt="在这里插入图片描述">

#### step2：点击添加守护进程

<img src="https://img-blog.csdnimg.cn/fcc01260bdae4166b1b2409bb71cd29b.png" alt="在这里插入图片描述">

#### step3：根据信息配置如下表单

<img src="https://img-blog.csdnimg.cn/bb953a537d02483d97f3b528bc960a29.png" alt="在这里插入图片描述">

#### step4：关闭掉mysql

说明：这里关闭可以通过在软件商店中查找，mysql的服务点击安装，也可以通过命令进行安装，在任务管理器中进行停止，都是可以的。 <img src="https://img-blog.csdnimg.cn/9daa7e2208f24d12bb401608656f8ca3.png" alt="在这里插入图片描述">

#### step5：开启进程守护

<img src="https://img-blog.csdnimg.cn/9870ffc1198f4d749fe9da7d8ab5966c.png" alt="在这里插入图片描述"> 提示：如果mysql服务没有关闭，则不能启动这个进程守护。前置条件一定要满足，无论是redis还是php等其他服务，都需要先关闭在这里进行启动。

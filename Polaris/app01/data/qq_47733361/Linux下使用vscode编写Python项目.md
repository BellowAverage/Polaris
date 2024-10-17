
--- 
title:  Linux下使用vscode编写Python项目 
tags: []
categories: [] 

---
我此处是使用VScode远程连接的服务器，具体方法可看如下：

### 1、vscode中安装Python插件

<img src="https://img-blog.csdnimg.cn/99406357f6804ccd89cf7680d1e4024f.png" alt="在这里插入图片描述"> 按上面步骤安装好Python插件后，重启vscode；

### 2、选择Python解释器

创建Python项目结构： <img src="https://img-blog.csdnimg.cn/289d0a32f0074628809fd1f560c89e77.png" alt="在这里插入图片描述"> 按下F1，打开vscode命令栏： <img src="https://img-blog.csdnimg.cn/6c7dfda3089642dd8ce3cee0115d023e.png" alt="在这里插入图片描述"> 输入：Python:Select Interpreter 选择解释器 <img src="https://img-blog.csdnimg.cn/6f6c7addf23f4a6ba1fb5fbe0dc8196b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6103e423a4434bad85ebe9cd27a97c17.png" alt="在这里插入图片描述">

### 3、运行Python代码

**首先编写代码：** 经典哦！！！

```
print("Hello World!")

```

**运行：** 点击右上角小三角，点击在专用终端中运行Python文件： <img src="https://img-blog.csdnimg.cn/8efaee85e13f4fb0ad52cdb3d4a3f117.png" alt="在这里插入图片描述"> 输出Hello World！成功！！！！

### 4、创建项目独有虚拟环境

虚拟环境可以隔离项目所需的依赖库，从而避免全局安装和权限问题。 

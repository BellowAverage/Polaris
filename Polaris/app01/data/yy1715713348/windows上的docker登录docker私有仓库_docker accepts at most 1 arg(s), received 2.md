
--- 
title:  windows上的docker登录docker私有仓库_docker accepts at most 1 arg(s), received 2 
tags: []
categories: [] 

---
##### 设置私有仓库

双击打开docker的desktop程序，进入到设置

<img src="https://img-blog.csdnimg.cn/2021020715270784.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L29vcHhpYWp1bjIwMTE=,size_16,color_FFFFFF,t_70" alt="">

选择 docker 引擎（Docker Engine）

<img src="https://img-blog.csdnimg.cn/20210207152334183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L29vcHhpYWp1bjIwMTE=,size_16,color_FFFFFF,t_70" alt=""> 添加 设置 私有仓库地址 registry-mirrors 和 insecure-registries

我的私有仓库地址为 192.168.100.48（我的端口默认为80，有些私有仓库在搭建时设置的是5000，注意端口）

```
{
  "registry-mirrors": ["http://192.168.100.48"],
  "insecure-registries": ["192.168.100.48"],
  "debug": false,
  "experimental": false
}

```

记得要重启docker（点下那个 “Allpy&amp;Restart”按钮）

##### 命令登录

```
docker login 192.168.100.48 -u admin -p 123456

WARNING! Using --password via the CLI is insecure. Use --password-stdin.

```

结果报错：使用标准密码输入方式才能登录

我以为是这种？？？？？

```
docker login 192.168.100.48 -u admin --password-stdin 123456

accepts at most 1 arg(s), received 2

```

还是不对，

我只能 docker login --help 了

```
docker login --help
Log in to a Docker registry or cloud backend.
If no registry server is specified, the default is defined by the daemon.

Usage:
  docker login [OPTIONS] [SERVER] [flags]
  docker login [command]

Available Commands:
  azure       Log in to azure

Flags:
  -h, --help              Help for login
  -p, --password string   password
      --password-stdin    Take the password from stdin
  -u, --username string   username

Global Flags:
      --config DIRECTORY   Location of the client config files DIRECTORY (default "C:\\Users\\Administrator\\.docker")
  -c, --context string     context
  -D, --debug              Enable debug output in the logs
  -H, --host string        Daemon socket(s) to connect to

Use "docker login [command] --help" for more information about a command.

```

要以非交互方式运行docker login命令，可以将 --password-stdin标志设置为通过STDIN提供密码。使用STDIN可以防止密码出现在shell的历史记录或日志文件中。

“非交互方式运行docker login命令 ” 什么鬼东西？？ 文件方式？(想想shell的.sh 文件，在文件中写执行命令，然后运行.sh 文件)

然我就大胆地尝试了一把

```
echo "123456"|docker login 192.168.100.48 -u admin --password-stdin
Login Succeeded

```

当然 你也可以把密码 单独用文件保存（pwd.txt中只写密码信息 123456）

```
docker login 192.168.100.48 -u admin --password-stdin &lt; ~/pwd.txt 

```

成功！

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

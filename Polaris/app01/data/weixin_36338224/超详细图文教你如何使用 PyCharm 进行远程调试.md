
--- 
title:  超详细图文教你如何使用 PyCharm 进行远程调试 
tags: []
categories: [] 

---
推荐阅读：

这一篇文章是以前的文章，有的朋友已经看过，但是没有关系，因为这次我准备介绍这几大调试工具都是如何调试，又该如何选择。

一般情况下，我们开发调试都是在个人PC上完成，遇到问题，开一下 `Pycharm` 的调试器，很快就能找到问题所在。

可有些时候，项目代码的运行会对运行环境有依赖，必须在部署了相关依赖组件的服务器上才可以运行，这就直接导致了我们不能在本地进行调试。

对于这种特殊的场景，就我所知，有如下两种解决方案：
- pdb- Remote Debug
本篇文章会先讲第二种方案，它是 `专业版Pycharm` 才开放的功能，需要你安装专业版的Pycharm，具体升级破解步骤，请自行 Google，这里不涉及。

远程调试的意思，是让我们可以在我们在 PC 上用 Pycharm 的图形化界面来进行调试代码，它和本地调试没有太大的区别，原来怎么调试的现在还是怎么调试。

区别就在于，本地调试不需要事前配置，只要你的代码准备好了，随时可以开始 Debug 。而远程调试需要不少前置步骤，这些设置过程，也是本文的主要内容。

#### 1. 新建一个项目

首先，要在Pycharm中新建一个空的项目，后面我们拉服务器上的项目代码就会放置在这个项目目录下。我这边的名字是 NOVA，你可以自己定义。

<img src="https://img-blog.csdnimg.cn/20201030084901334.png" alt="">

#### 2. 配置连接服务器

Tools -&gt; Deployment -&gt; configuration

<img src="https://img-blog.csdnimg.cn/20201030084901895.png" alt="">

添加一个`Server`
- Name：填你的服务器的IP - Type：设定为SFTP 
<img src="https://img-blog.csdnimg.cn/20201030084902300.png" alt="">

点击`OK`后，进入如下界面，你可以按我的备注，填写信息：
- SFTP host：公网ip- Port：服务器开放的ssh端口- Root path：你要调试的项目代码目录- Username：你登陆服务器所用的用户- Auth type：登陆类型，若用密码登陆的就是Password- Password：选密码登陆后，这边输入你的登陆密码，可以选择保存密码。
这里请注意，要确保你的电脑可以ssh连接到你的服务器，不管是密钥登陆还是密码登陆，如果开启了白名单限制要先解除。

<img src="https://img-blog.csdnimg.cn/20201030084903107.png" alt="">

填写完成后，切换到`Mappings`选项卡，在箭头位置，填写`\`

<img src="https://img-blog.csdnimg.cn/20201030084903730.png" alt="">

以上服务器信息配置，全部正确填写完成后，点击`OK`

接下来，我们要连接远程服务器了。 Tools -&gt; Deployment -&gt; Browse Remote Host

<img src="https://img-blog.csdnimg.cn/20201030084904357.png" alt="">

#### 3. 下载项目代码

如果之前填写的服务器登陆信息准确无误的话，现在就可以看到远程的项目代码。

<img src="https://img-blog.csdnimg.cn/20201030084904864.png" alt="">

选择下载远程代码要本地。

<img src="https://img-blog.csdnimg.cn/20201030084905352.png" alt="">

下载完成提示。

<img src="https://img-blog.csdnimg.cn/20201030084905743.png" alt="">

现在的IDE界面应该是这样子的。

<img src="https://img-blog.csdnimg.cn/20201030084906274.png" alt="">

#### 4. 下载远程解释器

为什么需要这步呢？

远程调试是在远端的服务器上运行的，它除了依赖其他组件之外，还会有一些很多Python依赖包我们本地并没有。

进入 File -&gt; Settings 按图示，添加远程解释器。

<img src="https://img-blog.csdnimg.cn/20201030084906894.png" alt="">

填写远程服务器信息，跟之前的一样，不再赘述。

<img src="https://img-blog.csdnimg.cn/20201030084907342.png" alt="">

点击`OK`后，会自动下载远程解释器。如果你的项目比较大，这个时间可能会比较久，请耐心等待。

#### 5. 添加程序入口

因为我们要在本地DEBUG，所以你一定要知道你的项目的入口程序。如果这个入口程序已经包含在你的项目代码中，那么请略过这一步。

如果没有，就请自己生成入口程序。

比如，我这边的项目，在服务器上是以一个服务运行的。而我们都知道服务的入口是`Service文件`。 `cat /usr/lib/systemd/system/openstack-nova-compute.service`

```
[Unit]
Description=OpenStack Nova Compute Server
After=syslog.target network.target libvirtd.service

[Service]
Environment=LIBGUESTFS_ATTACH_METHOD=appliance
Type=notify
NotifyAccess=all
TimeoutStartSec=0
Restart=always
User=nova
ExecStart=/usr/bin/nova-compute

[Install]
WantedBy=multi-user.target
```

看到那个`ExecStart`没有？那个就是我们程序的入口。 我们只要将其拷贝至我们的Pycharm中，并向远程同步该文件。

<img src="https://img-blog.csdnimg.cn/20201030084907858.png" alt="">

#### 6. 调试前设置

开启代码自动同步，这样，我们对代码的修改Pycharm都能识别，并且为我们提交到远程服务器。

<img src="https://img-blog.csdnimg.cn/20201030084908850.png" alt="">

开启 `Gevent compatible`，如果不开启，在调试过程中，很可能出现无法调试，或者无法追踪/查看变量等问题。

<img src="https://img-blog.csdnimg.cn/20201030084909467.png" alt="">

#### 7. 开始调试代码

在你的程序入口文件处，点击右键，选择Debug即可。

如果你的程序入口，需要引入参数，这是经常有的事，可以的这里配置。

<img src="https://img-blog.csdnimg.cn/20201030084909952.png" alt="">

配置完点击保存即可。

<img src="https://img-blog.csdnimg.cn/20201030084910502.png" alt="">

#### 8. 友情提醒

按照文章的试调试代码，会自动同步代码至远端，千万不要在生产环境使用，一定要在开发环境中使用，否则后果自负。

调试工具给了程序员提供了很大的便利，但还是希望你不要过度依赖。尽量在每次写代码的时候，都追求一次成型，提高自己的编码能力。

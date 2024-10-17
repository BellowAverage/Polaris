
--- 
title:  RabbitMQ安装Erlang安装 windows 
tags: []
categories: [] 

---
        首先可以进入rabbitMQ官网上查看  。

<img alt="" height="361" src="https://img-blog.csdnimg.cn/1d6fa6311d194b00b50ecc07af752389.png" width="858">

 当前RabbitMQ的最新版本是3.10.7，要求Erlang版本最低是24.0，最高是25.0。我们选择安装最新版RabbitMQ也就是3.10.7。

** 一、 下载安装Erlang**

1.  进入到Erlang官网下载  。<img alt="" height="387" src="https://img-blog.csdnimg.cn/056e881f16394651b534d9e6bf043bea.png" width="618">

       我们选择Erlang25.0 windows 64位的安装包，点击下载。

 2. 找到下载的Erlang安装包，右键以管理员身份运行。

<img alt="" height="221" src="https://img-blog.csdnimg.cn/d33ee91448b345dcb6b73f1d22008955.png" width="508">

 按照步骤next , 安装路径，我这里安装到D:\tools_setup下 注意这里的路径**不能包含中文****。**

<img alt="" height="373" src="https://img-blog.csdnimg.cn/51bd41f016ad493fa1b8bfaf650482fc.png" width="496">

 3. 安装完成后配置环境变量

        在系统变量中新建一个ERLANG_HOME的变量名，变量值为上述Erlang的安装路径。

<img alt="" height="478" src="https://img-blog.csdnimg.cn/004719fe26b94e3c9a1c0274aa946aa4.png" width="707">

 4. path中添加环境变量 %ERLANG_HOME%\bin 。

<img alt="" height="384" src="https://img-blog.csdnimg.cn/5e3a219f56ce4e25955b0132c7831884.png" width="1009">

 5. 验证Erlang是否安装成功，打开cmd 输入 erl 。

<img alt="" height="192" src="https://img-blog.csdnimg.cn/a0787bba948d48fcbbf6cb70dba83ff6.png" width="471">

       如果出现如图结果则证明安装成功。

**二、安装RabbitMQ**

1. 进入到RabbitMQ官网下载安装包， 。

      因为我们是最新版本直接从这下载，如果不是最新版本需要找到对应的版本下下载。        <img alt="" height="273" src="https://img-blog.csdnimg.cn/53ae4d58a7ec44d09155323432f6441f.png" width="784">

2. 找到下载的安装包右键以管理员身份运行。

        <img alt="" height="292" src="https://img-blog.csdnimg.cn/d27d792775324dd49d550d132a7f9d55.png" width="499">

选择安装目录，我们的安装目录在 D:\tool_setup,注意这里的目录**不能有中文**。

<img alt="" height="396" src="https://img-blog.csdnimg.cn/096ae6b4d8f946179bbe2a05ecd54227.png" width="498">

 3. 安装完成后，在win菜单下找到 RabbitMQ command prompt。

<img alt="" height="162" src="https://img-blog.csdnimg.cn/25d33728f0d54d48a54b82e1c9260dff.png" width="311">

4. 输入命令，激活rabbitmq的ui界面。

>  
 rabbitmq-plugins.bat enable rabbitmq_management   


<img alt="" height="186" src="https://img-blog.csdnimg.cn/f6b20c5996d2487889f7b7ed1c18d3c0.png" width="857">

 5. 激活完成后，重启rabbitmq。

<img alt="" height="435" src="https://img-blog.csdnimg.cn/2ba75c1eb4f1465c895f5493426f9036.png" width="845">

 6. 重启完成后，验证是否成功，登录到 localhost:15672,出现如下图登录页面即安装成功。

<img alt="" height="208" src="https://img-blog.csdnimg.cn/5f157ce5980046ea9d5fb9fcb1b78f01.png" width="664">



 7.RabbitMQ默认的登录用户和密码为 guest guest 。

<img alt="" height="167" src="https://img-blog.csdnimg.cn/8f313ade1d1c4e1f8eb14f415ab92782.png" width="524">

登录成功后进入到页面，RabbitMQ的安装就算完成。

<img alt="" height="512" src="https://img-blog.csdnimg.cn/cdd383dfb2014770a4c0a90f1617e019.png" width="1200">

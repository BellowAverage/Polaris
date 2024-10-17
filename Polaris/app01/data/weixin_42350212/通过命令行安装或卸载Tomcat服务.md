
--- 
title:  通过命令行安装或卸载Tomcat服务 
tags: []
categories: [] 

---
一、安装Tomcat服务

1.打开命令提示符

方法1： 按住win+R，打开运行，输入cmd，打开命令提示符

方法2：在开始菜单》所有程序》附件》命令提示符



2. 通过命令进入到tomcat安装的的路径下的bin文件夹里，如：D:\app\apache-tomcat-8.5.24-solr-8888\bin

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/04a57e4e8fc2b5f9a8520b3a7350cdb7.png">



3.在命令提示符中输入 cd: D:\app\apache-tomcat-8.5.24-solr-8888\bin 进入到tomcat的bin目录下

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/62cd1720929c5f495043069944da7934.png">

4. 输入安装命令：服务命名为tomcat8080（服务名称可以自己修改）：

service.bat install  tomcat8080

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/9ebbedcd70eb20b2e59b1ef1319bd5bc.png">

服务安装完成之后，去服务列表页面。看一下

<img alt="" height="315" src="https://img-blog.csdnimg.cn/3e1c03fcf7a64a69907e2bc79b5ddee3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_13,color_FFFFFF,t_70,g_se,x_16" width="435">

 

二、卸载服务

1. 打开命令提示符（同上）

2. 进入到tomcat安装的bin目录下(同上)

3. 输入卸载命令：service.bat  remove tomcat8080

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/78529f3d727ffcc3bd88f46c864ba1d5.png">



三、启动服务

1. 打开命令提示符（同上）

2. 进入到tomcat安装的bin目录下(同上)

3. 执行启动服务的bat文件：startup.bat



<img alt="" src="https://img-blog.csdnimg.cn/img_convert/623d55c38b7dceb1fb85d3ed3a70cf0a.png">



四、停止服务

1. 打开命令提示符（同上）

2. 进入到tomcat安装的bin目录下(同上)

3. 执行启动服务的bat文件：shutdown.bat

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d053705d906766adbd45cceadb20e9d6.png">



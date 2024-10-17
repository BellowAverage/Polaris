
--- 
title:  Jenkins之Jenkins2.4在linux环境下安装 
tags: []
categories: [] 

---
## 一、Jenkins简介

  Jenkins是一个自包含的开源自动化服务器，可用于自动化与构建、测试、交付或部署软件相关的各种任务。Jenkins可以通过本机系统包、Docker安装，甚至可以由任何安装了Java Runtime Environment（JRE）的机器独立运行。Jenkins 2.4相比于之前的版本，引入了许多新的功能和改进，以提高开发团队的效率和生产力。Jenkins 2.4的主要特点包括：
- Pipeline as Code：Jenkins 2.4引入了Pipeline插件，允许用户将构建过程定义为可维护的代码，以便更好地管理和版本控制。这使得构建过程更加灵活和可重复，并且可以与其他工具和服务集成。- 增强的用户界面：Jenkins 2.4改进了用户界面，使其更加直观和易于使用。新的界面提供了更多的可视化工具和报告，帮助开发人员更好地理解和分析构建过程中的问题。- 分布式构建：Jenkins 2.4支持分布式构建，允许将构建任务分发到多个代理节点上并行执行。这提高了构建的速度和可伸缩性，并减少了构建队列的等待时间。- 安全增强：Jenkins 2.4引入了更多的安全功能，如基于角色的访问控制和单一登录集成。这些功能可以帮助保护敏感的构建和部署过程，防止未经授权的访问和操作。
  总体而言，Jenkins 2.4是一个功能强大且易于使用的持续集成和持续交付工具，它可以帮助开发团队更好地管理和自动化软件开发过程，提高软件交付的质量和效率。

## 二、环境说明

  从Jenkins 2.357版本开始要求安装java11或者java17，当前Jenkins最新版本为2.414，要求java11以上版本。另外Jenkins在2023年11月16日以后将停止对centos7的支持，博主这里只是进行Jenkins实验，如果是生产环境，建议使用centos8以上。博文实验环境如下：
- 操作系统：centos7.9- JAVA版本：17.0.8- Jenkins版本：2.414
## 三、安装步骤

### 1、下载java17

>  
 [root@s209 opt]# cd /usr/local/ [root@s209 local]# wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz 


### 2、解压软件包

>  
 [root@s209 local]# tar -zxvf jdk-17_linux-x64_bin.tar.gz 


### 3、创建软链接

>  
 [root@s209 local]# ln -s jdk-17.0.8 java 


### 4、配置java环境变量

  配置java17的环境变量，java17并没有jre环境，我们只需要配置java_home即可。配置完成后记得使用source命令使环境变量配置生效。

>  
 [root@s209 local]# cat /etc/profile … export JAVA_HOME=/usr/local/java export CLASSPATH=$JAVA_HOME/lib:$CLASSPATH export PATH=${JAVA_HOME}/bin:$PATH [root@s209 local]# source /etc/profile 


### 5、下载Jenkins镜像源文件

>  
 [root@s209 yum.repos.d]# wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo [root@s209 yum.repos.d]# rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key 


### 6、更新系统

>  
 [root@s209 yum.repos.d]# yum upgrade 


### 7、yum安装Jenkins

>  
 [root@s209 /]# yum install -y jenkins … Installed: jenkins.noarch 0:2.414.1-1.1  Complete! 


### 8、自定义服务端口

  修改JENKINS_PORT服务端口为自定义端口，新版本中是修改/usr/lib/systemd/system/jenkins.service 此文件中的JENKINS_PORT参数，Jenkins2.3以前的历史版本是修改/etc/sysconfig/jenkins中的参数，网上找到的多是修改此处，经博主实验测试修改/etc/sysconfig/jenkins文件无效，但是安装的时候确实会生成此文件，如果有知道原因的博友欢迎留言回复。

>  
 [root@s209 /]# [root@s209 /]# vim /usr/lib/systemd/system/jenkins.service #将如下行中默认的8080修改为自定义的8888端口，修改完成后保存 [root@s209 /]# cat /usr/lib/systemd/system/jenkins.service |grep Environment |grep -v “#” Environment=“JENKINS_HOME=/var/lib/jenkins” Environment=“JENKINS_WEBROOT=%C/jenkins/war” Environment=“JAVA_OPTS=-Djava.awt.headless=true” Environment=“JENKINS_PORT=8888” 


### 9、重新加载系统配置

>  
 [root@s209 /]# systemctl daemon-reload 


### 10、修改java环境变量软链接

  建议修改/etc/alternatives/java软链接方式更新系统java版本，否则启动Jenkins的时候一直报错java环境不匹配。当然除了修改软链接方式，还可以通过环境变量参数指定，修改/usr/lib/systemd/system/jenkins.service文件，增加一行Environment=“JENKINS_JAVA_CMD=/usr/local/java17/bin/java”，后面详细路径为主机的java17环境安装路径。推荐使用方式二，这种方式不影响现有主机的其他服务。

>  
 [root@s209 /]# rm -rf /etc/alternatives/java [root@s209 /]# ln -s /usr/local/java/bin/java /etc/alternatives/java [root@s209 /]# /etc/alternatives/java -version java version “17.0.8” 2023-07-18 LTS Java™ SE Runtime Environment (build 17.0.8+9-LTS-211) Java HotSpot™ 64-Bit Server VM (build 17.0.8+9-LTS-211, mixed mode, sharing) 


### 11、启动Jenkins

>  
 [root@s209 /]# systemctl start jenkins 


### 12、登录系统

  初次登录系统需要输入密码，初始密码文件通过如下方式查找。

>  
 [root@s209 local]# cat /var/lib/jenkins/secrets/initialAdminPassword cf659af39e414ac9919292e9c24f50cb 


### 13、初始化安装插件

  第一次登录会提示插件安装，博主选择了推荐安装后安装内容如下。 <img src="https://img-blog.csdnimg.cn/f09033d9bf8940ed97d7534cfdc05c64.png" alt="在这里插入图片描述">

### 14、创建管理员用户

  Jenkins2.4是支持角色管理的，可以创建多个管理员用户，当然我们也可以选择跳过，使用admin账户继续。 <img src="https://img-blog.csdnimg.cn/d2f9aa1dcd7f4113885ecf817e020a48.png" alt="在这里插入图片描述">

### 15、实例配置

  实例配置实际上就是配置Jenkins的访问URL，选择默认的即可。 <img src="https://img-blog.csdnimg.cn/608809f2a6e540269c37768db1032637.png" alt="在这里插入图片描述">

### 16、Jenkins就绪

  看到如下提示说明Jenkins初始化安装完成，点击开始使用我们就可以正式使用Jenkins服务啦。 <img src="https://img-blog.csdnimg.cn/4f749d1bb5da4d09a2e52b8c5a02c2bd.png" alt="在这里插入图片描述">

### 17、登录界面

  如下就是第一次登录之后的界面。 <img src="https://img-blog.csdnimg.cn/8623e1fa807940d9ba2d002dfdf60305.png" alt="在这里插入图片描述">

### 18、正式登录

  退出后重新登录Jenkins，登录界面如下。这个时候我们需要输入用户名和密码登录，用户名默认只有admin，密码为初始 <img src="https://img-blog.csdnimg.cn/5f1b02fc30c243acad23d6f7f908e67c.png" alt="在这里插入图片描述">

## 四、QA

### 1、启动报错无效的java环境
- 报错信息：jenkins: invalid Java version: openjdk version “1.8.0_181”- 报错原因：java环境版本不匹配当前Jenkins版本- 解决方案：修改/etc/rc.d/init.d/jenkins中的candidates参数，增加java17路径，也无效。删除/etc/alternatives/java软链接，将软链接指向java17安装路径，步骤详细参考安装步骤章节第10步。
### 2、无法启动Jenkins
- 报错信息：jenkins.service: main process exited, code=exited, status=1/FAILURE <img src="https://img-blog.csdnimg.cn/1c4f87ce75f34bb3a2279736ed7e4789.png" alt="在这里插入图片描述">- 报错原因：服务端口被占用，博文实验主机上8080端口已经开启了其他服务，博主自定义服务端口修改的/etc/sysconfig/jenkins文件，无效- 解决方案：参照安装步骤章节第8步，自定义服务端口。
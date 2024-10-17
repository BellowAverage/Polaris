
--- 
title:  linux搭建SVN教程 
tags: []
categories: [] 

---
#### 系统环境

Linux CentOS6.6

SVN 1.8

#### SVN版本源切换

这里我们选择安装svn1.7以上的版本，由于svn版本低于1.7时可能会跟svn客户端的版本有冲突，所以为了能够更好的兼容版本问题，最好选择高于svn1.7的版本。

可以使用 yum list | grep subversion命令查看当前的版本。我们服务器中默认的svn版本是低于1.7的，因此就需要自己修改svn源码库（我自己在网上找了一个源码库 svn1.8版本的）。

>  
 cd /etc/yum.repos.d/ 


新建一个svn源的文件。

>  
 touch wandisco-svn.repo 
 vi wandisco-svn.repo 


将一下的配置复制到文件里

>  
 [WandiscoSVN] 
 name=Wandisco SVN Repo 
 baseurl=http://opensource.wandisco.com/centos/6/svn-1.8/RPMS/$basearch/ 
 enabled=1 
 gpgcheck=0 


配置完成后 使用yum安装就默认都是安装svn1.8的版本了。

#### SVN安装

##### 1. SVN安装

可以先查看服务器是否已安装svn。

>  
  rpm -qa subversion 


如果发现已安装了svn就需要先卸载。

>  
 yum remove subversion 


如果没有安装就直接可以安装。

>  
 yum install subversion 


直接等待服务器进行安装，安装完毕后查看svn版本 。

>  
 rpm -qa subversion 


 <img alt="" height="134" src="https://img-blog.csdnimg.cn/2122fef514644e6e9a623b40b323745c.png" width="639">



##### 2. 创建svn代码库

首先需要先指定svn代码库的路径，我这里的路径为： /var/svn/repository/source

使用 svnadmin create 创建代码库

>  
 svnadmin create /var/svn/repository/source 


创建完成后，进入到source目录下，可以看到以下几个文件：

<img alt="" height="163" src="https://img-blog.csdnimg.cn/574f38ac0cd44b06b097b75c8aa26159.png" width="879">

>  
 README.txt  //这个不用管它 
 conf // 配置文件的目录 
 db //以后svn的仓库数据 
 fomat //只有存储库版本号 
 hooks //svn的钩子，一般做svn自动更新可以使用到 
 locks // svn锁 


##### 3. svn 服务器的配置

进入到conf文件下

>  
 cd conf/ 


查看目录下，有以下几个文件：

<img alt="" height="132" src="https://img-blog.csdnimg.cn/bff605ccf91a49b99241b69be07bfb12.png" width="938">

>  
 authz //权限控制文件 
 passwd //设置账号密码 
 svnserve.conf //svn配置文件 


修改svnserve.conf

>  
 vi svnserve.conf 


>  
 anon-access = read #匿名用户可读，您也可以设置 anon-access = none，不允许匿名用户访问。设置为 none，可以使日志日期正常显示 
 auth-access = write #授权用户可写 
 password-db = passwd #使用哪个文件作为账号文件 
 authz-db = authz #使用哪个文件作为权限文件 
 realm = /var/svn/repository/source #认证空间名，版本库所在目录 


<img alt="" src="https://img-blog.csdnimg.cn/6b84b13389c344fda244b24d9f5ae2c1.png">

##### 4. 添加用户

添加svn用户，编辑passwd文件

>  
 vi passwd 


在[users]下添加 用户名 = 密码 例如 张三 = 123456

<img alt="" height="250" src="https://img-blog.csdnimg.cn/0f0add7c3024425d951a56f3f004a6f5.png" width="655">

##### 5. 设置用户权限

权限的设置在authz文件，进入到authz文件

>  
 vi authz 


在文件最后设置权限，添加以下设置，（注意：在设置权限前 需要有 [/]）

>  
 [/] 
 zhangsan = rw 


rw： 设置为读写权限

r：设置为只读权限

w：设置为可写权限



##### 6. 开启svn和访问

svn配置完成后就可以开启svn服务。

>  
 svnserve -d -r /var/svn/repository/ 


查看是否开启成功

>  
 ps -ef | grep svn 


开启完成后客户端使用ip访问

svn://IP

如果需要域名访问话需要在Apache或者是nginx的host配置中进行配置。

我这里使用的是apache,具体配置如下：

>  
    &lt;VirtualHost *:80&gt;            ServerName 域名            &lt;Location /&gt;            DAV svn            SVNPath /var/svn/repository/source            AuthType Basic           AuthName "Authorization Realm"           #AuthUserFile /var/svn/user  //配置用户列表，我把用户从conf中提取出来了，可先注释           AuthzSVNAccessFile /var/svn/repository/source/conf/authz                   Require valid-user           &lt;/Location&gt;           ErrorLog "错误日志文件路径"           CustomLog "访问日志文件路径" common   &lt;/VirtualHost&gt;<img alt="" height="377" src="https://img-blog.csdnimg.cn/e6b83c4b8f6e424c9d4912b1c8a940d7.png" width="737"> 


配置完成后需要重启svn 和apache,才能使用域名访问。

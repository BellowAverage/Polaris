
--- 
title:  CentOS 7 服务器配置篇(二):Mysql 8.0的安装 
tags: []
categories: [] 

---
1.去官网下载linux版本的MySql数据库()

     centOS 是基于 红帽的，所以按图示选择

     <img alt="" class="has" height="409" src="https://img-blog.csdnimg.cn/20190510142710651.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="724">

2.通过XShell上传Mysql压缩安装包

   执行  rz (如果报错，请看 )

3.查看 文件是否上传成功

<img alt="" class="has" height="50" src="https://img-blog.csdnimg.cn/20190510181945735.PNG" width="625">

4.解压  tar -xvf mysql-8.0.16-2.el7.x86_64.rpm-bundle.tar

<img alt="" class="has" height="275" src="https://img-blog.csdnimg.cn/2019051018204068.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="661">

5.1 .执行 ** rpm -ivh **mysql-community-common-8.0.16-2.el7.x86_64.rpm** --nodeps --force  **

 <img alt="" class="has" height="101" src="https://img-blog.csdnimg.cn/20190510183000623.PNG" width="775">

**<strong>  common 安装完毕！**</strong>

5.2.执行 **<strong><strong> rpm -ivh mysql-community-libs-8.0.16-2.el7.x86_64.rpm --nodeps --force**</strong></strong>

**<strong><strong>  **</strong></strong><img alt="" class="has" height="81" src="https://img-blog.csdnimg.cn/20190510190811693.PNG" width="763">

如果报错:<img alt="" class="has" height="22" src="https://img-blog.csdnimg.cn/20190510190925693.PNG" width="332">这是因为有多余的空格，请仔细检查，去掉多余的空格即可

**<strong><strong>   ****<strong>libs 安装完毕！**</strong></strong></strong>

**5.3 执行**** rpm -ivh mysql-community-client-8.0.16-2.el7.x86_64.rpm --nodeps --force **

<img alt="" class="has" height="75" src="https://img-blog.csdnimg.cn/20190510185858740.PNG" width="797">

**  客户端 安装成功！**

5.4执行 **<strong><strong><strong><strong><strong><strong> rpm -ivh mysql-community-server-8.0.11-1.el7.x86_64.rpm --nodeps --force**</strong></strong></strong></strong></strong></strong>

<img alt="" class="has" height="81" src="https://img-blog.csdnimg.cn/20190510190001845.PNG" width="787">

**<strong><strong><strong><strong><strong><strong> ****<strong>server 安装成功** </strong></strong></strong></strong></strong></strong></strong>

**<strong><strong><strong><strong><strong><strong>5.5执行<strong> rpm -qa | grep mysql    命令查看 mysql 的安装包**</strong></strong></strong></strong></strong></strong></strong>

 <img alt="" class="has" height="77" src="https://img-blog.csdnimg.cn/20190510191229891.PNG" width="376">

 6**<strong><strong><strong><strong><strong><strong><strong>. 通过以下命令，完成对 mysql 数据库的初始化和相关配置**</strong></strong></strong></strong></strong></strong></strong>

    1）mysqld --initialize;

     如果报错:<img alt="" class="has" height="39" src="https://img-blog.csdnimg.cn/20190510192257564.PNG" width="763">

     解决方法:执行 yum install -y libaio

            <img alt="" class="has" height="417" src="https://img-blog.csdnimg.cn/20190510192530311.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="781">

           <img alt="" class="has" height="324" src="https://img-blog.csdnimg.cn/20190510192609209.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="769">

 2）.chown mysql:mysql /var/lib/mysql -R;

 3)执行: systemctl start mysqld.service;

   如果报错:<img alt="" class="has" height="35" src="https://img-blog.csdnimg.cn/2019051020574747.PNG" width="1082">

    3.1 执行: cat /etc/my.cnf   //查看系统日志

 <img alt="" class="has" height="106" src="https://img-blog.csdnimg.cn/20190510213034835.PNG" width="451">  

   (如果是 #datadir=/var/lib/mysql ，则通过vi 命令将注释 # 去掉)

  3.2 执行: cat /var/log/mysqld.log  //查看错误日志信息

<img alt="" class="has" height="39" src="https://img-blog.csdnimg.cn/20190510210017312.PNG" width="1034">

 （意思就是:里边已有数据了， 这时请删除之前的初始化数据 ，执行:rm -rf /var/lib/mysql/*（就是上边 datadir路径下的文件全删      了），从1)重新执行）

    4）systemctl enable mysqld;

7.  执行  **<strong>cat /var/log/mysqld.log | grep password  //查看数据库密码**</strong>

**<strong> **</strong><img alt="" class="has" height="100" src="https://img-blog.csdnimg.cn/20190510215631746.PNG" width="887">

8. 执行 **<strong> mysql -uroot -p **</strong> //进入数据库登录界面

   password为 刚才查到的密码，即图片 圈出来的

    <img alt="" class="has" height="210" src="https://img-blog.csdnimg.cn/20190510220332967.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="505">

9.执行 **<strong>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '新密码'; //修改密码**</strong>

<img alt="" class="has" height="75" src="https://img-blog.csdnimg.cn/20190510221459831.PNG" width="616">

10.然后执行 exit; 退出数据库，通过新密码重新进入

11.**<strong>通过以下命令，增加用户，进行远程访问的授权**</strong>

**<strong>    1).执行   **</strong>create user '用户名'@'%' identified with mysql_native_password by '密码'; //%的意思是可以通过任何IP访问，如果           你 只想让你某个Ip访问，则直接写指定IP即可

    2).执行  grant all privileges on *.* to '用户名'@'%' with grant option;  //进行授权

<img alt="" class="has" height="429" src="https://img-blog.csdnimg.cn/20200112161959924.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="866">

    3)执行 flush privileges;//刷新保存修改

    4)执行 exit;

    5)执行  mysql -u 刚才新增加的用户名 -p

      password: 为刚才设置的

    6)当需要修改账户密码时:

      执行: update mysql.user set password=password('新密码') where User="用户名" and Host="%";

      执行:flush privileges;

12.新建数据库  CREATE DATABASE 数据库名;

13.列出所有数据库： show databases;

14.打开数据库: use '数据库名';

15.列出所有表: show tables;

16.列出表的结构： describe 表名;

    导入sql文件    source  sql文件的路径

    导出sql文件   mysqldump -u 用户名 -p 数据库名 &gt; 导出的文件名

    导出一个表    mysqldump -u 用户名 -p 数据库名 表名 &gt; 导出的文件名

17.启动数据库  service mysqld status

     <img alt="" class="has" height="36" src="https://img-blog.csdnimg.cn/20190511102730479.PNG" width="366">若出现这个，则按提示执行 /bin/systemctl mysqld.service

   查看Mysql是否启动的   service mysqld status

    <img alt="" class="has" height="203" src="https://img-blog.csdnimg.cn/20190511102911525.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="587">

**<strong> 18.如果想通过本地navicat访问服务器的Mysql,此时，一定要记住设置开放防火墙对应的端口**</strong>

**<strong> **</strong><img alt="" class="has" height="294" src="https://img-blog.csdnimg.cn/2019051023163678.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1140">

19.通过本地navicat访问服务器mysql

<img alt="" class="has" height="510" src="https://img-blog.csdnimg.cn/20190510231820626.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="559">

#### （如有问题，请留言！！！）

## 二、在线安装

>  
 yum/apt-get  install mysql-server 
 <hr> 
 systemctl start mysqld.service 
 <hr> 
 systemctl status mysqld 
 <hr>systemctl enable mysqld​​​​​​​ 
 <hr> 
 #确认MySQL服务正在运行后，需要设置MySQL服务的根密码，这可以通过运行内置的MySQL安全脚本命令来完成 
 mysql_secure_installation 
 首次运行需要是提示输入密码，默认为空，按回车即可。 
 <img alt="" height="342" src="https://img-blog.csdnimg.cn/6fd5624dcbf44ca3a16b62f26a2fb1f5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"> 
 <hr> 
 # 询问是否删除“test”数据库，一般删除即可。 
 <img alt="" height="215" src="https://img-blog.csdnimg.cn/88e1e7d12a144020acd5b392dc45a3eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1014"> 
 <hr> 
  #询问是否刷新权限，键入“y”。 
 <img alt="" height="134" src="https://img-blog.csdnimg.cn/a104752d08d14db98693185744b2ddff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="939"> 
 mysql -u root -p  


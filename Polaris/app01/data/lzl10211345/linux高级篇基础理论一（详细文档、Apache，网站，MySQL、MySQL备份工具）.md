
--- 
title:  linux高级篇基础理论一（详细文档、Apache，网站，MySQL、MySQL备份工具） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的  脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


运维人员辛苦和汗水总结的干货理论希望对你有所帮助

<img alt="" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

**目录**



































### web网站服务

###### 1、Apache的特点

开放源代码、跨平台应用 支持多种网页编程语言 模块化设计，运行稳定，良好的安全性

###### 2、Apache的主要目录和配置文件

主要目录和文件 : 服务目录: /usr/local/httpd 主配置件:/usr/local/httpd/conf/httpd.conf 网页目录:/usr/local/httpd/htdocs 服务脚本:/usr/local/httpd/bin/apachectl 执行程序:/usr/local/httpd/bin/httpd 访问日志: /usr/local/httpd/log/access_log 错误日志: /usr/local/httpd/log/error_log

###### 3、主配置文件说明（httpd.conf）

Listen:监听的IP地址、端口号 User: 运行服务的用户身份 Group: 运行服务的组身份 ServerAdmin:管理员邮箱 ServerName: 网站服务器的域名 DocumentRoot:网页文档的根目录 DirectoryIndex:默认的索引页文件 Include:需要包含进来的其他配置文件

###  web网站服务二

##### 1、httpd服务的常用访问控制方式：

客户机地址限制（限制IP,网段，域名) 用户授权限制（需要输入用户名和密码验证）

##### 2、httpd服务支持的认证方式：

摘要认证(Digest) 基本认证(Basic)

##### 3、httpd支持的虚拟主机类型：

基于域名的虚拟主机 基于IP地址的虚拟主机 基于端口的虚拟主机

### MySQL（linux）

##### 1、MySQL的特点

多线程、多用户 基于C/S(客户端/服务器)架构 单易用、查询速度快 安全可靠

##### 2、mysq1的常用操作：

(1)mysq1的登录 没有密码：mysq1 -u root  有密码：mysq1  -u root (2)修改mysq1用户的密码（系统提示符#下） 没有密码，设置新的密码：mysqladmin -u root password新密码 有密码，修改密码：mysqladmin -u root -p password新密码                              提示输入旧密码 (3)退出mysql控制台 exit (4)查看所有数据库列表 show databases； (5)查看数据库中的表 use  数据库名； show  tables； (6)查看表的结构 describe    表名； (7)创建数据库 create   database    数据库名； (8)创建表 use   数据库名； create    table    表名   （字段1   数据类型， 字段2  数据类型，....）； (9)删除表 use    数据库名 drop   table  表名； (10)删除数据库 drop    database    数据库名；

(11)插入数据的语法 insert  into   表名    （字段1，字段2，....）  values  (‘值1’，‘值2’，...)； （12）查询表中数据 select   *   from    表名      where     条件； （13）更新表中的数据 update    表名    set   列名=‘更新值’    where   条件； （14） 删除表中的数据 delete    from    表名    where   条件； （15）设置用户的权限（用户不存在，则创建新的用户） grant   权限列表    on     数据库名.表名   to   用户名@来源地址   identified   by    ‘密码’；  备注：权限列表：all (所有权限)，select，update，delete，insert 来源地址：localhost （本机）     192.168.1.100（一个主机）     192.168.1.%(代表一个网段)     % （代表所有网段） （16）查看用户的权限： show   grants   for    用户名@来源地址； （17）撤销用户的权限： revoke     权限列表   on     数据库名.表名    from    用户名@来源地址； （18）远程登录MySQL mysql    -u    授权的用户名   [-p]      -h    客户端地址

### **MySQL数据库备份与恢复(linux)**

###### 1、数据库的备份类型

（1）物理与逻辑的角度 物理备份：冷备份、热备份、温备份 逻辑备份：导入和导出 （2）数据库的备份策略角度 完全备份 差异备份 增量备份

###### 2、常见的备份方法：

（1）物理冷备份：主要备份数据文件     tar命令 （2）专用备份工具：逻辑备份     mysqldump     mysqlhotcopy （3）二进制日志：增量备份

###### 3、mysql配置文件说明

主配置：     /etc/my.cnf 数据文件存储位置：  /usr/local/mysql/data 重启服务： systemctl  restart   mysqld 服务端口号： tcp   3306

###### 4、逻辑备份（完整备份）：使用mysqldump来备份

（1）备份： 备份一个表：mysqldump  -u root [-p]  库名  表名1  [表名2]   &gt;   /备份路径/文件名 备份一个库：mysqldump  -u root [-p] --databases  库名1    [库名2]     &gt;   /备份路径/文件名 备份所有库：mysqldump  -u root [-p]  [--opt]   --all-databases  &gt;   /备份路径/文件名 （2）还原： 还原一个表：mysql  -u  root  [-p]   库名   &lt;  /备份路径/文件名 还原一个库：mysql    -u   root   [-p]   &lt;    /备份路径/文件名

###### 5、常用增量恢复的方法：

（1）一般恢复：恢复整个日志文件的所有数据。                              （2）基于位置恢复：可以只恢复日志文件中的部分数据。                （3）基于时间点恢复：可以只恢复日志文件中的部分数据。          

从日志开头截止到某个时间点的恢复： mysqlbinlog [--no-defaults] --stop-datetime=’年-月-日 小时:分钟:秒’ 二进制日志 | mysql -u 用户名 -p 密码 从某个时间点到日志结尾的恢复： mysqlbinlog [--no-defaults] --start-datetime=’年-月-日 小时:分钟:秒’ 二进制日志 | mysql -u 用户名 -p 密码 从某个时间点到某个时间点的恢复： mysqlbinlog [--no-defaults] --start-datetime=’年-月-日 小时:分钟:秒’ --stop-datetime=’年-月-日小时:分钟:秒’ 二进制日志 | mysql -u 用户名 -p 密码

--no-defaults    //#位置选项              --start-datetime       //:时间点选项                             二进制日志文件路径：例：mysql_bak/mysql_bin.000001

备注：日志分为开头和结尾 应用方法分为：     开头到某个时间点     某个时间点到结尾     某个时间点到某个时间点

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 


<img alt="" height="80" src="https://img-blog.csdnimg.cn/99bcd5859d1d4d9db251577b137dc595.gif" width="640">

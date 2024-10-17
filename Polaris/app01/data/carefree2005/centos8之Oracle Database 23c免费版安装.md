
--- 
title:  centos8之Oracle Database 23c免费版安装 
tags: []
categories: [] 

---
## 一、oracle23c简介

  Oracle Database 23c是Oracle Database的下一个长期支持版本。Oracle Database 23c，代号为“App Simple”，加速了Oracle的使命，使开发和运行所有数据驱动的应用程序变得简单。这是Oracle Database 21c创新发布的所有功能加上300多项新功能和增强功能的总和。重点领域包括JSON、图形、微服务和开发人员生产力。Oracle 23c数据库具有以下特点：
- 高性能：Oracle 23c数据库采用了先进的多线程架构和优化技术，可以处理大规模的数据和高并发访问请求，提供快速的数据处理能力。- 高可用性：Oracle 23c数据库提供了多种高可用性解决方案，包括数据复制、故障转移和自动故障恢复等功能，确保数据库的连续性和可靠性。- 安全性：Oracle 23c数据库提供了强大的安全功能，包括身份验证、权限管理、数据加密和审计等，保护数据库中的数据免受未经授权的访问和恶意攻击。- 扩展性：Oracle 23c数据库支持水平和垂直扩展，可以根据需求灵活调整数据库的规模和性能。- 大数据处理：Oracle 23c数据库集成了大数据处理技术，可以与Hadoop和Spark等开源框架无缝集成，实现对大规模数据的分析和处理。
## 二、安装要求及环境说明

  Oracle Database 23c安装要求包括系统要求、swap要求、系统内核参数要求，具体要求如下，其中内核参数可以通过预安装脚本完成设置。博主是在CentOS Stream release 8环境下安装的Oracle Database 23c。
- 系统要求：centos8以上- 内存：最小1G，建议2G以上- SWAP分区：建议2G以上- 系统参数要求 <img src="https://img-blog.csdnimg.cn/direct/5b461eff37a9480786d42af05c2d2e23.png" alt="在这里插入图片描述">
## 三、安装步骤

### 1、安装wget命令

>  
 [root@oracledb opt]# dnf install -y wget 


### 2、下载预安装脚本

>  
 [root@oracledb opt]# wget https://yum.oracle.com/repo/OracleLinux/OL8/developer/x86_64/getPackage/oracle-database-preinstall-23c-1.0-1.el8.x86_64.rpm 


### 3、安装预安装rpm包

  dnf安装预安装rpm包时会安装部分依赖，

>  
 [root@oracledb opt]# dnf -y localinstall oracle-database-preinstall-23c-1.0-1.el8.x86_64.rpm [root@oracledb opt]# /etc/init.d/oracle-database-preinstall-23c-firstboot start Starting oracle-database-preinstall-23c-firstboot (via syst[ OK ] <img src="https://img-blog.csdnimg.cn/direct/16789173738e48019fcb4db1df1b2c07.png" alt="在这里插入图片描述"> 


### 4、下载oracle-free软件rpm包

>  
 [root@oracledb opt]# wget https://download.oracle.com/otn-pub/otn_software/db-free/oracle-database-free-23c-1.0-1.el8.x86_64.rpm 


### 5、执行dnf本地安装

>  
 [root@oracledb opt]# dnf -y localinstall oracle-database-free-23c-1.0-1.el8.x86_64.rpm 


### 6、配置oracle

  执行configure配置时需要设置SYS账户密码，密码复杂度要求大小字母、数字组成，8个字符以上。配置完成后会启动一个实例，会显示实例监听端口，如1539。

>  
 [root@oracledb opt]# /etc/init.d/oracle-free-23c configure Specify a password to be used for database accounts. Oracle recommends that the password entered should be at least 8 characters in length, contain at least 1 uppercase character, 1 lower case character and 1 digit [0-9]. Note that the same password will be used for SYS, SYSTEM and PDBADMIN accounts: Confirm the password: Configuring Oracle Listener. Listener configuration succeeded. Configuring Oracle Database FREE. … Connect to Oracle Database using one of the connect strings: Pluggable database: oracledb:1539/FREEPDB1 Multitenant container database: oracledb:1539 <img src="https://img-blog.csdnimg.cn/direct/68c1a781246f4549a8854aa5e61d08a7.png" alt="在这里插入图片描述"> 


### 7、配置环境变量

>  
 [root@oracledb opt]# echo “export ORACLE_HOME=/opt/oracle/product/23c/dbhomeFree” &gt;&gt; /etc/profile [root@oracledb opt]# echo “export PATH=${ORACLE_HOME}/bin:$PATH” &gt;&gt; /etc/profile [root@oracledb opt]# source /etc/profile 


### 8、连接数据库

>  
 [root@oracledb bin]# ./sqlplus sys/password@localhost:1539 as sysdba <img src="https://img-blog.csdnimg.cn/direct/8b80b2cd1dce4785a88f922fd565d33f.png" alt="在这里插入图片描述"> 


### 9、查看数据库版本

>  
 SQL&gt; select * from V$version; <img src="https://img-blog.csdnimg.cn/direct/3ab307dee5974f878c75193818b9fe25.png" alt="在这里插入图片描述"> 


### 10、查看所有库实例

>  
 SQL&gt; select name From v$database; <img src="https://img-blog.csdnimg.cn/direct/0ca6274a9e464a65ac924560ba1ffefe.png" alt="在这里插入图片描述"> 


## 四、oracle数据库服务启停管理

### 1、停止数据库

>  
 [root@oracledb bin]# /etc/init.d/oracle-free-23c stop Shutting down Oracle Database instance FREE. Oracle Database instance FREE shut down. Stopping Oracle Net Listener. Oracle Net Listener stopped. 


### 2、启动数据库

>  
 [root@oracledb bin]# /etc/init.d/oracle-free-23c start Starting Oracle Net Listener. Oracle Net Listener started. Starting Oracle Database instance FREE. Oracle Database instance FREE started. 


### 3、查看数据库状态

>  
 [root@oracledb bin]# /etc/init.d/oracle-free-23c status Status of the Oracle FREE 23c service:  LISTENER status: RUNNING FREE Database status: RUNNING 


### 4、查看数据库监状态

<img src="https://img-blog.csdnimg.cn/direct/b358bcc07321436e8579840f14deb579.png" alt="在这里插入图片描述">

### 5、重启数据库

>  
 [root@oracledb bin]# /etc/init.d/oracle-free-23c restart 


### 6、使用systemctl管理服务

  我们也可以使用systemctl管理oracle-free-23c服务，如果安装后系统未重启我们需要重载systemctl服务。

>  
 #重载systemctl服务 [root@oracledb bin]# systemctl daemon-reload #停止oracle服务 [root@oracledb bin]# systemctl stop oracle-free-23c #启动oracle服务 [root@oracledb bin]# systemctl start oracle-free-23c #查看oracle服务状态 [root@oracledb bin]# systemctl status oracle-free-23c #重启oracle服务 [root@oracledb bin]# systemctl restart oracle-free-23c #将oracle服务添加到开机自启动 [root@oracledb bin]# systemctl enable oracle-free-23c #取消oracle服务从开机自启动 [root@oracledb bin]# systemctl disable oracle-free-23c 


## 五、Oracle免费版23c的限制策略

  Oracle免费版23c并不是无限制使用的，它对CPU、内存、存储空间大小、实例数量都有限制，详细限制信息如下。

### 1、Oracle数据库可用CPU限制

  Oracle Database Free自动将自己限制为两个核心进行处理。例如，在具有2个双核CPU（4个核心）的计算机上，如果大量数据库客户端试图同时运行CPU密集型查询，则即使有更多的CPU容量，Oracle database Free也将仅以两个核心的速率处理查询。

### 2、Oracle数据库免费安装和运行时限制

  Oracle Database Free将其自身限制为每个逻辑环境只能安装一次。逻辑环境可以是诸如VM或容器之类的虚拟主机，也可以是物理主机。如果您试图在这样的逻辑环境中启动多个Oracle Database Free安装，则会显示ORA-00442：Oracle Database Free单实例冲突错误，并且您的数据库将不会启动。这不会影响Oracle Database Standard Edition 2或Oracle Database Enterprise Edition的任何现有安装或新安装。

### 3、Oracle数据库免费用户数据限制

  Oracle Database Free中的最大用户数据量不能超过12 GB。如果用户数据增长超过此限制，则系统显示ORA-12954：请求超过了允许的最大数据库大小12 GB错误。

### 4、Oracle数据库可用RAM限制

  Oracle Database Free的最大RAM量不能超过2 GB，即使有更多可用RAM。

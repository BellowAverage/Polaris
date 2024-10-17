
--- 
title:  Python使用MySQL数据库 
tags: []
categories: [] 

---
一，安装mysql

 

如果是windows 用户，mysql 的安装非常简单，直接下载安装文件，双击安装文件一步一步进行操作即可。

 

Linux 下的安装可能会更加简单，除了下载安装包进行安装外，一般的linux 仓库中都会有mysql ，我们只需要通过一个命令就可以下载安装：

 

Ubuntu\deepin

 

&gt;&gt;sudo apt-get install mysql-server 

 

&gt;&gt;Sudo apt-get install mysql-client

 

centOS/redhat

 

&gt;&gt;yum install mysql

二，安装MySQL-python

 

要想使python可以操作mysql 就需要MySQL-python驱动，它是python 操作mysql必不可少的模块。

 

下载地址：MySQL-python · PyPI

 

下载MySQL-python-1.2.5.zip 文件之后直接解压。进入MySQL-python-1.2.5目录:

 

&gt;&gt;python setup.py install

三，测试

 

测试非常简单，检查MySQLdb 模块是否可以正常导入。

 

fnngj@fnngj-H24X:~/pyse$ python 

Python 2.7.4 (default, Sep 26 2013, 03:20:56) 

[GCC 4.7.3] on linux2

Type "help", "copyright", "credits" or "license" for more information.

&gt;&gt;&gt; import MySQLdb

没有报错提示MySQLdb模块找不到，说明安装OK ，下面开始使用python 操作数据库之前，我们有必要来回顾一下mysql的基本操作：

 

四，mysql 的基本操作

 

$ mysql -u root -p （有密码时）

 

$ mysql -u root （无密码时）

 

mysql&gt; show databases; // 查看当前所有的数据库

+--------------------+

| Database |

+--------------------+

| information_schema |

| csvt |

| csvt04 |

| mysql |

| performance_schema |

| test |

+--------------------+

6 rows in set (0.18 sec)

 

mysql&gt; use test; //作用与test数据库

Database changed

mysql&gt; show tables; //查看test库下面的表

Empty set (0.00 sec)

 

//创建user表，name 和password 两个字段

mysql&gt; CREATE TABLE user (

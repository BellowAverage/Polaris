
--- 
title:  Linux上修改MySQL字符集为UTF8 
tags: []
categories: [] 

---
### Linux上修改MySQL字符编码为UTF8

开始在linux上装好了MySQL服务，在后期的使用过程中，突然发现在插入记录时，部分字段不能为中文，报错信息如下：

```
mysql&gt; insert into syudent values(1,'陶盼',21);
ERROR 1366 (HY000): Incorrect string value: '\xE9\x99\xB6\xE7\x9B\xBC' for column 'name' at row 1

```

<img src="https://img-blog.csdnimg.cn/514ae1533fbb45eab58bd2aa419b665f.png#pic_center" alt="在这里插入图片描述">

经过我坚持不懈的查找资料，终于解决了该问题。下面给大家分享我的解决方法：

##### 1、数据库中查看MySQL状态：

```
# 查看mysql状态
mysql&gt; status;
mysql&gt; quit;

```

<img src="https://img-blog.csdnimg.cn/2791498b5f1343d19eb9894f4b1cf3c4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

##### 2、修改配置文件：

```
#退出数据库
systemctl stop mysqld.service
#编辑my.cnf配置文件
vim /etc/my.cnf
[client]                   //如果没有[client]段，就自己添加上去
default-character-set=utf8
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci

```

编辑好配置文件后，重启MySQL服务；

```
systemctl start mysqld 

```

重启成功后，重新查询一下mysql的状态，显示如下即可：

```
mysql -u root -p'你的密码'
mysql&gt; status;

```

<img src="https://img-blog.csdnimg.cn/908b45ee5be949ec94a412732932b911.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

这时候进入数据库即可正常插入中包含文字段数据了。

##### 3、若是还没成功，可能是创建mysql时的配置或者刚上一步MySQL没有停止服务编辑 my.cnf 配置文件。

这里我们还需对表和字段设置字符集为utf8；

```
#查看一下表的创建过程
mysql&gt; use ky15;
mysql&gt; show create table syudent;

```

<img src="https://img-blog.csdnimg.cn/8b9a962d6f214ce596f4caf0a97c6386.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
#将表的字符集设置为utf8
mysql&gt; alter table 表名 character set utf8;
#将想要插入中文的字段的字符集改为utf8
mysql&gt; alter table 表名 change name name char(20) character set utf8;
#查看表的字符集和字段的字符集
mysql&gt; show create table syudent;

```

<img src="https://img-blog.csdnimg.cn/b0507381772e4784ac2a441ba77e0c24.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

```
#测试，插入中文
mysql&gt; insert into syudent values(1,'陶盼',21);
mysql&gt; insert into syudent values(2,'王旭',21);
mysql&gt; select * from syudent;

```

<img src="https://img-blog.csdnimg.cn/0adeadb535cd40249a0755e35a183556.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5rKD5bCU56CB,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

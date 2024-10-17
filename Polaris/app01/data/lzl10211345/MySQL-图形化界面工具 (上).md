
--- 
title:  MySQL-图形化界面工具 (上) 
tags: []
categories: [] 

---
>  
  ♥️**作者：小刘在C站** 
  ♥️**个人主页：<strong>**</strong> 
  ♥️**每天分享云计算网络运维课堂笔记，努力不一定有收获，但一定会有收获加油！一起努力，共赴美好人生！** 
  ♥️**树高千尺，落叶归根人生不易，人间真情** 
 

**目录**































### MySQL

MySQL是一个******，**由瑞典 公司开发，属于  旗下产品。MySQL 是最流行的之一，在  应用方面，MySQL是最好的  (Relational Database Management System，) 应用软件之一。

MySQL是一种关系型数据库管理系统，将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

MySQL所使用的 SQL 语言是用于访问数据库的最常用标准化语言。MySQL 软件采用了双授权政策，分为社区版和，由于其体积小、速度快、总体拥有成本低，尤其是这一特点，一般中小型和大型网站的开发都选择 MySQL 作为。



### 主要存在以下两点问题： 



###  **1 ****安装**

### 1). 找到资料中准备好的安装包，双击开始安装 



### <img alt="" height="61" src="https://img-blog.csdnimg.cn/96a208164f3b44feb497491309821da1.png" width="314">

###  2). 点击next，一步一步的完成安装 

<img alt="" height="324" src="https://img-blog.csdnimg.cn/98b539fe3ad74f6389492ee1991db355.png" width="400">

 选择DataGrip的安装目录，然后选择下一步

<img alt="" height="544" src="https://img-blog.csdnimg.cn/87c761f94d0349f1ad17e45212e2b03a.png" width="400">



<img alt="" height="329" src="https://img-blog.csdnimg.cn/db174f3554a54474a977a01961fa8358.png" width="400">

 下一步，执行安装                

<img alt="" height="328" src="https://img-blog.csdnimg.cn/00afbeae9ba74746b57b06cdbc6ff818.png" width="400">



<img alt="" height="328" src="https://img-blog.csdnimg.cn/a422c31690294f578f759c7a13b36b10.png" width="400">

###  **2 使用**

#### 1). 添加数据源

<img alt="" height="300" src="https://img-blog.csdnimg.cn/9b2e8b2a62f1404797df43653e6165eb.png" width="566">

### 2). 展示所有数据库 

###  3). 创建数据库

<img alt="" height="169" src="https://img-blog.csdnimg.cn/94fa0cad7e364500ad96df80e27e3b00.png" width="606">

>  
   注意:  
   
   以下两种方式都可以创建数据库：  
   
   
   A. create database db01;  
   
   
   B. create schema db01; 
   
 

### 4). 创建表 

 <img alt="" height="562" src="https://img-blog.csdnimg.cn/3b7d977c5c4d4c3ebb7511dea216d022.png" width="621">

###  5). 修改表结构 

 <img alt="" height="465" src="https://img-blog.csdnimg.cn/c3a9668a9f87489e8df02a85a5ce8b82.png" width="619">

>  
     如果想增加字段，直接点击+号，录入字段信息，然后点击Execute即可。  
     
     如果想删除字段，直接点击 
     - 
     号，就可以删除字段，然后点击 
     Execute 
     即可。  
     
     
     如果想修改字段，双击对应的字段，修改字段信息，然后点击 
     Execute 
     即可。  
     
     
     如果要修改表名，或表的注释，直接在输入框修改，然后点击 
     Execute 
     即可。 
     
   

### 6). 在DataGrip中执行SQL语句

 然后就可以在打开的Query Console控制台，并在控制台中编写SQL，执行SQL。 

###  **3 DML **

```
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...);
```

```
insert into employee(id,workno,name,gender,age,idcard,entrydate)
values(1,'1','Itcast','男',10,'123456789012345678','2000-01-01');
```

 B. 方式二 

```
insert into employee(id,workno,name,gender,age,idcard,entrydate)
values(1,'1','Itcast','男',-1,'123456789012345678','2000-01-01');
```

###  **2). ****给全部字段添加数据**

```
insert into employee values(2,'2','张无忌','男',18,'123456789012345670','2005-01-
01');
```

```
INSERT INTO 表名 (字段名1, 字段名2, ...) VALUES (值1, 值2, ...), (值1, 值2, ...), (值
1, 值2, ...) ; 
```

```
INSERT INTO 表名 VALUES (值1, 值2, ...), (值1, 值2, ...), (值1, 值2, ...) ;
```

```
insert into employee values(3,'3','韦一笑','男',38,'123456789012345670','2005-01-
01'),(4,'4','赵敏','女',18,'123456789012345670','2005-01-01');
```

>  
              
              注意事项 
              :  
              
              
              •  
              插入数据时，指定的字段顺序需要与值的顺序是一一对应的。  
              
              
               
               •  
               字符串和日期型数据应该包含在引号中。  
               
               
               •  
               插入的数据大小，应该在字段的规定范围内。 
               
               
               ♥️关注，就是我创作的动力 
               ♥️点赞，就是对我最大的认可 
               ♥️这里是小刘，励志用心做好每一篇文章，谢谢大家 
               
              
            

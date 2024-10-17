
--- 
title:  这些mysql基础命令、基础知识还记得吗？（面试，学习，复习都可以）一万三千字总结 
tags: []
categories: [] 

---


#### mysql知识清单【详细】
- <ul><li>- <ul><li>- - - - - - - - - - - - - - - - - - - - - 


### 互联网通信

#### 一、什么是互联网通信

```
两台计算机通过网络进行资源文件共享活动

```

#### 二、互联网通信角色

```
 1.客户端计算机：负责发送请求，索要资源文件
 2.服务端计算机：负责接收请求，对外提供共享资源文件

```

#### 三、通信模型：

1.C/S通信模型： C，client software 客户端软件/客户端应用程序 1) 帮助客户端计算机向指定的服务端计算机发送请求 2) 将服务端计算机返回的二进制数据解析为数字/文字/ 图片/视频 S，server 服务器 1)服务器是安装在服务端计算机中一种软件 2)接收指定客户端发送请求 3)自动定位索要的资源文件 4)将资源文件以二进制形态推送到发起请求的客户端 软件上 2.B/S通信模型： B,browser ，浏览器 1)安装在客户端计算机上一种软件 2)帮助客户端计算机向任意服务端计算机发送请求 3)可以将服务端计算机返回的二进制形态数据解析 数字/文字/图片/视频

S.Http Server，http服务器 1）Http服务器安装在服务端计算机上一种软件 2）自动接收任意浏览器发送的请求 3）自动定位被访问资源文件 4）自动将定位资源文件内容以二进制形式 推送回发起请求的浏览器

#### MySql关系型数据库服务器

#### 一、介绍：

#### 二、名词解释：

```
表文件:
        1.表文件以".frm"结尾文件
        2.表文件以数据行形式存储数据
        3.一个表文件内部有一个标题行和若干个数据行组成
数据库：
        1.专门存放表文件的文件夹而已 
数据库服务器:
        1.数据库服务器就是一个应用程序
        2.应用程序就是一个带有main方法的Java类
        3.数据库服务器启动之后可以24小时不间断工作
        4.可以接收客户端软件发送请求
        5.对指定数据库下表文件进行操作

```

#### 三、数据库服务器分类：

```
1.关系型数据库服务器:

  1)目的:通过读取多张表文件内容向用户展示"一个尽可能【详细】的信息"
  2)特点：
      每次读取信息往往从硬盘上多个表文件读取，因此效率相对较低

```

非关系型数据库服务器:

```
  1)目的：快速将核心信息交给用户
  2)特点：
          采用键值对方式存储数据，数据大多存放在内存中
          执行效率快，但是携带信息量相对较少

```

#### 四、卸载mysql服务器

```
1.关闭mysql服务器
  [开始]---&gt;services.msc---&gt;MySql服务器"停止"

2.使用windows对mysql服务器进行卸载
  控制面板---程序与功能---mysql5.5---&gt;卸载

3.手动将mysql服务器在硬盘上残留文件删除
 
    C:\Program Files (x86)将MySql文件夹删除

4.手动将mysql服务器管理的数据库删除
   C:\ProgramData下MySql文件删除

5.清除注册表中所有mysql信息

  开始---&gt;regedit---&gt;HKEY-LOCAL-MACHINE
                         |
		     |_____ System
		             |
			     |————————&gt;controllSet001
			                 |
					 |————Services
					        |
						|————————&gt;eventLog
						           |——————&gt;Application

```

6.必须重启电脑 |————————&gt;MySql 进行删除

#### 五、基本信息

1.MySql服务器安装地址： C:\Program Files (x86)\MySQL\MySQL Server 5.5 2.MySql服务器管理的数据库位置 C:\ProgramData\MySQL\MySQL Server 5.5\data 3.MySql服务器核心配置文件 C:\Program Files (x86)\MySQL\MySQL Server 5.5\my.ini

#### 六、MySql服务器配置:

```
  1.MySql服务器命令词典:
         C:\Program Files (x86)\MySQL\MySQL Server 5.5\bin
  2.环境变量path配置

```

#### 七、登录：

```
      mysql -uroot -p123

```

#### 八、SQL命令:

```
    1.SQL命令是关系型数据库服务器提供的一种编程语言
2.各个关系型数据库服务器使用SQL命令语法90%一致
3.SQL =Struct Query Language；结构化查询语言
4.SQL命令不区分英文字母大小写  

```

#### 九 SQL命令分类:

```
    1. DDL命令(不许要背)：DataBase Defined Language 数据库维护语言

2. DML命令(常用):     Data Modify Language      数据维护语言

3. DQL命令(重点)：    Data Query  Language      数据查询语言

```

#### 十.DDL命令（不用背）

```
    1.作用:
      1)通知mysql服务器对数据库进行管理
      2)通知mysql服务器对表文件管理
      3)通知mysql服务器对表文件中标题行进行管理

    2.通知mysql服务器对数据库进行管理
      1) show databases; 询问mysql服务器管理的数据库名
      
      2) create database 数据库名; 通知mysql服务器创建一个数据库

      3) drop database 数据库名; 通知mysql服务器删除数据库

   3.通知mysql服务器对表文件管理

          1）查看某个数据库下所有表文件名称

           use 数据库名; 通知mysql服务器接下来的命令对哪个数据库进行操作

	   show tables;

          2)删除某个数据库下表文件
         
	   drop table 表文件名;

          3)在某个数据库服务器下创建一个表文件

           create table 表文件名(
	      字段名  数据类型名,
	      字段名  数据类型名 #最后一个字段不能有逗号
	   );
	   例子:
	   create table student(
	       sid   int,
	       sname varchar(20)
	   );

   4.通知mysql服务器对表文件中标题行进行管理

             1) show create table 表文件名;
	    通知mysql服务器展示表文件基本信息

             2) alter table 表文件名  add 新字段名 数据类型;
	    通知mysql服务器为表文件增加新字段

	    例子: 为student表新增age字段
	    alter table student add age double;
	    例子：为student表新增sex字段
	    alter table student add sex varchar(1);
             
	 3) alter table 表文件名 drop 字段名;
                例子:将student表sex字段进行销毁
	    alter table student drop sex;

             4) 修改字段(名称/数据类型)
	    modify/change----[上网]

```

#### 十一、DML命令

```
  1.介绍:
    对于表文件中数据进行维护(插入数据行/更新数据行/删除数据行)

  2.insert
    1)作用:通知mysql服务器对指定表文件添加一行数据

2)格式: insert into 表(字段名1,字段名2)
        values(值1,'值2');
    3)例子:

       insert into student(sid,sname,age)
       values(10,'mike',22);

       insert into student (sid ,sname)
       values(20,'smith');

    4) 可能遇到错误:

      1) 表文件名写错

          insert into Studnet (sid ,sname)
          values(20,'smith');

	  ERROR 1146 (42S02): Table 'bjpowernode.studnet' doesn't exist

         2) 赋值个数与赋值字段个数不匹配

          insert into Student(sid,sname)
	  values(30,'tom',22)

	  ERROR 1136 (21S01): Column count doesn't match value count at row 1

        3) SQL命令写错

          insert into student(sid,sname)
	  valuse(60,'smith'); 

	  ERROR 1064 (42000): You have an error in your SQL syntax; 
	  check the manual that corresponds to your MySQL server version 
	  for the right syntax to use near 'valuse(60,'smith')' at line 2

	  insert inot student(sid,sname)
	  valuse(60,'smith'); 
	  ERROR 1064 (42000): You have an error in your 
	   SQL syntax; check the manual that corresponds to 
	   your MySQL server version for the right syntax to 
	   use near 'student(sid,sname) valuse(60,'smith')'

  3.insert简化版:
  
       1)格式 : insert into 表文件名  values(值1，值2，值3);

   2)注意: 如果插入的数据行可以对表文件中每一个字段都赋值
           省略赋值字段声明,赋值内容声明顺序必须与表文件
	   字段声明顺序保持一致

       3)例子：
           insert into student values(30,'ford',22);
               QUERY OK

	   insert into student values(40,'allen');
	   Column count doesn't match value count at row 1

   4.Insert批处理插入

       1)格式:  insert into 表名(字段名1,字段名2)
            values
	    (值1，值2),(值1，值2).....;

	    insert into 表名
            values
	    (值1，值2),(值1，值2).....;

       2) 例子:

            insert into student
	    values
	    (40,'king',21),
	    (50,'scott',24),
	    (60,'cuicui',23);
  5.表文件备份

      1) 命令格式:  create table 新表名 select * from 旧表

  2) 命令作用: 将旧表复制一份备份

  3) 例子:  create table student_2 select  * from student;

  6.数据行备份

      1) 命令格式:  insert into 新表 select * from 旧表

  2) 命令作用:  将旧表中数据行复制到新表
                不要求新表中字段名称与旧表中字段名称相同
		要求新表中字段类型与旧表字段类型相同

      3)例子：
                insert into student_3 select * from student;
		ERROR 1146 (42S02): Table 'bjpowernode.student_3' doesn't exist

                    create table student_3(
		   stuSid int,
		   stuSname varchar(20),
		   stuAge int
		);

		insert into student_3 select * from student;

  7.(背-面试常考题)

           create table...select 与 insert into...select

  8.Delete:

     1) 命令格式:

       delete from 表名; #将表文件所有的数据行都删除掉

       delete from 表名 where 判断条件; #要求mysql服务器将满足条件的数据行进行删除

  9.Update

    1) 命令作用：对数据行指定字段信息进行修改

2) 命令格式:

                update 表名 set 字段1='新值',字段2='新值'

	    #要求mysql服务器对表文件中所有数据行字段内容进行修改
	    例子:
	      update student set sid=100,sname='new_stu';


                update 表名 set 字段1='新值',字段2='新值' WHERE 判断条件

	    #将满足条件的数据行指定字段内容进行更新
	     update student_2 set age=age+1  where sid&lt;=30;

```

MySql服务器管理方案

#### 一、存储引擎:

```
1.定义：mysql服务器对表文件进行管理方案

2.存储引擎基本操作:
    
 1)查看当前版本下mysql服务器支持存储引擎
       SHOW ENGINES
     2)默认存储引擎设置
   C:\Program Files (x86)\MySQL\MySQL Server 5.5\my.ini
   default-storage-engine=INNODB
     3)查询表文件依赖的存储引擎
    show  create table  表文件名
     4) 修改表文件依赖的存储引擎
    alter table 表文件名  engine=新存储引擎名
 3. MyIsam 与 InnoDB 区别(稍微关注)

    MyIsam:
        1)将表文件内容分成三个文件存储
	   
	    XXXX.frm---------存放表文件字段信息
	    XXXX.myd---------存放表文件数据行
	    XXXX.myi---------存放表文件索引数据

            2)MyIsam存储引擎为了提供表文件查询操作速度

	3)MyIsam存储引擎管理的表文件存在一个属性用于
	  记录表文件总行数、此时执行SELECT COUNT(*)
	  FROM EMP,直接返回总行数避免全表扫描，提升速度

            4)MyIsam存储引擎管理的表文件中的数据行被修改时(insert/delete/update)
	  是不会生成备份的、用于提供表文件数据修改速度

     InnoDB:

        1) mysql_5.5服务器默认采用的存储引擎就是InnoDB

	2) InnoDB管理的表文件只有一个文件(XXX.frm)、存储
	   字段信息，数据行信息，索引信息

            3) InnoDB保障表文件中数据行安全性、每次在修改表文件
	   数据时，都需要先生成一个备份然后再修改

            4)InnoDB管理表文件不会自动存储总行数、执行
	  SELECT COUNT(*) FROM EMP时，对表文件总行数进行
	  全表扫描

            5) 在MySql5.5服务器中八个存储引擎，只有InnoDB存储
	   引擎支持事务管理

```

#### 二、约束管理方案

```
 1.定义: 管理字段下内容，确保字段下内容都是合法内容

 2.分类:
         1) 非空约束
     2) 唯一性约束
     3) 主键约束
     4) 外键约束
     5) 自定义约束

3.非空约束
         1) 作用：确保字段下内容不会出现null值

     2) 例子：
               CREATE TABLE Student(
	          sid int,#学号
	          sname varchar(50)  not null #学员姓名
	       )

	       insert into Student(sid,sname)
	       values(10,"mike");#ok

	       insert into Student(sid,sname)
	       values(null,"allen");#ok

	        insert into Student(sid,sname)
	       values(30,null);# Column '字段名' cannot be null

```

4.唯一性约束: 1)作用: 要求被管理的字段下内容不能出现重复内容、但是可以 出现多个NULL值

```
       2) 例子:
              CREATE TABLE Student(
	          sid int,#学号
	          sname varchar(50)  not null, #学员姓名
		  email varchar(50)  unique
	       ) 

                   insert into Student(sid,sname,email)
	       values(10,"mike",'mike@163.com');#ok

	       insert into Student(sid,sname,email)
	       values(20,"allen",'mike@163.com');# Duplicate entry '值' for key '字段名'

	       insert into Student(sid,sname,email)
	       values(30,"tom",null);#ok

	         insert into Student(sid,sname,email)
	       values(40,"jones",null);#ok

```

5.主键约束: 1)作用：管理主键字段,要求主键字段内容不能存在NULL值同时 要求主键字段内容不能出现重复值 2)例子：

```
           CREATE TABLE Student(
	          sid int primary key,#学号
	          sname varchar(50)  not null, #学员姓名
		  email varchar(50)  unique
	       ) 

                  insert into Student(sid,sname,email)
	       values(10,"mike",'mike@163.com');#ok

	       insert into Student(sid,sname,email)
	       values(null,"allen",'allen@163.com');#error

	       insert into Student(sid,sname,email)
	       values(10,"smith",'smith@163.com');#error

```

6.外键约束: 1)作用: 外键约束管理多方表中外键字段、要求外键字段内容 只能来自于一方表主键字段下已经存在的值，但是允许 多方表外键字段存在多个NULL值

```
     2) 命令:

             alter table 多方表 add constraint 约束实例对象名 
	 foreign key(多方表外键字段)
	 references  一方表(一方表主键字段)

```

#### 三、auto_increment

```
    1.介绍：
       1)MySql服务器内部提供自增变量
       2)用于降低主键值赋值难度

    2.使用规则:
        1) auto_increment默认值1
	2) 如果插入操作中没有指定主键值，此时mysql
	   服务器自动将auto_increment的值作为本次数据
	   的主键值、在插入结束后auto_increment自动加一

            3) 如果插入操作中指定主键值.本次插入数据的主键值
	   有用户提供、插入完毕后,如果手动指定的主键值大于
               auto_increment，此时auto_increment=主键值+1
	   如果手动指定的主键值小于auto_increment值，插入完毕
	   后auto_increment值不会变化

            4） auto_increment的值只能增加，不能减少、
	    如果执行删除命令，对auto_increment的值没有任何影响
     3.例子:
            create table Student(
	          sid int primary key  auto_increment,
		  sname varchar(20)
	    )

	    insert into Student(sname)
	    values("学生1"); # sid=1  auto_increment=2

	    insert into Student(sname)
	    values("学生2"); # sid=2  auto_increment=3

	    insert into Student(sid,sname)
	    values(10,"学生10"); # sid=10  auto_increment=11


               insert into Student(sname)
	    values("学生11"); # sid=11  auto_increment=12

	    insert into Student(sid,sname)
	    values(5,"学生5"); # sid=5  auto_increment=12

	     insert into Student(sname)
	    values("学生12"); # sid=12  auto_increment=13

	     delete from Student; #auto_increment=13

                 insert into Student(sname)
	    values("学生13"); # sid=13  auto_increment=14

```

#### 四、索引(索引内容都要背住,原因近两年来北京地区面试必考题)

```
1.查询速度逐渐缓慢的原因

   select ename,sal   from emp where sal&lt;=1000
   [where]:现在职员表有14行数据.where循环遍历14次
           才能得到满足条件的数据行
       半年以后，职员表可能140000行数据.where
       where循环遍历14000次
       这条查询语句随着表中数据行增加，运行速度将会越来越慢
       解决方案：SQL优化

2.SQL优化:不改变查询语句业务特征条件下，确保查询语句不会因为
           表文件中数据行增加而大幅度降低运行效率

3.索引介绍:

          1) 索引就是一个数组 【】【】【】
      2) 如果表文件采用MyIsam存储引擎管理、索引存放
         ".myi"文件中、如果表文件采用InnoDB存储引擎.
	 索引存放".frm"文件中
          3) 索引按照升序存放表字段下所有的数据以及数据所在行数

                   Student.frm
               SID       SNAME     AGE
                1         st1       23------0行
	    2         st2       20------1行
	    3         st3       18------2行
	    4         st4       20------3行
	    5         st5       25------4行
	    6         st6       28------5行
              索引  age_index  [18 (2)]   [20 (1,3)]   [23 (0)] [25 (4)] [28 (5)]
          4)  索引帮助查询命令，避免查询命令通过全表扫描的方式得到需要数据行

```

4.索引增加运行效率原因： 1）索引中数据按照升序排列，从有序数据读取最大值或则最小值 运行效率高于从无序数据定位 select max(age)

```
	 age 字段   23  20 18 20 25  28

	 age_index  18  20 23 25 28

          2) 在定位字段中，中间位置的数据时.MySql服务器
         使用BTREE算法在索引中快速定位

```

5.BTREE算法: 1)MySql服务器最开始采用二叉树算法，后来 升级为平衡二叉树算法，到mysql5.0版本开始 使用BTREE算法

```
          2)二叉树算法缺点：
               缺点1：维护过于繁琐,大幅度降低数据行修护速度
	       缺点2: 需要频繁从根节点遍历整棵树

                          【23 ---（0）】

	        【20 (1,3)】          【25 （4）】

           【18 （2）】    【19 ---(6)】           【28  （5）】

        执行时需要在内存形成一个[树].[数]上每一个数据都是真实
	此时对表中数据进行修改（insert/update/delete）.需要
	销毁到内存中树，根据最新数据状态从建一个树

	select * from Student where  age=18  or age =28

	第一次： 23---&gt;20---&gt;[18] 返回数据行位置2

	         23---&gt;25---&gt;[28] 返回数据行位置5

        3)BTREE算法优点:
           
	   优点1：BTREE算法构建树由【节点】和【数据块】组成
	          【节点】中数据都是计算得到数据，也就是说并不是
		   表文件真实的数据、表文件真实数据存放在【数据块】

		                       【 30 】
                          
		            【26】 	              【35】

		    【20】          【 27 】

		【&lt;----------【---------------&gt;【
		  18---2        20---(1,3)      28---(5)
		  19---6        23---(0)
		                25---(4) 
		 】-----------&gt;】&lt;--------------】

              优点2： 数据块以双向链表数据结果连接
	          根据数据升序结果连接，有效避免mysql服务器
		  多次从根节点定位数据

		  select * from Student where  age=18  or age =28

		  [30]--&gt;[26]--&gt;[20]---【18】---&gt;【】--【28】

```

6.索引基本操作：（不用背）:

```
          1) 查看表文件相关字段上是否已经建立了索引

            show index from 表文件

           ***MySql服务器在创建表文件时，如果发现字段存在
          唯一性约束，主键约束，外键约束时 ，自动为
	  字段生成索引

         2)  为指定字段添加索引

                create index sal_index  on emp(sal)
         3)  将指定索引删除
            drop index  索引对象名  on 表

```
<li> 执行计划： <pre><code>      1） 命令  explain  查询语句
</code></pre> </li>
8.执行计划之type属性:

```
         1) 作用： 描述定位数据行方式同时也表示查询语句执行效率

     2) 分类:  根据慢-----快

               type=all: 采用全表扫描方式，定位数据行、是DBA进行优化时
	                 必须避免级别

                   type=index: 采用全表扫描方式，定位数据行、但是定位的数据行
	                   内容来自于索引，因此定位数据行不需要再排序

			    explain select     sal    from emp  order by sal asc  # all
                                create index  sal_index on emp(sal)
                                explain select     sal    from emp                         # index
                   type=range: 通过索引根据区间条件定位、这个查询速度级别是DBA进行优化时
	                   到达最低标准

			    drop  index  sal_index on emp
                                explain   select * from emp where sal &lt;=1000 # all
                                create index  sal_index on emp(sal)
                                explain   select * from emp where sal &lt;=1000 # range

			    range级别及其容易失效
			    explain   select * from emp where sal &lt;=2000 #all
			    ***mysql服务器如果发现从索引得到行数达到了总行数1/3时
			       放弃使用BTREE算法从索引提取数据行位置

                   type=ref   DBA尽可能达到查询速度级别、每次通过索引只能返回一行数据地址
          
               type=const 通过聚合索引每次返回一行内容、是执行速度最快但是难以实现

	                       explain   select * from emp where empno=7369 #const

```

9.聚簇索引与非聚簇索引

```
               非聚簇索引: 关联的字段都是非主键字段，在索引存放数据以及数据所在数据行位置
	                mySql服务器使用BTREE非聚簇索引得到满足条件的数据行位置、这个位置
			交给where之后，where可以根据位置将临时表数据行读取出来

               聚簇索引:   关联的字段是主键字段、一个表文件有且必须存在一个聚簇索引
	                聚簇索引存储主键值以及当前数据行非主键值.
			聚簇索引返回一行完整的数据、此时where直接将数据存入到新临时表
			避免到原有临时表抓取数据步骤

			           [10---Account,New York]  [20---sales,Boston]

```

10.索引失效原因：

```
             1) 如果通过索引返回行数达到总行数1/3时，此时MySql
	    服务器放弃从索引定位数据行位置  

             2) 如果在索引关联的字段上进行数学运算，导致索引失效
	      explain   select * from emp where sal&lt;900 #range
                  explain   select * from emp where sal+100&lt;1000 #all

             3)  如果在索引关联的字段上进行函数处理,导致索引失效
	        explain   select * from emp where ename='smith' #ref
                    explain   select * from emp where upper(ename)='SMITH'#ALL

             4)  如果在索引字段进行隐式数据类型转换，导致索引失效
	        explain select * from emp where ename='100' #ref
                    explain select * from emp where ename=100  #all

             5） 模糊查询：

	        在前置模糊查询中，如果定位总行数小于总行数1/3索引有效
		 explain select * from emp where ename like 's%'  #range

                    后置模糊查询和包含模糊查询都会导致索引失效

             6. 联合索引，如果没有使用第一个索引字段，导致索引失效

	           explain   select * from emp where ename='mike'  and   job='clerk'  and sal=800 #ref
                       explain   select * from emp where    job='clerk'  and sal=800  and ename='mike' #ref
                       explain    select * from emp where   job='clerk' and sal=800
                       explain    select * from emp where   ename='smith'  and sal=800 

```

#### 五、视图(view)

```
 1. 介绍:
        1) MySql服务器提供的一种管理对象，内部结构类似Map
    2) 视图对象key存储一个查询语句 value存放查询语句关联的字段的管理权

                              VIEW对象
                    key                         value
            select empno,ename from emp         Emp表中 empno,ename使用权

 2.命令: 创建 视图
               
             create view  视图实例对象名 as 查询语句

 3. 作用:
            1) 降低查询语句书写难度，增加查询语句复用性
	    create view view_1  as select  empno,ename,job  from emp
                select  *  from view_1

            2) 分配表文件中字段使用权利

	   #借助于视图完成插入操作
              insert into view_1 (empno,ename,job) values(200,'小崔','cleaner')

              insert into view_1 (empno,ename,job,sal) values(201,'小菲','cleaner',5000)

```

借助于视图完成删除操作

```
   delete from view_1  where empno=200
   delete from view_1  where  deptno=20

```

借助于视图更新

```
  update view_1 set  job='guard'  where empno=200

update view_1 set  job='guard' , sal=sal+200 where empno=200

```

#### 六、Transaction:

1.什么是事务: 表文件进行备份.比如执行delete from dept、可以在 删除命令执行前，对dept表进行一次备份

2.事务与存储引擎关系：

只有表文件采用INNODB管理时，才执行事务

3.事务使用:

start transaction; # 生成事务管理对象

delte from dept; # dept_bak

commit; #通知事务管理对象将本次操作中所有备份表文件删除

rollback; #通知事务管理对象将本次操作中所有备份表文件覆盖到原始表，来撤销本次操作

4.事务使用原则:

1)原子性原则:哪些SQL语句应该交给同一个事务管理对象进行管理

答案: 只有来自于同一个业务下的SQL语句才应该交给同一个事务管理

业务特征：一个业务往往包含多个分支任务，只有在所有分支任务都确认成功 才可以任务业务处理成功

例子：穿越到东汉 业务(拯救大汉) 分支任务: 干掉孙权 delete from 吴国 where name=‘孙权’ 分支任务: 干掉刘备 delete from 蜀国 where name=‘刘备’ 分支任务: 干掉曹操 delete from 魏国 where name=‘曹操’

正确使用事务: 业务删除部门20以及开除部门20下员工

start transaction; #transaction_1 delete from dept where deptno=20;# dept_bak delete from emp where deptno=20;# emp_bak commit/rollback;

错误使用事务: 业务删除部门20以及开除部门20下员工

start transaction; #transaction_1 delete from dept where deptno=20;# dept_bak delete from emp where deptno=20;# emp_bak update car set color=“red” where master=‘老板’; commit/rollback;

2.一致性原型: 指定使用rollback场景、一个业务中只要有一个分支任务执行失败 此时就应该认为业务执行失败、此时业务中涉及的所有表文件都应该 恢复到本次业务执行之前状态()

正确使用事务: 业务删除部门20以及开除部门20下员工

start transaction; #transaction_1 delete from dept where deptno=20;# dept_bak delete from emp WEHRE deptno=20;# emp_bak error rollback;

错误使用事务: 业务删除部门20以及开除部门20下员工

start transaction; #transaction_1 delete from dept where deptno=20;# dept_bak delete from emp WEHRE deptno=20;# emp_bak error commit;

3.持久性: commit命令执行之后是无法使用rollback回滚

4.隔离性: 对表文件读取操作与对表文件数据修改操作彼此之间应该互不影响

#### 七、char与varchar

1.varchar： 定长可变字符串

drop table student; create table student( sname varchar(2) #最多可以存储两个英文字符或者两个汉字  ) insert into student values(‘ab’); insert into student values(‘老崔’); insert into student values(‘abc’); #Data too long for “sname”

sname varchar(3) “abc” [a] [b] [c] “ab” [a] [b]

2.char 定长不可变字符串

drop table student; create table student( sname char(3) #最多可以存储三个英文字符或者三个汉字

)

sname char(3)

‘abc’ [a] [b] [c]

‘ab’ [a] [b] [空格] #从char类型字段读取数据时，mysql服务器自动将结尾出所有空格撤销掉
1. drop table student; create table student(
str_1 varchar(3), str_2 char(3) );

insert into student(str_1,str_2) values('ab ','ab ')

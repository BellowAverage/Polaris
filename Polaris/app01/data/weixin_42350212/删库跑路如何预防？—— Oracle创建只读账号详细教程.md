
--- 
title:  删库跑路如何预防？—— Oracle创建只读账号详细教程 
tags: []
categories: [] 

---
**目录**





















#### 需求说明

现有数据库账号：HEPSUSR：具有完整权限，增删改查。

需要创建一个数据库账号：HTREADER，对HEPSUSR账号下所有的表具有只读权限。

#### 第一步：创建只读账号

```
--创建只读账号 第一步
CREATE USER htreader identified by 123456;
```

#### 第二步：赋予账号连接数据库等基本权限

```
--赋予htreader连接等常规权限
grant connect to htreader;
grant create view to htreader;
grant create session to htreader;
grant create synonym to htreader;
```

#### 第三步：获取原账号的查询权限

```
获取原账号HEPSUSR用户的所有查询表权限
select 'grant select on '||owner||'.'||object_name||' to htreader;'
from dba_objects
where owner in ('HEPSUSR')
and object_type='TABLE';

--查询结果为新账号的赋值语句，如下图
```

#### <img alt="" height="415" src="https://img-blog.csdnimg.cn/20210129143942324.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="655">

#### 第四步：将原账号权限赋值为新账号

```
在原账号HEPSUSR下执行，将原账号的查询权限 赋值给新账号
-------
grant select on HEPSUSR.ENTRY_CERT to htreader;
grant select on HEPSUSR.SUB_MESSAGE_INFO to htreader;
grant select on HEPSUSR.ENTRY_CERT_RELATION to htreader;
grant select on HEPSUSR.ENTRY_CERT_RELATION to htreader;
grant select on HEPSUSR.ENTRY_DECL_TAX to htreader;
grant select on HEPSUSR.ENTRY_DOCU to htreader;
grant select on HEPSUSR.ENTRY_FEES to htreader;
grant select on HEPSUSR.ENTRY_GOODS_TAX to htreader;
grant select on HEPSUSR.ENTRY_HEAD to htreader;
grant select on HEPSUSR.ENTRY_LIST to htreader;
grant select on HEPSUSR.ENTRY_WORKFLOW to htreader;
grant select on HEPSUSR.IQ_APPEND to htreader;
grant select on HEPSUSR.IQ_CERT to htreader;
grant select on HEPSUSR.SUB_SWAP to htreader;
grant select on HEPSUSR.VIN_LIST to htreader;
```

#### 第五步：在新账号端创建同位显示表

因为新创建的只读账号，Tables栏中显示为空，我们需要在PL/SQL显示栏中为新账号登录界面添加显示同位元素，如下：

```
--在原账号HEPSUSR端执行，获取需要显示的表名称
select 'create or replace SYNONYM htreader.'||object_name|| ' for ' ||owner|| '.'||object_name||';'
from dba_objects
where owner in ('HEPSUSR')
and object_type='TABLE'
```

#### <img alt="" height="658" src="https://img-blog.csdnimg.cn/20210129145312812.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="807">

#### 第六步：查询结果在新账号端执行

```
在只读账号HTREADER端执行：添加显示各个表信息；在SYSNONYM目录下，tables目录下无显示
create or replace SYNONYM htreader.VIN_LIST for HEPSUSR.VIN_LIST;
create or replace SYNONYM htreader.SUB_SWAP for HEPSUSR.SUB_SWAP;
create or replace SYNONYM htreader.SUB_MESSAGE_INFO for HEPSUSR.SUB_MESSAGE_INFO;
create or replace SYNONYM htreader.IQ_CERT for HEPSUSR.IQ_CERT;
create or replace SYNONYM htreader.IQ_APPEND for HEPSUSR.IQ_APPEND;
create or replace SYNONYM htreader.ENTRY_WORKFLOW for HEPSUSR.ENTRY_WORKFLOW;
create or replace SYNONYM htreader.ENTRY_LIST for HEPSUSR.ENTRY_LIST;
create or replace SYNONYM htreader.ENTRY_HEAD for HEPSUSR.ENTRY_HEAD;
create or replace SYNONYM htreader.ENTRY_GOODS_TAX for HEPSUSR.ENTRY_GOODS_TAX;
create or replace SYNONYM htreader.ENTRY_FEES for HEPSUSR.ENTRY_FEES;
create or replace SYNONYM htreader.ENTRY_DOCU for HEPSUSR.ENTRY_DOCU;
create or replace SYNONYM htreader.ENTRY_DECL_TAX for HEPSUSR.ENTRY_DECL_TAX;
create or replace SYNONYM htreader.ENTRY_CONTAINER for HEPSUSR.ENTRY_CONTAINER;
create or replace SYNONYM htreader.ENTRY_CERT_RELATION for HEPSUSR.ENTRY_CERT_RELATION;
create or replace SYNONYM htreader.ENTRY_CERT for HEPSUSR.ENTRY_CERT;
```

#### 第七步：执行完成之后 登录新账号，查看结果

新账号可以查询原账号的所有表结构，但是无法执行 增删改相关操作

<img alt="" height="560" src="https://img-blog.csdnimg.cn/20210129145038409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="599">

#### 第八步：执行删除、修改sql语句测试

<img alt="" height="219" src="https://img-blog.csdnimg.cn/20210203091243239.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="387">

#### 附录：Oracle查询账号及权限详细语句

```
1.查看所有用户：
select * from dba_users;
select * from all_users;
select * from user_users;

2.查看用户或角色系统权限(直接赋值给用户或角色的系统权限)：
select * from dba_sys_privs;
select * from user_sys_privs;

3.查看角色(只能查看登陆用户拥有的角色)所包含的权限
sql&gt;select * from role_sys_privs;

4.查看用户对象权限：
select * from dba_tab_privs;
select * from all_tab_privs;
select * from user_tab_privs;

5.查看所有角色：
select * from dba_roles;

6.查看用户或角色所拥有的角色：
select * from dba_role_privs;
select * from user_role_privs;
```

###  推荐阅读

#### JDK资源合集
- 【JDK5】jdk1.5x64位 windows版.zip- - 【JDK6】jdk-6u45-windows-x64 jdk1.6 64位 Windows版- - 【JDK7】jdk-7u72-windows-i586-32位- - 【JDK8】jdk-8u131-linux-x64.tar.gz- - 【JDK8】jdk-8u131-linux-x64.tar.gz- 
#### MySql数据库资源
- mysql 5.7 64位安装包 windows版- - mysql5.7 64位安装包 Linux版- 
#### **Oracle数据库补丁合集**
- 【Oracle数据库官方下载】 OPatch补丁工具20.0+版本- 
#### **Oracle客户端工具**
- oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64 rpm包合集- - Oracle客户端x32位 windows版.zip- 
#### **Oracle数据库合集【Linux+Windows】**
- Oracle10g数据库 Windows32位+Linux32位 合集- - Oracle数据库10gx32位安装包 Linux版+client客户端- - Oracle数据库11gx64位安装包 Linux版- - Oracle数据库11gx64位+Windows版安装包+Oracle客户端+Plsql工具- - Oracle 11G 11.2.0.3 客户端 for windows 64位- - oracle 11g Linux64位安装包- - oracle 11g Linux64位安装包- - Linux版Oracle11g x32位 数据库安装包- - spotlight_for_oracle_rac.5.0.1.1022.zip- - Linux_Oracle客户端全部rpm包- - Oracle12c客户端+plsql12- - **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - ****- 
**python实战**
- ****- ****- **...**- ****- ****- ****
**【pygame开发实战开发30例 完整源码】**
- 
**【pygame游戏开发专栏，获取完整源码+教程】**
- ****- ****- ****- ****- ** **- ****
#### CSDN官方学习推荐 ↓ ↓ ↓
- **CSDN出的Python全栈知识图谱，太强了，推荐给大家！**
<img alt="" height="625" src="https://img-blog.csdnimg.cn/20210607120133619.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM1MDIxMg==,size_16,color_FFFFFF,t_70" width="351">

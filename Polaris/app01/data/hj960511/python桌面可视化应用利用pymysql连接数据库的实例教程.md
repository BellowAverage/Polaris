
--- 
title:  python桌面可视化应用利用pymysql连接数据库的实例教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解python桌面可视化应用利用pymysql连接数据库的实例教程 作者：任聪聪 日期：2022年6月1日 


桌面应用的sql连接方式实际上就是把我们的sql账户和信息写在我们的代码中，进行封装，可以对其书写在一个特定的文件中，将其封装并在其他文件中【函数或者服务】进行调用即可。

python链接数据库的方法是很多的，常见的有pymysql、peewee这两个中间件库，通过他们可以很轻松的操作数据库的增删改查。我们本次只讲解pymsql的使用方法

## pymysql的连接方式说明

特点：可以直接使用sql原生语句进行操作，可以尽情的div封装。

## 使用pymsql

本篇文章的python环境为3.9.6

### 步骤一、安装pymysql

```
pip install pymysql
或者设置一个路径：
pip install --target=c:\users\admin\appdata\local\programs\python\python39\lib\ pymysql  

```

<img src="https://img-blog.csdnimg.cn/7b268a5d40e5461bb57aa9032fd9a3ec.png" alt="在这里插入图片描述"> tips：如果有报错记得设置路径，使用有路径的那个命令即可安装

##### 步骤二、导入包

```
import pymysql as myDb

```

##### 步骤三、使用数据类

提示：数据类的代码片段在文章下方

```
import mysqlDbClass as sqlDb

theDbObj = sqlDb.mysqlDbClass(['root','root','127.0.0.1','3306','test'])
#查询表中的所有内容
theDbObj.playSql('select * from s')
#显示所有的表
theDbObj.playSql('show tables')

```

说明： 1.playSql可以执行所有的sql原生语句 2.mysqlDbClass 链接后即可进行playsql操作

## 效果展示

数据库中的内容 <img src="https://img-blog.csdnimg.cn/0b5edd30e0ed40f4a093adfecd367bdc.png" alt="在这里插入图片描述"> 查询结果 <img src="https://img-blog.csdnimg.cn/7dffb0d737834a6399dbab9d5e304584.png" alt="在这里插入图片描述">

## 代码实例

集合封装了pymysql的调用类，可以更快速的上手。

### pymysql的实用类

<img src="https://img-blog.csdnimg.cn/a2a427d5586e46069cde3e91284a148c.png" alt="在这里插入图片描述">

## pymysql桌面可视化应用的实操

<img src="https://img-blog.csdnimg.cn/4fd97c2daba54d17a9b990d9cb3e10e0.gif#pic_center" alt="在这里插入图片描述"> 说明：增删改查直接通过原生sql即可，本实例封装的函数和方法+sql语句可以畅通数据库的相对应操作。

## 完整代码附件

环境说明：python3.9.6 pymsql1.0.2 tkinter 文章附件地址：

### 使用说明：

#### 1.需要安装tkinter

执行命令

```
pip install python-tk 或 pip install tkinter

```

#### 2.需要安装pymysql

执行命令

```
pip install pymysql

```

### 3.查询包的版本的命令：

说明：一定要确保版本号是对的，否则代码实例可能无法执行。

```
pip show 包名

```

### 懒人安装方法

进入到代码实例目录执行下列命令直接安装代码实例环境

```
pip install -r requirements.txt --upgrade

```

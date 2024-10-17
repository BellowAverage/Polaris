
--- 
title:  MyBatisCodeHelperPro插件使用 
tags: []
categories: [] 

---
## 一、下载

MyBatisCodeHelperPro插件下载地址：

## 二、配置

数据库用的tinyInt 或者 smallInt生成java类型是 byte 和 short 两种类型。在java代码里面操作 byte 和 short 类型比较麻烦，经常需要强制转换，下面是设置使用Integer 来替代byte和short还有使用Java8的日期时间类型

<img alt="" height="814" src="https://img-blog.csdnimg.cn/20200715093031704.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

## 三、使用

### 根据实体类生成建表sql

按alt+insert

<img alt="" height="821" src="https://img-blog.csdnimg.cn/20200715095732939.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 生成的SQL语句：

<img alt="" height="559" src="https://img-blog.csdnimg.cn/20200715100331957.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="976">

生成好了建表语句后，到数据库中执行， 然后从数据库来生成crud代码

<img alt="" height="275" src="https://img-blog.csdnimg.cn/20200715100732531.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="463">

<img alt="" height="510" src="https://img-blog.csdnimg.cn/20200715100902769.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1039">

### 根据表生成Bean、Dao+mapper和Service

第一步：在Intellij中连接上MySQL数据库，在指定的表上右键

<img alt="" height="359" src="https://img-blog.csdnimg.cn/20200715101037979.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="465">

第二步：配置生成信息

<img alt="" height="1044" src="https://img-blog.csdnimg.cn/2020071510215166.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="776">

第三步：查看各个生成的目录

<img alt="" height="484" src="https://img-blog.csdnimg.cn/20200715102417967.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="467">

### 根据接口中的方法名生成对应的mapper

只需要一个方法名，不需要参数和返回值，输入方法名后，按alt+enter–Generate mybatis sql 就可以生成了

<img alt="在这里插入图片描述" height="694" src="https://img-blog.csdnimg.cn/20200416115437152.gif" width="903">

方法名生成sql时支持if test

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200416115459157.gif">

一键添加@param注解

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200414161755356.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpYW5naGVjYWk1MjE3MTMxNA==,size_16,color_FFFFFF,t_70">

### 生成mapper映射文件中resultMap未使用的字段

光标放到resultmap标签type属性值上 -&gt; alt + enter -&gt; generate unUsed properties

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200414162105231.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpYW5naGVjYWk1MjE3MTMxNA==,size_16,color_FFFFFF,t_70">

### 根据mapper接口生成mapper映射文件

创建一个接口 -&gt; 光标放到接口名上 -&gt; alt + enter -&gt; generate mybatis mapper for current class -&gt; 选择mapper映射文件位置

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200414162249529.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpYW5naGVjYWk1MjE3MTMxNA==,size_16,color_FFFFFF,t_70">

### 生成find方法

根据方法名 直接生成sql代码 方法名有自动提示 单表操作的代码只有写个方法名就好了 find方法

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200414162730776.gif">

### 生成测试用例

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200415161228737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpYW5naGVjYWk1MjE3MTMxNA==,size_16,color_FFFFFF,t_70">

### 生成分页查询 （依赖于 pageHelper)

<img alt="" height="409" src="https://img-blog.csdnimg.cn/20200715112826151.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

<img alt="" height="323" src="https://img-blog.csdnimg.cn/20200715112853693.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="811">

<img alt="" height="129" src="https://img-blog.csdnimg.cn/20200715112918193.png" width="1200">

## 四、DAO层方法的命名规则

### find方法

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200416115830202.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpYW5naGVjYWk1MjE3MTMxNA==,size_16,color_FFFFFF,t_70">

### update方法

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200416115846320.png">

### delete方法

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200416115930916.png">

### count方法

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20200416115942566.png">

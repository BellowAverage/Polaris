
--- 
title:  【Wiki】XWiki数据备份 
tags: []
categories: [] 

---
XWiki为主题使用java开发的开源wiki，官网地址如下： https://www.xwiki.org/xwiki/bin/view/Main/



#### 目录
- - <ul><li>- - 


## 1、 XWiki升级数据备份

升级约等于xwiki重新部署，部署参见上篇，部署完成后填充数据库与持久化目录即可。

### 1.1、 获取XWiki配置的数据库与持久化目录信息

数据库存储各种显式信息，持久化目录存储wiki上各格式附件与图片。 在WEB-INF/**hibernate.cfg.xml**获取数据库配置信息。（WEB-INF目录为TOMCAT部署的webapps下目录）

```
cat hibernate.cfg.xml

```

```
&lt;property name="hibernate.connection.url"&gt;jdbc:postgresql://127.0.0.1:5432/xwiki&lt;/property&gt;
&lt;property name="hibernate.connection.username"&gt;xwiki&lt;/property&gt;
&lt;property name="hibernate.connection.password"&gt;xwiki&lt;/property&gt;

```

在**xwiki.properties**获取持久化配置信息

```
cat xwiki.properties  |grep 'environment.permanentDirectory'

```

持久化参数项名为:environment.permanentDirectory

```
environment.permanentDirectory=/data/local/xwiki-14.6/

```

### 1.2 备份数据库信息

以使用的postgresql为例。 **备份**：

```
# 进入postgresql目录
cd /etc/postgresql/9.5/main
# 执行备份命令
pg_dump -h 127.0.0.1 -U dbUserName dbName &gt; /home/io/databasename.bak
# 示例
pg_dump -h 127.0.0.1 -U xwiki xwiki &gt; /home/billapp/XWiki_backup/databasexwiki.bak

```

|参数|解释
|------
|127.0.0.1|数据库所在计算机ip(必须保证数据库外部访问权限)
|dbUserName|需要备份的数据库的用户名
|dbName|是需要备份的数据库名
|/home/io/databasename.bak|是最后生成的文件的路径和文件名称(可自定义)

**还原**:

```
psql -h 127.0.0.1 newdbUserName -d newdbName &lt; /home/io/ databasename.bak
#示例
psql -h 127.0.0.1 -U xwiki xwiki &gt; /home/billapp/XWiki_backup/databasexwiki.bak

```

|参数|解释
|------
|127.0.0.1|数据库所在计算机ip(必须保证数据库外部访问权限)
|newdbUserName|需要还原的数据库的用户名
|newdbName|是需要还原的数据库名
|/home/io/databasename.bak|之前生成的备份文件

### 1.3 备份持久化目录

创建备份目录，使用cp命令，备份持久化目录

```
mkdir /data/local/xwiki-14.6_backup
cp -a /data/local/xwiki-14.6/ /data/local/xwiki-14.6_backup

```

cp -a：此选项通常在复制目录时使用，它保留链接、文件属性，并复制目录下的所有内容。其作用等于dpR参数组合。

## 2、XWiki数据迁移

**如若需要以PDF或者DOC文档形式保留现有WIKI内容，目前没有！！！** 目前只支持单个页面pdf导出。也许可以通过自建xwiki的插件、应用、macro实现？

虽然功能很多很全，但是这点大概是和页面没别人好看一样，限制了xwiki的传播？

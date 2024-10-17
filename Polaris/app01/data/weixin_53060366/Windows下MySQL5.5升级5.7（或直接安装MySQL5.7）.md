
--- 
title:  Windows下MySQL5.5升级5.7（或直接安装MySQL5.7） 
tags: []
categories: [] 

---
## Windows下MySQL5.5升级5.7（或直接安装MySQL5.7）

#### 1、关闭MySQL服务：

Ctrl + shift + Esc找到服务，找到下面的MySQL服务，停止服务。

#### 2、卸载程序：

控制面板中卸载mysql5.5。

#### 3、删除mysql5.5的安装目录及注册表：
- 找到 `mysql` 安装的位置，将整个 `mysql`目录删除。
删除注册表：
- win + R --》regedit --》打开注册表。- HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\Eventlog\Application\MySQL 目录删除。- HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\Services\Eventlog\Application\MySQL 目录删除。- HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Eventlog\Application\MySQL 目录删除。- 我的只找到了第一个，都不要紧的，有就删除，没有就算了。- `C:\Documents and Settings\All Users\Application Data\MySQL` 这里还有MySQL的数据文件，必须要删除。
#### 4、下载mysql：

[官网下载：]() 选择自己想要的版本。

<img src="https://img-blog.csdnimg.cn/10e361aa12a1409894f29e7a74377d6b.png#pic_center" alt="在这里插入图片描述">

#### 5、配置mysql环境变量：
- 解压刚下载的压缩包；- 设置环境变量：此电脑–》右键属性 --》 高级系统设置 --》 环境 变量 --》 新建 – 》编辑Path变量。
<img src="https://img-blog.csdnimg.cn/293c6d9200754d309f7593fbbf1b4b98.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/15d645ba2c9c49dbaf1a37b9b325270c.png#pic_center" alt="在这里插入图片描述">

#### 6、创建mysql配置文件，my.ini文件
- 在mysql安装目录下新建 my.ini 文件
```
[client]
port = 3306
 
[mysqld]
port = 3306
basedir=D:\KY15\mysql\mysql-5.7.38-winx64
datadir=D:\KY15\mysql\mysql-5.7.38-winx64\data
max_connections=200
character-set-server=utf8
default-storage-engine=INNODB
sql_mode=STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION
event_scheduler=ON

[mysql]
default-character-set=utf8

```

<img src="https://img-blog.csdnimg.cn/092ece5f99ba4183ac94d9b1da8eba84.png#pic_center" alt="在这里插入图片描述">

#### 7、初始化mysql，安装mysql：

使用**管理员**权限打开`cmd`窗口，注意一定要是**管理员权限**，依次输入如下命令。

```
# 初始化mysql
mysqld --initialize-insecure --user=mysql
# 安装mysql
mysqld -install
# 启动mysql
net start mysql

```

#### 8、设置密码：

安装好后，默认密码为空，使用Navicat设置密码：

<img src="https://img-blog.csdnimg.cn/9e18031c36c14c5ca1c56ba217eeaa09.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/48e83caacbe74740bdcd44d94460287d.png#pic_center" alt="在这里插入图片描述">

>  
 Windows下的mysql5.7安装完成。 


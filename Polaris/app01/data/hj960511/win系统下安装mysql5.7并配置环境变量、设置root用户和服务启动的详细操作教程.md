
--- 
title:  win系统下安装mysql5.7并配置环境变量、设置root用户和服务启动的详细操作教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：win系统下安装mysql5.7并配置环境变量、设置root用户和服务启动的详细操作教程 日期：2024年2月22日 作者：任聪聪 


## 一、mysql5.7版本的下载

官方下载地址：

### 步骤一、选择版本号

<img src="https://img-blog.csdnimg.cn/direct/f24513fae3a04790addb900cb3f60d43.png" alt="在这里插入图片描述"> 说明：如上图选择合适的版本信息，检索出所需的系统版本安装包。

### 步骤二、选择win系统的安装版本

<img src="https://img-blog.csdnimg.cn/direct/2ab24996b3504753ac6234a695ac18b3.png" alt="在这里插入图片描述"> end：等待下载完毕进入到安装环节教程。 <img src="https://img-blog.csdnimg.cn/direct/a4ee4148042a4d82a20a2840a719efae.png" alt="在这里插入图片描述">

## 二、安装mysql5.7并配置相关信息

### 步骤一、解压缩mysql5.7的zip包

<img src="https://img-blog.csdnimg.cn/direct/0c481a16d0774132a4687ed21d335b83.png" alt="在这里插入图片描述">

### 步骤二、移动到自己常用的或者专门的文件目录下

<img src="https://img-blog.csdnimg.cn/direct/b0d60612799f4e9bb2e03583564915a9.png" alt="在这里插入图片描述"> end：完成后进入到环境变量配置环节。

## 三、配置mysql5.7的环境变量

### 步骤一、打开搜索，输入 环境变量如下图：

<img src="https://img-blog.csdnimg.cn/direct/059f05037d1f4f19a6563cfdbeab86e5.png" alt="在这里插入图片描述">

### 步骤二、点击进入设置，找到环境变量配置，如下图。

<img src="https://img-blog.csdnimg.cn/direct/910bbffa46f0489ca44d96720c7c1f46.png" alt="在这里插入图片描述">

### 步骤三、进入到环境变量配置界面，找到path的配置，并双击，进入到如下界面：

<img src="https://img-blog.csdnimg.cn/direct/268384d10a914b58aad2af10616dab5f.png" alt="在这里插入图片描述">

### 步骤四、添加mysql路径，如下图

<img src="https://img-blog.csdnimg.cn/direct/39ad4ffc262544e890e3431529f21071.png" alt="在这里插入图片描述">

### 步骤五、打开cmd测试mysql的命令是否生效。

输入命令：`mysql --version`，如下图，如果结果一致则说明配置环境变量完成。 <img src="https://img-blog.csdnimg.cn/direct/6700b5c33a7b4b8bbbb811126f767db3.png" alt="在这里插入图片描述">

## 四、安装mysql的win系统服务，并启动mysql5.7服务

cmd操作安装服务和卸载服务命令说明：`mysqld -install`安装、`mysqld -remove`卸载。

### 步骤一、安装mysql服务：

<img src="https://img-blog.csdnimg.cn/direct/fe47894ba10a4086bc5efe9bed8f4cdc.png" alt="在这里插入图片描述">

### 步骤二、服务初始化

命令：`mysqld --initialize-insecure --user=mysql` <img src="https://img-blog.csdnimg.cn/direct/3134bbeff9014039bc1b54b08d7a1f1b.png" alt="在这里插入图片描述">

### 步骤三、启动mysql服务：

命令：`net start mysql` <img src="https://img-blog.csdnimg.cn/direct/7ae500e6562f400e83ce4285c4d2539a.png" alt="在这里插入图片描述"> 注意：上述我有变更过一次mysql的安装目录，请结合自己的实际目录进行配置即可！如果以前有安装过，不要轻易修改注册表路径，建议直接在原有的服务目录进行操作，将自己的mysql包安装到原有目录中。

停止服务：`net stop mysql`

## 五、登录mysql数据库，并创建数据库和导入数据

### 步骤一、登录数据库

输入命令：`mysql -u root -p` ，如下图： <img src="https://img-blog.csdnimg.cn/direct/ceac7f7c44384fb389c1e0b4a6711ded.png" alt="在这里插入图片描述"> 注意：默认密码是为空的，不需要输入，开发环境建议保持，如果不是建议设置密码。

### 步骤二、给root用户设置密码，admin888

输入命令：

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'admin888';

```

<img src="https://img-blog.csdnimg.cn/direct/f5318a9835884db5978219deae3b2e96.png" alt="在这里插入图片描述">

刷新权限：

```
FLUSH PRIVILEGES; 

```

<img src="https://img-blog.csdnimg.cn/direct/8d6103f55bcd464fad1da692c121353f.png" alt="在这里插入图片描述"> 退出登录：

```
exit;

```

重新登录： <img src="https://img-blog.csdnimg.cn/direct/c31dc008b9d3464fbd16c16baab81a67.png" alt="在这里插入图片描述">

## 六、常见问题说明：

### 1.系统报错4

如果安装后提示，系统文件错误的情况，请再次执行mysqld -install,查看实际的默认路径，如果默认路径和自己的路径不一致，建议直接转移mysql到默认地址，注意bin文件目录的位置，即可解决问题。

### 2.无权限报错

安装mysql服务时，记得以管理员身份进行运行cmd，如果不是则没有权限安装系统服务。

### 3.系统报错5或无法服务初始化

<img src="https://img-blog.csdnimg.cn/direct/a4c0bc948920404f9d1684b372d43ee7.png" alt="在这里插入图片描述"> 如果系统报错5，那么记得自己在安装目录下创建my.ini文件内容如下，或检查其他安装事项：

```
[mysqld]
# 设置MySQL服务器的端口号，默认为3306
port = 3306

# 设置MySQL服务器的安装目录
basedir = C:\Program Files\MySQL\MySQL Server 5.7\

# 设置MySQL服务器的数据存储目录
datadir = C:\Program Files\MySQL\MySQL Server 5.7\mysqld\data\

# 设置MySQL服务器的最大连接数，默认为150
max_connections = 150

# 设置MySQL服务器的字符集，推荐使用utf8mb4以支持更多的字符
character-set-server = utf8mb4

# 设置MySQL服务器的排序规则，推荐使用utf8mb4_general_ci以支持更多的字符
collation-server = utf8mb4_general_ci

# 设置每个MySQL线程的堆栈大小，默认为256KB
thread_stack = 256K

# 设置事务隔离级别，默认为READ-COMMITTED
transaction_isolation = READ-COMMITTED

# 设置是否开启二进制日志，用于记录数据库的所有更改，默认为0（不开启）
log-bin = 0

# 设置MySQL服务器的ID，用于标识不同的MySQL服务器，默认为1
server-id = 1


```

**位置：** <img src="https://img-blog.csdnimg.cn/direct/c889bd23eb06409b8c9d31b51c3bacfd.png" alt="在这里插入图片描述">


--- 
title:  Windows下MySQL5.7压缩包安装教程 
tags: []
categories: [] 

---
在`Win10`和`Win11`环境下测试安装成功，其他环境请自测（2022-09-12更新）

### 下载MySQL5.7压缩包

官网下载： <img src="https://img-blog.csdnimg.cn/18bb9b5a23254ae3a6af2b3d04830bea.png" alt="旧版本"> <img src="https://img-blog.csdnimg.cn/b166ababb1594fc2b45e51695c324eb0.png" alt="选择下载">

>  
 如果你之前安装过`MySQL`或者在这安装过程中出现任何问题想重新安装 
 <pre><code class="prism language-mysql">sc delete mysql
</code></pre> 
 删除已经安装好的`MySQL`服务 


### 安装MySQL5.7

下载后会得到一个**zip**安装文件，我这里解压到`D:\MySql5.7\`目录下

>  
 注：确定好路径就不要乱动了，不然后面初始化数据库那一步会出问题 


添加**系统环境变量**，此电脑右键→属性→高级系统设置→环境变量→系统变量 然后在PATH变量中添加`MySQL`安装目录下的`bin`目录：**D:\MySql5.7\bin** <img src="https://img-blog.csdnimg.cn/0ec5926e2d68471e873cfcd0611d248e.png" alt="环境变量"> 在安装目录下（`D:\MySql5.7\`）创建`my.ini`文件，用记事本方式打开即可，写入以下内容：

```
[client]
port=3306
default-character-set=utf8
[mysqld]
# 设置为自己MYSQL的安装目录
basedir=D:\mysql5.7\
# 设置为MYSQL的数据目录
datadir=D:\mysql5.7\data\
port=3306
character_set_server=utf8
# 跳过安全检查
skip-grant-tables

```

使用**管理员权限**打开`cmd命令窗口`，执行：

```
# 先进入MySql安装目录下的bin目录
cd D:\mysql5.7\bin
# 然后执行
mysqld -install
mysqld --initialize-insecure --user=mysql

```

如果执行成功，`MySql5.7`目录下会生成`data`目录 启动`MySQL`服务:

```
net start mysql

```

### 登录MySQL5.7

`cmd命令窗口`输入命令：

```
mysql -u root -p 

```

因为刚安装的，所以当前`root`用户密码是空的，直接回车不要输入密码 <img src="https://img-blog.csdnimg.cn/8c84625dd04e401cb2fbfb7273c96b37.png" alt="请添加图片描述">

#### 设置密码

我这里修改`root`用户密码为`123456`

```
use mysql;  
update user set authentication_string=password('123456') where user='root' and Host='localhost';
# 刷新权限
flush privileges;
# 退出
quit;

```

然后我们去修改`my.ini`文件，把最后一行跳过安全检查注释掉，后面登录`MySQL`就需要输入我们修改后的密码了

```
# skip-grant-tables

```

重新启动`MySQL`

```
net stop mysql
net start mysql

```

再次进入`MySQL`, 输入正确的用户名和密码就可以登录了

#### 修改密码

```
mysqladmin -u 用户名 -p 旧密码 password 新密码

```

### 后续问题解决

如果你把`MySQL`的进程关了或者其他异常问题，再次打开可能出现拒绝访问啥的，直接进`bin`目录下用**管理员身份**执行`cmd命令窗口`重启一下`MySQL`再进行登录就可以正常访问了

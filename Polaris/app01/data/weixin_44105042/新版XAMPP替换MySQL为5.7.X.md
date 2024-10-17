
--- 
title:  新版XAMPP替换MySQL为5.7.X 
tags: []
categories: [] 

---
写这篇文章起初是我想搭建一个虚拟机内开发实验环境，然后就想到了`XAMPP`这个工具可以一键启动`Apache`，`MySQL`…这些服务嘛，懒得去折腾那些个环境了 我这里下载的是`XAMPP 7.4.29`的版本，在官方那边同时上传的还有`8.0.19`和`8.1.6`两个版本。问我为啥用`7.4.29`，跟着大众下载的步伐永远不会错嘿嘿 下载地址： <img src="https://img-blog.csdnimg.cn/0a32b112ce804d0db4f549b629f8c8d6.png" alt="下载"> <img src="https://img-blog.csdnimg.cn/037949a216674cf8a1759d230bfa89eb.jpeg" alt="表情"> 随后装好了我们打开`XAMPP`软件去启动`MySQL`服务，然后输入命令`mysql -V`看一下版本号

>  
 这里推荐用`XAMPP`软件的右边的功能：`Shell`打开命令窗口，不然不好连接`MySQL` 


<img src="https://img-blog.csdnimg.cn/5a0003ea54a24970a7032bf96f20925b.png" alt="MySQL版本"> （呃…不认得这个版本）去搜了下，`MariaDB 10.4.24`是`MySQL`的一个分支，操作方式都和`MySQL`几乎一致，但是`10.4.24`这个版本还是太高了，怕高版本的数据库对我的项目兼容性不好，我这里将`MySQL`替换版本为`5.7.X`的 先去下载个`5.7.X`解压版的文件 下载链接：

>  
 改版本之前记得先停止`XAMPP`的`MySQL`服务 
 先将`XAMPP`安装目录下的`mysql`目录备份一下 


解压一下刚刚下载的`MySQL`压缩包 将里面的`bin`，`lib`，`share`目录复制到`XAMPP`目录下的`mysql`目录内 <img src="https://img-blog.csdnimg.cn/47815747e04c43f0bb899d485a8ce3e1.png" alt="MySQL目录"> 如果`XAMPP`目录下的`data`目录内有文件，**全部删掉** 用**管理员身份**打开`cmd`进入`XAMPP`目录下的`mysql\bin\`目录，然后运行命令：

```
mysqld --initialize

```

进行初始化，它会在`data`目录下自动创建新的文件 **将刚刚备份的`mysql`目录里面的`bin`目录下的`my.ini`文件复制替换到`XAMPP`目录下的`mysql\bin\`目录** 进行到这里，理论上可以了，我们运行`XAMPP`的`MySQL`服务看看 <img src="https://img-blog.csdnimg.cn/b754c44fe909424e828920f8d5723645.png" alt="XAMPP"> 有报错，我们检查一下`Logs`日志文件 <img src="https://img-blog.csdnimg.cn/a1a1929c42ee45358951a5408de95fdd.png" alt="Log"> 发现问题，提示未知变量，我猜这个应该就是`MariaDB 10.4.24`新增的了，我们去`mysql\bin\my.ini`文件里找找 <img src="https://img-blog.csdnimg.cn/8bceeb477abb4822a19f0da04c938399.png" alt="my.ini"> 果真有，将它注释掉，然后再次运行`MySQL`服务 <img src="https://img-blog.csdnimg.cn/394242e449944a158ed28cd4547c5d25.png" alt="XAMPP"> 成功换版本 然后现在你会发现一个新问题，从`XAMPP`软件的右边的`Shell`进入`MySQL`： <img src="https://img-blog.csdnimg.cn/067479660ae248d2ad3eb873b7963ac9.png" alt="SHELL"> 密码不对了 现在我们关掉`XAMPP`的`MySQL`服务 用**管理员身份**打开`cmd`进入`XAMPP`目录下的`mysql\bin\`目录，输入命令跳过权限验证（这个`cmd`窗口不要关闭，这个跳过权限验证的方法是临时的，关掉这个窗口后就失效了，放后台就好）：

```
mysqld --skip-grant-tables

```

你会发现`XAMPP`里的`MySQL`服务自动打开了 现在我们从`XAMPP`的`Shell`中登录`MySQL`，用户名root，密码为空直接回车

```
mysql -u root -p

```

<img src="https://img-blog.csdnimg.cn/933071ffd2b74bcca3583502fd29d1bc.png" alt="请添加图片描述"> 现在便登录上来了 然后我们继续输入`MySQL`命令修改root用户密码，**不要输入别的，这里必须先将密码改为空**

```
use mysql;
update user set authentication_string='' where user='root';
quit;

```

输入完后把所有`cmd`窗口和`XAMPP Shell`窗口**关掉**，再在`XAMPP`中重新开关一下`MySQL`服务 接下来继续进入新的`XAMPP Shell`窗口，输入命令：

```
mysql -u root -p

```

密码为空直接回车，然后重置密码，我这里改成`123456`，大家按照自己想法来

```
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
quit;

```

然后重新输入命令登录

```
mysql -u root -p

```

现在就会发现密码修改好了

好了，写完了，`XAMPP`上面的`MySQL`折腾起来跟直装的还是不一样哈哈，理论上来说此方法换`MySQL`其他版本的应该也适用，如果要装`8.X`的话就是跳过密码验证那里可能不同，可以参照一下这篇博客：

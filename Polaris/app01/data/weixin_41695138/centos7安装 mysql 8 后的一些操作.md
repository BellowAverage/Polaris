
--- 
title:  centos7安装 mysql 8 后的一些操作 
tags: []
categories: [] 

---
 如果安装过程中出现问题，如：

```
mysql-community-server-8.0.31-1.el7.x86_64.rpm 的公钥尚未安装


 失败的软件包是：mysql-community-server-8.0.31-1.el7.x86_64
 GPG  密钥配置为：file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

```

<img src="https://img-blog.csdnimg.cn/ed69981f0c0d44279629a4c7205064bc.png" alt="在这里插入图片描述"> 则可参考  请根据自己的实际情况执行检查命令 如小编的是： rpm --checksig /var/cache/yum/x86_64/7/mysql80-community/packages/mysql-community-server-8.0.31-1.el7.x86_64.rpm <img src="https://img-blog.csdnimg.cn/e8ab1fa6f7bb4ae68fd2a3cd55442a81.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6a31dc4a53a94cc881211b132b3d04b3.png" alt="在这里插入图片描述">

### centos7安装 mysql 8

上个博客一直到登录到mysql, 后面的内容执行下面的步骤
1. 更改用户名密码： ALTER USER ‘root’@‘localhost’ IDENTIFIED BY ‘new password’;
```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';

```

<img src="https://img-blog.csdnimg.cn/07e98e79ebac4a55a920af429869f6ba.png" alt="在这里插入图片描述"> 说明 密码不符合当前策略 2. 先修改密码，才能执行下面的步骤，后面再改回来 ALTER USER ‘root’@‘localhost’ IDENTIFIED BY ‘Qinenqi123@’; <img src="https://img-blog.csdnimg.cn/76d3074ac9c94386963d6194ff676dea.png" alt="在这里插入图片描述">
1. 修改 当前策略 validate_password.length 是密码的最小长度，默认是8，我们把它改成4 输入：set global validate_password.length=4; validate_password.policy 验证密码的复杂程度，我们把它改成0 输入：set global validate_password.policy=0; validate_password.check_user_name 用户名检查，用户名和密码不能相同，我们也把它关掉 输入：set global validate_password.check_user_name=off; <img src="https://img-blog.csdnimg.cn/20c4a7d1665f452eadb17f13a84af67a.png" alt="在这里插入图片描述">1. 更改为简单的密码：
```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';

```
1. 开启mysql 远程访问：
```
use mysql 

```

```
update user set host='%' where user='root' and host='localhost';

```

```
flush privileges;   

```

<img src="https://img-blog.csdnimg.cn/dfbc8c9bb58943bf8907c351474bd345.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 6. 本地 navicate 连接一下 <img src="https://img-blog.csdnimg.cn/9515f81dcd454b49a003c7e9737395f0.png" alt="在这里插入图片描述">

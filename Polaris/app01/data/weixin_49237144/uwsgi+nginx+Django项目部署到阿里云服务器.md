
--- 
title:  uwsgi+nginx+Django项目部署到阿里云服务器 
tags: []
categories: [] 

---
## uwsgi+nginx+Django项目部署到阿里云服务器

Hello小伙伴们，你们好，又是日常get新技能的一天，0基础入门，趁着热乎，快上车啦 ~~。 今天，咱们来整一下如何使用uwsgi+nginx+Django项目部署到阿里云服务器的 ~~。

#### 一、环境准备

阿里云云服务器ECS突发性能 t5（免费领取的）

云服务器镜像：Ubuntu18.04 64位 （自带Python 2.7.17 、Python 3.6.9）

Django == 3.2.4

uWSGI == 2.0.19.1

nginx == 1.14.0

MySQL == 5.7.34

工具：Xshell7、Xftp7、SQLyog

#### 二、配置项目所需环境

##### 1. 同步源，并且更新源

```
root@localhost:~# sudo apt-get update
root@localhost:~# sudo apt-get upgrade
# 1、apt-get update是同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包。
# 2、apt-get update只是更新了apt的资源列表，没有真正的对系统执行更新。如果需要，要使用apt-get upgrade来更新。
# 3、最后，需要注意的一点是，每回更新之前，我们需要先运行update，然后才能运行upgrade和dist-upgrade，因为相当于update命令获取了包的一些信息，比如大小和版本号，然后再来运行upgrade去下载包，如果没有获取包的信息，那么upgrade就是无效的啦！

# 4、如果报错了操作如上面
其实错误信息已经很明确了，Unable to locate packet就是无法找到包嘛，
那还不赶紧sudo apt-get update下！

```

（1.1）安装python3-pip（基本不需要操作，因为系统自带的python都有pip）

```
root@localhost:~# apt-get install python3-pip
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-pip is already the newest version (9.0.1-2.3~ubuntu1.18.04.5).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
# 返回信息说明了Ubuntu18.04.5 已经有pip并且版本为9.0.1-2.3

```

（1.2） 一定要更新pip命令:

```
root@localhost:~# python3 -m pip install --upgrade pip
Collecting pip
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/ca/31/b88ef447d595963c01060998cb329251648acf4a067721b0452c45527eb8/pip-21.2.4-py3-none-any.whl (1.6MB)
    100% |████████████████████████████████| 1.6MB 35.9MB/s 
Installing collected packages: pip
  Found existing installation: pip 9.0.1
    Not uninstalling pip at /usr/lib/python3/dist-packages, outside environment /usr
Successfully installed pip-21.2.4

```

##### 2. 安装虚拟环境和虚拟环境管理包（基本自带，没有就下载）

```
root@localhost:~# /usr/local/lib/python3.6/dist-packages  # 查看是否有virtualenv 和 virtualenvwrapper 
# 没有的话就操作如下
root@localhost:~# pip3 install virtualenv  # 要先更新pip
root@localhost:~# pip3 install virtualenvwrapper  # 包管理工具

```

##### 3. 修改./bashrc文件，使用命令：vi .bashrc

（3.1）查看安装目录

which python3

which virtualenvwrapper.sh

提示：.开头的都是隐藏文件，需要命令：ls -al 或者 ls -lha 才能看到。

按键盘 i 进入编辑模式，按左上角esc退出编辑模式，按shift+：wq 保存退出。

（3.2）添加内容，如下所示。

```
# 虚拟环境存放目录(无需自己创建)
export WORKON_HOME=~/Envs

# 激活virtualenvwrapper包管理
source /usr/local/bin/virtualenvwrapper.sh

# 虚拟环境指定python路径
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

```

（3.3）刷新配置文件

```
root@localhost:~# source .bashrc

```

##### 4. 新建一个虚拟环境及其常用命令

（4.1）新建一个虚拟环境

```
# 新建了一个web的虚拟环境，并且进入了web这个环境。
root@localhost:~# mkvirtualenv web

```

（4.2）退出当前虚拟环境

```
(web)root@localhost:~# deactivate

```

（4.3）查看所有的虚拟环境

```
# 这两个命令一般都是可以的。
(web)root@localhost:~# workon 
or 
(web)root@localhost:~# lsvirtualenv

```

（4.4）删除虚拟环境

```
# 删除了env虚拟环境
(web)root@localhost:~# rmvirtualenv env

```

（4.5）进入某个虚拟环境

```
# 即使没有退出当前虚拟环境，workon也是直接可以切换到其他虚拟环境的
(web)root@localhost:~# workon web

```

##### 5. 迁移项目上虚拟环境中所有包到阿里云服务器上

（5.1）更新虚拟环境里的pip

```
(web)root@localhost:~# python -m pip install --upgrade pip

```

（5.2）下载项目所需包（一定要进入虚拟环境）

```
(web)root@localhost:~# pip3 install 库名
requests
django3.2.4
pymysql
uwsgi

```

##### 6. 安装数据库MySQL

（6.1）最好更新一下源，再下载

```
(web)root@localhost:~# apt-get update #更新源
(web)root@localhost:~# apt-get install mysql-server -y  # -y参数就是一路yes

```

（6.2）两个依赖包

```
(web)root@localhost:~# apt-get install mysql-client

(web)root@localhost:~# apt-get install libmysqlclient-dev -y  # -y参数就是一路yes

```

（6.3）初始化配置（参考：https://blog.csdn.net/weixx3/article/details/80782479）

```
(web)root@localhost:~# mysql_secure_installation

```
1. 验证密码插件可以用来测试密码和提高安全性。它检查密码的强度，并允许用户只设置那些密码足够安全。要设置验证密码插件吗？ 选择：n 2. 默认情况下，mysql 安装有一个匿名用户，允许任何人登录 mysql 而无需为其创建用户帐户。 这只是为了测试，并使安装过程更顺利。 您应该在进入生产环境之前删除它们。 选择：y 3. 通常，root 应该只允许从“ localhost”连接。这样可以确保有人无法从网络中猜到 root 密码。 选择：y 4. 默认情况下，mysql 有一个任何人都可以访问的数据库“ test”。这也只是为了测试，应该在移动到生产环境之前删除。删除测试数据库并访问它？ 选择：n 5. 重新加载特权表将确保到目前为止所做的所有更改将立即生效？ 选择：y
（6.4）修改mysqld.cnf配置文件

```
(web)root@localhost:~# vim /etc/mysql/mysql.conf.d/mysqld.cnf

```

​ 跳过密码登录（这里作者不用）skip-grant-tables

​ 开启远程登录（注释下面代码 或者换成0.0.0.0）

```
#bind-address = 127.0.0.1
bind-address = 0.0.0.0

```

​ 查看IP

```
(web)root@localhost:~# ifconfig（必须下载apt install net-tools，云服务器好像有了）
(web)root@localhost:~# ip addr（无需下载）

```

​ 检查mysql服务状态

```
(web)root@localhost:~# systemctl status mysql.service 
(web)root@localhost:~# systemctl start mysql.service  # 开启MySQL服务

```

​

（6.5）默认情况下，MySQL只允许本地登录，开启远程连接如下：

```
(web)root@localhost:~# mysql -uroot -p  # 输入root密码

```

​ 创建数据库，并指定字符集（根据自己的需求创建数据库）

```
mysql&gt;create database django_mysql charset=utf8;

```

​ MySQL远程连接权限，授权所有用户拥有数据库的所有权限。

```
# '%':配置所有ip可以通过root:123456访问数据库（%换成你的公网ip也行，一定要重启服务）
mysql&gt;GRANT ALL PRIVILEGES ON *.* TO root@'%' IDENTIFIED BY "123456";
mysql&gt;flush privileges;  # 一定要刷新系统权限表

```

​ 查看用户权限是否变更

```
mysql&gt;select User,authentication_string,Host from user; 

```

##### 7. 迁移数据

（7.1）首先必须要回到阿里云服务器，点击更多，选择网络和安全组 看到右边的配置规则，进去添加3306端口。 一定要重启服务

（7.2）通过SQLyog工具将Ubuntu数据库数据复制到阿里云服务器上的MySQL数据库里

##### 8.Django项目迁移到云服务器上

方式一：在这里作者使用 xShell7 和 xFTP7 进行项目迁移的。

方式二：也可以 scp 命令传输

```
(web)root@localhost:~# scp -r /home/ubuntu/renjie/MyFirstWeb root@localhost:/root/renjie/MyFirstWeb  

```
1. /home/ubuntu/renjie/MyFirstWeb是项目的根目录；1. root是阿里云服务器的用户名；1. localhost是你阿里云服务器的公网IP；1. /root/renjie/MyFirstWeb 是阿里云服务器上的文件位置；1. 会提示输入你的阿里云服务器登录密码，密码正确后就会开始传输。
##### 9. 配置uwsgi
1. 进入虚拟环境workon web
```
(web)root@localhost:~# pip3 install uwsgi

```
1. 先进入setting修改
```
DEBUG = False  # 关闭调试模式。
ALLOWED_HOSTS = ['*']  #后续会更改的，域名或者公网IP，允许所有主机访问。

```
1. 创建配置文件myfirstweb.ini（更setting同级）
```
[uwsgi]

# uwsgi才使用
#http=127.0.0.1:8000

# 有了NGINX使用
socket=127.0.0.1:8000

# 项目的绝对路径
chdir=/root/renjie/MyFirstWeb

# wsgi.py相对路径
wsgi-file=myfirstweb/wsgi.py

# 进程数
process=4

# 线程数
threads=2

# 进程pid
pidfile=myfirstweb.pid

# 后台运行日志输出
daemonize=myfirstweb.log

# 主进程
master=True

```
<li> 测试uwsgi（进入MyFirstWeb） 4.1 测试方法一 ​ 启动uwsgi <pre><code class="prism language-shell">(web)root@localhost:~# uwsgi --ini myfirstweb.ini
</code></pre> ​ 停止uwsgi <pre><code class="prism language-shell">(web)root@localhost:~# uwsgi --stop myfirstweb.pid
</code></pre> ​ 进程查看（无论启动还是关闭，都需要看一下进程） ​ Django中有代码任何的修改，都需要重新启动uwsgi <pre><code class="prism language-shell">(web)root@localhost:~# ps aux|grep 'uwsgi'
</code></pre> 4.2 测试方法二 <pre><code class="prism language-shell">(web)root@localhost:~# uwsgi --http :8000 --module myfirstweb.wsgi
</code></pre> </li>
##### 9.安装NGINX
1. 安装
```
(web)root@localhost:~# apt-get install nginx

```

​ 验证：浏览器直接输入虚拟机的ip直接回车
1. 配置NGINX
```
(web)root@localhost:~# vim /etc/nginx/sites-enabled/default

```

```
location / {
		#First attempt to serve request as file, then
		#as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;

		uwsgi_pass 127.0.0.1:8000;
		include /etc/nginx/uwsgi_params;
}
#项目静态文件的绝对路径。即：告诉nginx应该去哪里找静态文件。
location /static {
        root /root/renjie/MyFirstWeb_static;
}

```

​ 保存退出，重启NGINX服务

```
(web)root@localhost:~# /etc/init.d/nginx restart

```

​ 重启成功后显示如下： ​ [ ok ] Restarting nginx (via systemctl): nginx.service. ​ 若是失败了：（会判断语法是否错误，会给行号）

```
(web)root@localhost:~# nginx -t
(web)root@localhost:~# vim /etc/nginx/nginx.conf
# 修改为 user root;

```

​ 进程查看（无论启动还是关闭，都需要看一下进程）

```
(web)root@localhost:~# ps aux|grep 'nginx'

```
1. setting添加
```
STATIC_ROOT = '/root/renjie/MyFirstWeb_static/static'

```
1. 把静态文件收集到 STATIC_ROOT中执行命令
```
(web)root@localhost:~# python manage.py collectstatic

```

启动NGINX

```
/etc/init.d/nginx start
或者 service nginx start

```

停止NGINX

```
/etc/init.d/nginx stop
或者 service nginx stop

```

重启NGINX

```
/etc/init.d/nginx restart
或者 service nginx restart

```

nginx日志位置

```
异常：/var/log/nginx/error.log
正常：/var/log/nginx/access.log

```

宗介：到这里呢 ~~ 我们基本就把Django项目所依赖的环境就搭建好了。

如有问题请及时联系本作者邮箱：wurenjie8@163.com

参考链接：

Django学习视频：https://www.bilibili.com/video/BV1vK4y1o7jH?from=search&amp;seid=659747147674964351

python虚拟环境创建：https://3g.163.com/dy/article/FEFB3H4B05315PUD.html?from=history-back-list

MySQL初始化：https://blog.csdn.net/weixx3/article/details/80782479


--- 
title:  小白如何在Ubuntu18.04上搭建Linux、Nginx、MySQL和PHP环境（LEMP stack） 
tags: []
categories: [] 

---
## 简介

LEMP是用来搭建动态网站的一组软件，首字母缩写分别表示**L**inux、Nginx（**E**ngine-X）、**M**ySQL和**P**HP。 本文将讲述如何在Ubuntu18.04上安装**LEMP**套件。当然，首先要安装Ubuntu18.04操作系统，接着按照以下方法完成其他组建的安装。

## 前言

以下演示将通过非管理员账号进行，即通过`sudo`命令完成安装，如果是普通账号（非管理员）可继续往下看。

#### 步骤一：安装Nginx网站服务器

```
 ~# sudo apt update
 ~# sudo apt dist-upgrade 
 ~# sudo apt install nginx

```

在`Ubuntu18.04`上，使用以上两条命令完成nginx安装就可以通过`localhost`访问了， 若访问失败，可能是已经安装了`Apache`等占用80端口的服务，或者是防火墙问题，若访问成功，应该如下图所示。 <img src="https://img-blog.csdnimg.cn/20200623194218572.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

`apt-get install`命令 1.下载的软件存放位置 `/var/cache/apt/archives` 2.安装后软件默认位置 `/usr/share` 3.可执行文件位置 `/usr/bin` 4.配置文件位置 `/etc` 5.lib文件位置 `/usr/lib` 软件安装完成后，可通过命令 `sudo dpkg -L`列出软件包所在的目录，及该软件包中的所有文件。以查看nginx的安装目录及相关文件为例，命令是`# sudo dpkg -L nginx`，其结果显示如下图所示： `# sudo dpkg -L nginx`

<img src="https://img-blog.csdnimg.cn/2020092714424766.png#pic_center" alt="在这里插入图片描述"> 大家还可通过命令 `sudo dpkg -l` 查看软件包的版本信息。以查看nginx的版本为例： `# sudo dpkg -l nginx`

<img src="https://img-blog.csdnimg.cn/20200927144453617.png#pic_center" alt="在这里插入图片描述">

#### 步骤二：安装MySQL数据库

```
~# sudo apt install mysql-server-5.7

```

执行该条命令安装`MySQL`，但仍不能使用，需要进行配置。考虑到安全问题，这里将通过一个脚本程序来完成`MySQL`的权限配置。

```
~# sudo mysql_secure_installation

```

执行该条命令，将会提示是否开启密码验证，如下所示，输入`Y`后按回车。

```
VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?
Press y|Y for Yes, any other key for No:

```

然后，就会问设置密码的强度，可以根据提示按实际需要选择，这里选择`0`。

```
There are three levels of password validation policy:
LOW    Length &gt;= 8
MEDIUM Length &gt;= 8, numeric, mixed case, and special characters
STRONG Length &gt;= 8, numeric, mixed case, special characters and dictionary                  file
Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0

```

接着，提示设置密码，连续输入两次密码后，会提示是否继续使用提供的密码修改其它选项，输入`N`后回车完成密码设置。

```
Please set the password for root here.
New password:
Re-enter new password: 

```

```
Estimated strength of the password: 100 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y

```

```
有些厂商提供的服务器上面输入 n 后会进入密码重置的循环，所以只能输 y 继续
如果这里输入y，就会出现以下选项

By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.
Remove anonymous users? (Press y|Y for Yes, any other key for No) :y
大致意思是：默认情况下，MySQL安装有一个匿名用户，允许任何人登录MySQL，而不必为他们创建用户帐户。这只是为了测试，并使安装进行更顺利一点。你应该在正式使用之前移除它们。是否删除匿名用户？

 ... skipping.
 
 
Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.
为了安全应该yes
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y
 
 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.
 默认情况下，MySQL附带一个名为“test”的数据库，任何人都可以访问。这也仅用于测试， 在正式投入使用前应将其移除。 
为了安全应该yes
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : No  
 
 ... skipping.
Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.
 重新加载特权表将确保所有更改 到目前为止，将立即生效。
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.
 

```

MySQL5.7默认情况下，`root`用户使用的是`auth_socket`插件进行身份认证，所以通过账号密码的方式是无法登陆的，比如`php`通过`root`和`password`的方式连接数据库会失败。 为了能够使MySQL5.7的`root`账号能够使用密码进行登陆，可以按照以下方法修改权限。

```
~# sudo mysql

```

通过该条命令使用`MySQL`自带的客户端连接数据库服务器，然后输入以下命令查看`root`的登陆验证方式。

```
mysql&gt; SELECT user,authentication_string,plugin,host FROM mysql.user;

```

```
+------------------+-------------------------------------------+-----------------------+-----------+
| user             | authentication_string                     | plugin                | host      |
+------------------+-------------------------------------------+-----------------------+-----------+
| root             |                                           | auth_socket           | localhost |
| mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| debian-sys-maint | *CC744277A401A7D25BE1CA89AFF17BF607F876FF | mysql_native_password | localhost |
+------------------+-------------------------------------------+-----------------------+-----------+
4 rows in set (0.00 sec)

```

可以看到，`root`账号使用的`auth_socket`登陆验证方式，需要将它改为`mysql_native_password`方式。

```
mysql&gt; ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root密码';

```

>  
 注意：将`root`密码修改为你上面设置的数据库密码再执行以上命令，如该密码可用于`php`连接数据库时使用。 


```
mysql&gt; FLUSH PRIVILEGES;

```

执行该条命令更新下配置，输入以下命令，再次查看`root`账号的登陆验证方式。

```
mysql&gt; SELECT user,authentication_string,plugin,host FROM mysql.user;

```

```
Output
+------------------+-------------------------------------------+-----------------------+-----------+
| user             | authentication_string                     | plugin                | host      |
+------------------+-------------------------------------------+-----------------------+-----------+
| root             | *3636DACC8616D997782ADD0839F92C1571D6D78F | mysql_native_password | localhost |
| mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| debian-sys-maint | *CC744277A401A7D25BE1CA89AFF17BF607F876FF | mysql_native_password | localhost |
+------------------+-------------------------------------------+-----------------------+-----------+
4 rows in set (0.00 sec)

```

可以看到，`root`的登陆验证方式已经从`auth_socket`变成`mysql_native_password`了。

```
mysql&gt; exit

```

退出`MySQL`客户端，届时，完成了`MySQL`安装和配置。

#### 步骤三：安装PHP和配置Nginx使用PHP处理器

通过以上操作，完成`Nginx`和`MySQL`的安装，而动态网页则是`PHP`的工作。 `Nginx`不像其他网站服务器自带`PHP`处理器，需要自己安装`php-fpm`，即`fastCGI process manager`，然后配置`Nginx`将客户端`PHP`请求传给它进行处理。

```
~# sudo apt install php-fpm php-mysql php-gd

sudo apt install php7.2-mysql php7.2-fpm php7.2-curl php7.2-xml php7.2-gd php7.2-mbstring php-memcached php7.2-zip

```

此时，`LEMP`全部所需的软件都安装好了，接着就是配置的工作了。 首先配置`Nginx`服务器区块的等级（服务器区块类似`Apache`服务器的虚拟站点）。服务器区块配置文件在`/etc/nginx/sites-available`目录下，这里新建的服务器区块的配置文件名为`hdpaii.com`，如下命令，创建`hdpaii.com`文件并进行编辑。

```
~# sudo nano /etc/nginx/sites-available/hdpaii.com

```

```
server {
        listen 80;
        root /var/www/html;
        index index.php index.html index.htm index.nginx-debian.html;
        server_name hdpaii.com;
        location / {
                try_files $uri $uri/ =404;
        }
        location ~ \.php$ {
               fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;

                fastcgi_index index.php;

                fastcgi_param SCRIPT_FILENAME /var/www/html$fastcgi_script_name;

                include fastcgi.conf;

                include fastcgi_params;
        }
        location ~ /\.ht {
                deny all;
        }
}

```

上述配置大概意思是： listen —— 网站监听端口，这里设置为80，即浏览器默认的HTTP端口号。

root —— 定义存储网站服务的文档根目录。

index —— 默认访问页,配置Nginx请求索引文件时优先处理index.php命名的文件。

server_name —— 网站访问域名，将此指令指向服务器的域名或公共IP地址。

location / —— 该区块有一个try_files命令，该指令检查是否存在满足URI请求的文件。如果Nginx找不到合适的文件，则会返回404错误。

location ~.php$ —— 该区块匹配.php后缀的文件并传给php-fpm进行处理,此位置块通过将Nginx指向fastcgi-php.conf配置文件和php7.2-fpm.sock文件来处理实际的PHP处理，该文件声明了与哪个套接字相关联php-fpm。检查/etc/php/7.0/fpm/pool.d/www.conf文件并查找“listen”行。

location ~ /.ht —— 该区块禁止.htaccess的访问,通过添加deny all指令，如果任何.htaccess文件碰巧进入文档根目录，它们将不会被提供给访问者。

保存以上配置后，通过创建软连接的方式，使配置文件能够被Nginx加载。

```
~# sudo ln -s /etc/nginx/sites-available/hdpaii.com /etc/nginx/sites-enabled/

```

然后测试配置文件是否正常。

```
~# sudo nginx -t

```

配置正常的话，就可以重新启动nginx使配置生效了。

```
~# sudo nginx -s reload

```

#### 步骤四：创建PHP文件和访问测试

在配置`nginx`时定义了网站根目录为`/var/www/html/`，可以在此目录创建`PHP`网页供访问测试。

```
~# sudo nano /var/www/html/info.php

```

```
&lt;?php
phpinfo();
?&gt;

```

保存后，打开浏览器输入`http://hdpaii.com/info.php`，访问成功的话，可以看到如下截图的类似界面。 <img src="https://img-blog.csdnimg.cn/20200624134823732.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Zjampsag==,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> 为了安全，该信息不应该被客户端看到，当测试访问正常后，应当将该文件删除。

```
~# sudo rm /var/www/html/info.php

```

重启服务

```
~# sudo service php7.2-fpm restart
~# sudo service nginx restart 

```

#### 安装phpmyadmin

```

~#  sudo apt-get install phpmyadmin(用上面安装的mysql设置的密码)

~#  sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin(配置nginx服务器，一般是8090端口)

```

在客户端网址中输入http://域名/phpmyadmin 就可以看到phpmyadmin的登录界面了

#### 总结

通过以上步骤的操作，`LEMP`已经能够正常使用了，但真正在网站发布时，仍需要根据实际情况进行配置部署。另外，`Nginx`能够支持`https`协议，使网站更安全。**

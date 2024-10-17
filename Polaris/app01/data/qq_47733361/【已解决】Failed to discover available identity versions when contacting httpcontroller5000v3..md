
--- 
title:  【已解决】Failed to discover available identity versions when contacting http://controller:5000/v3. 
tags: []
categories: [] 

---
输入**openstack domain create --description “An Example Domain” example**命令后出现错误：

>  
 Failed to discover available identity versions when contacting http://controller:5000/v3. Attempting to parse version from URL. Unable to establish connection to http://controller:5000/v3/auth/tokens: HTTPConnectionPool(host=‘controller’, port=5000): Max retries exceeded with url: /v3/auth/tokens (Caused by NewConnectionError(’&lt;requests.packages.urllib3.connection.HTTPConnection object at 0x7f61db3410d0&gt;: Failed to establish a new connection: [Errno 111] \xe6\x8b\x92\xe7\xbb\x9d\xe8\xbf\x9e\xe6\x8e\xa5’,)) 


<img src="https://img-blog.csdnimg.cn/787f28ba3c004ca189d65d00cb692ce6.png" alt="在这里插入图片描述">

## 解决方法：

### 一、输入如下指令，确保35357端口开启

```
netstat -anpt | grep 35357

```

若没反应进行下面操作！

### 二、设置/etc/httpd/conf.d/wsgi-keystone.conf文件

使用下面指令进入vi编辑器进行编辑：

```
vim /etc/httpd/conf.d/wsgi-keystone.conf

```

复制下面内容进入文件，保存退出：

```
Listen 5000

Listen 35357

&lt;VirtualHost *:5000&gt;

WSGIDaemonProcess keystone-public processes=5 threads=1 user=keystone group=keystone display-name=%{<!-- -->GROUP}

WSGIProcessGroup keystone-public

WSGIScriptAlias / /usr/bin/keystone-wsgi-public

WSGIApplicationGroup %{<!-- -->GLOBAL}

WSGIPassAuthorization On

LimitRequestBody 114688

&lt;IfVersion &gt;= 2.4&gt;

ErrorLogFormat "%{cu}t %M"

&lt;/IfVersion&gt;

ErrorLog /var/log/httpd/keystone.log

CustomLog /var/log/httpd/keystone_access.log combined

&lt;Directory /usr/bin&gt;

&lt;IfVersion &gt;= 2.4&gt;

Require all granted

&lt;/IfVersion&gt;

&lt;IfVersion &lt; 2.4&gt;

Order allow,deny

Allow from all

&lt;/IfVersion&gt;

&lt;/Directory&gt;

&lt;/VirtualHost&gt;

&lt;VirtualHost *:35357&gt;

WSGIDaemonProcess keystone-admin processes=5 threads=1 user=keystone group=keystone display-name=%{<!-- -->GROUP}

WSGIProcessGroup keystone-admin

WSGIScriptAlias / /usr/bin/keystone-wsgi-admin

WSGIApplicationGroup %{<!-- -->GLOBAL}

WSGIPassAuthorization On

ErrorLogFormat "%{cu}t %M"

ErrorLog /var/log/httpd/keystone-error.log

CustomLog /var/log/httpd/keystone-access.log combined

&lt;Directory /usr/bin&gt;

Require all granted

&lt;/Directory&gt;

&lt;/VirtualHost&gt;

Alias /identity /usr/bin/keystone-wsgi-public

&lt;Location /identity&gt;

SetHandler wsgi-script

Options +ExecCGI

WSGIProcessGroup keystone-public

WSGIApplicationGroup %{<!-- -->GLOBAL}

WSGIPassAuthorization On

&lt;/Location&gt;

```

**注：vi编辑器保存退出方法** 在修改完上述内容后，按Esc键，输入 **:wq** ，然后回车即可保存退出。

### 三、重启httpd服务

输入下面指令，重启httpd服务：

```
systemctl restart httpd

```

### 四、完结撒花（运行成功）

<img src="https://img-blog.csdnimg.cn/bf1b29cfea554564bec2911c2aac708e.png" alt="在这里插入图片描述">

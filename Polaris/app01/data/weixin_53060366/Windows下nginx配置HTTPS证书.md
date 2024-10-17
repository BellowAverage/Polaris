
--- 
title:  Windows下nginx配置HTTPS证书 
tags: []
categories: [] 

---
## Windows下nginx配置HTTPS证书

### 一、openssl安装教程：

官网下载：openSSL: http://slproweb.com/products/Win32OpenSSL.html

<img src="https://img-blog.csdnimg.cn/222e24be6c184aecb137734595639815.png#pic_center" alt="在这里插入图片描述">

#### 1、双击 Win64OpenSSL_Light-3_1_0.exe

#### 2、安装 openssl

<img src="https://img-blog.csdnimg.cn/0f35925bada54e8ba7bed855c0d03055.png#pic_center" alt="在这里插入图片描述">

#### 3、选择安装路径：安装在nginx根目录下。

<img src="https://img-blog.csdnimg.cn/7df7b7ef5b81459dbe3473c7e64ae5f6.png#pic_center" alt="在这里插入图片描述">

#### 4、接下来默认即可，一直点击 Next。一直到finish。

<img src="https://img-blog.csdnimg.cn/d203cc938c6f47e7af8cc71679ace018.png#pic_center" alt="在这里插入图片描述">

### 二、配置 **OpenSSL** 环境变量：

#### 1）在系统变量中添加**OpenSSL**，地址为安装路径。

右击此电脑 --》点击属性 --》点击高级系统设置 --》点击环境变量 --》找到系统变量，点击新建。

将变量名和变量值填入。（变量值为OpenSSL的bin目录）

<img src="https://img-blog.csdnimg.cn/92c1e76b0735438e933a1c0ebfffeb13.png#pic_center" alt="在这里插入图片描述">

#### 2）在系统变量 **PATH** 中添加 **%OpenSSL%**

找到 Path --》 点击编辑 --》点击新建 --》填写%OpenSSL%–》一直点击确定即可。

<img src="https://img-blog.csdnimg.cn/912d0566db5449b697059b10908cc4eb.png#pic_center" alt="在这里插入图片描述">

### 三、使用OpenSSL命令生成https证书：
- 在 nginx文件夹下创建**ssl**文件夹，用于存放证书。- 在创建的**ssl**文件夹下打开系统窗口。- 创建私钥，设置一个自己的密码，后面会用到。
```
创建私钥: openssl genrsa -des3 -out 666tp.key 1024
这里需要输入密码：123456

创建csr证书：openssl req -new -key 666tp.key -out 666tp.csr
输入密码：123456
接下来一直回车即可，全部默认。

复制文件： copy 666tp.key 666tp.key.copy

去除密码： openssl rsa -in 666tp.key.copy -out 666tp.key
输入密码：123456

生成 crt 证书： openssl x509 -req -days 365 -in 666tp.csr -signkey 666tp.key -out 666tp.crt

```

<img src="https://img-blog.csdnimg.cn/2e6f928fb2be4c1f9d75a5d4220a5974.png#pic_center" alt="在这里插入图片描述">

### 四、修改 nginx.conf配置文件：

证书生成完成，配置 nginx 配置文件。
- 打开nginx文件夹下\conf\nginx.conf
```
server {<!-- -->
       listen       443 ssl;
       server_name  localhost;

       ssl_certificate      D:/nginx/nginx-1.22.1/ssl/666tp.crt;
       ssl_certificate_key  D:/nginx/nginx-1.22.1/ssl/666tp.key;
       ssl_session_cache    shared:SSL:1m;
       ssl_session_timeout  5m;
       ssl_ciphers  HIGH:!aNULL:!MD5;
       ssl_prefer_server_ciphers  on;

       location / {<!-- -->
           root   html;
           index  index.html index.htm;
       }
    }

```
<li> 配置好后，重启nginx： <pre><code class="prism language-shell">nginx.exe -s reload
</code></pre> </li>-  查看 **nginx** 启动状态，启动成功后，使用https进行访问（以上为自签证书，可做为测试使用，但可能会提示不安全，需自行购买或申请证书） 
<img src="https://img-blog.csdnimg.cn/7adea704ed2d440caea023fcfb2fd27b.png#pic_center" alt="在这里插入图片描述">


--- 
title:  华为云云耀云服务器L实例评测｜个人博客搭建 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/e3e3838380f247d3844d9acebc96c315.png#pic_center" alt="在这里插入图片描述"> 

#### 文章目录
- - <ul><li>- - - - 


本文详细介绍一下使用`华为云云耀云服务器L实例`搭建个人博客的全过程，希望能对大家有帮助。

<font color="red">**感谢华为云提供的优惠券，直接打价格打下来。**</font>

## 1. 华为云云耀云服务器L实例介绍

### 1.1 产品介绍

  华为云云耀云服务器L实例是新一代开箱即用、面向中小企业和开发者打造的全新轻量应用云服务器。云耀云服务器L实例提供丰富严选的应用镜像，实现应用一键部署，助力客户便捷高效的在云端构建电商网站、Web应用、小程序、学习环境、各类开发测试等。

### 1.2 产品定位

  云耀云服务器L实例使用门槛较低，如果您是正在了解云计算服务的入门用户，或是需要在服务器中部署简单应用的个人开发者、中小企业，那么推荐您选择云耀云服务器L实例。

### 1.3 产品特色

<img src="https://img-blog.csdnimg.cn/7fb0646b9cbc4e749e5a6ec0f8dcbc1c.png#pic_center" alt="在这里插入图片描述">

  好了，<font color="red">`华为云云耀云服务器L实例`</font>的简单介绍就到这里，更加详细的介绍，请移步详细了解，已经心动的朋友们可以进行购买。

## 2. 简单配置

  购买完成之后，我们需要简单的对服务器进行一下配置。

  控制台地址：

<img src="https://img-blog.csdnimg.cn/0196814597dd4f87b3e6a496de421284.png#pic_center" alt="请添加图片描述">

  点击下面实例，进入到管理页面。

<img src="https://img-blog.csdnimg.cn/2c9afe3de2d4479dbf85a9758ae23c47.png#pic_center" alt="请添加图片描述">

  打开上面截图中的<font color="red">`流程引导`</font>，可以直接显示我们需要进行的配置，真的太贴心了，那么我们就跟着引导进行一步步的配置吧。

<img src="https://img-blog.csdnimg.cn/d3ad6353da014f668c03db6465fde901.png#pic_center" alt="请添加图片描述">

### 2.1 管理员密码设置

点击<font color="red">`设置/重置密码`</font>，进行管理员密码设置。

<img src="https://img-blog.csdnimg.cn/15c19a96e653434bb8e87288fe0cbe70.png#pic_center" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/bc831dca12b947eb976c7bc765834d72.png#pic_center" alt="请添加图片描述">

### 2.2 配置安全组

点击<font color="red">`配置规则`</font>，进行安全组设置。

<img src="https://img-blog.csdnimg.cn/1e3d79631a314a63b8457c3717468955.png#pic_center" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/cf5711bdf6fb427ea2708c5ea174e755.png#pic_center" alt="请添加图片描述">

**安全组配置说明:**
- 可以通过 <font color="red">`更改安全组`</font> 修改当前实例绑定的安全组，在对应的界面中有添加安全组的操作。- 一般情况下，我们直接修改当前绑定的安全组即可。- 推荐的入方向的端口，要保持`22`、`80`这些端口打开即可。 我自己的安全组配置了`22`、`80`、`443`、`8888`端口。
**端口介绍**

|端口|作用|备注
|------
|22|SSH协议远程连接|
|80|HTTP协议端口|
|443|HTTPS协议端口|没有https需求的可以不开启
|8888|宝塔Linux面板管理端口|宝塔Linux面板管理平台

## 3. 上传个人博客

  本人使用的`hexo`来生成的个人博客，这里就不再进行赘述了，感兴趣的小伙伴可以移步自行学习。

  最终生成的博客文件如下： <img src="https://img-blog.csdnimg.cn/218c8036a15745d089dfa6a96be35647.png#pic_center" alt="请添加图片描述">

  接下来，我们需要把这些文件打包，搬运到我们的<font color="red">`华为云云耀云服务器L实例`</font>服务器上面。直接使用`sftp`即可。

```
# 1. 压缩博客文件
cd my_blog
zip -r my_blog.zip .

# 2. 链接服务器
sftp root@ip地址
# 输入密码

# 进入home目录，我们把博客文件放到这里
cd /home

# 传输文件
put {<!-- -->文件全路径}/my_blog.zip


```

接下来，我们把上传的文件进行一下解压缩。这个时候是在我们已经退出`sftp`的情况下。

```
ssh root@ip地址
# 输入密码
# 进入home目录
cd /home
# ls 查看文件是否存在，不要放错了位置

# 解压缩 添加-d 解压到my_blog 这个目录里面
unzip -d my_blog my_blog.zip


```

  至此，我们已经把博客文件全部放到<font color="red">`华为云云耀云服务器L实例`</font>服务器上面了。

## 4. nginx安装和配置

nginx的安装步骤如下所示：

```

# 安装
apt install nginx
# 查看配置文件路径
nginx -t


```

修改配置文件如下：

```


#user  nobody;
worker_processes  1;

events {
    worker_connections  1024;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                     '$status $body_bytes_sent "$http_referer" '
                     '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  3000;

    #gzip  on;

    log_format access '$remote_addr - $remote_user [$time_local] "$request" '
            '$status $body_bytes_sent "$http_referer" '
            '"$http_user_agent" $http_x_forwarded_for';

    server {
        listen 0.0.0.0:80;
        listen [::]:80;
        server_name 你的IP;

        access_log  /etc/nginx/my_blog.log  main;

        location / {
            root /home/my_blog;
            autoindex on;
            index index.html;
        }
    }

}


```

## 5. 启动服务

```
# 直接启动nginx即可
nginx

```

<img src="https://img-blog.csdnimg.cn/5211e518d39c452b871a4f2e035a3dea.png#pic_center" alt="在这里插入图片描述">

## 6. 总结

  通过以上的步骤进行操作，大家应该可以自己动手操作完成个人博客的一个搭建了，当然，最最重要的，还是我们的<font color="red">`华为云云耀云服务器L实例`</font>服务器。这一步步走下来，个人体会到的是简便和好用，从购买到设置，他都在一步步的引导着我应该怎么操作，详细的介绍文档也能在关键时刻给予我帮助。

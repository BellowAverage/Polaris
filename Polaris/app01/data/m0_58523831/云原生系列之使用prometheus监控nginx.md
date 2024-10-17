
--- 
title:  云原生系列之使用prometheus监控nginx 
tags: []
categories: [] 

---
#### 文章目录
- - - <li> 
  <ul>- - - - - - - - - - - - - <li> 
    <ul>- - - - - - - - - - - - - - - - - 
## 一. 实验环境

本次实验环境见下表：

|操作系统|服务器IP|hostname
|------
|centos7.9|10.0.0.7|mufengrow7
- 查看操作系统
```
[root@mufengrow ~]# cat /etc/redhat-release 
CentOS Linux release 7.9.2009 (Core)

```
- 查看hostname
```
# 修改hostname
[root@mufengrow ~]# hostname mufengrow7
[root@mufengrow ~]# bash

# 查看hostname
[root@mufengrow7 ~]# hostname
mufengrow7

```
- 查看ip
```
[root@mufengrow7 ~]# ifconfig |grep inet |awk 'NR==1{print $2}'
10.0.0.7

```

本文中的prometheus监控软件已经安装好了，如果你还没安装，可以参考上一篇文章：

更多内容关注csdn 【我是沐风晓月】

## 二. nginx-vts-exporter简介

### 2.1 如何获取nginx exporter

我们可以从prometheus官方的下载页面上看到，prometheus官方并没有提供官方对nginx的监控exporter。

那我们要怎么通过prometheus监控nginx呢？

在prometheus官方的下载页面，里面有提供一些比较好的第三方开源的exporter供我们使用。

prometheus官方下载页面：https://prometheus.io/download/

<img src="https://img-blog.csdnimg.cn/b6c8dd1913044e7d9695fdebe137ca6e.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/d59c053aeeef40d0b1fbeefd6d28aefc.png" alt="请添加图片描述">

### 2.2 nginx-vts-exporter简介

我们都知道，nginx可以通过“ngx_http_stub_status_module”模块来显示自身的状态信息。但是状态页面显示的出来的结果又比较的简单，而且不符合prometheus采集数据的规范。所以就有人针对`nginx`开源了一款prometheus监控nginx的exproter——“nginx-vts-exporter”。

nginx-vts-exporter的github地址：

通过查看github介绍可以知道该exproter不像官方提供的exporter一样简单的安装上了就可以采集数据。它需要nginx在编译安装的时候加上一个第三方的模块“nginx-module-vts”。通过这个第三方模块，将nginx更加详细的数据展示出来，然后通过“nginx-vts-exporter”进行采集展示，最后由prometheus进行采集汇总。

第三方模块的github地址：

### 2.3 nginx-module-vts简介

“nginx-module-vts”是一个第三方的`nginx模块`，提供了对nginx状态信息的访问。

“nginx-module-vts”模块提供了几种方式展示自己的状态，这个之后会说明。

但是“nginx-module-vts”模块对nginx的版本的支持是有要求的，在nginx1.4.x之前的版本都不支持。使用的时候需要注意。<img src="https://img-blog.csdnimg.cn/63b6a9b747c140b087f1624d247c29d7.png" alt="请添加图片描述">

## 三. 安装nginx1.22

### 3.1 下载nginx源码

下载`nginx-1.22`的源码

```
[root@mufengrow7 ~]# cd /usr/local/src/
[root@mufengrow7 ~]# wget http://nginx.org/download/nginx-1.22.1.tar.gz

```

### 3.2 下载nginx-module-vts模块

下载nginx-module-vts用于之后的nginx编译安装

```
[root@mufengrow7 src]# wget https://github.com/vozlt/nginx-module-vts/archive/refs/tags/v0.2.1.tar.gz

```

### 3.3 解压所有源码

解压nginx1.22的源码和解压nginx-module-vts模块的源码

```
#解压nginx1.22源码
[root@mufengrow7 src]# tar zxf nginx-1.22.1.tar.gz 
#解压nginx-module-vts模块源码
[root@mufengrow7 src]# tar zxf v0.2.1.tar.gz

```

代码注释：

`z`：指定解压的文件有gzip属性

`x`：从归档文件中解压出文件。

`f`：使用指定使用哪个归档文件。

### 3.4 安装编译nginx需要的依赖

编译安装nginx需要解决openssl和pcre的依赖，所以要提前将这两个包安装上

```
[root@mufengrow7 src]# yum install -y openssl-devel pcre-devel

```

### 3.5 编译安装nginx

编译安装nginx1.22，但是要注意的是我们需要在编译的参数里加上添加模块的参数“–add-module”，然后指向“nginx-module-vts”模块的源码路径

```
#进入nginx源码目录
[root@mufengrow7 src]# cd nginx-1.22.1/
#指定编译安装的参数，并进行检查，生成Makefile文件
[root@mufengrow7 nginx-1.22.1]# ./configure --prefix=/apps/nginx \
&gt; --with-http_ssl_module \
&gt; --with-http_v2_module \
&gt; --with-http_realip_module \
&gt; --with-http_stub_status_module \
&gt; --with-http_gzip_static_module \
&gt; --with-pcre \
&gt; --with-file-aio \
&gt; --with-stream \
&gt; --with-stream_ssl_module \
&gt; --with-stream_realip_module \
&gt; --add-module=/usr/local/src/nginx-module-vts-0.2.1/ #指向“nginx-module-vts”模块源码的目录
#编译安装nginx
[root@mufengrow7 nginx-1.22.1]# make &amp;&amp; make install
#查看nginx安装信息
[root@mufengrow7 nginx-1.22.1]# /apps/nginx/sbin/nginx -V
nginx version: nginx/1.22.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC) 
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: --prefix=/apps/nginx --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_stub_status_module --with-http_gzip_static_module --with-pcre --with-file-aio --with-stream --with-stream_ssl_module --with-stream_realip_module --add-module=/usr/local/src/nginx-module-vts-0.2.1/ #可以看到“nginx-module-vts”模块已经安装到nginx里了

```

代码注释：

`-V`：显示nginx版本和安装的配置

### 3.6 修改nginx配置文件

有人在想，如何修改nginx的配置文件才能让nginx的状态显示出来？

“nginx-module-vts”的github网页已经给出配置了<img src="https://img-blog.csdnimg.cn/1d43571dd6094e52b9843dfd58ce3bbe.png" alt="请添加图片描述"> 根据“nginx-module-vts”官方给除的配置修改nginx的配置文件，让nginx能展示出自己的状态。

```
#进入nginx的安装目录
[root@mufengrow7 nginx]# cd /apps/nginx/
#修改nginx的配置
[root@mufengrow7 nginx]# vim conf/nginx.conf
......
http {
    ......;
    vhost_traffic_status_zone;
    ......;
    server{
        ......;
        location /status {
            vhost_traffic_status_display;
            vhost_traffic_status_display_format html;
        }
    }
}

```

### 3.7 检查nginx配置文件语法

修改配置文件后，需要检查nginx配置文件语法，查看是否出现语法上的错误

```
[root@mufengrow7 nginx]# ./sbin/nginx -t
nginx: the configuration file /apps/nginx/conf/nginx.conf syntax is ok #这里显示ok就证明语法没问题，可以启动nginx
nginx: configuration file /apps/nginx/conf/nginx.conf test is successful

```

代码注释：

`-t`：检查配置文件。

### 3.8 启动nginx

启动nginx

```
[root@mufengrow7 nginx]# ./sbin/nginx

```

### 3.9 查看nginx启动情况

```
[root@mufengrow7 nginx]# ps -ef | grep nginx | grep -v grep
root       5358      1  0 12:00 ?        00:00:00 nginx: master process ./sbin/nginx
nobody     5359   5358  0 12:00 ?        00:00:00 nginx: worker process

```

代码注释：
-  `-ef`：在`-ef`里可以分出两个选项`-e`和`-f` -  `-e`：显示所有执行程序的进程（除会话领导者与终端关联的进程） -  `-f`：显示UID,PPIP,C与STIME栏位 -  `-v`：选择不匹配的行 
### 3.10 登录网页验证模块

#### 3.10.1 使用“nginx-module-vts”默认模式查看nginx状态

浏览器访问：

```
10.0.0.7/status

```

进入网页后，我们能看到模块给我们现实的结果

<img src="https://img-blog.csdnimg.cn/4ab2677f7d0e4774b1526f4a38d1b307.png" alt="请添加图片描述">

#### 3.10.2 使用“nginx-module-vts”其他模式查看nginx状态

“nginx-module-vts”内置了4种查看`nginx状态`的格式，我们上一点已经展示过使用html格式来展示nginx的状态，接下来我们会用“json”、“jsonp”、“prometheus”来展示nginx的状态。
- “json”格式
浏览器访问：http://10.0.0.7/status/format/json

<img src="https://img-blog.csdnimg.cn/dbaa6b3225bf431eac9c09a244972bb4.png" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/0342d6061b9a4e7db83ae422abfaf7ec.png" alt="请添加图片描述">

## 四. 安装nginx-vts-exporter

### 4.1 下载nginx_vts_exporter

下载nginx_vts_exporter二进制包

```
#进入安装目录
[root@mufengrow7 nginx]# cd /apps
#下载nginx_vts_exporter二进制包
[root@mufengrow7 apps]# wget https://github.com/hnlq715/nginx-vts-exporter/releases/download/v0.10.3/nginx-vts-exporter-0.10.3.linux-amd64.tar.gz

```

### 4.2 解压nginx_vts_exporter

对nginx_vts_exporter二进制包进行`解压`

```
[root@mufengrow7 apps]# tar xf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz
[root@mufengrow7 apps]# cd nginx-vts-exporter-0.10.3.linux-amd64/

```

解压后可以看到里面之后一个可执行文件

```
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# ls
LICENSE  nginx-vts-exporter

```

### 4.3 查看帮助文档

```
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# ./nginx-vts-exporter --help
Usage of ./nginx-vts-exporter:
  -insecure
    	Ignore server certificate if using https (default true)
  -metrics.namespace string
    	Prometheus metrics namespace. (default "nginx")
  -nginx.scrape_timeout int
    	The number of seconds to wait for an HTTP response from the nginx.scrape_uri (default 2)
  -nginx.scrape_uri string
    	URI to nginx stub status page (default "http://localhost/status")
  -telemetry.address string
    	Address on which to expose metrics. (default ":9913")
  -telemetry.endpoint string
    	Path under which to expose metrics. (default "/metrics")
  -version
    	Print version information.

```

为了更直观一些，我们把参数用表格来展示：

|参数|描述
|------
|-insecure|如果使用https，忽略服务器证书(默认为true)
|-metrics.namespace|prometheus的metrics的命名空间（默认是nginx）
|-nginx.scrape_timeout|等待来自nginx的HTTP相应的秒数（默认是2秒）
|-nginx.scrape_uri|指定nginx状态页面的URI（默认是"http://localhost/status"）
|-telemetry.address|exporter暴露的端口（默认是9913）
|-telemetry.endpoint|公开的metrics路径（默认是“/metrics”）
|-version|显示版本信息

### 4.4 启动nginx-vts-exporter

这里添加选项，让nginx-vts-exporter从nginx-module-vts的json格式下采集数据

```
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# nohup /apps/nginx-vts-exporter-0.10.3.linux-amd64/nginx-vts-exporter -nginx.scrape_uri http://localhost/status/format/json &amp;
[1] 5440
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# nohup: ignoring input and appending output to ‘nohup.out’ #出现日志文件路径信息，继续按回车
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# #回到标准输入的状态

```

### 4.5 查看nginx-vts-exporter启动状态

我们可以通过查看pid、端口和查看日志的方式确实“nginx-vts-exporter”的启动状态，通过下面的结果，我们可以看出“nginx-vts-exporter”已经在正常运行。

```
#查看pid
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# ps -ef | grep nginx-vts-exporter | grep -v grep
root       5440   1680  0 12:36 pts/0    00:00:00 /apps/nginx-vts-exporter-0.10.3.linux-amd64/nginx-vts-exporter
#查看端口
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# ss -tnl | grep 9913 | grep -v grep
LISTEN     0      128       [::]:9913                  [::]:*
#查看日志
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# tail -f nohup.out 
2023/03/07 12:36:37 Starting nginx_vts_exporter (version=0.10.3, branch=HEAD, revision=8aa2881c7050d9b28f2312d7ce99d93458611d04)
2023/03/07 12:36:37 Build context (go=go1.10, user=root@56ca8763ee48, date=20180328-05:47:47)
2023/03/07 12:36:37 Starting Server at : :9913
2023/03/07 12:36:37 Metrics endpoint: /metrics
2023/03/07 12:36:37 Metrics namespace: nginx
2023/03/07 12:36:37 Scraping information from : http://localhost/status

```

### 4.6 查看nginx-vts-exporter采集的数据

浏览器访问

10.0.0.7:9913/metrics

<img src="https://img-blog.csdnimg.cn/dcb88daed814474cb76b6581e358a7ce.png" alt="请添加图片描述">

## 五. 配置prometheus拉取数据

### 5.1 修改prometheus的配置文件

修改的方式如图：

其中job_name、prometheus读取配置文件的方式、目标的ip和端口都可以根据需求自行修改。 <img src="https://img-blog.csdnimg.cn/b897dbb12b9143da8fffaa0b4a407d4c.png" alt="请添加图片描述">

### 5.2 让prometheus重新读取配置文件
- 检查prometheus配置文件语法：
```
#进入prometheus安装目录
[root@mufengrow7 nginx-vts-exporter-0.10.3.linux-amd64]# cd /apps/prometheus
#执行命令检查语法
[root@mufengrow7 prometheus]# ./promtool check config prometheus.yml 
Checking prometheus.yml
 SUCCESS: prometheus.yml is valid prometheus config file syntax

```
- 重启prometheus
通过重启，让prometheus重新读取配置文件

```
[root@mufengrow7 prometheus]# systemctl restart prometheus

```

## 六.查看prometheus的监控数据

### 6.1 到网页端查看prometheus监控目标

我们到prometheus的网页端，查看prometheus采集数据的目标是否有有nginx，通过下图，我们知道`prometheus`已经有采集nginx的数据了。<img src="https://img-blog.csdnimg.cn/ee5e119cd89b4a31835e909820e539c0.png" alt="请添加图片描述">

### 6.2 在prometheus网页查询结果

接下来我们到prometheus的查询面板查看prometheus有没有采集到nginx的数据
- 查询nginx版本
<img src="https://img-blog.csdnimg.cn/e2770a452e46448eb731790fffbe7217.png" alt="在这里插入图片描述">
- 查看nginx出现“4XX”的次数
<img src="https://img-blog.csdnimg.cn/0e530a03c8b44159ad77401ffd7c3ba8.png" alt="请添加图片描述">
- 查看nginx的requests的次数 <img src="https://img-blog.csdnimg.cn/591c7f085367465ea914e108c00a0899.png" alt="请添加图片描述">- 计算nginx在一分钟内的QPS
如果通过prometheus内置函数计算QPS，可以参考文章：prometheus常用的内置函数

<img src="https://img-blog.csdnimg.cn/f630144dd3de4ba3873c981070499be6.png" alt="请添加图片描述"> 通过以上的查询，我们也知道了prometheus有采集到nginx-vts-exproter的数据

## 七、grafana导入模板

本文中的grafana已经安装好了，如果你还未安装，可以参考文章：

### 7.1 导入模板

`grafana模板`推荐编号：2949

导入模板：
-  输入模板编号，点击Load <img src="https://img-blog.csdnimg.cn/97ddef7b4b034d48bbc26855764b3574.png" alt="请添加图片描述"> -  点击import 
<img src="https://img-blog.csdnimg.cn/a4e12b4cb91c4465a3779574f579da07.png" alt="请添加图片描述">
- 修改数据源，点击Import <img src="https://img-blog.csdnimg.cn/8c3612a2299144dd92633462030237c2.png" alt="请添加图片描述">
### 7.2 查看模板效果<img src="https://img-blog.csdnimg.cn/ffb5e71d08024346be9b294f2237dace.png" alt="请添加图片描述">

思考：

既然“nginx-module-vts”有专门给prometheus采集的格式，那么是否可以直接通过prometheus采集“nginx-module-vts”的数据，而不必添加一个“nginx-vts-module”的中间件呢？

答案：prometheus可以直接采集“nginx-module-vts”的数据
- 修改配置文件，如下图： <img src="https://img-blog.csdnimg.cn/b639172e34f04083b329c4e7c6da3da5.png" alt="请添加图片描述">- Prometheus重启后，查看target <img src="https://img-blog.csdnimg.cn/2880e18491314113bd68a85e57e9f02c.png" alt="请添加图片描述">- 查询数据nginx的连接数
注意：对应的查询语句也要跟着改变，如果不知道查询语句的可以到“http://10.0.0.7/status/format/prometheus”进行查询

<img src="https://img-blog.csdnimg.cn/42d31729fc54447bb77aec6b7fc13105.png" alt="请添加图片描述">

## 八、Nginx常见监控指标

### 8.1 基本活跃指标

nginx的基本活跃指标是可以通过“ngx_http_stub_status_module”模块来获取的。

|名称|描述
|------
|Accepts（接受）|nginx接受客户端的连接数
|Handled（已处理）|成功处理客户端连接数
|Active（活跃）|当前活跃的客户端连接数
|Requests（请求数）|客户端请求书
|Waiting（等待）|正在等待的连接数
|Reading（读）|正在读操作的连接数
|Writing（写）|正在写操作的连接书

### 8.2 nginx的QPS

我们可以使用Prometheus的PromQL的内置函数进行计算。

通过nginx计算的QPS，我们可以看出nginx服务的请求情况，通过QPS监控，可以了解是否有恶意攻击和对nginx的可行性进行判断。

### 8.3 nginx错误率

通过对错误代码的监控，可以知道客户端收到的结果是否正确。如果某段时间内错误结果不断飙升，证明网站可能出现物体

错误代码为：4XX（表示客户端错误代码） 5XX（表示服务端错误代码）

## 九、总结

Prometheus监控nginx的步骤为：
1. 安装Prometheus1. 编译安装nginx，注意nginx需要安装“nginx-moudle-vts”模块1. 安装“nginx-vts-exporter”，在设置对应的参数后启动1. 修改Prometheus的配置文件，添加监控ngxin的实例，并重新读取配置文件1. 进入Prometheus的WEB页面进行查看
转载自：https://blog.csdn.net/wisdom_futrue/article/details/129392953

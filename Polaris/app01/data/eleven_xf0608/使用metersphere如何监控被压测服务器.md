
--- 
title:  使用metersphere如何监控被压测服务器 
tags: []
categories: [] 

---
在metersphere上做性能测试时，我们需要监控被压测服务器，

**需要在被压测系统所在的服务器安装对应的服务：**

**需要监控操作系统层面**：安装node_exporter，收集cpu、内存、磁盘、网络

**需要监控数据库层面**：安装mysqlld_exporter，收集当前的会话数据、缓存命中率、慢查询

**需要监控应用进程**，比如java进程的监控：安装：jmx_exporter，收集堆内存、栈内存、占的空间

**docker****容器层面的监控**等。

安装好上面的几个exporter之后，只需要在metersphere平台的页面上，添加对应的服务器ip和端口，以及需要添加的指标，页面上就能正常展示你想看到的数据

下面以node_exporter为例，讲解如何下载和安装这个服务。

**一、下载：**

node_exporter下载地址：https://github.com/prometheus/node_exporter/releases

<img alt="" height="672" src="https://img-blog.csdnimg.cn/a91bcf90254e4c23bc4e48bca6b35012.png" width="990">



下载完后里面有个可执行文件 ，把这个可执行文件运行起来，node_exporter服务就正常启动了。

其它的mysqlld_exporter、jmx_exporter等都是在github上面下载

**二、安装**

安装node_exporter方法：

**cd /apps/svr/node_exporter**  进入需要安装的目录（这里是我自己的目录，大家可以进入自己需要安装的目录，然后把文件**放到**这个目录下

**ll**  查看刚放进来的文件是否存在

**tar xf node_exporter-1.6.1.linux-amd64.tar.gz**  解压（这个命令只能解压.tar.gz这种格式，其它格式用其它命令）

**cd node_exporter-1.6.1.linux-amd64**  进入解压的这个目录

**ll** 查看一下当前目录的文件

**nohup ./node_exporter &amp;** 让它在后台运行（一定要加&amp;，表示后台运行，否则关掉连接，这个服务就关了）

**netstat -ntlup**   查看端口有没有启动

**三、其它组件及资源下载地址**
<td style="background-color:#0f6fc6;border-color:#ffffff #ffffff #000000;text-align:left;vertical-align:middle;width:121pt;">**组件及资源名称**</td><td style="background-color:#0f6fc6;border-color:#ffffff #ffffff #000000;text-align:left;vertical-align:middle;width:224pt;">**源码地址**</td><td style="background-color:#0f6fc6;border-color:#ffffff #ffffff #000000;text-align:left;vertical-align:middle;width:143px;">**用处**</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">Node Controller</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/metersphere/node-controller/releases</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">收集cpu、内存、磁盘、网络</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">mysqld_exporter</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/prometheus/mysqld_exporter/releases</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">收集当前的会话数据、缓存命中率、慢查询</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">Kafka</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/metersphere/jmeter-backend-listener-kafka</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">接收JMeter产生的性能测试结果数据。JMeter中用到了Kafka监听器插件</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">Data Streaming</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/metersphere/data-streaming</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">从Kafka中获取性能测试结果数据进行处理后存入 MySQL数据库</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">Docker Engine</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/metersphere/jmeter-image</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">为Node Controller提供JMeter Master容器运行环境</td>
<td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:121pt;">Chrome Plugin</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:224pt;">https://github.com/metersphere/chrome-extensions</td><td style="background-color:#ffffff;border-color:#000000;text-align:left;vertical-align:middle;width:143px;">浏览器插件，录制Web访问请求生成JMeter脚本，并导入到MeterSphere中用于接口测试及性能测试</td>

**四、在metersphere中添加被监控服务器**

<img alt="" height="596" src="https://img-blog.csdnimg.cn/6a5ed42c5b9d4e78b8168aa699eaecb6.png" width="1200">



**五、执行性能测试场景，查看被监控指标**

<img alt="" height="494" src="https://img-blog.csdnimg.cn/a44dd97a9a7f47db81f9e47af08dc22e.png" width="1200">



<img alt="" height="343" src="https://img-blog.csdnimg.cn/6884268421b94199abd170c7f59ce761.png" width="1200">

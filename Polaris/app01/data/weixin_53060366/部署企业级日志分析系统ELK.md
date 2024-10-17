
--- 
title:  部署企业级日志分析系统ELK 
tags: []
categories: [] 

---
## 部署企业级日志分析系统ELK



#### 文章目录
- - <ul><li>- <ul><li>- - - - - - - <ul><li>- - - - - - - - - - - - - - - - - - 


### 1、ELK日志分析系统简介：

#### 01）ELK：

是由Elasticsearch（日志存储和搜索）、Logstash（日志收集）、Kibana（查看日志）三个开源软件的组成的一个组合体，完成更强大的用户对日志的查询、排序、统计需求。

#### 02）Elasticsearch：

**ElasticSearch**：是基于Lucene（一个全文检索引擎的架构）开发的分布式存储检索引擎，用来存储各类日志。 **Elasticsearch** ：是用 Java 开发的，可通过 RESTful Web 接口，让用户可以通过浏览器与 Elasticsearch 通信。 **Elasticsearch**：是个分布式搜索和分析引擎，优点是能对大容量的数据进行接近实时的存储、搜索和分析操作。

#### 03）Logstash：
- **Logstash**：主要用于日志收集，同时可以对数据处理，并输出给 Elasticsearch。 Logstash 由JRuby 语言编写，运行在 Java 虚拟机（JVM）上，是一款强大的数据处理工具， 可以实现数据传输、格式处理、格式化输出。- Logstash 具有强大的插件功能，常用于日志处理。
#### 04）Kibana:

**Kiabana**：是基于 Node.js 开发的展示工具，可以为 Logstash 和 ElasticSearch 提供图形化的日志分析 Web 界面，可以汇总、分析和搜索重要数据日志。

#### 05）Filebeat：
- Filebeat：轻量级的开源日志文件数据搜集器。- 通常在需要采集数据的客户端安装 Filebeat，并指定目录与日志格式，Filebeat 就能快速收集数据，并发送给 logstash 进行解析，或是直接发给 Elasticsearch 存储，性能上相比运行于 JVM 上的 logstash 优势明显。
### 2、ELK的优点：
1. 处理方式灵活；1. 配置相对简单；1. 检索性能高效；1. 集群线性扩展；1. 前端操作绚丽；
### 3、ELK工作原理：
- 在所有需要收集日志的服务器上部署Logstash；或者先将日志进行集中化管理在日志服务器上，在日志服务器上部署 Logstash。- Logstash 收集日志，将日志格式化并输出到 Elasticsearch 群集中。- Elasticsearch 对格式化后的数据进行索引和存储。- Kibana 从 ES 群集中查询数据生成图表，并进行前端数据的展示。
### 4、ELK环境搭建：

#### 1、实验环境：

|主机|IP地址|软件
|------
|node1|192.168.111.10|elasticsearch，kibana
|node2|192.168.111.20|elasticsearch
|apache|192.168.111.30|logstash，Apache

#### 2、配置elasticsearch环境（node1、node2）

##### （1）关闭防火墙：

```
systemctl stop firewalld.service
setenforce 0

```

##### （2）添加IP，域名，修改主机名：

```
echo '192.168.111.10 node1' &gt;&gt; /etc/hosts
echo '192.168.111.20 node2' &gt;&gt; /etc/hosts

#node1（192.168.111.10）
hostnamectl set-hostname node1
#node2（192.168.111.20）
hostnamectl set-hostname node1
#Apache（192.168.111.30）
hostnamectl set-hostname apache

```

<img src="https://img-blog.csdnimg.cn/853c9d4685ec41e2bdccf82a8eb19146.png#pic_center" alt="在这里插入图片描述">

这里查看一下java版本：

```
[root@node1 ~]#java -version
openjdk version "1.8.0_131"
OpenJDK Runtime Environment (build 1.8.0_131-b12)
OpenJDK 64-Bit Server VM (build 25.131-b12, mixed mode)

```

JDK包含了Java的运行环境（即JRE）和Java工具。JRE包含了一个Java虚拟机（JVM）以及一些标准的类别函数库。总的来说，JDK、JRE、JVM三者都处在一个包含关系内，JDK包含JRE，而JRE又包含JVM。

具体地讲：

JDK = JRE + 开发工具集（例如Javac编译工具等）

JRE = JVM + Java SE标准类库 <img src="https://img-blog.csdnimg.cn/c686f58bc7b34fcdab49d423b9f781e3.png#pic_center" alt="在这里插入图片描述">

##### （3）安装elasticsearch：

```
cd /opt    #拉入软件包
rpm -ivh elasticsearch-5.5.0.rpm、
systemctl daemon-reload                  #重载后台进程
systemctl enable elasticsearch.service   #开启开局自启

```

<img src="https://img-blog.csdnimg.cn/c0e5ed91dab94c3bb0492c8e103dda41.png#pic_center" alt="在这里插入图片描述">

```
cp /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.bak

vim /etc/elasticsearch/elasticsearch.yml
cluster.name: my-elk_cluster                          #17行，集群名字
node.name: node1                                      #23行，节点名字，Node2节点为node2
path.data: /data/elk_data                             #33行，数据存放路径
path.logs: /var/log/elasticsearch/                    #37行，日志存放路径
bootstrap.memory_lock: false                          #43行，不在启动的时候锁定内存（前端缓存。与IOPS-性能测试方式，每秒读写次数相关）
network.host: 0.0.0.0                                 #55行，提供服务绑定的IP地址，0.0.0.0代表所有地址
http.port: 9200                                       #59行，侦听端口为9200
discovery.zen.ping.unicast.hosts: ["node1", "node2"]  #68行，集群发现通过单播实现

grep -v "^#" /etc/elasticsearch/elasticsearch.yml

```

<img src="https://img-blog.csdnimg.cn/eceb0504b5d44b4290f7fb9f459af1f6.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/97a28fee989748978c14c33c8564a4dc.png#pic_center" alt="在这里插入图片描述">

```
#创建数据存放路径并更改属主属组
mkdir -p /data/elk_data
chown elasticsearch:elasticsearch /data/elk_data/

#启动elasticsearch是否成功开启
systemctl start elasticsearch.service
netstat -natp | grep 9200

```

<img src="https://img-blog.csdnimg.cn/8bba9f955e034553896484f3fbac0599.png#pic_center" alt="在这里插入图片描述">

```
#查看节点信息
#浏览器访问  http://192.168.111.10:9200  、 http://192.168.111.20:9200 查看节点 Node1、Node2 的信息。

#浏览器访问 http://192.168.111.10:9200/_cluster/health?pretty  、 http://192.168.111.20:9200/_cluster/health?pretty查看群集的健康情况，可以看到 status 值为 green（绿色）， 表示节点健康运行。

#浏览器访问 http://192.168.111.10:9200/_cluster/state?pretty  检查群集状态信息。

```

<img src="https://img-blog.csdnimg.cn/1e0b1e8c5d00478bbea218deb80610ff.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/adcb1d385b5044d0b4efc733675a9d23.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c52dee00485649d9b4902aab799ecbea.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b74025c55bd4458481b5793f9cf10228.png#pic_center" alt="在这里插入图片描述">

#### 3、安装elasticsearch-head插件

**用上述方式查看集群，非常不方便，我们可以通过安装elasticsearch-head插件来管理集群。**

##### （1）编译安装node：

```
yum install -y gcc gcc-c++ make

cd /opt            #拉入软件包
tar zxvf node-v8.2.1.tar.gz
#cd到node-v8.2.1/
cd node-v8.2.1/
#编译安装（这里编译的时间较久）
./configure
make -j 2 &amp;&amp; make install

```

##### （2）安装 phantomjs（前端框架）

```
cd /opt           #拉入软件包
tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/src/
cd /usr/local/src/phantomjs-2.1.1-linux-x86_64/bin
cp phantomjs /usr/local/bin

```

##### （3）安装 Elasticsearch-head 数据可视化工具

```
cd /opt           #拉入软件包
tar zxvf elasticsearch-head.tar.gz -C /usr/local/src/
cd /usr/local/src/elasticsearch-head/
npm install

```

<img src="https://img-blog.csdnimg.cn/29dafc0bf4f0428b893fca4b5fafcc85.png#pic_center" alt="在这里插入图片描述">

##### （4）修改 Elasticsearch 主配置文件

```
vim /etc/elasticsearch/elasticsearch.yml
--大G到末尾添加以下内容--
http.cors.enabled: true				#开启跨域访问支持，默认为 false
http.cors.allow-origin: "*"			#指定跨域访问允许的域名地址为所有

systemctl restart elasticsearch

```

<img src="https://img-blog.csdnimg.cn/a5d2264c0acf438289f354123fef55e5.png#pic_center" alt="在这里插入图片描述">

##### （5）启动 elasticsearch-head 服务：

必须在解压后的 elasticsearch-head 目录下启动服务，进程会读取该目录下的 gruntfile.js 文件，否则可能启动失败。

```
cd /usr/local/src/elasticsearch-head/
npm run start &amp;

#elasticsearch-head 监听的端口是 9100
netstat -natp |grep 9100


```

<img src="https://img-blog.csdnimg.cn/12490f5e39f34b5bbe3a3eb117a013c4.png#pic_center" alt="在这里插入图片描述">

##### （6）通过 Elasticsearch-head 查看 Elasticsearch 信息：

```
通过浏览器访问 http://192.168.111.10:9100/ 地址并连接群集。如果看到群集健康值为 green 绿色，代表群集很健康。
在Elasticsearch 后面的栏目中输入http://192.168.111.10:9200  

```

<img src="https://img-blog.csdnimg.cn/fdd26ea7fd574a34b0ac47404cbc33f5.png#pic_center" alt="在这里插入图片描述">

##### （7）插入索引（node1）:

通过命令插入一个测试索引，索引为 index-demo，类型为 test。

```
curl -X PUT 'localhost:9200/index-demo/test/1?pretty&amp;pretty' -H 'content-Type: application/json' -d '{"user":"lisi","mesg":"hello world"}'

```

<img src="https://img-blog.csdnimg.cn/30276860ae824b0c92a70e125f63596e.png#pic_center" alt="在这里插入图片描述">
- 宿主机浏览器访问 http://192.168.111.10:9100/ 查看索引信息;- 可以看见索引默认被分片5个，并且有一个副本;- 点击数据浏览–会发现在node1上创建的索引为index-demo,类型为test, 相关的信息;
<img src="https://img-blog.csdnimg.cn/f8ea82b63ae74395937bc2edb3885123.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/3776525745d9493283f56861b7ece657.png#pic_center" alt="在这里插入图片描述">

#### 4、Logstash部署 （apache节点）

Logstash 一般部署在需要监控其日志的服务器。在本案例中，Logstash 部署在 Apache服务器上，用于收集 Apache 服务器的日志信息并发送到 Elasticsearch。

##### （1）安装Apahce服务（httpd）

```
yum -y install httpd
systemctl start httpd

```

##### （2）安装Java环境

```
java -version        #如果没有装 安装yum -y install java

```

##### （3）安装logstash

```
cd /opt                #拉入软件包
rpm -ivh logstash-5.5.1.rpm                           
systemctl start logstash.service                      
systemctl enable logstash.service

ln -s /usr/share/logstash/bin/logstash /usr/local/bin/

```

<img src="https://img-blog.csdnimg.cn/cfe657f2a0414ff9ae57d78cb9ab1b87.png#pic_center" alt="在这里插入图片描述">

##### （4）logstash（Apache）与elasticsearch（node）功能是否正常，做对接测试

```
Logstash常用选项

-f 通过这个选项可以指定logstash的配置文件，根据配置文件配置logstash
-e 后面跟着字符串 该字符串可以被当做logstash的配置（如果是” ”,则默认使用stdin做为输入、stdout作为输出）
-t 测试配置文件是否正确，然后退出

```

输入采用标准输入 、输出采用标准输出—登录192.168.111.30在Apache服务器上；

```
logstash -e 'input { stdin{} } output { stdout{} }'
......
The stdin plugin is now waiting for input:
13:05:22.995 [Api Webserver] INFO  logstash.agent - Successfully started Logstash API endpoint {<!-- -->:port=&gt;9600}
www.baidu.com										#键入内容（标准输入）
2020-12-22T03:58:47.799Z node1 www.baidu.com		#输出结果（标准输出）
www.sina.com									    #键入内容（标准输入）
2017-12-22T03:59:02.908Z node1 www.sina.com.cn		#输出结果（标准输出）
#ctrl+c 退出

```

```
logstash -e 'input { stdin{} } output { stdout{ codec=&gt;rubydebug } }'
... ...
The stdin plugin is now waiting for input:
13:08:46.338 [Api Webserver] INFO  logstash.agent - Successfully started Logstash API endpoint {<!-- -->:port=&gt;9600}
www.baidu.com
{<!-- -->
    "@timestamp" =&gt; 2018-10-12T02:15:39.136Z,
      "@version" =&gt; "1",
          "host" =&gt; "apache",
       "message" =&gt; "www.baidu.com"

```

```
logstash -e 'input { stdin{} } output { elasticsearch { hosts=&gt;["192.168.111.10:9200"] } }'
... ...
The stdin plugin is now waiting for input:
13:40:09.504 [Api Webserver] INFO  logstash.agent - Successfully started Logstash API endpoint {<!-- -->:port=&gt;9600}
www.baidu.com                    #输入内容
www.sina.com.cn                  #输入内容
www.google.com.cn                #输入内容

```

<img src="https://img-blog.csdnimg.cn/727ca3368b204c56891a0c73b34a9c7f.png#pic_center" alt="在这里插入图片描述">

**打开浏览器 输入http://192.168.111.10:9100/ 查看索引信息，发现多出 logstash-2021.12.30，点击数据浏览查看响应的内容**

<img src="https://img-blog.csdnimg.cn/b34cb04b70244c85a5994453d69a7fe0.png#pic_center" alt="在这里插入图片描述">

##### （5）logstash配置文件（Apache主机 做对接配置）

Logstash配置文件主要由三部分组成：input、output、filter（根据需要）

```
#配置文件中定义的是收集系统日志（system）
chmod +r /var/log/messages	
ll /var/log/messages

vim /etc/logstash/conf.d/system.conf
input {<!-- -->
	file{<!-- -->
		path =&gt;"/var/log/messages"						#指定要收集的日志的位置
		type =&gt;"system"									#自定义日志类型标识
		start_position =&gt;"beginning"					#表示从开始处收集
	}
}
output {<!-- -->
	elasticsearch {<!-- -->										#输出到 elasticsearch
		hosts =&gt; ["192.168.111.10:9200"]					#指定 elasticsearch 服务器的地址和端口
		index =&gt;"system-%{+YYYY.MM.dd}"					#指定输出的索引格式
	}
}

systemctl restart logstash 

```

<img src="https://img-blog.csdnimg.cn/d3fd5935e4a3428baa83d4088667e940.png#pic_center" alt="在这里插入图片描述">

#### 5、部署kibana（node1）

##### （1）安装kibana

```
cd /usr/local/src              
#拉入软件包
rpm -ivh kibana-5.5.1-x86_64.rpm

```

<img src="https://img-blog.csdnimg.cn/515d81c6d6fb41c3b2e950dfacb30ae8.png#pic_center" alt="在这里插入图片描述">

##### （2）修改kibana配置文件：

```
cd /etc/kibana/
cp kibana.yml kibana.yml.bak
vim kibana.yml

server.port: 5601                                   #2行，kibana打开的端口
server.host: "0.0.0.0"                              #7行，kibana侦听的地址
elasticsearch.url: "http://192.168.111.10:9200"     #21行，和elasticsearch建立联系
kibana.index: ".kibana"                             #30行，在elasticsearch中添加.kibana索引

systemctl start kibana.service         #启动kibana服务
systemctl enable kibana.service        #开机启动kibana服务

```

<img src="https://img-blog.csdnimg.cn/d8ed3a382cbc4ca78bbd2c78d03743e2.png#pic_center" alt="在这里插入图片描述">

##### （3）测试：

宿主机浏览器输入192.168.111.10:5601 首次登录创建一个索引 名字：system-* （这是对接系统日志文件） Index name or pattern #下面输入system-*，然后点最下面的出面的create 按钮创建

<img src="https://img-blog.csdnimg.cn/9ae5170fd0844685887edb3645e9641f.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/af456c593b734d048502535743903383.png#pic_center" alt="在这里插入图片描述">

**然后点下面的host旁边的add 会发现右面的图只有 Time 和host 选项了 这个比较友好。**

<img src="https://img-blog.csdnimg.cn/b00d21d933de4affb877fa59e263550c.png#pic_center" alt="在这里插入图片描述">

##### （4）对接Apache主机的Apache 日志文件（访问日志、错误日志）（apache节点）

```
cd /etc/logstash/conf.d/
touch apache_log.conf
vi apache_log.conf

input {<!-- -->
       file{<!-- -->
        path =&gt; "/etc/httpd/logs/access_log"
        type =&gt; "access"
        start_position =&gt; "beginning"
        }
       file{<!-- -->
        path =&gt; "/etc/httpd/logs/error_log"
        type =&gt; "error"
        start_position =&gt; "beginning"
        }
        
      }
output {<!-- -->
        if [type] == "access" {<!-- -->
        elasticsearch {<!-- -->
          hosts =&gt; ["192.168.111.10:9200"]
          index =&gt; "apache_access-%{+YYYY.MM.dd}"
          }
        }
        if [type] == "error" {<!-- -->
        elasticsearch {<!-- -->
          hosts =&gt; ["192.168.111.10:9200"]
          index =&gt; "apache_error-%{+YYYY.MM.dd}"
          }
        }
}
cd /etc/logstash/conf.d/
/usr/share/logstash/bin/logstash -f apache_log.conf

```

```
宿主机浏览器打开浏览器 输入http://192.168.111.10:9100/ 查看索引信息能发现 ：
apache_error-2019.04.16     apache_access-2019.04.16 

```

<img src="https://img-blog.csdnimg.cn/599cc179503240d3a9e73235fb5b8baf.png#pic_center" alt="在这里插入图片描述">

```
打开浏览器 输入http://192.168.111.10:5601
点击左下角有个management选项 &gt; index  patterns &gt; create index pattern &gt; 分别创建apache_error-* 和 apache_access-* 的索引

```

<img src="https://img-blog.csdnimg.cn/4edb6c0d1ca04157976e7d3ad53c47dc.png#pic_center" alt="在这里插入图片描述">

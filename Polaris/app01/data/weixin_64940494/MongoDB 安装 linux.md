
--- 
title:  MongoDB 安装 linux 
tags: []
categories: [] 

---
     

**目录**



















本文介绍一下MongoDB的安装教程。

系统环境：CentOS7.4 

可以用 cat /etc/redhat-release 查看本机的系统版本号

## 一、MongoDB版本选择

        当前最新的版本为7.0，但是由于7.0版本安装需要升级glibc2.25以上,所以这里我暂时不安装该版本。我们选择的是6.0.9版本。

## 二、MongoDB安装

        这里我们选用的是下载安装包的安装方式。

### 1. 安装地址

        进入MongoDB的安装包,如下图，选择版本为6.0.9，环境为CentOS7.0 X64，安装包类型为tgz。 

<img alt="" height="679" src="https://img-blog.csdnimg.cn/012766d786c0441b9b4fe4012dfec1a9.png" width="1147">

        鼠标移到 download按钮上右键，复制地址，如下图<img alt="" height="287" src="https://img-blog.csdnimg.cn/947a798847d44688b10ded6b0e819ef1.png" width="528">

###  2. 服务器下载安装

       进入服务器上下载安装包。这里我的安装地址是在 /usr/local/ 下。

>  
         cd /usr/local/ 
         wget  


        如果 wget 报以下错误时，可以直接在命令最后面添加 --no-check-certificate

>  
 To connect to ftp.gnu.org insecurely, use ‘--no-check-certificate’. 


        对安装包进行解压

>  
         tar -zxvf  mongodb-linux-x86_64-rhel70-6.0.9.tgz 


        解压后的文件名字太长，把文件名修改成简单的名字 mongodb

>  
         mv mongodb-linux-x86_64-rhel70-6.0.9 mongodb 


### 3. MongoDB配置

        进入到 mongodb目录下，新增data/db、data/log、conf 、tmp四个目录。

        data/db 数据存储的目录

        data/log 日志文件目录

        conf 配置文件目录

        tmp 用于其他临时文件目录，配置文件中pid文件存储在该目录

>  
         cd mongodb 
         mkdir -p data/db 
         mkdir -p data/log 
         mkdir conf 
         mkdir tmp 


        进入到conf目录下创建一个mongod.conf文件,并添加配置

>  
         cd conf/ 
         touch mongd.conf 
         vi mongod.conf 


        配置项如下

>  
 systemLog: #日志文件   destination: file   path: /usr/local/mongodb/data/log/mongodb.log    logAppend: true #storage Options storage: #数据存储配置   engine: "wiredTiger"   directoryPerDB: true   dbPath: /usr/local/mongodb/data/db   #indexBuildRetry: true   journal:     #是否启用持久性化     enabled: true #net Options net:   port: 27017   bindIp: localhost processManagement: #是否启用后台守护进程模式   fork: true   pidFilePath:  /usr/local/mongodb/tmp/mongo_27017.pid 


### 4. 启用MongoDB服务

>  
        /usr/local/mongodb/bin/mongod -f /usr/local/mongodb/conf/mongod.conf 


当出现successfully 则证明启动成功。

<img alt="" height="97" src="https://img-blog.csdnimg.cn/b01d075118f84b5a8394b4e922695217.png" width="1058">

也可以通过查看Mongod服务进程看是否启动成功。

>  
 ps -ef | grep mongod 


<img alt="" height="123" src="https://img-blog.csdnimg.cn/89b9466b2e2a436ab5b4fab455d17496.png" width="934">

 到这一步MongoDB服务则正式完成。

## 三、MongoSH安装

        从MongoDB6.0开始，则不会自带mongo客户端命令，则需要自己安装客户端MongoSH。

        安装步骤：

        先从官网下载，选择对应的安装包，这里我们选择的是不带openssl的安装包。<img alt="" height="607" src="https://img-blog.csdnimg.cn/d9d1f3c13751411a99388a98e9aa6792.png" width="1017">

        同样的操作右键复制链接地址

        回到服务器进行安装，我的安装目录还是 /usr/local/ 。

>  
         cd /usr/local/ 
         wget   


>  
         rpm -i mongodb-mongosh-1.10.5.x86_64.rpm 


        安装完成可以使用mongosh命令进入客户端，并正常使用MongoDB数据库了。

<img alt="" height="344" src="https://img-blog.csdnimg.cn/cf0c3b576bbf4fcf84fa92664ddc9d5a.png" width="1200">

         默认进入的是test数据库，可以使用use 命令切换数据库

<img alt="" height="74" src="https://img-blog.csdnimg.cn/9ef1f9d80b3f49aab68e618c06f8c3b7.png" width="925">

## 四、compass连接 

        进入compass客户端点击 new connection。我的compass版本是1.36.4，别的版本可能会有一些不一样。

<img alt="" height="198" src="https://img-blog.csdnimg.cn/01ebd9a3eaca4b18942af9c6dca8e3b3.png" width="1024">

advanced connectication options &gt; general

<img alt="" height="646" src="https://img-blog.csdnimg.cn/a42bb92a25194c95b9126eb95e45ed02.png" width="707">

 advanced connectication options &gt; proxy/SSH &gt; SSH with password

<img alt="" height="203" src="https://img-blog.csdnimg.cn/c96f21a5c88c4b04b1f25f7d111e219d.png" width="690">

 添加服务器信息<img alt="" height="463" src="https://img-blog.csdnimg.cn/bf29aed73e584d288277a06b1724a8a0.png" width="732">

         点击connect完成连接。

<img alt="" height="302" src="https://img-blog.csdnimg.cn/60273ae2dad5471483ef752d252c30ad.png" width="650">

        进入该页面后则证明连接成功，并可以在客户端操作。

## 五、总结

        当前MongoDB最新的版本是7.0，刚开始我也是准备安装7.0，在安装时才发现7.0版本要求glibc2.25以上的版本，然后我试着去升级glibc2.25又发现python、make等都要升级，在我升级glibc2.25时出现各种问题，比如说修改了libc.so.6软连接导致很多命令都用不了，最后我还是放弃安装7.0选择了低一个版本6.0进行安装，之前在网上有人就提醒过不要轻易的升级glibc库不然你的服务器就要看你的造化了。我得出的结论就是，我们在安装时需要先了解自己服务器的版本信息后再根据服务器的版本选择相应的MongoDB版本。如果必要使用最新版本建议有专业运维人员介入进行安装。 

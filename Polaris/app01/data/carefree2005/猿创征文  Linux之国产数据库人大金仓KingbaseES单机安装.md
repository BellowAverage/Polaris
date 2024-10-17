
--- 
title:  猿创征文 | Linux之国产数据库人大金仓KingbaseES单机安装 
tags: []
categories: [] 

---
## 一、人大金仓KingbaseES简介

  KingbaseES是一款面向大规模并发交易处理的企业级关系型数据库。该产品支持严格的ACID特性、结合多核架构的极致性能、行业最高的安全标准，以及完备的高可用方案，并提供可覆盖迁移、开发及运维管理全使用周期的智能便捷工具。产品融合了人大金仓在数据库领域几十年的产品研发和企业级应用经验，可满足各行业用户多种场景的数据处理需求。人大金仓数据库优势：
- 迁移开发 简单高效：兼容97%以上的Oracle语法，迁移平滑、成本更低；- 高度容错 稳定可靠：国家电网智能电网调度系统，10余年7x24稳定运行；- 性能强劲 表现出众：读写分离集群，只读性能线性增长，承载“万”级用户并发数；- 系统自治 简单易用：配套有诸多工具，性能诊断信息自动收集和分析；- 纵深防御 确保安全：安全四级销售许可证、信息技术产品安全分级评估证书(EAL4+)等；- 上下兼容 深度适配：全面适配国家专用项目相关产品，具备来自上下游1300多家公司4000+份兼容认证。
  **博文实验环境说明：**
- 操作系统：centos 7.6- kingbase：V008R006C006B0021- JAVA版本：1.8.0_271
  **数据库kingbaseV8安装要求：**
- 内存3G以上；- 磁盘空间20G以上；- JDK版本1.8及以上；- 操作系统要求安装桌面环境。
## 二、安装步骤

### 1、官网下载软件包

  通过下载软件包，根据CPU型号选择对应的版本进行下载，下载的时候需要填写手机号和验证码即可完成申请试用下载。 <img src="https://img-blog.csdnimg.cn/9b885587f75d4ba896e46467081a4e81.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/bcaca6d4f49f4bd6a4e05b19631bc3b0.png" alt="在这里插入图片描述">

### 2、安装JDK

  人大金仓数据库管理系统KingbaseES需要安装jdk1.8及以上的jdk环境和图形化桌面环境支持。JDK的安装可以参考博文。

### 3、安装桌面

>  
 [root@s152 tmp]# yum -y groupinstall “GNOME 桌面” #可以使用命令yum grouplist查看支持的软件组 <img src="https://img-blog.csdnimg.cn/9e9f7b2017c844eca5f5be23162154e7.png" alt="在这里插入图片描述"> 


### 4、将软件包iso文件和licence文件上传到服务器

  我们将第一步下载好的iso文件和软件licence授权文件上传到服务器指定目录，我这里是上传到了/tmp目录。

>  
 [root@s152 tmp]# ll -h |grep iso -rw-r–r–. 1 root root 2.5G 10月 8 14:46 KingbaseES_V008R006C006B0021_Lin64_install.iso [root@s152 tmp]# ll -h |grep zip -rw-r–r–. 1 root root 2.6K 10月 8 17:08 kingbase_license_V8R6.zip 


### 5、创建一个安装用户

>  
 [root@s152 tmp]# useradd kingbase 


### 6、创建安装目录

>  
 [root@s152 tmp]# mkdir -p /opt/Kingbase/ES/V8 [root@s152 tmp]# chown -R kingbase.kingbase /opt/Kingbase/ES/V8 


### 7、创建数据存储目录

>  
 [root@s152 tmp]# mkdir -p /data/kingbase/v8/data [root@s152 tmp]# chown -R kingbase.kingbase /data/kingbase/v8/data 


### 8、挂载iso文件

>  
 [root@s152 tmp]# mkdir -p /mnt/cdrom [root@s152 tmp]# mount -o loop KingbaseES_V008R006C006B0021_Lin64_install.iso /mnt/cdrom/ mount: /dev/loop0 写保护，将以只读方式挂载 [root@s152 tmp]# ll /mnt/cdrom/ 总用量 6 dr-xr-xr-x. 2 root root 2048 9月 2 16:36 setup -r-xr-xr-x. 1 root root 3829 9月 2 16:36 setup.sh 


### 9、执行安装脚本开始安装

  切换到普通用户kingbase执行安装脚本，按照提示操作即可。

>  
 [root@s152 tmp]# su - kingbase [kingbase@s152 ~]$ cd /mnt/cdrom/ [kingbase@s152 cdrom]$ sh setup.sh Now launch installer… … <img src="https://img-blog.csdnimg.cn/a515ff82c7694602a5e8b4b9e7327823.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e93155cf568f42e2906ccf955378c395.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e558213a62404c8ea796c55fa82e6774.png" alt="在这里插入图片描述"> 按照提示持续输入几个ENTER <img src="https://img-blog.csdnimg.cn/285966c5dc0f48e3a68695200bf1cf95.png" alt="在这里插入图片描述"> 


### 10、选择安装集

<img src="https://img-blog.csdnimg.cn/72d408c4e5cc4e0f8e7bb048c38716e2.png" alt="在这里插入图片描述">

### 11、选择授权文件

  这里需要选择我们上次到授权文件，记得提前将授权文件解压，下载的压缩包是中文建议先将文件名改为英文后上传。通过cat查看授权文件，我们可以看到试用期试用时常为90天。 <img src="https://img-blog.csdnimg.cn/0ff1db7db658405185eabd632e0b0c4a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f6cc8e5b95a242fcbbe7971a9bafffd2.png" alt="在这里插入图片描述">

### 12、选择安装目录

  人大金仓默认安装到/opt/Kingbase/ES/V8，如果需要自定义安装路径也可以，请提前创建好目录并修改目录属主。 <img src="https://img-blog.csdnimg.cn/77bb4d94d0b242169bc4d8917c93fd11.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2dd096d31cff4825968732f1ff16716e.png" alt="在这里插入图片描述">

### 13、选择存储数据的文件夹

<img src="https://img-blog.csdnimg.cn/5cba901e02474851a2e0f478fcd1f5a8.png" alt="在这里插入图片描述">

### 14、配置数据库监听端口

  数据库默认监控端口54321，为了安全可以修改数据库服务端口号。 <img src="https://img-blog.csdnimg.cn/b721e251104b4be8948a8fc1cf02f4ef.png" alt="在这里插入图片描述">

### 15、设置管理员账户及密码

  设置管理员账户及密码，默认system账户，不建议修改，密码设置尽量满足密码要求，此处不支持backspace删除，所以尽量一次输入正确哦。 <img src="https://img-blog.csdnimg.cn/e94985c19623461a947f109c14f764a0.png" alt="在这里插入图片描述">

### 16、设置数据库服务字符集

<img src="https://img-blog.csdnimg.cn/7b833851abec43b5b06081be59cc82c7.png" alt="在这里插入图片描述">

### 17、设置数据库兼容模式

  设置数据库兼容模式，支持PG和oracle，默认兼容oracle。 <img src="https://img-blog.csdnimg.cn/7346ae77d4a04cdd81206d0c7e6815cd.png" alt="在这里插入图片描述">

### 18、设置字符大小写敏感特性

  设置字符集大小写敏感特性，默认大小写敏感，博主常用mysql，设置为了NO。 <img src="https://img-blog.csdnimg.cn/b4537209d5534a6591a93836fdc7099a.png" alt="在这里插入图片描述">

### 19、设置存储块大小

  设置完存储块大小后回车就开始正式安装了，需要耐心等待一会，安装过程中会每秒刷新显示请稍候。 <img src="https://img-blog.csdnimg.cn/772a4bb1c228452b94cc0194c5ae865b.png" alt="在这里插入图片描述">

### 20、安装完成

  看到如下提示说明安装完成。 <img src="https://img-blog.csdnimg.cn/225dc59c95f44a42afe93f7dd2d31110.png" alt="在这里插入图片描述">

### 21、设置数据库服务自启动

>  
 [kingbase@s152 cdrom]$ exit 登出 [root@s152 tmp]# cd /home/kingbase/ES/V8/install/script/ [root@s152 script]# sh root.sh Starting KingbaseES V8: waiting for server to start… done server started KingbaseES V8 started successfully 


### 22、查看服务进程及监听端口

  使用netstat -tnpl可以查看监听的服务端口，使用ps -ef |grep kingbase查看服务进程。 <img src="https://img-blog.csdnimg.cn/c4e1461f01b54cbc809e8eb717bf6e41.png" alt="在这里插入图片描述">

## 三、数据库使用简介

### 1、管理员身份连接数据库

  使用如下命令登陆数据库管理员账户。

>  
 [kingbase@s152 bin]$ ./ksql -U system -W test 口令： … <img src="https://img-blog.csdnimg.cn/4af4193fde6a4b40ae789ee43350c267.png" alt="在这里插入图片描述"> 


### 2、获取命令帮助

  使用\h可以获取SQL命令的帮助，使用\?可以获取ksql命令的帮助，通过\q命令退出命令行管理。 <img src="https://img-blog.csdnimg.cn/208bce341cfa41db8624dbc803fd2edb.png" alt="在这里插入图片描述">

### 3、查看数据库版本

>  
 test=# select version(); <img src="https://img-blog.csdnimg.cn/8ef3174b61f24e18a5a59927740e616a.png" alt="在这里插入图片描述"> 


### 4、查看数据库列表

>  
 test=# \l <img src="https://img-blog.csdnimg.cn/c05199e9920f4b0790416d252e27583d.png" alt="在这里插入图片描述"> 


### 5、查看数据库连接数

>  
 test=# select connections(); connections ------------- 7 (1 行记录) 


### 6、停止数据库

>  
 [kingbase@s152 bin]$ ./sys_ctl stop -D /data/kingbase/v8/data/ 


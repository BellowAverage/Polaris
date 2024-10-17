
--- 
title:  KubeSphere - 搭建 mysql 主从复制结构 
tags: []
categories: [] 

---
KubeSphere - 搭建 mysql 主从复制结构

以project-regular登入系统

### mysql 主节点

### 创建 PVC 存储卷
1.  登入系统，点击进入项目按钮 <img src="https://img-blog.csdnimg.cn/26a9d181d3cb4f32ad685c7439b84b46.png" alt="在这里插入图片描述"> 1.  点击存储卷 <img src="https://img-blog.csdnimg.cn/56cc1027248542e3b94d9046cc6c055b.png" alt="在这里插入图片描述"> 1.  点击创建 <img src="https://img-blog.csdnimg.cn/4fba149fe42e4c6ba66e0af33a8e8f96.png" alt="在这里插入图片描述"> 1.  选择存储类型与访问模式后，点击下一步，创建 <img src="https://img-blog.csdnimg.cn/09842a06d5c54f6794eac2c7d3ffda9b.png" alt="在这里插入图片描述"> 1.  mysql-master-pvc 创建成功 <img src="https://img-blog.csdnimg.cn/ff9549c54dc84984babd05034654c4d6.png" alt="在这里插入图片描述"> 
### 创建 my.cnf 配制
1. 创建 mysql-master-cnf<img src="https://img-blog.csdnimg.cn/4020c6ff312f48ae810226bf6fb7c19a.png" alt="在这里插入图片描述">1. 基本信息 <img src="https://img-blog.csdnimg.cn/1720f7ea4a8e415ab5f44ef78b2375f8.png" alt="在这里插入图片描述">1. 配置设置 配置文件的内容
```
[client]
default-character-set=utf8mb4
[mysql]
default-character-set=utf8mb4
[mysqld]
init_connect='SET collation_connection = utf8_unicode_ci' 
init_connect='SET NAMES utf8mb4' 
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci 
skip-character-set-client-handshake
skip-name-resolve

server_id=1
log-bin=mysql-bin
read-only=0
binlog-do-db=gulimall_ums
binlog-do-db=gulimall_pms
binlog-do-db=gulimall_oms
binlog-do-db=gulimall_sms
binlog-do-db=gulimall_wms
binlog-do-db=gulimall_admin
replicate-ignore-db=mysql
replicate-ignore-db=sys
replicate-ignore-db=information_schema
replicate-ignore-db=performance_schema

```

注意： 此配置文件只同步这些表（！！！！！！！！） binlog-do-db=gulimall_ums binlog-do-db=gulimall_pms binlog-do-db=gulimall_oms binlog-do-db=gulimall_sms binlog-do-db=gulimall_wms binlog-do-db=gulimall_admin

<img src="https://img-blog.csdnimg.cn/7943ea6ed2b9431299589bec57d3fb2e.png" alt="在这里插入图片描述"> 4. mysql-master-cnf 配置成功

<img src="https://img-blog.csdnimg.cn/130f3edb0dfb4190b0c43b997332688e.png" alt="在这里插入图片描述">

### 创建 mysql master 服务
1. 点击创建按钮 <img src="https://img-blog.csdnimg.cn/15b3562c701c4331b978f7b23a51d478.png" alt="在这里插入图片描述">1. 选择有状态服务 <img src="https://img-blog.csdnimg.cn/16f51bd91cee47af94c77c5c66be3727.png" alt="在这里插入图片描述">3. 基本信息配置 <img src="https://img-blog.csdnimg.cn/4d104173d1ae42febefb7186ccd8d369.png" alt="在这里插入图片描述">1. 容器镜像： mysql:5.7 <img src="https://img-blog.csdnimg.cn/636b8328fc784631a3be98fd90d95689.png" alt="在这里插入图片描述"> 把内存调大一点 <img src="https://img-blog.csdnimg.cn/04c72577dae9454dba3b43f037ffda4a.png" alt="在这里插入图片描述"> 选择提前配好的mysql秘钥， 点击下一步 **<img src="https://img-blog.csdnimg.cn/53a92a9a400b4c618ea71002973e6ffd.png" alt="加粗样式"> **1. 挂载存储卷: /var/log/mysql <img src="https://img-blog.csdnimg.cn/e6d790d4cb1141449d336c77f66a8ab3.png" alt="在这里插入图片描述"> 配置文件和秘钥： /etc/mysql <img src="https://img-blog.csdnimg.cn/146537f6c2ad4b01acae417dec5c5388.png" alt="在这里插入图片描述">1. 点击对号–下一步–创建即可 <img src="https://img-blog.csdnimg.cn/df91d7cdbc0b47ab9a30548e8ffe3773.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f5fb25cee7504774b9b41cb8eec967d5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6873d0a44b8c4db1a8d0660b82440e17.png" alt="在这里插入图片描述">
### mysql 从节点搭建

创建pvc,与主节点类似：mysql-slave-pvc <img src="https://img-blog.csdnimg.cn/a5cc70f5b3784d05ad1cc9d862561aa0.png" alt="在这里插入图片描述">

### 创建 mysql-slave-cnf

配置内容

```
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
[mysqld]
init_connect='SET collation_connection = utf8_unicode_ci' 
init_connect='SET NAMES utf8mb4' 
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci 
skip-character-set-client-handshake
skip-name-resolve


server_id=2
log-bin=mysql-bin
read-only=1
binlog-do-db=gulimall_ums
binlog-do-db=gulimall_pms
binlog-do-db=gulimall_oms
binlog-do-db=gulimall_sms
binlog-do-db=gulimall_wms
binlog-do-db=gulimall_admin
replicate-ignore-db=mysql
replicate-ignore-db=sys
replicate-ignore-db=information_schema
replicate-ignore-db=performance_schema

```

<img src="https://img-blog.csdnimg.cn/4d11a29998e749e1a352ed621aa6f52a.png" alt="在这里插入图片描述">

### 创建mysql的从节点
1. 创建 <img src="https://img-blog.csdnimg.cn/40d5bb9a0c2e4189928bc80135c8ce8a.png" alt="在这里插入图片描述">1. 与mysql主节点类似，其余步骤省略，创建成功 <img src="https://img-blog.csdnimg.cn/ab852a48eb014c4293d17f1bd216bc55.png" alt="在这里插入图片描述">
### mysql 主从配制
1. 进入mysql主节点，点击终端，进入容器内部 <img src="https://img-blog.csdnimg.cn/a14405373a0a4bdba66f8c2b534bd443.png" alt="在这里插入图片描述">1. 输入用户用户名和密码，进入mysql <img src="https://img-blog.csdnimg.cn/62848d7ebc294615a38ff034475cdf14.png" alt="在这里插入图片描述">1. 输入
```
GRANT REPLICATION SLAVE ON *.* to 'backup'@'%' identified by '123456';

```

<img src="https://img-blog.csdnimg.cn/dbf172724f4f46e8b4c92094339bd1cf.png" alt="在这里插入图片描述"> 4. 查看主节点的状态

```
show master  status 

```

<img src="https://img-blog.csdnimg.cn/8479ae8032fa485794cbc32166be4289.png" alt="在这里插入图片描述"> mysql-bin.000003文件，后面的从节点要同步这个文件。

### 从节点配制
1. 进入从节点，输入命令
```
change master to master_host='mysql-master.demo-project',master_user='backup',master_password='123456',master_log_file='mysql-bin.000003',master_log_pos=439,master_port=3306;

```

<img src="https://img-blog.csdnimg.cn/e92073014521486ea9f81e941188b296.png" alt="在这里插入图片描述"> 开始同步： <img src="https://img-blog.csdnimg.cn/64e2200eb53e4789913cd94a983c5797.png" alt="在这里插入图片描述"> 查看同步的状态： <img src="https://img-blog.csdnimg.cn/4755e656fd95401982fc14b2530ea0ae.png" alt="在这里插入图片描述"> 测试主从，主从成功（此处就补贴图片了）

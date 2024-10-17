
--- 
title:  Docker快速搭建ssh蜜罐cowrie 
tags: []
categories: [] 

---
目录











**注意：蜜罐ssh的端口不能和真实的ssh端口一样，设置不一样的即可。**



#### 安装数据库

```
docker run -itd --name mysql --restart=always -p 33060:3306 -e MYSQL_ROOT_PASSWORD=你的数据库密码 -e TZ=Asia/Shanghai mysql
```

#### 数据库建表

创建数据库**cowrie**

然后执行以下sql

```
CREATE TABLE IF NOT EXISTS `auth` (
  `id` int(11) NOT NULL auto_increment,
  `session` char(32) NOT NULL,
  `success` tinyint(1) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `timestamp` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ;

CREATE TABLE IF NOT EXISTS `clients` (
  `id` int(4) NOT NULL auto_increment,
  `version` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ;

CREATE TABLE IF NOT EXISTS `input` (
  `id` int(11) NOT NULL auto_increment,
  `session` char(32) NOT NULL,
  `timestamp` datetime NOT NULL,
  `realm` varchar(50) default NULL,
  `success` tinyint(1) default NULL,
  `input` text NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `session` (`session`,`timestamp`,`realm`)
) ;

CREATE TABLE IF NOT EXISTS `sensors` (
  `id` int(11) NOT NULL auto_increment,
  `ip` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ;

CREATE TABLE IF NOT EXISTS `sessions` (
  `id` char(32) NOT NULL,
  `starttime` datetime NOT NULL,
  `endtime` datetime default NULL,
  `sensor` int(4) NOT NULL,
  `ip` varchar(15) NOT NULL default '',
  `termsize` varchar(7) default NULL,
  `client` int(4) default NULL,
  PRIMARY KEY  (`id`),
  KEY `starttime` (`starttime`,`sensor`)
) ;

CREATE TABLE IF NOT EXISTS `ttylog` (
  `id` int(11) NOT NULL auto_increment,
  `session` char(32) NOT NULL,
  `ttylog` varchar(100) NOT NULL,
  `size` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ;

CREATE TABLE IF NOT EXISTS `downloads` (
  `id` int(11) NOT NULL auto_increment,
  `session` CHAR( 32 ) NOT NULL,
  `timestamp` datetime NOT NULL,
  `url` text NOT NULL,
  `outfile` text default NULL,
  `shasum` varchar(64) default NULL,
  PRIMARY KEY  (`id`),
  KEY `session` (`session`,`timestamp`)
) ;

CREATE TABLE IF NOT EXISTS `keyfingerprints` (
  `id` int(11) NOT NULL auto_increment,
  `session` CHAR( 32 ) NOT NULL,
  `username` varchar(100) NOT NULL,
  `fingerprint` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ;

CREATE TABLE IF NOT EXISTS `params` (
  `id` int(11) NOT NULL auto_increment,
  `session` CHAR( 32 ) NOT NULL,
  `arch` varchar(32) NOT NULL,
  PRIMARY KEY  (`id`)
) ;
CREATE INDEX arch_index ON params (arch);

CREATE TABLE IF NOT EXISTS `ipforwards` (
  `id` int(11) NOT NULL auto_increment,
  `session` CHAR(32) NOT NULL,
  `timestamp` datetime NOT NULL,
  `dst_ip` varchar(255) NOT NULL default '',
  `dst_port` int(5) NOT NULL,
  PRIMARY KEY  (`id`),
  FOREIGN KEY (`session`) REFERENCES `sessions`(`id`)
) ;

CREATE TABLE IF NOT EXISTS `ipforwardsdata` (
  `id` int(11) NOT NULL auto_increment,
  `session` CHAR(32) NOT NULL,
  `timestamp` datetime NOT NULL,
  `dst_ip` varchar(255) NOT NULL default '',
  `dst_port` int(5) NOT NULL,
  `data` text NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `session` (`session`,`timestamp`),
  FOREIGN KEY (`session`) REFERENCES `sessions`(`id`)
) ;
```

#### 部署cowrie

```
docker run -itd -p 22:2222 \
  -e COWRIE_OUTPUT_MYSQL_ENABLED=true \
  -e COWRIE_OUTPUT_MYSQL_HOST=你的数据库公网ip \
  -e COWRIE_OUTPUT_MYSQL_DATABASE=cowrie \
  -e COWRIE_OUTPUT_MYSQL_USERNAME=root \
  -e COWRIE_OUTPUT_MYSQL_PASSWORD=你的数据库密码 \
  -e COWRIE_OUTPUT_MYSQL_PORT=33060 \
  --name cowrie cowrie/cowrie
```

#### 效果

能看到攻击者执行的指令

<img alt="" height="499" src="https://img-blog.csdnimg.cn/direct/2c1635243c0049f0931cb13d40c22939.png" width="696">

攻击者上传的文件

<img alt="" height="503" src="https://img-blog.csdnimg.cn/direct/325f0ef8ccbe41ed8f3c273c680d3c18.png" width="849">

爆破使用的密码

<img alt="" height="337" src="https://img-blog.csdnimg.cn/direct/ca7ac992157041ea823a6ab7c9c9c458.png" width="423">

还有很多数据都被记录到数据库中。

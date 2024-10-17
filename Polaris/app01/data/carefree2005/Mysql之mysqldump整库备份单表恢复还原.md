
--- 
title:  Mysql之mysqldump整库备份单表恢复还原 
tags: []
categories: [] 

---
## 一、需求场景说明

  日常运维中，我们往往都是整库备份，整库还原。实际工作中会存在需要还原部分表或者单表的情况。例如在开发或者测试环境中，开发人员因为误操作或者测试需要删除或者清空了某个表，我们需要还原这个被删除或者清空的表。为了恢复这个误删表，我们如果使用整库还原会存在2点问题：一、直接还原到在用库，可能导致其他表已更新数据被覆盖；二、使用临时库整库还原后copy单表会耗时费力（如下图所示，单库整库备份大小将近4G）。实际上我们只需要截取出单表数据，恢复单表即可。 <img src="https://img-blog.csdnimg.cn/7a5757ad8cc7406c8778636a1e7f2bc4.png" alt="在这里插入图片描述">   如何实现整库备份，单表还原的需求场景呢？此博文就是针对此场景进行介绍说明。博文实验环境：
- 操作系统：centos7.6- mysql版本：5.7
## 二、单表还原步骤

### 1、查看数据库备份文件

  mysqldump备份的数据实际上就是sql数据导出方式。我们使用cat查看备份的sql文件，可以看到备份工具的版本，数据库版本，数据库名和参数信息等。查看具体内容可以发现导出的数据使用insert into语句存储，不过插入多少行数据，对于文本来说就是一行，而且都包含表名，这个是我们实现单表还原的关键。 <img src="https://img-blog.csdnimg.cn/842f936708f14840a134185e34b0f1b7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e2be8814809543369f01ec824671469d.png" alt="在这里插入图片描述">   为了对比验证单表恢复还原数据的可行性，我们先整库还原了备份数据，耗时1个多小时。其中personchangeinfo表总计9889行。 <img src="https://img-blog.csdnimg.cn/f814a24419044cfc9085929f6cd8f77d.png" alt="在这里插入图片描述">

### 2、使用grep过滤单表数据

  使用grep过滤需要还原的表数据。 <img src="https://img-blog.csdnimg.cn/6d63752bc71f44d4bd22a7fa42cc38e4.png" alt="在这里插入图片描述">

>  
 [wuhs@s152 tmp]$ cat testdb_all.sql |grep -E ‘INSERT INTO `personchangeinfo`’ &gt; personchangeinfo1.sql [wuhs@s152 tmp]$ ll -lrt 总用量 3934600 … -rw-rw-r–. 1 wuhs wuhs 1033114 11月 15 14:39 personchangeinfo1.sql 


### 3、使用sed命令筛出单表数据

  使用sed -n从整库备份文件中筛查出需要恢复的表数据。 <img src="https://img-blog.csdnimg.cn/797680e0aa814b67b0af7016b83c5ea2.png" alt="在这里插入图片描述">

>  
 [wuhs@s152 tmp]$ sed -n ‘/INSERT INTO `personchangeinfo`/p’ testdb_all.sql &gt; personchangeinfo2.sql [wuhs@s152 tmp]$ ll -lrt 总用量 3934600 … -rw-rw-r–. 1 wuhs wuhs 1033114 11月 15 14:36 personchangeinfo2.sql3 11月 15 14:29 personchangeinfo2.sql 


### 4、创建表结构

  在备份文件中找到创建表空间语句，并执行。 <img src="https://img-blog.csdnimg.cn/ce7e429361fc467fb817423841ee7ea0.png" alt="在这里插入图片描述">

### 4、单表还原测试

  我们分别使用grep和sed导出数据进行还原测试，还原结果与整库还原结果一致，说明此方式还原单表可行。 <img src="https://img-blog.csdnimg.cn/4a5142dccdac4c0abcdf00502845845a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7f89057999864e03b359db357d374b99.png" alt="在这里插入图片描述">

## 三、通过脚本实现单表还原

### 1、脚本内容

```
[wuhs@s152 tmp]$ cat onetableimport.sh 
#!/bin/bash
#script name: onetableimport.sh
#author: 524627027@qq.com
#用途：此脚本用于从mysqldump整库备份文件中导出单表数据
#使用方式：将整库备份文件重命名为testdb_all.sql,并与此脚本放置在同一个目录下

#参数定义
workPath=$(cd $(dirname $0); pwd)
t1=""
tblist=""
outportfile=$workPath/outport.sh

#获取数据库表清单
cat testdb_all.sql |grep "CREATE TABLE " &gt; 1.txt
tblist=`awk -F " " '{print $3}' 1.txt`
echo "$tblist"
#通过键盘输入需要导出的表
read -p "请输入需要还原的表名(请带符号复制并黏贴):" t1
read -p "请输入导出后文件名：" tname

#创建单表导出脚本
if [ ! -f $outportfile ]; then
  cat &gt; $outportfile &lt;&lt;EOF
sed -n '/CREATE TABLE $t1/,/Dumping data for table $t1/p' testdb_all.sql &gt; $tname.sql
sed -n '/INSERT INTO $t1/p' testdb_all.sql &gt;&gt; $tname.sql
EOF
fi

#执行单表数据导出脚本
chmod u+x $outportfile
sh $outportfile
#结束通知
echo "$tname 数据机构及数据导出完成"
#删除临时文件
rm -rf 1.txt
rm -rf $outportfile

```

### 2、脚本测试

>  
 [wuhs@s152 tmp]$ sh onetableimport.sh `personchangeinfo` … 请输入需要还原的表名(请带符号复制并黏贴): 请输入导出后文件名：personchangeinfo personchangeinfo 数据机构及数据导出完成 


### 3、查看导出文件

<img src="https://img-blog.csdnimg.cn/762dbf1fc03e4864af51aecaa55a83b2.png" alt="在这里插入图片描述">

### 4、数据恢复测试

  导出后对比发现数据导出成功，脚本既截取了数据表结构创建sql，也导出了数据内容。 <img src="https://img-blog.csdnimg.cn/68ca0de2b5274ebdbc05f4d36b3a0748.png" alt="在这里插入图片描述">

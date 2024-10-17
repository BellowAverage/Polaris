
--- 
title:  Linux 计划任务crontab详解，含笔试题讲解 
tags: []
categories: [] 

---


#### 文章目录

  - 
  <li>
   <ul>
    <li>
     <ul>
      - 
      - 
      - 
      - 
      - 
      <li>
       <ul>
        - 
        - 
        - 
        - 
        - 
        - 
       


## 计划任务（crontab）

计划任务<mark>不是必须要</mark>的，但是它有很大的作用

<mark>优势：解放人力，提升效率，自动化</mark>

<mark>定时定点去执行脚本（程序）</mark>

#### crontab -e：创建计划任务 -e edit

#### crontab -l：查看计划任务 -l list

```
[root@master 417]# crontab -e  #创建计划任务的命令   -e  编辑  edit

30 3 * * *  bash  /lianxi/417/backup_log.sh    每天凌晨3:30执行脚本backup_log.sh
[root@master 417]# crontab  -l  #查看计划任务  list
30 3 * * *  bash  /lianxi/417/backup_log.sh

#示例
# 20 8 23 7 *  bash  /lianxi/417/backup_log.sh  
# 7月23日的早上8点20 执行脚本

# /  间隔的时间频率，间隔多久
# ,  单个的，多个不连续的时间点
# -  连续的时间范围
# */1 * * * *   每分钟去执行
# */5 * * * *   每5分钟去执行
# 30 8 3,8,10 * *   每月的3号，8号，10号的8点30执行
# 30 8 8-18 * *     每月的8号到18号的8点30执行
# 30 8-18 * * *     每天的8点30 9点30 ....  18点30执行

```

#### 查看计划任务格式

```
# 默认只能精确到分钟，最短时间间隔是1分钟
[root@master 417]# cat  /etc/crontab 
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

```

#### 停止、启动、重启crond服务

```
#停止crond服务：
[root@localhost lianxi]
```

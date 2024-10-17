
--- 
title:  查看hive表储存在hdfs的哪个目录下 
tags: []
categories: [] 

---
## 查看hive表储存在hdfs的哪个目录下

使用Hive的`DESCRIBE FORMATTED`命令。

具体步骤如下：
1.  打开Hive终端，并连接到Hive数据库。 1.  运行以下命令，将表名替换为你要查询的表名： 
```
DESCRIBE FORMATTED your_table_name;

```
1. 在输出中，查找`Location`字段，这个字段会显示表在HDFS中的存储路径。
#### 查看一个HDFS目录占用了多少磁盘空间

可以使用hadoop fs -du命令。该命令会返回目录（或文件）的大小，以字节为单位。

以下是具体步骤：
1.  打开终端并连接到Hadoop集群节点。 1.  运行以下命令，将HDFS目录的路径替换为你要查看的目录路径： 
```
hadoop fs -du -h /your/hdfs/directory/path

```

在上面的命令中，-h参数指示以人类可读的格式显示目录大小。
1. 命令输出会显示目录占用的总磁盘空间。例如：
```
12.5 M  /your/hdfs/directory/path

```

在上述示例中，目录/your/hdfs/directory/path占用了12.5MB的磁盘空间。

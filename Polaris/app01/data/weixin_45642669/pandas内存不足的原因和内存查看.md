
--- 
title:  pandas内存不足的原因和内存查看 
tags: []
categories: [] 

---
## 问题

pandas需要处理数据的时候必然需要加载在内存里面，这个可不是数据库，似乎是没有办法的。

确认内存占用： 我这边有一个20M的文件，然后使用：

```
df = pandas.read_csv(r"F:\mail_log\idc\mail_file\1624-信息.csv", encoding="utf-8")
df.info(memory_usage="deep")

```

然后返回值：

```
 #   Column  Non-Null Count   Dtype 
---  ------  --------------   ----- 
 0   地市      136153 non-null  object
 1   机位编码    136153 non-null  object
 2   机位名称    136153 non-null  object
 3   开始U     136153 non-null  int64 
 4   所属机柜    136153 non-null  object
 5   占用U     136153 non-null  int64 
 6   状态      136153 non-null  object
dtypes: int64(2), object(10)
memory usage: 93.4 MB

进程已结束，退出代码为 0


```

内存占用是文件大小的5倍。 文件是1G，那么使用的内存大概在5G左右。所以当文件过大的时候会出现内存不足的问题

所以如果你程序的可用内存是32G，那么为了保证系统可用需要留一半内存，可以估计可读的最大文件是：32 /5 / 2 = 3.2G。大于3.2G的文件就不能够使用pandas了（在不出现内存交换的情况下）

这就是故障的本质

## 解决

分析工具的话，可用分片 + 汇总的结果

```
table = pandas.read_csv(r"F:\mail_log\idc\mail_file\1624-信息.csv", encoding="utf-8", dtype=object, chunksize=10000)
for df in table:
    df.info(memory_usage="deep")

```

这样文件会小一些，然后通过append合并到一个df里面

```
dtypes: object(12)
memory usage: 4.9 MB

```

可是问题是：这样的话必须分析后的结果也是可以分片的！！！代码需要重写！！！ 比如说需要排序、哈希、汇总、join这些就没法子了 如果算法需要一次读入内存执行排序那也是没有办法的  

在读取之前预先确定类型和只保留分析的列，这个也是可以的；但是问题是：治标不治本。 你数据量是1G、2G这么玩还可以，文件一大还是不行。。

数据量过大的话，还得用hadoop生态的来解决问题


--- 
title:  go-fastdfs个人使用笔记 
tags: []
categories: [] 

---
### 中文文档



### 安装请参考docker 安装配置

### 文件删除不了的情况（需要配置cfg.json）

**文件地址：**

```
/data/fastdfs_data/conf

```

**使用vim修改**

```
vim /data/fastdfs_data/conf/cfg.json

```

**原因是要放行ip，所有修改admin_ips**

```
"admin_ips": ["127.0.0.1","192.168.3.30","106.12.156.86"],

```

**重启docker 的go-fastdfs就可以了**

### 上传文件同一个文件的时候，老是返回上次的数据，怎么解决，答案如下：

>  
 原因是：go-fastdfs 使用了去重的处理机制导致的 md5算法和去重是冲突的 解决方案是把go-go-fastdfs的cfg.json配置文件改一下，把去重去掉。 文件默认是 true ，把它改成false 


```
"文件是否去重": "默认去重",
"enable_distinct_file": false,

```

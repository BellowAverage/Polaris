
--- 
title:  SpringBoot整合Hadoop的案例代码demo,含HDFS文件操作、MapReduce分词操作、案例数据分析，系统推荐等 
tags: []
categories: [] 

---
### 简介

springboot整合Hadoop，进击大数据一小步。 下载地址：

### 功能介绍

**1、hdfs基本操作**

###### ① 实现最基本的文件操作系统 √

**2、MapReduce基本操作**

###### ① 实现简单的分词和统计 √

**3、yaml基本了解以及操作**

**4、案例**

###### ① 数据分析（日志为案例） √

###### ② 电影推荐 √

③ 职位推荐

④ 图书推荐

② 个体价值计算

### Hadoop 3.1.2安装（仅展示win下安装方式）



### 工程结构

```
hadoop-demo
├── docs -- 相关文件存放
├── src
├──── base -- 前端视图基础类
├──── config -- hadoop配置类
├──── controller -- hdfs操作接口 
├──── executor -- 案例任务执行器
├────── analyze -- 数据分析
├────── mapReduce -- mapReduce相关操作-单词统计
├────── recommend -- 系统推荐
├──────── movie -- 电影推荐
├──── hdfs -- hdfs 相关配置以及操作
├──── props -- hadoop属性配置
├──── util -- 工具类 
└──── HadoopDemoApplication.java -- springboot启动类

```

### 一、HDFS接口功能展示

**1、查看目录**

```
GET请求 请求地址: http://127.0.0.1:8080/file/getPathInfo
参数说明：{"path": ${目录路径}}
参数示例：{"path": "/"}

```

**2、创建目录**

```
POST请求 请求地址: http://127.0.0.1:8080/file/mkdir
参数说明：{"folderPath": ${目录路径}}
form-data参数示例：{"folderPath": "/data"}

```

**3、上传文件**

```
POST请求 请求地址: http://127.0.0.1:8080/file/upload
参数说明：{"uploadPath": ${hdfs目录路径}, "file": ${MultipartFile文件}}
form-data参数示例：{"uploadPath": "/data", "file": ${MultipartFile文件}}

```

**4、上传本地文件到hdfs**

```
POST请求 请求地址: http://127.0.0.1:8080/file/uploadFileFromLocal
参数说明：{"path": ${本地文件路径}, "uploadPath": ${上传的hdfs路径}}
form-data参数示例：{"path": "C:\Users\XXX\Desktop\用户信息-导入模板.xlsx", "uploadPath": "/data"}

```

**5、获取目录下文件列表**

```
GET请求 请求地址: http://127.0.0.1:8080/file/getPathInfo
参数说明：{"path": ${目录路径}}
参数示例：{"path": "/"}

```

**6、下载文件**

```
POST请求 请求地址: http://127.0.0.1:8080/file/download
参数说明：{"path": ${hdfs目录路径}, "fileName": ${MultipartFile文件}}
form-data参数示例：{"path": "/data", "fileName": "用户信息-导入模板.xlsx"}

```

**7、下载文件到本地电脑**

```
POST请求 请求地址: http://127.0.0.1:8080/file/downloadFileFromLocal
参数说明：{"path": ${hdfs文件路径}, "downloadPath": ${本地电脑路径}}
form-data参数示例：{"path": "/data", "downloadPath": "C:\Users\XXX\Desktop\"}

```

**8、复制文件**

```
POST请求 请求地址: http://127.0.0.1:8080/file/copyFile
参数说明：{"sourcePath": ${hdfs源文件路径}, "targetPath": ${hdfs目标文件路径}}
form-data参数示例：{"sourcePath": "/data/用户信息-导入模板.xlsx", "targetPath": "/test/用户信息-导入模板.xlsx"}

```

**9、读取文件内容**

```
POST请求 请求地址: http://127.0.0.1:8080/file/readFile
参数说明：{"filePath": ${hdfs文件路径}}
form-data参数示例：{"filePath": "/data/计税公式.txt"}

```

**10、文件或文件夹重命名**

```
POST请求 请求地址: http://127.0.0.1:8080/file/renameFile
参数说明：{"oldName": ${hdfs旧文件名称}, "newName": ${hdfs新文件名称}}
form-data参数示例：{"oldName": "/data/用户信息-导入模板.xlsx", "newName": "/data/用户信息-重命名.xlsx"}

```

**11、删除文件或文件夹**

```
POST请求 请求地址: http://127.0.0.1:8080/file/rmdir
参数说明：{"path": ${hdfs文件路径}, "fileName": ${文件名称，不填为删除文件夹}}
form-data参数示例：{"path": "/data", "fileName": "用户信息-导入模板.xlsx"}

```

### 二、MapReduce接口功能展示

**1、单词统计(统计指定key单词的出现次数)**

```
GET请求 请求地址: http://127.0.0.1:8080/reduce/wordCount
参数说明：{"jobName": ${任务名称}, "inputPath": ${分词路径，如果是文件家路径，则默认分词该文件夹下所有的文件}}
参数示例：{"jobName": "test", "inputPath": "/fenci"}

```

HDFS结果查询（指令）

```
遍历根目录下的文件 
hadoop fs -ls / 

查看分词结果
hadoop fs -cat /output/test/part-r-00000

```

**2、数据分析（日志为案例）**

日志数据为nginx产生的日志，Linux一般存放在/var/log/nginx，自行下载上传到hdfs的/log目录下，也可以从项目的docs文件下获取“access.log-20190720”数据文件

日志分析三种指标（案例只列出以下几种指标，可自行分析其他指标）

① 请求地址

② 响应结果

③ 请求类型

```
POST请求 请求地址: 127.0.0.1:8080/analyze/log
参数说明：{"jobName": ${任务名称}, "inputPath": ${分词路径，如果是文件家路径，则默认分词该文件夹下所有的文件}}
参数示例：{"jobName": "log", "inputPath": "/log"}

查看请求类型统计
hadoop fs -cat /output/log-request/part-r-00000

查看响应结果统计
hadoop fs -cat /output/log-requestStatus/part-r-00000

查看请求类型统计
hadoop fs -cat /output/log-requestMethod/part-r-00000

```

**3、电影推荐**

```
POST请求 请求地址: 127.0.0.1:8080/recommend/movie
参数说明：{"jobName": ${任务名称}, "inputPath": ${测试数据，文件路径，如果是文件的根路径，则默认该文件夹下所有的文件}}
参数示例：{"jobName": "movie", "inputPath": "/data/small.csv"}

步骤1 - 查看用户与物品的评分矩阵
hadoop fs -cat /output/recommend/movie/step1/part-r-00000

步骤2 - 查看物品的同现矩阵
hadoop fs -cat /output/recommend/movie/step2/part-r-00000

步骤3 - 查看合并同现矩阵和评分矩阵后的矩阵
hadoop fs -cat /output/recommend/movie/step3_1/part-r-00000
hadoop fs -cat /output/recommend/movie/step3_2/part-r-00000

步骤4 - 查看电影推荐结果上【矩阵相乘结果】
hadoop fs -cat /output/recommend/movie/step4/part-r-00000

步骤5 - 查看电影推荐结果下【矩阵相加结果】
hadoop fs -cat /output/recommend/movie/step5/part-r-00000

```

### 提示

此demo只是作为Hadoop学习demo

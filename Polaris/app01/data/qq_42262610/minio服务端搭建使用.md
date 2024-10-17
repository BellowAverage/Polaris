
--- 
title:  minio服务端搭建使用 
tags: []
categories: [] 

---
一.文件服务搭建

 非docker环境部署(Linux部署)

1.官网下载安装包：

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/54622ebde846481a9294d56b7d5339c1.png" width="1200">

 2、上传安装包文件到目录(这个可以自由选择)

/home/minio/

3、为minio添加权限

sudo chmod +x minio

4、 创建minio文件存储目录及日志目录

sudo mkdir  -p /home/minio/data

sudo mkdir  -p /home/minio/minio.log

5、在 minio/目录下，新建一个minio.sh（使用命令 sudo vi minio.sh 新建）并编辑以下内容，然后将以下内容保存到minio.sh

6、为其赋予执行权限

sudo chmod 777 minio.sh

7、启动minio并查看日志

8、查看minio日志文件


--- 
title:  在CentOS7上搭建svn服务器 
tags: []
categories: [] 

---1. 创建新用户,添加密码
```
useradd svnuser
passwd svnuser

```
1. 下载vim编辑器
```
yum install vim -y

```
1. 修改普通用户权限
```
vim /etc/sudoers  -- 权限不够
visudo  -- 可以直接修改
添加：svnuser ALL=(ALL) ALL

```
1. 下载svn
```
sudo yum install subversion -y

```
1. 创建svn仓库,路径自己来
```
mkdir -p /svn/data
svnadmin create /svn/data/test

```
1. 进入前面创建的路径，修改三个配置文件 6.1 authz文件
```
root = root,svnuser  #设定root组，其成员有：root和svnuser
[/] #设定项目下的文件，均可浏览
@root=rw #root用户组，拥有读写权限

* = r   #所有访问，必须有用户名和密码；即匿名用户无读权限

```

6.2 passwd文件

```
root = 123456
svnuser = 123456

```

6.3 svnserver.conf文件

```
放开以下注释
anon-access=read #匿名用户可读
auth-access=write #授权用户可写
password-db=passwd #用户认证信息指向passwd，即从passwd中读取用户名和密码
authz-db=authz #权限文件
realm=/svn/data/ # 版本库目录

```
1. 开启服务svn
```
svnserve -d -r /data/svn/

```
1. 添加
```
firewall-cmd --zone=public --add-port=3690/tcp --permanent  #（–permanent永久生效，没有此参数重启后失效）

```
1. 关闭防火墙、添加端口号
```
systemctl stop firewalld
systemctl disable firewalld

```
1. 在windows上创建文件夹，右键选择 svn Checkout
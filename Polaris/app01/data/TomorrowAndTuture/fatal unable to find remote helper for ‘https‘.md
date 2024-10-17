
--- 
title:  fatal: unable to find remote helper for ‘https‘ 
tags: []
categories: [] 

---
### 问题 

```
git clone ​​​​​​https://gitee.com/&lt;username&gt;/&lt;project&gt;.git
```

上面 git clone 使用 https 的项目链接时，可能会报如下错误。

```
fatal: unable to find remote helper for 'https'

```

### 解决办法

#### 修改配置

编辑 /etc/profile 文件，在末尾添加下行： 

```
export PATH=${PATH}:/usr/libexec/git-core
```

source /etc/profile 让文件立即生效或者重启一下机器：

```
source /etc/profile

```

再次执行克隆命令即可正常克隆项目了。

#### 使用 ssh 链接

使用 git@gitee.com 的链接克隆

```
git clone --recursive git@gitee.com:&lt;username&gt;/&lt;project&gt;.git
```

#### 安装 git-http

网上也有答案说使用 yum install git-http

但是有些机器上似乎行不通（比如 centos7，尽管我已经安装过了 epel-release）：

```
[root@master ~]# yum install git-http
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                                                            | 6.8 kB  00:00:00     
 * base: mirrors.aliyun.com
 * epel: mirror.lzu.edu.cn
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base                                                                                                            | 3.6 kB  00:00:00     
crystal                                                                                                         | 2.9 kB  00:00:00     
docker-ce-stable                                                                                                | 3.5 kB  00:00:00     
epel                                                                                                            | 4.7 kB  00:00:00     
extras                                                                                                          | 2.9 kB  00:00:00     
jenkins                                                                                                         | 2.9 kB  00:00:00     
updates                                                                                                         | 2.9 kB  00:00:00     
(1/2): epel/x86_64/updateinfo                                                                                   | 1.0 MB  00:00:00     
(2/2): epel/x86_64/primary_db                                                                                   | 7.0 MB  00:00:01     
No package git-http available.
Error: Nothing to do

```



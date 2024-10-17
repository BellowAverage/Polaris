
--- 
title:  rpm软件包管理 
tags: []
categories: [] 

---
原文链接：

## rpm

### rpm简介

Linux rpm 命令用于管理套件。rpm(redhat package manager) 原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于它遵循 GPL 规则且功能强大方便，因而广受欢迎。逐渐受到其他发行版的采用。RPM 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度。

### 包名解析

例如：`rp-pppoe-3.11-5.el7.x86_64.rpm`

|名称|含义
|------
|rp-pppoe|软件名
|3.11|版本号
|5|发布此时
|.el7.x86_64|硬件平台
|rpm|后缀
- 版本号：通常分为主版本和小版本，这里主版本是3，小版本就是11- 硬件平台：目前只要是x86的平台
### 常用命令

rpm 一般会从本地查，dnf 一般会从 yum repo 地址去查

#### rpm -q --provides &lt;package&gt;  （dnf repoquery --provides &lt;package&gt;）

看包提供了哪些功能（capability）

```
[root@localhost ~]# rpm -q --provides python2-enum34-1.1.6-8.noarch.rpm 
python-enum34 = 1.1.6-8
python2-enum34 = 1.1.6-8
python2.7dist(enum34) = 1.1.6
python2dist(enum34) = 1.1.6

```

```
[root@localhost ~]# dnf repoquery --provides python2-enum34-1.1.6-8.noarch.rpm 
Last metadata expiration check: 2:57:29 ago on Mon 26 Apr 2021 12:06:41 PM CST.
python-enum34 = 1.1.6-8
python2-enum34 = 1.1.6-8
python2.7dist(enum34) = 1.1.6
python2dist(enum34) = 1.1.6

```

#### rpm -q --whatprovides &lt;capability&gt;  （dnf repoquery --whatprovides &lt;capablility&gt;）

看某个功能是哪个包提供的

```
root@master ~# rpm -q --whatprovides python-enum34
python-enum34-1.0.4-1.el7.noarch

```

```
[root@localhost ~]# dnf repoquery --whatprovides python-enum34
Last metadata expiration check: 2:53:08 ago on Mon 26 Apr 2021 12:06:41 PM CST.
python-enum34-0:1.0.4-1.el7.noarch

```

#### rpm -q --requires &lt;package&gt;  （dnf repoquery --requires &lt;package&gt;）

看包依赖于哪些功能

```
[root@localhost ~]# rpm -q --requires python2-enum34-1.1.6-8.noarch.rpm 
python(abi) = 2.7
rpmlib(CompressedFileNames) &lt;= 3.0.4-1
rpmlib(FileDigests) &lt;= 4.6.0-1
rpmlib(PartialHardlinkSets) &lt;= 4.0.4-1
rpmlib(PayloadFilesHavePrefix) &lt;= 4.0-1
rpmlib(PayloadIsXz) &lt;= 5.2-1
```

```
[root@localhost ~]# dnf repoquery --requires python2-enum34-1.1.6-8.noarch.rpm 
Last metadata expiration check: 2:59:40 ago on Mon 26 Apr 2021 12:06:41 PM CST.
python(abi) = 2.7
rpmlib(CompressedFileNames) &lt;= 3.0.4-1
rpmlib(FileDigests) &lt;= 4.6.0-1
rpmlib(PartialHardlinkSets) &lt;= 4.0.4-1
rpmlib(PayloadFilesHavePrefix) &lt;= 4.0-1
rpmlib(PayloadIsXz) &lt;= 5.2-1

```

#### rpm -q --whatrequires &lt;capability&gt;  （dnf repoquery --whatrequires python-enum34）

看某个功能被哪些包依赖

```
[root@localhost ~]# rpm -q --whatrequires python-enum34
python2-cmd2-0.8.8-5.el7.noarch
python2-oslo-config-6.4.2-1.el7.noarch
python2-oslo-concurrency-3.27.0-1.el7.noarch
python2-oslo-privsep-1.29.2-1.el7.noarch
python2-taskflow-3.2.0-1.el7.noarch
python2-tooz-1.62.1-1.el7.noarch
python-nova-17.0.3.37.dev211-1.el7.noarch

```

```
[root@localhost ~]# dnf repoquery --whatrequires python-enum34
Last metadata expiration check: 2:51:00 ago on Mon 26 Apr 2021 12:06:41 PM CST.
openstack-zaqar-1:6.0.0-0.1.0rc1.el7.noarch
openstack-zaqar-1:6.0.0-1.el7.noarch
openstack-zaqar-1:6.0.1-1.el7.noarch
openstack-zaqar-1:7.0.0-0.1.0rc1.el7.noarch
...
```

**如果是从给定的未安装的 rpm 查询的话，记得添加 -p （--package）。低版本的 rpm 可能不支持 -R（--requires）、-P（--provides）的选项。**

#### **rpm -qp --requires &lt;package&gt; （rpm -qpR &lt;package&gt;）**

查询 rpm 需要哪些依赖 

```
[root@master ~]# rpm -qp --requires Cython-0.19-5.el7.x86_64.rpm 
/usr/bin/python
libc.so.6()(64bit)
libc.so.6(GLIBC_2.2.5)(64bit)
libc.so.6(GLIBC_2.3)(64bit)
libc.so.6(GLIBC_2.4)(64bit)
libpthread.so.0()(64bit)
libpython2.7.so.1.0()(64bit)
python
python(abi) = 2.7
rpmlib(CompressedFileNames) &lt;= 3.0.4-1
rpmlib(FileDigests) &lt;= 4.6.0-1
rpmlib(PartialHardlinkSets) &lt;= 4.0.4-1
rpmlib(PayloadFilesHavePrefix) &lt;= 4.0-1
rtld(GNU_HASH)
rpmlib(PayloadIsXz) &lt;= 5.2-1

```

#### **rpm -qp --provides &lt;package&gt; （rpm -qpP &lt;package&gt;）**

查询 rpm 提供了哪些依赖

```
[root@master ~]# rpm -qp --provides Cython-0.19-5.el7.x86_64.rpm 
Cython = 0.19-5.el7
Cython(x86-64) = 0.19-5.el7
python2-Cython = 0.19-5.el7

```

### 安装路径

一般来说，在安装RPM类型的文件时，会先去读取文件内记录的设置参数内容，然后将这些参数和Linux环境比对，找出是否有相关依赖未安装的情况。

如果环境合格，RPM文件的信息就会被写入到`var/lib/rpm`下的数据库文件中，这个目录非常重要，记录着所有软件的信息。但是文件本体去了哪里呢？会被打散，分别安装到`/etc，/usr/bin，/usr/lib`等路径下

**总结一下**，如果把Linux系统比作一个冰箱，把一道美食（例如番茄炒蛋，番茄和蛋）比作一个文件。
1. 把番茄炒蛋原材料放入冰箱前，先会在冰箱前的菜单上进行记录菜名，例如：`17.番茄炒蛋`。1. 然后再把鸡蛋放到冰箱里蛋类的仓库，番茄放到冰箱蔬菜类的仓库。
### rpm安装
- -i install安装的意思- -v 查看更详细的安装信息- -h 显示安装进度
### 正常安装

传统安装命令

```
rpm -ivh 网址或者本地机器具体包名

```

或者同时安装多个包

```
rpm -ivh 1.rpm 2.rpm *.rpm

```

范例

```
rpm -ivh http://mirrors.163.com/centos/6/os/x86_64/Packages/rp-pppoe-3.10-16.el6.x86_64.rpm
Retrieving http://mirrors.163.com/centos/6/os/x86_64/Packages/rp-pppoe-3.10-16.el6.x86_64.rpm
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
	package rp-pppoe-3.10-16.el6.x86_64 is intended for a different architecture

```

### 缺少依赖

但是通常会提示缺少依赖，这个时候就需要我们先把依赖包安装好

```
[root@localhost npm_test]# rpm -ivh http://mirrors.163.com/centos/6/os/x86_64/Packages/tclx-8.4.0-15.el6.x86_64.rpm
Retrieving http://mirrors.163.com/centos/6/os/x86_64/Packages/tclx-8.4.0-15.el6.x86_64.rpm
warning: /var/tmp/rpm-tmp.baqAQf: Header V3 RSA/SHA256 Signature, key ID c105b9de: NOKEY
error: Failed dependencies:
	libc.so.6(GLIBC_2.2.5)(64bit) is needed by tclx-8.4.0-15.el6.x86_64
	libc.so.6(GLIBC_2.3)(64bit) is needed by tclx-8.4.0-15.el6.x86_64
	libc.so.6(GLIBC_2.3.4)(64bit) is needed by tclx-8.4.0-15.el6.x86_64
	libc.so.6(GLIBC_2.4)(64bit) is needed by tclx-8.4.0-15.el6.x86_64
	libm.so.6(GLIBC_2.2.5)(64bit) is needed by tclx-8.4.0-15.el6.x86_64

```

### 强制安装

针对rpm报错可以选择合适命令再安装

|命令|使用时机|危险性
|------
|--nodeps|当出现依赖问题报错，不验证套件档的相互关联性|可能导致软件无法正常使用
|--replacefiles|出现**某个文件已经安装**，或者出现**版本不符合**，可以直接覆盖|覆盖文件是无法恢复的
|--replacepkgs|重新**安装某个已经安装过的软件**，提示软件已经存在时|
|--force|replacefiles和replacepkgs集合体，可以找到是否有依赖问题|
|--test|尝试安装|
|--justdb|由于rpm数据库损坏时，用这个命令更新库信息|
|--nosignature|需要跳过数字签名检查时|
|--prefix 新路径|需要将软件安装到非正常路径下|
|--noscripts|不想让软件安装时执行系统命令|

通常情况下`ivh`命令已经可以满足要求，如果必须暴力安装，如下

```
rpm -ivh 包名 --强制命令

```

例如对于包依赖忽视安装命令

```
rpm -ivh http://mirrors.163.com/centos/6/os/x86_64/Packages/rp-pppoe-3.10-16.el6.x86_64.rpm --nodeps --force
Retrieving http://mirrors.163.com/centos/6/os/x86_64/Packages/rp-pppoe-3.10-16.el6.x86_64.rpm
warning: /var/tmp/rpm-tmp.Vrx3mU: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
	package rp-pppoe-3.10-16.el6.x86_64 is intended for a different architecture

```

### rpm升级更新

只需要记住两个参数
- -Uvh 安装的软件没有安装过，则系统将直接安装，如果安装的软件安装过旧版本，系统直接安装到最新- -Fvh 如果软件没有安装过，系统不会安装，只有安装过的软件才会安装
### rpm查询
- -q 仅查询软件是否安装，后面需跟具体软件名- -qa 列出安装在本机上的所有软件- **-qi 列出该软件的详细信息，后面需跟具体软件名**- -ql 列出该软件所有的文件目录所在完整文件名，后面需跟具体软件名- -qc 列出该软件所有的配置文件，后面需跟具体软件名- -qd 列出该软件所有的说明文件，后面需跟具体软件名- -qR 列出该软件有关的依赖软件所含的文件，后面需跟具体软件名- -qf 后面直接跟一个文件，可以查出这个文件属于哪个软件- **-qp[icdlR] 注意：-qp 后面接的所有参数与上面的说明一致。但用途仅在于找出某个 RPM （可以不用安装）档案内的信息，而非已安装的套件信息，其中的 -p 可以简单理解为 package 的简写。**
```
[root@localhost npm_test]# rpm -q kexec-tools
kexec-tools-2.0.17-15.oe1.aarch64

# 具体信息
[root@localhost npm_test]# rpm -qi kexec-tools
Name        : kexec-tools
Version     : 2.0.17
Release     : 15.oe1
Architecture: aarch64
Install Date: Fri 03 Apr 2020 05:45:06 PM CST
Group       : Unspecified
Size        : 1304543
License     : GPLv2
Signature   : RSA/SHA1, Tue 24 Mar 2020 05:34:57 AM CST, Key ID d557065eb25e7f66
Source RPM  : kexec-tools-2.0.17-15.oe1.src.rpm
Build Date  : Tue 24 Mar 2020 05:33:02 AM CST
Build Host  : obs-worker-003
Packager    : http://openeuler.org
Vendor      : http://openeuler.org
URL         : https://www.kernel.org/
Summary     : The kexec/kdump userspace component
Description :
kexec-tools provides /sbin/kexec binary that facilitates a new
kernel to boot using the kernel's kexec feature either on a
normal or a panic reboot. This package contains the /sbin/kexec
binary and ancillary utilities that together form the userspace
component of the kernel's kexec feature.

# 查询相关依赖
[root@localhost npm_test]# rpm -qR kexec-tools
/bin/bash
/bin/sh
/bin/sh
/bin/sh
/bin/sh
/bin/sh
config(kexec-tools) = 2.0.17-15.oe1
coreutils
dracut &gt;= 047-34.git20180604
dracut-network &gt;= 044-117
ethtool
ld-linux-aarch64.so.1()(64bit)
ld-linux-aarch64.so.1(GLIBC_2.17)(64bit)
libbz2.so.1()(64bit)
libc.so.6()(64bit)
libc.so.6(GLIBC_2.17)(64bit)
libdl.so.2()(64bit)
libdl.so.2(GLIBC_2.17)(64bit)
libdw.so.1()(64bit)
libdw.so.1(ELFUTILS_0.122)(64bit)
libdw.so.1(ELFUTILS_0.126)(64bit)
libdw.so.1(ELFUTILS_0.143)(64bit)
libelf.so.1()(64bit)
libelf.so.1(ELFUTILS_1.0)(64bit)
libelf.so.1(ELFUTILS_1.5)(64bit)
liblzo2.so.2()(64bit)
libpthread.so.0()(64bit)
libpthread.so.0(GLIBC_2.17)(64bit)
libsnappy.so.1()(64bit)
libtinfo.so.6()(64bit)
libz.so.1()(64bit)
libz.so.1(ZLIB_1.2.0)(64bit)
libz.so.1(ZLIB_1.2.2.3)(64bit)
rpmlib(CompressedFileNames) &lt;= 3.0.4-1
rpmlib(FileDigests) &lt;= 4.6.0-1
rpmlib(PayloadFilesHavePrefix) &lt;= 4.0-1
rpmlib(PayloadIsXz) &lt;= 5.2-1
rtld(GNU_HASH)
sed
systemd
systemd
systemd
zlib

```

### rpm验证

#### 验证

当数据丢失或者误删某个文件时，或者不知道修改了哪个文件时，可以用以下方法验证
- -V 后直接跟软件名，如果软件所含的文件被修改过才会显示- -Va 列出目前系统上可能被修改过的文件- -Vp 后直接跟软件名，列出该软件内可能被修改过的文件- -qf 显示某个文件是否被修改过
```
[root@localhost npm_test]# rpm -V kexec-tools
.......T.  c /etc/kdump.conf

```

在c前有一堆点，前面出的英文大写有：
- S：文件容量大小是否改变- M：文件的类型和属性是否改变- 5：MD5校验值- D：设备的主次代码改变- L：链接路径- U：文件所属的用户- G：文件所属的用户组- T：文件建立的时间- P：功能改变
这个c表示配置文件，除此之外还有：
- d：数据文件- g：幽灵文件- l：许可证文件- r：自述文件
当我们用Va检查系统文件时，就可以检查哪些文件被修改过

```
[root@localhost npm_test]# rpm -Va
.M.......  g /run/cryptsetup
.M.......  g /run/dbus
.M.......  c /etc/machine-id
S.5......  c /etc/rc.d/rc.local
S.5....T.  c /etc/sysctl.conf
.M.......  g /var/log/btmp
.M....G..  g /var/log/journal
S.5....T.  c /etc/dnf/dnf.conf
.M.......  g /var/log/dnf.librepo.log
.M.......  g /var/log/hawkey.log
..5....T.  c /etc/openEuler_security/security
S.5....T.    /etc/profile.d/zzz_openEuler_history.csh
S.5....T.    /etc/profile.d/zzz_openEuler_history.sh
S.5....T.    /usr/lib/systemd/system/openEuler-security.service
S.5....T.  c /etc/yum.repos.d/openEuler_aarch64.repo
S.5....T.  c /etc/bashrc
S.5....T.  c /etc/csh.cshrc
S.5....T.  c /etc/csh.login
S.5....T.  c /etc/profile.d/csh.local
S.5....T.    /etc/profile.d/lang.csh
S.5....T.    /etc/profile.d/lang.sh
S.5....T.  c /etc/profile.d/sh.local
.M....G..  g /var/log/lastlog

```

### 数字签名

#### rpm卸载软件与重构数据库

如果只是卸载软件，只需执行

```
rpm -e 软件名

```

但是由于软件会互相依赖就会导致，有的软件不能被卸载，除非要把相关依赖也一同卸载

另外rpm数据库`var/lib/rpm`可能会文件损坏，这个时候需要**重构数据库**

```
rpm --rebuilddb

```

#### rpmbuild

RPM有五种基本的操作功能：安装、卸载、升级、查询和验证。

linux软件包分为两大类：

（1）二进制类包，包括rpm安装包（一般分为i386和x86等几种）

（2）源码类包，源码包和开发包应该归位此类（.src.rpm）。

有时候为了方便源码包的安装，和我们自己订制软件包的需求，我们会把一些源码包按照我们的需求来做成rpm包，当有了源码包就可以直接编译得到二进制安装包和其他任意包。spec file是制作rpm包最核心的部分，rpm包的制作就是根据spec file来实现的。在制作自定义rpm包的时候最好不要使用管理员进行，因为管理员权限过大，如果一个命令写错了，结果可能是灾难性的，而制件一个 rpm 包普通用户完全可以实现。

#### 安装

RPM打包使用的是rpmbuild命令，这个命令来自rpm-build软件包，这个是必装的。

```
yum install rpm-build -y

```

#### 常用命令
- -bp 只作准备 （解压与打补丁）- -bc 准备并编译- -bi 编译并安装- -bl 检验文件是否齐全- -ba 编译后做成`\*.rpm`和`src.rpm`- -bb 编译后做成`\*.rpm`- -bs 只做成`\*.src.rpm`
#### 目录结构

当执行rpmbuild命令之后，会在当前目录下（一般是根目录）生成一个rpmbuild目录，该目录中包含下面的6个目录（或者用 rpmdev-setuptree 命令生成目录）
1. BUILD：源代码解压以后放的位置，只需提供BUILD目录，具体里面放什么，不用我们管，所以真正的制作车间是BUILD目录。1. BUILDROOT：假根，使用`install`临时安装到这个目录，把这个目录当作根来用的，所以在这个目录下的目录文件，才是真正的目录文件。当打包完成后，在清理阶段，这个目录将被删除。1. RPMS：制作完成后的rpm包存放目录，为特定平台指定子目录（i386,i686,ppc）。1. SOURCES：收集的源文件，源材料，补丁文件等存放位置。1. SPECS：存放spec文件，作为制作rpm包的领岗文件，文件以`.spec`结尾。1. SRPMS：src格式的rpm包位置 ，既然是src格式的包，就没有平台的概念了。
#### 查看rpm包源码

openEuler常用源码包下载地址

```
https://repo.openeuler.org/openEuler-20.03-LTS/source/Packages/

```

以openjdk为例

```
rpm -ivh java-1.8.0-openjdk

```

安装好后

```
cd /root/rpmbuild/SPECS
rpmbuild -bp java-1.8.0-openjdk.spec

```

再进入 BUILD，查看源码

```
cd BUILD
```

## yum

### yum简介

Yum（Yellow dogUpdater, Modified）是一个在Fedora和RedHat以及CentOS中的Shell前端软件包管理器。基于**RPM包**管理，能够从指定的服务器自动下载RPM包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软件包，无须繁琐地一次次下载、安装。yum提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。

yum相比rpm优势是更加智能和傻瓜，用yum安装一个软件时会自动把其他依赖安装上，不过需要配置好源。

**总结一下**，还是拿之前那个冰箱（Linux），一道菜（软件）来比喻，用rpm安装文件时我们需要考虑，冰箱里是否有蔬菜库和鸡蛋库，如果没有我们需要再去配置，这就好比去处理依赖。这时yum的强大之处就来了，我们只需要配置好超市和安装厂家（软件源网址），就会有人亲自来帮你检查依赖和配置，一步到位，把菜放进冰箱。

### 配置yum

#### yum源配置

查看配置文件：每个源的配置文件都不一样，但都存放在`/etc/yum.repos.d/`该目录下，软件列表都放在`/var/cache/yum`

这里以openEuler_aarch64.repo源为例，首先打开

```
[root@localhost yum.repos.d]# vim /etc/yum.repos.d/openEuler_aarch64.repo 

```

内容如下

```
[mainline]
name=mainline
baseurl=https://mirrors.huaweicloud.com/openeuler/openEuler-20.03-LTS/everything/aarch64/
enabled=1
gpgcheck=0
priority=1

```
- `[mainline]`：这个表示的是名称，yum的ID，**必须唯一**，本地有多个yum源的时候，这里必须是唯一的- `name`：具体的yum源名字，其实相当于对它的描述描述信息。centos的那么会含有`$releasever`，这个变量参考红帽企业Linux发行版，也就是说表示当前发行版的大版本号。- `baseurl`：是镜像服务器地址，只能写具体的确定地址，只能有一个baseurl，但里面可以包含多个url- `mirrorlist`：这个不一定会有，是镜像服务器的地址列表，里面有很多的服务器地址。baseurl和mirrorlist都是指向yum源的地址，不同点是包含地址的多少。你若自己写的话，我们一般只写一个地址，直接用baseurl就行- `gpgcheck与gpgkey`：决定要不要进行验证。gpgcheck若是1，将对下载的rpm将进行gpg的校验，校验密钥就是gpgkey，一般自己的yum源是不需要检测的。gpgcheck=0，那么gpgkey就可以不填写- `enabled`：0禁用，1启用- `priority`：填写的数组范围为：1-99，数字越大，优先级越低
#### **修改或替换yum源操作**

1.备份源文件：要习惯做备份

```
[root@localhost yum.repos.d]# mv openEuler_aarch64.repo openEuler_aarch64.repobak

```

2.网上下载源文件，或者自己修改配置文件

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo 

```

3.列出目前yum服务器所使用的源有哪些

```
[root@localhost yum.repos.d]# yum repolist all
repo id                                    repo name                                  status
mainline                                   mainline                                   enabled

```

4.最后，还需要去除本机上的旧数据，运行以下命令生成缓存，执行以下命令

```
yum clean [packages|headers|all]

```
- packages：将已经下载的安装文件删除- headers：将下载的安装文件删除- all：将所有的软件源数据删除
最后的最后，生成新的缓存

```
yum makecache

```

#### yum.conf配置

存放位置于`/etc/yum.conf`，通常如下，一般来说无需修改此文件

```
[main]
cachedir=/var/cache/yum         #yum下载的RPM包的缓存目录
keepcache=0                        #缓存是否保存，1保存，0不保存。
debuglevel=2                       #调试级别(0-10)，默认为2(具体调试级别的应用，我也不了解)。
logfile=/var/log/yum.log         #yum的日志文件所在的位置
exactarch=1             #在更新的时候，是否允许更新不同版本的RPM包，比如是否在i386上更新i686的RPM包。
obsoletes=1             #这是一个update的参数，具体请参阅yum(8)，简单的说就是相当于upgrade，允许更新陈旧的RPM包。
gpgcheck=1             #是否检查GPG(GNU Private Guard)，一种密钥方式签名。
plugins=1             #是否允许使用插件，默认是0不允许，但是我们一般会用yum-fastestmirror这个插件。
installonly_limit=3         #允许保留多少个内核包。
exclude=selinux*         #屏蔽不想更新的RPM包，可用通配符，多个RPM包之间使用空格分离。

```

### 查询搜索
- check-update 列出所有可更新的软件清单- list 列出所有可安裝的软件清单- search 查找软件包- info 获取软件包信息
### 安装升级
- install 仅安装指定的软件- localinstall 安装本地rpm包- update 仅更新指定的软件- -y 当yum安装需要确认yes的时候，这个选项自动yes
### 删除软件

remove 删除软件包

### 下载软件

有一种情况时候是只下载软件，但不进行安装（会把依赖也下载）可以采用以下命令，

```
# yum install --downloadonly --downloaddir=/xxx/xxx 软件包名

```
- downloadonly 表示只下载不安装- --downloaddir 用于指定下载文件夹目录
### 清除缓存

```
清除缓存命令:
yum clean packages: 清除缓存目录下的软件包
yum clean headers: 清除缓存目录下的 
headersyum clean oldheaders: 清除缓存目录下旧的
headersyum clean, yum clean all (= yum clean packages; yum clean oldheaders) :清除缓存目录下的软件包及旧的headers*
```

## dnf

### dnf简介

**DNF** 是新一代的rpm软件包管理器。他首先出现在 Fedora 18 这个发行版中。而最近，它取代了yum，正式成为 Fedora 22 的包管理器。

DNF包管理器克服了YUM包管理器的一些瓶颈，提升了包括用户体验，内存占用，依赖分析，运行速度等多方面的内容。DNF使用 RPM, libsolv 和 hawkey 库进行包管理操作。尽管它没有预装在 CentOS 和 RHEL 7 中，但你可以在使用 YUM 的同时使用 DNF 。

### 安装DNF包管理器

1、为了安装 DNF ，您必须先安装并启用 epel-release 依赖。

在系统中执行以下命令：

```
# yum install epel-release

```

或者

```
# yum install epel-release -y

```

2、使用 epel-release 依赖中的 YUM 命令来安装 DNF 包。在系统中执行以下命令：

```
# yum install dnf

```

### 示例仓库源配置

这里是为后续案例做说明，假设文件在`/etc/yum.repos.d/openEuler_aarch64.repo`下，内容如下

```
[openEuler-source]
name=openEuler-source
baseurl=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/source/
enabled=1
gpgcheck=1
gpgkey=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/source/RPM-GPG-KEY-openEuler
 
[openEuler-os]
name=openEuler-os
baseurl=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/OS/aarch64/
enabled=1
gpgcheck=1
gpgkey=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/OS/aarch64/RPM-GPG-KEY-openEuler

[openEuler-everything]
name=openEuler-everything
baseurl=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/everything/aarch64/
enabled=1
gpgcheck=1
gpgkey=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/everything/aarch64/RPM-GPG-KEY-openEuler
 
[openEuler-EPOL]
name=openEuler-epol
baseurl=https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS/EPOL/aarch64/
enabled=1
gpgcheck=0

```

### 相关命令

#### 1、查看版本

用处：该命令用于查看安装在您系统中的 DNF 包管理器的版本

```
# dnf --version

```

#### 2、查看系统中的软件库（源）

用处：该命令用于显示系统中可用的 DNF 软件库

```
# dnf repolist

```

结果

```
[root@localhost ~]# dnf repolist
仓库标识										 仓库名称
repo id                                             repo name
openEuler-EPOL                                      openEuler-epol
openEuler-everything                                openEuler-everything
openEuler-os                                        openEuler-os
openEuler-source                                    openEuler-source

```

可以加上**all**，用于显示系统中可用和不可用的所有的 DNF 软件库

```
# dnf repolist all

```

结果

```
[root@localhost ~]# dnf repolist all
仓库标识                  仓库名称                        启用状态
repo id                  repo name                       status
openEuler-EPOL           openEuler-epol                  enabled
openEuler-everything     openEuler-everything            enabled
openEuler-os             openEuler-os                    enabled
openEuler-source         openEuler-source                enabled

```

#### 3、列出系统或源上的RPM包

用处：该命令用于列出用户系统上的**所有来自软件库**的可用软件包和所有已经安装在系统上的软件包

```
# dnf list

```

结果

```
安装包                    版本                       所属源
zstd-help.noarch      1.3.6-3.oe1             openEuler-everything
zvbi.aarch64          0.2.35-7.oe1            openEuler-EPOL      
zvbi-devel.aarch64    0.2.35-7.oe1            openEuler-EPOL      
zvbi-help.aarch64     0.2.35-7.oe1            openEuler-EPOL      
zziplib.aarch64       0.13.69-5.oe1           openEuler-os

```

也可以只列出所有**安装**了的 RPM 包

```
# dnf list installed

```

也可以列出来自所有可用软件库的可供安装的软件包

```
# dnf list available

```

#### 4、搜索软件库中的RPM包

用处：当你不知道你想要安装的软件的准确名称时，你可以用该命令来搜索软件包。你需要在”search”参数后面键入软件的部分名称来搜索。（在本例中我们使用”mysql”）

```
# dnf search mysql

```

结果

```
[root@localhost ~]# dnf search mysql
Last metadata expiration check: 3:00:11 ago on 2021年02月08日 星期一 17时27分06秒.
===================================== Name Exactly Matched: mysql ======================================
mysql.src : The world's most popular open source database
mysql.aarch64 : The world's most popular open source database
==================================== Name &amp; Summary Matched: mysql =====================================
redland-mysql.aarch64 : Redland MySQL storage
pcp-pmda-mysql.aarch64 : PCP metrics for MySQL
python-PyMySQL.src : Pure Python MySQL Client
python2-PyMySQL.noarch : Pure Python2 MySQL Client
python3-PyMySQL.noarch : Pure Python3 MySQL client
qt5-qtbase-mysql.aarch64 : MySQL driver for Qt5's SQL classes
python-mysqlclient.src : MySQL database connector for Python
freeradius-mysql.aarch64 : MySQL support of the FreeRADIUS package
python2-mysqlclient.aarch64 : MySQL database connector for Python2
python3-mysqlclient.aarch64 : MySQL database connector for Python3
perl-DBD-MySQL-help.aarch64 : Including man files for perl-DBD-MySQL
perl-DBD-MySQL.src : Perl [DBI] driver for access to MySQL databases.
perl-DBD-MySQL.aarch64 : Perl [DBI] driver for access to MySQL databases.
php-mysqlnd.aarch64 : A module for PHP applications that use MySQL databases
python2-mysqlclient-debug.aarch64 : Python2 interface to MySQL, built for the CPython debug runtime
python3-mysqlclient-debug.aarch64 : Python3 interface to MySQL, built for the CPython debug runtime

```

#### 5、查找某一文件的提供者

用处：当你想要查看是哪个软件包提供了系统中的某一文件时，你可以使用这条命令。

例如这里我们查找`/lib64/libpthread.so.0`属于哪个rpm包

```
# dnf provides /lib64/libpthread.so.0

```

结果会在所有系统启动的库内搜索，列出所有含有该文件的rpm包

```
[root@localhost bin]# dnf provides /lib64/libpthread.so.0
Last metadata expiration check: 0:03:21 ago on 2021年02月08日 星期一 20时28分37秒.
glibc-2.28-36.oe1.aarch64 : The GNU libc libraries
Repo        : openEuler-os
Matched from:
Filename    : /lib64/libpthread.so.0

glibc-2.28-36.oe1.aarch64 : The GNU libc libraries
Repo        : openEuler-everything
Matched from:
Filename    : /lib64/libpthread.so.0

glibc-2.28-127.el8.aarch64 : The GNU libc libraries
Repo        : @System
Matched from:
Filename    : /lib64/libpthread.so.0

```

#### 6、查看软件包详情

用处：当你想在安装某一个软件包之前查看它的详细信息时，这条命令可以帮到你。

例如查找mysql

```
dnf info mysql

```

结果会列出所有源下该包信息

```
Available Packages
Name         : mysql
Version      : 8.0.17
Release      : 3.oe1
Architecture : aarch64
Size         : 416 M
Source       : mysql-8.0.17-3.oe1.src.rpm
Repository   : openEuler-everything
Summary      : The world's most popular open source database
URL          : http://www.mysql.com/
License      : GPLv2
Description  : The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
             : and robust SQL (Structured Query Language) database server. MySQL Server
             : is intended for mission-critical, heavy-load production systems as well
             : as for embedding into mass-deployed software. MySQL is a trademark of
             : Oracle and/or its affiliates
             : 
             : The MySQL software has Dual Licensing, which means you can use the MySQL
             : software free of charge under the GNU General Public License
             : (http://www.gnu.org/licenses/). You can also purchase commercial MySQL
             : licenses from Oracle and/or its affiliates if you do not wish to be bound by the terms of
             : the GPL. See the chapter "Licensing and Support" in the manual for
             : further info.

Name         : mysql
Version      : 8.0.17
Release      : 3.oe1
Architecture : aarch64
Size         : 416 M
Source       : mysql-8.0.17-3.oe1.src.rpm
Repository   : openEuler-os
Summary      : The world's most popular open source database
URL          : http://www.mysql.com/
License      : GPLv2
Description  : The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
             : and robust SQL (Structured Query Language) database server. MySQL Server
             : is intended for mission-critical, heavy-load production systems as well
             : as for embedding into mass-deployed software. MySQL is a trademark of
             : Oracle and/or its affiliates
             : 
             : The MySQL software has Dual Licensing, which means you can use the MySQL
             : software free of charge under the GNU General Public License
             : (http://www.gnu.org/licenses/). You can also purchase commercial MySQL
             : licenses from Oracle and/or its affiliates if you do not wish to be bound by the terms of
             : the GPL. See the chapter "Licensing and Support" in the manual for
             : further info.

Name         : mysql
Version      : 8.0.17
Release      : 3.oe1
Architecture : src
Size         : 177 M
Source       : None
Repository   : openEuler-source
Summary      : The world's most popular open source database
URL          : http://www.mysql.com/
License      : GPLv2
Description  : The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
             : and robust SQL (Structured Query Language) database server. MySQL Server
             : is intended for mission-critical, heavy-load production systems as well
             : as for embedding into mass-deployed software. MySQL is a trademark of
             : Oracle and/or its affiliates
             : 
             : The MySQL software has Dual Licensing, which means you can use the MySQL
             : software free of charge under the GNU General Public License
             : (http://www.gnu.org/licenses/). You can also purchase commercial MySQL
             : licenses from Oracle and/or its affiliates if you do not wish to be bound by the terms of
             : the GPL. See the chapter "Licensing and Support" in the manual for
             : further info.


```

其他可选项

```
--all                 显示所有的软件包（默认）
--available           只显示可用的软件包
--installed           只显示已安装的软件包
--extras              只显示额外的软件包
--updates             只显示需要被升级的软件包
--upgrades            只显示需要被升级的软件包
--autoremove          只显示需要被删除的软件包
--recent              限制最近被改变的软件包

```

#### 7、下载软件包相关

用处：从配置的源中下载指定软件包到本地目录

```
# dnf download 二进制rpm包名 --downloaddir=指定目录

```

结果

```
[root@localhost ~]# dnf download vim --downloaddir=/root/
Last metadata expiration check: 0:46:36 ago on 2021年02月09日 星期二 08时35分32秒.
vim-enhanced-8.1.450-8.oe1.aarch64.rpm                                  2.1 MB/s | 1.3 MB     00:00   

```

其他相关主要参数

```
  --source              取而代之下载源代码软件包 src.rpm
  --debuginfo           取而代之下载 -debuginfo 软件包
  --debugsource         下载debugsource包
  --arch [arch], --archlist [arch] 限定查询指定架构的软件包
  --resolve             解析并下载所需的依赖关系
  --alldeps             使用resolve运行时，下载所有依赖项，不排除已经安装的
  --url, --urls         打印 rpm 可被下载的 url 列表而不是直接下载
  --urlprotocols        当执行时带有 --url 参数，则限制使用指定协议

```

#### 8、匹配软件包的相关信息

用处：很常用的命令，用于在源中匹配与需要查询的包的一系列相关包信息（带 repoquery 的命令实质上都是从 primary.sqlite 等数据库查询结果的）

```
dnf repoquery [--conflicts|--enhances|--obsoletes|--provides|--recommends|--requires|--suggest|--supplements|--whatrequires] [key] [--tree]

```

如下

```
--whatdepends REQ     选择 requires、suggest、supplement、enhance 或 recommend
                        软件包提供和文件 REQ 的结果
--whatobsoletes REQ   只显示废弃 REQ 的结果
--whatprovides REQ    仅显示提供指定依赖的结果
--whatrequires REQ    仅显示需要指定软件包提供和文件的结果，谁安装依赖这个包
--whatrecommends REQ  仅显示推荐指定依赖的结果
--whatenhances REQ    仅显示增强指定依赖的结果
--whatsuggests REQ    仅显示建议指定依赖的结果
--whatsupplements REQ
                        仅显示补充指定依赖的结果
--alldeps             检查未明示的依赖（文件及提供者）；默认选项
--exactdeps           检查如输入指出的依赖关系，并非 --alldeps
--recursive           与 --whatrequires、--requires 和 --resolve一起使用，递归查询软件包
--deplist             列出这些软件包的依赖关系以及提供这些软件的源
--querytags           显示可被 --queryformat 使用的标签
--resolve             解析功能所来自的软件包
--tree                显示软件包的递归树
  --srpm                在相关源 RPM 中操作
  --latest-limit LATEST_LIMIT
                        显示 N 个指定 name.arch 下最新的软件包（或者最旧的如果 N 为负值）
  --disable-modular-filtering
                        同时列出非活动模块流的软件包
  -i, --info            显示关于软件包的详细信息
  -l, --list            显示软件包中的文件列表
  -s, --source          显示软件包的源 RPM 名称
  --changelogs          显示软件包的 changelogs
  --qf QUERYFORMAT, --queryformat QUERYFORMAT
                        用于显示已查找到软件包的格式
  --nevra               使用 name-epoch:version-release.architecture
                        的格式来输出找到的软件包（默认格式）。
  --nvr                 使用 name-version-release 的格式来输出找到的软件包（使用 rpm 查询的默认格式）。
  --envra               使用 epoch:name-version-release.architecture
                        的格式来输出找到的软件包。

--provides            显示软件包所提供的功能
--requires            显示软件包所依赖的功能
--requires-pre        如果没有安装软件包，则显示它所依赖的运行%pre和%post
                        脚本程序的能力。如果安装了软件包，则显示%pre， %post，

```

**查看某个命令是哪个包提供的**

```
[root@localhost packages]# dnf repoquery --whatprovides openssl
Last metadata expiration check: 0:38:14 ago on Wed 14 Apr 2021 02:50:03 PM CST.
openssl-1:1.1.1f-1.oe1.x86_64

```

**查看哪些包的安装依赖这个包**

```
[root@localhost packages]# dnf repoquery --whatrequires perl-Socket
Last metadata expiration check: 0:26:51 ago on Wed 14 Apr 2021 02:50:03 PM CST.
amanda-0:3.5.1-18.oe1.x86_64
drpmsync-0:3.6.2-4.oe1.x86_64
ldirectord-0:4.2.0-2.oe1.x86_64
mariadb-3:10.3.9-9.oe1.src
mariadb-test-3:10.3.9-9.oe1.x86_64
mrtg-0:2.17.7-3.oe1.x86_64
mrtg-help-0:2.17.7-3.oe1.noarch
mysql5-0:5.7.21-3.oe1.src
mysql5-test-0:5.7.21-3.oe1.x86_64
...
```

**安装软件包**

用处：使用该命令，系统将会自动安装对应的软件及其所需的所有依赖（在本例中，我们将用该命令安装nano软件）

```
# dnf install nano

```

**升级软件包**

用处：该命令用于升级制定软件包（在本例中，我们将用命令升级”systemd”这一软件包）

```
# dnf update systemd

```

**检查系统软件包的更新**

用处：该命令用于检查系统中所有软件包的更新

```
# dnf check-update

```

**升级所有系统软件包**

用处：该命令用于升级系统中所有有可用升级的软件包

```
# dnf update 或 # dnf upgrade

```

**删除软件包**

用处：删除系统中指定的软件包（在本例中我们将使用命令删除”nano”这一软件包）

```
# dnf remove nano 或 # dnf erase nano

```

**删除无用孤立的软件包**

用处：当没有软件再依赖它们时，某一些用于解决特定软件依赖的软件包将会变得没有存在的意义，该命令就是用来自动移除这些没用的孤立软件包。

```
# dnf autoremove

```

**删除缓存的无用软件包**

用处：在使用 DNF 的过程中，会因为各种原因在系统中残留各种过时的文件和未完成的编译工程。我们可以使用该命令来删除这些没用的垃圾文件。

```
# dnf clean all

```

**获取有关某条命令的使用帮助**

用处：该命令用于获取有关某条命令的使用帮助（包括可用于该命令的参数和该命令的用途说明）（本例中我们将使用命令获取有关命令”clean”的使用帮助）

```
# dnf help clean

```

**查看所有的DNF命令及其用途**

用处：该命令用于列出所有的 DNF 命令及其用途

```
# dnf help

```

**查看DNF命令的执行历史**

用处：您可以使用该命令来查看您系统上 DNF 命令的执行历史。通过这个手段您可以知道在自您使用 DNF 开始有什么软件被安装和卸载。

```
# dnf history

```

**查看所有的软件包组**

用处：该命令用于列出所有的软件包组

```
# dnf grouplist

```

**安装一个软件包组**

用处：该命令用于安装一个软件包组（本例中，我们将用命令安装”Educational Software”这个软件包组）

```
# dnf groupinstall ‘Educational Software’

```

**升级一个软件包组中的软件包**

用处：该命令用于升级一个软件包组中的软件包（本例中，我们将用命令升级”Educational Software”这个软件包组中的软件）

```
# dnf groupupdate ‘Educational Software’

```

**删除一个软件包组**

用处：该命令用于删除一个软件包组（本例中，我们将用命令删除”Educational Software”这个软件包组）

```
# dnf groupremove ‘Educational Software’

```

**从特定的软件包库安装特定的软件**

用处：该命令用于从特定的软件包库安装特定的软件（本例中我们将使用命令从软件包库 epel 中安装 phpmyadmin 软件包）

```
# dnf –enablerepo=epel install phpmyadmin

```

**更新软件包到最新的稳定发行版**

用处：该命令可以通过所有可用的软件源将已经安装的所有软件包更新到最新的稳定发行版

```
# dnf distro-sync

```

**重新安装特定软件包**

用处：该命令用于重新安装特定软件包（本例中，我们将使用命令重新安装”nano”这个软件包）

```
# dnf reinstall nano

```

**回滚某个特定软件的版本**

用处：该命令用于降低特定软件包的版本（如果可能的话）（本例中，我们将使用命令降低”acpid”这个软件包的版本）

```
# dnf downgrade acpid

```

样例输出：

```
Using metadata from Wed May 20 12:44:59 2015
No match for available package: acpid-2.0.19-5.el7.x86_64
Error: Nothing to do.

```



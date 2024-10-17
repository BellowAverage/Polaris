
--- 
title:  rpmbuild 构建 rpm 包 
tags: []
categories: [] 

---
### 生成 rpmbuild 目录 

如果需要自己完全从源码构建的话，就需要先构造好 rpmbuild 目录了。

```
[root@localhost ~]# yum install rpmdevtools
[root@localhost ~]# rpmdev-setuptree
[root@localhost ~]# tree rpmbuild/
rpmbuild/
├── BUILD                       #存放生成的源码包
├── RPMS                        #存放生成的二进制包
├── SOURCES                     #放置打包资源，包括源码打包文件和补丁文件等
├── SPECS                       #放置SPEC文档
└── SRPMS                       #存放生成的源码包

5 directories, 0 files

```

```
yum install rpmbuild   # 或者 yum install rpm-build
```

如果已经有了 .src.rpm 的源码包的话，就先用 rpm 命令进行安装。

```
[root@localhost ~]# rpm -ivh abrt-2.1.11-60.el7.centos.src.rpm 
Updating / installing...
   1:abrt-2.1.11-60.el7.centos        ################################# [100%]

```

然后在用户 home 目录下，就会出现一个 rpmbuild 目录。

```
[root@localhost ~]# tree rpmbuild/ -L 1
rpmbuild/
├── SOURCES
└── SPECS

2 directories, 0 files

```

### 从 spec 构建 rpm 包

其中 SPECS 下就是 spec 文件：

```
[root@localhost rpmbuild]# ll SPECS/
total 140
-rw-rw-r--. 1 root root 141637 Oct  1  2020 abrt.spec

```

SOURCES 目录下自然就是源码目录了（其内容本质类似于用 rpm2cpio *.src.rpm | cpio -div 解压得到的源码文件）：

```
[root@localhost rpmbuild]# ll SOURCES/
total 15284
-rw-rw-r--. 1 root root    1033 Sep 30  2020 0001-Do-not-enabled-Shortened-reporting-in-GNOME.patch
-rw-rw-r--. 1 root root    1607 Sep 30  2020 0002-remove-abrt-bodhi-from-configuration.patch
-rw-rw-r--. 1 root root    2073 Sep 30  2020 0003-replace-all-Fedora-URLs-by-corresponding-values-for-.patch
-rw-rw-r--. 1 root root     823 Sep 30  2020 0004-have-AutoreportingEnabled-by-default.patch
...
-rw-rw-r--. 1 root root     996 Oct  1  2020 1000-event-don-t-run-the-reporter-bugzilla-h-on-RHEL-and-.patch
-rw-rw-r--. 1 root root    1697 Oct  1  2020 1002-plugin-set-URL-to-retrace-server.patch
-rw-rw-r--. 1 root root     954 Oct  1  2020 1004-turn-sosreport-off.patch
-rw-rw-r--. 1 root root    4905 Oct  1  2020 1005-cli-list-revert-patch-7966e5737e8d3af43b1ecdd6a82323.patch
-rw-rw-r--. 1 root root 2250176 Oct  1  2020 abrt-2.1.11.tar.gz

```

如果直接构建的话，难免会出现很多构建依赖需要安装：

```
root@master ~/build# rpmbuild -ba abrt.spec 
error: Failed build dependencies:
	dbus-devel is needed by abrt-2.1.11-60.el7.x86_64
	gtk3-devel is needed by abrt-2.1.11-60.el7.x86_64
	rpm-devel &gt;= 4.6 is needed by abrt-2.1.11-60.el7.x86_64
	libnotify-devel is needed by abrt-2.1.11-60.el7.x86_64
	dbus-glib-devel is needed by abrt-2.1.11-60.el7.x86_64
	python-devel is needed by abrt-2.1.11-60.el7.x86_64
	intltool is needed by abrt-2.1.11-60.el7.x86_64
	libtool is needed by abrt-2.1.11-60.el7.x86_64
	nss-devel is needed by abrt-2.1.11-60.el7.x86_64
	asciidoc is needed by abrt-2.1.11-60.el7.x86_64
	doxygen is needed by abrt-2.1.11-60.el7.x86_64
	xmlto is needed by abrt-2.1.11-60.el7.x86_64
	libreport-devel &gt;= 2.1.11-46 is needed by abrt-2.1.11-60.el7.x86_64
	satyr-devel &gt;= 0.13-10 is needed by abrt-2.1.11-60.el7.x86_64
	systemd-python is needed by abrt-2.1.11-60.el7.x86_64
	libreport-gtk-devel &gt;= 2.1.11-46 is needed by abrt-2.1.11-60.el7.x86_64
	polkit-devel is needed by abrt-2.1.11-60.el7.x86_64
	python-nose is needed by abrt-2.1.11-60.el7.x86_64
	python-sphinx is needed by abrt-2.1.11-60.el7.x86_64
	python2-devel is needed by abrt-2.1.11-60.el7.x86_64

```

手动用 yum install 去安装的话显然太累了，这时候我们就可以用 yum-builddep 去安装依赖了（spec 里边写好了需要安装的依赖）。

```
[root@localhost SPECS]# yum-builddep -y abrt.spec 
Loaded plugins: fastestmirror
Enabling base-source repository
Enabling extras-source repository
Enabling updates-source repository
Loading mirror speeds from cached hostfile
 * base: mirrors.163.com
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.163.com
Checking for new repos for mirrors
Getting requirements for abrt.spec
...
Dependency Installed:
  at-spi2-atk-devel.x86_64 0:2.26.2-1.el7                                         at-spi2-core-devel.x86_64 0:2.28.0-1.el7                                        

Complete!

```

如果你机器上还没有 **yum-builddep** 的话，用 yum provides 命令查一下，然后安装一下，比如这块是 **yum-utils** 。

```
[root@localhost SPECS]# yum provides yum-builddep
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.163.com
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.163.com
yum-utils-1.1.31-54.el7_8.noarch : Utilities based around the yum package manager
Repo        : base
Matched from:
Filename    : /usr/bin/yum-builddep



yum-utils-1.1.31-54.el7_8.noarch : Utilities based around the yum package manager
Repo        : @base
Matched from:
Filename    : /usr/bin/yum-builddep


[root@localhost SPECS]# yum install yum-utils
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.163.com
 * extras: mirrors.huaweicloud.com
 * updates: mirrors.163.com
Resolving Dependencies
--&gt; Running transaction check
---&gt; Package yum-utils.noarch 0:1.1.31-54.el7_8 will be installed
--&gt; Finished Dependency Resolution

Dependencies Resolved
...
```

然后执行构建命令，开始构建就好了（当然，构建也不一定会成功）。

```
[root@localhost SPECS]# rpmbuild -ba abrt.spec 
...
+ cd /root/rpmbuild/BUILD
+ cd abrt-2.1.11
+ rm -rf /root/rpmbuild/BUILDROOT/abrt-2.1.11-60.el7.x86_64
+ exit 0

```

提示：-ba 表示 build all，即生成包括二进制包和源代码包的所有 RPM 包，如果正常的话，rpmbuild 将正常退出，同时在 RPMS（二进制包） 目录和SRPMS（源码包） 目录中将生成对应的 RPM 包。

```
[root@localhost rpmbuild]# tree -d -L 2
.
├── BUILD
│   └── abrt-2.1.11
├── BUILDROOT
├── RPMS
│   ├── noarch
│   └── x86_64
├── SOURCES
├── SPECS
└── SRPMS

9 directories

```

如果需要自己完全从源码构建的话，就需要先构造好 rpmbuild 目录了。

```
[root@localhost ~]# yum install rpmdevtools
[root@localhost ~]# rpmdev-setuptree
[root@localhost ~]# tree rpmbuild/
rpmbuild/
├── BUILD                       # 存放生成的源码包
├── BUILDROOT                   # 相当于系统 / 目录，里面的文件结构，最后在 rpm 安装的时候会按照 buildroot 目录下的文件层级结构安装到 / 目录下。
├── RPMS                        # 存放生成的二进制包
├── SOURCES                     # 放置打包资源，包括源码打包文件和补丁文件等
├── SPECS                       # 放置SPEC文档
└── SRPMS                       # 存放生成的 src.rpm 源码包

6 directories, 0 files

```

然后把源码和 spec 文件分别放到对应的目录下，接着继续执行上面的步骤就好了。 

### 关键字和宏

对于我们小白来说，最难的莫过于理解里边大量的关键字和宏。而且有些宏对应的值是根据不同的系统而有差异的。

但是我们一般可以使用 **rpm --eval "%{_topdir}" **这种的形式直接在命令行查看宏实际的值。



```
root@master ~# rpm --eval "%{_bindir}"
/usr/bin
root@master ~# rpm --eval "%{_topdir}"
/root/rpmbuild
root@master ~# rpm --eval "%{_buildrootdir}"
/root/rpmbuild/BUILDROOT

```

**Name: **软件包的名称，后面可使用 %{name} 的方式引用**Summary: **软件包的内容概要**Version:** 软件的实际版本号，例如：1.0.1等，后面可使用 %{version} 引用**Release:** 发布序列号，例如：1 等，标明第几次打包，后面可使用 %{release} 引用，一般会包含在打好的 rpm 包的文件名里边。

**Build Arch:** 指编译的目标处理器架构，noarch 表示不指定架构（或者说打出的 rpm 包架构无关）。

一般默认情况下，打出来的包类似于 **%{name}-%{version}-%{release}.%{arch}.rpm** 的命名结构，比如：**test-1.0-1.noarch.rpm****Group: **软件分组，建议使用标准分组**License: **软件授权方式，通常就是GPL**Source: **源代码包，可以带多个用Source1、Source2等源，后面也可以用 %{source1}、%{source2} 引用 

**BuildRoot: **这个是安装或编译时使用的“虚拟目录”

**Requires:** 该rpm包所依赖的软件包名称，可以用&gt;=或&lt;=表示大于或小于某一特定版本

**Provides:** 指明本软件一些特定的功能，以便其他rpm识别**Packager:** 打包者的信息

**%install** 开始把软件安装到虚拟的根目录中 这个很重要，因为如果这里的路径不对的话，则下面%file中寻找文件的时候就会失败。

**%pre** rpm安装前执行的脚本**%post** rpm安装后执行的脚本**%preun** rpm卸载前执行的脚本**%postun** rpm卸载后执行的脚本

**%preun %postun 的区别是什么呢？**

前者在升级的时候会执行，后者在升级rpm包的时候不会执行

%**files** 定义那些文件或目录会放入rpm中**%exclude** 列出不想打包到rpm中的文件 ※小心，如果%exclude指定的文件不存在，也会出错的。 **%changelog** 变更日志



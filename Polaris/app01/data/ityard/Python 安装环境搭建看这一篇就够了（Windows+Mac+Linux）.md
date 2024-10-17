
--- 
title:  Python 安装环境搭建看这一篇就够了（Windows+Mac+Linux） 
tags: []
categories: [] 

---
### Windows

**1. 下载Python安装包**

访问Python官网（www.python.org），点击页面上的“Downloads”，选择你的操作系统：

笔者的电脑是Windows 10系统，所以进入了Windows的下载页面，我们要下载Python的最新版，因此点击下载区域的“Latest Python 3 Release - Python 3.9.5“，如图：

当然，如果要下载指定版本，你也可以在“Stable Releases”中找到需求版本。进入了Python3.9.5的安装包下载页面，翻滚到最底部，找到下载表格：

根据系统位数选择安装包并下载。

**2. 运行Python安装包**

打开下载的安装包exe，如图：

等待进度条，安装完毕后，退出页面：

**3. IDLE编辑器使用**

IDLE是Python自带的集成开发环境，首先在开始菜单中搜索“IDLE”，打开搜索到的程序：

键入指令：

```
&gt;&gt;&gt; print("Hello, world !")

```

接下来学习如何新建，保存和运行一个Python程序。

点击菜单栏中的“File” --&gt; “New File”，新建文件并写入代码：

再次点击“FIie” --&gt; “Save”，保存Python文件。

然后，点击“Run” --&gt; “Run Module”， 运行程序：

作者：wangzirui32 原文链接：https://blog.csdn.net/wangzirui32/article/details/117156716

### Mac

**1. 下载安装文件**

访问Python官网（www.python.org），选取稳定版本，如：macOS 64-bit installer点击下载。

**2. 安装文件**

打开下载的安装文件，按照提示信息点击“继续”安装，直至安装完成。

**3. 配置mac默认版本是python3**

打开终端，输入命令which python3，查看python3的安装目录

将路径配入环境变量。

在文件最后加上alias python="/Library/Frameworks/Python.framework/Versions/3.8/bin/python3"，保存并退出

在终端输入source ~/.bash_profile使其生效，查看当前python版本：

作者：lemon柚子 原文链接：https://blog.csdn.net/lemontree_cxs/article/details/107431120

### Linux

Linux，centos系统本身默认安装有python2.x，版本x根据不同版本系统有所不同，可通过 python --V 或 python --version 查看系统自带的python版本

有一些系统命令时需要用到python2，不能卸载

**1. 安装依赖包**

1）首先安装gcc编译器，gcc有些系统版本已经默认安装，通过  gcc --version  查看，没安装的先安装gcc，yum -y install gcc

2）安装其它依赖包，（注：不要缺少，否则有可能安装python出错，python3.7.0以下的版本可不装 libffi-devel ）

yum-yinstallzlib-develbzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

**2. 下载python3.7.3源码，根据需求下载**

1）去python官网下载源码包

```
https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz

```

2）下载

3）解压Python-3.7.2.tgz

```
tar -zvxf Python-3.7.2.tgz

```

**3. 建立一个空文件夹，用于存放python3程序**

```
mkdir/usr/local/python3  //做完了需要每次新建单个文件夹 mkdir usr 建完之后 cd usr 到usr文件夹继续建剩下，步骤一致

```

**4. 执行配置文件，编译，编译安装**

```
cd Python-3.7.2 先进去桌面已经解压文件
在执行下面这段 ./configure --prefix=/usr/local/python3 &amp;&amp;make &amp;&amp;make install
安装完成没有提示错误便安装成功了

```

**5. 建立软连接**

```
ln -s /usr/local/python3/bin/python3.7/usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7/usr/bin/pip3

```

**6. 测试一下python3是否可以用**

```
如果Python3 查看不到Python3.7.2版本，需要添加系统变量
export PATH=$PATH:$HOME/bin:/usr/local/python3/bin  这个只是当前窗口临时查看
复制代码

```

**7. 添加永久系统变量**

通过修改profile文件:

```
执行 vim /etc/profile
/export PATH //找到设置PATH的行，添加
export PATH=/usr/local/python37/bin:$PATH
:wq  //保存文件并退出vi

```

生效方法：
- 系统重启- 要想马上生效还要运行
```
# source /etc/profile

```

不然只能在下次重进此用户时生效。

有效期限：永久有效 用户局限：对所有用户

到这里，就可以执行查看到Python 3.7.2版本！

作者：灰太狼的精神 原文链接：https://juejin.cn/post/6844903987146145800

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/c3bcdb7345cc16456960960486bb8ddd.gif">

微信扫码关注，了解更多内容

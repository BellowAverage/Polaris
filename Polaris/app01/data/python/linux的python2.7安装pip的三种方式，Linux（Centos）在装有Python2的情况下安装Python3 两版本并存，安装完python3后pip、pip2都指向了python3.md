
--- 
title:  linux的python2.7安装pip的三种方式，Linux（Centos）在装有Python2的情况下安装Python3 两版本并存，安装完python3后pip、pip2都指向了python3 
tags: []
categories: [] 

---
## 安装pip的三种方式

pip是python的一个工具，用来安装python包特别方便。 Linux系统是是内置python程序，因为许多Linux内置文件都是使用python来编写的，比如说yum。

### 1.脚本安装

<mark>推荐安装方式</mark> 通过脚本的方式可以保证都能够安装到最新版本的pip，同时操作简单。

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

```

```
python get-pip.py

```

### 2.源码包安装

下载地址：https://pypi.org/search/?q=pip

```
wget --no-check-certific ate https://pypi.python.org/packages/source/p/pip/pip-10.0.1.tar.gz &gt;&gt;/dev/null

```

```
tar -zvxf pip-10.0.1.tar.gz &gt;&gt; /dev/null

```

```
cd pip.10.0.1

```

```
python3 setup.py build

```

```
python3 setup.py install

```

注意，这里是安装到python3中，默认是安装到python所链接的具体版本中。

### 3.python安装

这种方式，直接通过python安装，与脚本安装类似，但是这个安装的是当前python版本所以依赖的pip，可能版本较低，因为内置python版本并不高。

```
yum upgrade python-setuptools

```

```
yum install python-pip

```

感兴趣的小伙伴可以看一下官方文档连接

## Linux安装pip

脚本安装方式，如果直接用yum install 安装可能会遇到很多问题。官网的这个方法可以很快很安全的安装好pip。也就是上述的方式一 官网地址： 1、打开后，点击“Installation” <img src="https://img-blog.csdnimg.cn/20210101135430633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 2、进入Installation页面后，右键点击“get-pip.py”,选择“复制链接地址” <img src="https://img-blog.csdnimg.cn/20210101135506438.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 3、在Linux中输入 wget 粘帖复制的地址

4、下载完成后，执行命令python get-pip.py <img src="https://img-blog.csdnimg.cn/20210101135542614.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

## Linux（Centos）在装有Python2的情况下安装Python3 两版本并存

Centos7自带python2.7版本，如果想要安装python3，要么卸载Linux自带的python(风险较大，浪费过一中午的时间)，再安装python3；要么在装有python2的基础上直接安装python3，让两版本并存【这部分就是详细展开说说…】

#### 1、查看Python2的位置

whereis python <img src="https://img-blog.csdnimg.cn/20210101141233234.png" alt="在这里插入图片描述"> 可知，python 在/usr/bin/中 <img src="https://img-blog.csdnimg.cn/20210101141333692.png" alt="在这里插入图片描述"> 从上面可以看出python和python2<mark>指向的</mark>都是python2。 <img src="https://img-blog.csdnimg.cn/20210101141500176.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 执行python和python2都可以启动python2.7，所以后续安装python3后可以将python3软连接到python。

#### 2、安装编译python的相关包

```
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make -y

```

<img src="https://img-blog.csdnimg.cn/20210101141730220.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 3、下载要安装的python3版本

去官网选择自己想要的版本去下载，下载网址：

小插曲： .tgz是.tar.gz 的简写形式

1.下载python3 （可以到官方先看最新版本多少，因为我windows上装的是3.7.8，所以我想在linux上也装3.7.8，大家可以根据自己的需求选择版本）

输入命令 `wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz` wget后面的地址根据自己的需求更换

2.安装Python3

我这里安装在/usr/bin/python3（具体安装位置看个人喜好） 在/usr/bin/目录下创建python3目录 （1）创建目录： mkdir python3

<img src="https://img-blog.csdnimg.cn/20210103191514857.png" alt="在这里插入图片描述"> （2）输入命令 tar -zxvf Python-3.7.1.tgz 解压下载的python压缩文件 （3）用mv 命令把解压过的python包移到/usr/bin/python3/目录下 （4）进入解压后的目录，编译安装。 4.1）（编译安装前需要安装编译器yum install gcc）安装gcc 用`which gcc`命令查看是否安装了gcc，如果没有执行下面命令 输入命令 `yum install gcc`，确认下载安装输入“y” <img src="https://img-blog.csdnimg.cn/20210103192751975.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4.2）3.7版本之后需要一个新的包libffi-devel

安装即可：yum install libffi-devel -y <img src="https://img-blog.csdnimg.cn/20210103192828528.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4.3）进入python文件夹，生成编译脚本(指定安装目录)：

```
 cd Python-3.7.8

```

进入Python-3.7.8文件下后，执行下面命令

```
./configure --prefix=/usr/bin/python3  

```

#/usr/bin/python3为上面步骤创建的目录 ，python3.7.8的安装路径。执行./configure命令，自动产生Makefile文件，不懂得，可以在这篇文章里去了解 4.4）编译：`make` <img src="https://img-blog.csdnimg.cn/20210103193817207.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2021010319424330.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 4.5）编译成功后，编译安装：make install <img src="https://img-blog.csdnimg.cn/20210103194313501.png" alt="在这里插入图片描述">

安装成功： <img src="https://img-blog.csdnimg.cn/20210103194457393.png" alt="在这里插入图片描述"> 4.6）检查python3.7的编译器：/usr/bin/python3/bin/python3.7<img src="https://img-blog.csdnimg.cn/20210103194729954.png" alt="在这里插入图片描述"> 3、添加软连接

（1）python软连接,这样以后输入python就会链接得python3版本，而不会去连接python2版本

将原来的python备份： `mv /usr/bin/python /usr/bin/python.bak` 添加python3的软连接 ： `ln -s /usr/local/python37/bin/python3.7 /usr/bin/python` <img src="https://img-blog.csdnimg.cn/20210103195427287.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20210103195617121.png" alt="在这里插入图片描述"> 有时候我们装完python3后，上面我们将python3软连接到python上，之前pip、pip2、pip2.7全都指向了python3，原因如下：

```
#vim /usr/bin/pip
将第一行 #!/usr/bin/python 修改为

#!/usr/bin/python2

然后pip 就指向python2了

```

```
#vim /usr/bin/pip2
将第一行 #!/usr/bin/python 修改为

#!/usr/bin/python2

然后pip2 就指向python2了

```

同理：

```
#vim /usr/bin/pip2.7
将第一行 #!/usr/bin/python 修改为

#!/usr/bin/python2

然后pip2.7 就指向python2了

```

上面的操作有利于我们统一规划，统一管理，然后我们建立pip的软连接 （2）pip软连接

此时查看pip版本pip -V 指向的还是python2 <img src="https://img-blog.csdnimg.cn/20210103202617176.png" alt="在这里插入图片描述">

因此pip也需要创建软连接

备份：mv /usr/bin/pip /usr/bin/pip.bak <img src="https://img-blog.csdnimg.cn/20210103202707857.png" alt="在这里插入图片描述">

创建软连接：ln -s /usr/bin/python3/bin/pip3 /usr/bin/pip <img src="https://img-blog.csdnimg.cn/20210103202806303.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNDAyNjQ4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

4.并将/usr/bin/python3/bin加入PATH

（1）`vim /etc/profile` 到最后一行

（2）按“i”，然后贴上下面内容：

```
# vim ~/.bash_profile

# .bash_profile

# Get the aliases and functions

if [ -f ~/.bashrc ]; then

. ~/.bashrc

fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin:/usr/bin/python3/bin

export PATH

```

（3）按ESC，输入:wq回车退出。

（4）修改完记得执行行下面的命令，让上一步的修改生效：

```
source ~/.bash_profile

```

7.检查Python及pip是否正常可用，是否匹配python3：

```
python -V

```

```
pip -V

```

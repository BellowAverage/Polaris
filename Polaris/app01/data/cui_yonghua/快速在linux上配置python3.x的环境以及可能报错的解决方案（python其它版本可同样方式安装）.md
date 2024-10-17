
--- 
title:  快速在linux上配置python3.x的环境以及可能报错的解决方案（python其它版本可同样方式安装） 
tags: []
categories: [] 

---
#### 一. linux安装python3.x

下面案例是安装python3.9 步骤，也可以指定其他版本安装

<mark>重要！！！ python3.11.x请参考</mark> ：

##### 步骤1：安装系统依赖（重要）

这一步不执行，后面各种错误。

```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel python3-devel libffi-devel

```

##### 步骤2：下载源码并解压：

```
# 下载源码
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz

# 解压
tar -zxvf Python-3.9.0.tgz

cd Python-3.9.0

```

##### 步骤3：编译安装

指定安装目录为/opt/python39

```
./configure --prefix=/opt/python39 
make &amp;&amp; make install

```

##### 步骤4：修改环境变量和验证

追加到PATH中，执行 `vim /etc/profile` 中追加

```
export PATH=/opt/python39/bin:$PATH

```

修改完成之后激活：`source /etc/profile`

最后，版本号验证

```
python3 --version
pip3 --version

```

<img src="https://img-blog.csdnimg.cn/0247ce302e134d8d8bdfa5f4e31d1808.png" alt="在这里插入图片描述">

#### 二. 报错汇总

##### 报错1

```
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for python3.9... no
checking for python3... no
checking for python... python
checking for --enable-universalsdk... no
checking for --with-universal-archs... no
checking MACHDEP... "linux"
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: in `/root/Python-3.9.0':
configure: error: no acceptable C compiler found in $PATH
See `config.log' for more details

```

解决方案： 查看得知未安装合适的编译器。

```
sudo yum install gcc-c++

```

(使用sudo yum install gcc-c++时会自动安装/升级gcc及其他依赖的包。)

重新执行: `./configure`， 即可成功！

##### 报错2

输入`pip3 list` , 出现下面情况时：

```
-bash: pip3: 未找到命令

```

先安装扩展源EPEL，`yum -y install epel-release` , 这个扩展源提供了很多软件包的下载。

安装 pip3 Centos系统：`yum install python3-pip -y` Ubuntu等系统：`sudo apt install python3-pip -y`

升级pip3可用指令：`pip3 install --upgrade pip`

##### 报错3 安装过Python3的其他版本

更改python3和pip3的指向即可。或者先卸载之前的python3，再安装新版本的python3

```
# 删除原先的Python3和pip3
rm -rf /usr/bin/python3
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
rm -rf /usr/bin/pip3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
ln -s /opt/python39/bin/pip3 /usr/local/bin/pip3

ln -s /opt/python39/lib/python3.9/site-packages/pip /usr/local/bin/pip3

```

#### 三. 其它

##### 1. 查看是否安装: `which python `

##### 2. 确定安装目录: 此处安装在：/opt/python3目录

##### 3. 安装依赖：

```
yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel

```

##### 4. 下载安装包

```
cd /opt/software/   

wget  https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz

```

##### 5. 解压压缩包并安装

```
1. 解压  
    tar  -xvf Python-3.9.13.tgz   
2. 进入解压的文件夹  
    cd   Python-3.9.13  
3. 执行初始化，配置安装路径  
    ./configure prefix=/opt/python3  
4. 执行编译安装  
    make   
    make install

5. 添加环境变量：  
    vim  /etc/profile  
    export PATH=/opt/python3/bin:$PATH  
  
    source /etc/profile  

```

##### 6. 添加软连接

```
[root@ec-new-app opt]# ln -s /opt/python3/bin/python3.9 /usr/bin/python3
[root@ec-new-app opt]# ln -s /opt/python3/bin/pip3.9 /usr/bin/pip3
[root@ec-new-app opt]# python3  -V
Python 3.9.13
[root@ec-new-app opt]# pip3  -V
pip 22.0.4 from /opt/python3/lib/python3.9/site-packages/pip (python 3.9)

```

能返回版本号就说明已经安装完成了！！

```
# 查看软连接指向
[root@ec-new-app opt]# ll /usr/bin/ |grep python
-rwxr-xr-x.   1 root root       11232 Aug 13  2019 abrt-action-analyze-python
lrwxrwxrwx    1 root root          23 May 23 17:09 pip3 -&gt; /opt/python3/bin/pip3.9
lrwxrwxrwx.   1 root root           7 Jun 10  2022 python -&gt; python2
lrwxrwxrwx.   1 root root           9 Jun 10  2022 python2 -&gt; python2.7
-rwxr-xr-x.   1 root root        7216 Aug  7  2019 python2.7
lrwxrwxrwx    1 root root          26 May 23 17:07 python3 -&gt; /opt/python3/bin/python3.9

[root@ec-new-app opt]# ll /usr/bin/ |grep pip
-rwxr-xr-x.   1 root root        2291 Jul 31  2015 lesspipe.sh
lrwxrwxrwx    1 root root          23 May 23 17:09 pip3 -&gt; /opt/python3/bin/pip3.9

```

附：卸载python3 1、进入源码目录：`cd /path/to/python3/source` 2、清理安装的文件：`make clean` 3、卸载python3：`make uninstall` 或者 1、卸载python3：`rpm -qa|grep python3|xargs rpm -ev --allmatches --nodeps` 卸载pyhton3 2、`whereis python3 |xargs rm -frv` 删除所有残余文件。成功卸载！ 3、whereis python 查看现有安装的python

若重新安装更高版本，则进入： 选择更高版本即可。

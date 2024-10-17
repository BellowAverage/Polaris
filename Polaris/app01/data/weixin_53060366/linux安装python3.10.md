
--- 
title:  linux安装python3.10 
tags: []
categories: [] 

---
## linux安装python3.10

>  
 在运维方面，用到的脚本比较多，有些脚本用shell 写会比较累，用python 会比较容易，因为python 有强大的类库，可以很好的处理各种环境。 


下面就演示一下linux 系统上安装python 的过程：

### 1、下载python 包：

这里我们去官网直接下载即可：（可能打开官网的速度有点慢。）

<img src="https://img-blog.csdnimg.cn/da25f041a83b461ebe697cf976c1ff16.png#pic_center" alt="在这里插入图片描述">

选择linux系统：

<img src="https://img-blog.csdnimg.cn/538c6e7c3e8049e69a014efebe69d01d.png#pic_center" alt="在这里插入图片描述">

下载稳定版中的新的：

<img src="https://img-blog.csdnimg.cn/f21794be8e9442f187e62c01dfe5a1d4.png#pic_center" alt="在这里插入图片描述">
- 这里因为网速慢的原因，可以考虑先下载到本地，在上传到服务器：- 也可以直接wget 命令下载，不过要耐心等一会
```
#下载python包
wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tgz

#这里没装wget的伙伴，可以yum装下
yum install -y wget

```

### 2、安装python 相关的依赖包：

```
yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

```

### 3、编译安装：
- 这里注意：原先linux 系统上就有python2 存在，我们不要去删除他，否则yum 和防火墙等无法使用。
```
#查看python
python -V
Python 2.7.5

```
- 解压python源码包：
```
tar -zxf Python-3.10.5.tgz
cd Python-3.10.5
./configure --prefix=/usr/local/python3/

```
- 编译安装：
```
make &amp;&amp; make install

```
- 添加环境变量：
```
#python
PATH=/usr/local/python3/bin:$PATH

#保存后，刷新配置文件
source /etc/profile

```
- 添加软连接：
>  
 添加执行文件到 /usr/bin 目录下，使其全局生效 在添加前，/usr/bin 目录下就有python2 版本的执行文件 


<img src="https://img-blog.csdnimg.cn/38b6195b01834c87a6a706ac27b73fe9.png#pic_center" alt="在这里插入图片描述">

```
#这里我们将原先的python 改个名
mv /usr/bin/python /usr/bin/python.bak

#再创建软连接
ln -s /usr/local/python3/bin/python3 /usr/bin/python
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip

python -V
#下面会显示：
Python 3.10.5

```

### 4、优化：

>  
 因为yum 和firewall 都依赖python，所以更改/usr/bin 下的执行文件会导致它们不可用，需要修改配置； 

- 修改yum 配置文件：
```
vi /usr/bin/yum
#将第一行 "#!/usr/bin/python" 改为 "#!/usr/bin/python2.7" 即可

vi /usr/libexec/urlgrabber-ext-down
#这里也一样，#!/usr/bin/python 改为 #!/usr/bin/python2.7

```
- 修改Firewalls配置：
```
vi /usr/bin/firewall-cmd
#将第一行 "#!/usr/bin/python" 改为 "#!/usr/bin/python2.7"

vi /usr/sbin/firewalld
#将第一行 "#!/usr/bin/python" 改为 "#!/usr/bin/python2.7"

```

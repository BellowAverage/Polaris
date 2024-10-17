
--- 
title:  python环境打包、centos 下openssl解决方案、fasttext安装失败 
tags: []
categories: [] 

---
### python环境打包

```
下载：

wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz

解压：

tar -xzvf Python-3.6.8.tgz

#指定python 安装路径

export PYTHON_ROOT=~/Python

#安装 python

cd Python-3.6.8

./configure --prefix="${PYTHON_ROOT}"

make

make install

```

### pip install 报错

按上述方式安装的python3，pip install 会报错：…the ssl module in Python is not available 解决方法： centos环境下的解决方式：

```
yum install openssl

yum install openssl-devel -y

```

重新运行

```
解压：

tar -xzvf Python-3.6.8.tgz

#指定python 安装路径

export PYTHON_ROOT=~/Python

#安装 python

cd Python-3.6.8

```

同时修改Moudles/Setup (该目录在python的解压目录下)

```
vim Modules/Setup.dist
#修改结果如下(将代码前面的注释去掉)：


#Socket module helper for socket(2)
_socket socketmodule.c 
#Socket module helper for SSL support; you must comment out the other
#socket line above, and possibly edit the SSL variable:
#SSL=/usr/local/ssl
_ssl _ssl.c \
-DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
-L$(SSL)/lib -lssl -lcrypto

```

然后cd Python-3.6.8

```
./configure --prefix="${PYTHON_ROOT}"

make

make install

```

done，大功告成

### python环境打包

进入到上述PYTHON_ROOT指定的路径下： cd ~/Python 新建shell脚本，一键上传到hadoop

```
rm -rf Python368.tar.gz

tar -cvzf Python368.tar.gz ./*

hadoop fs -rm viewfs:///home/users/Python368.tar.gz

 hadoop fs -put Python368.tar.gz viewfs:///home/users/

```

### fasttext安装失败

但后面遇到fasttext安装失败，报一大堆红色错误，gcc版本较低 解决方案如下：

```
第一步：安装scl源：

   yum install centos-release-scl scl-utils-build 
   
第二步： 列出scl可用源

   yum list all --enablerepo='centos-sclo-rh'
   
   yum list all --enablerepo='centos-sclo-rh' | grep "devtoolset-"
   
第三步： 安装8版本的gcc、gcc-c++、gdb工具链（toolchian）： 

   yum install -y
   
   devtoolset-8-toolchain
   
   scl enable devtoolset-8 bash
   
最后：查看结果 

   gcc --version

```

重新pip3 install fasttext！

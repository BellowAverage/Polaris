
--- 
title:  Linux Python离线下载模块 
tags: []
categories: [] 

---
**1、单模块下载安装：**

以pymysql模块为例 下载离线安装包

```
pip download -d python_packages pymysql

```

离线安装

```
pip install --no-index --find-links=python_packages pymysql

```

**2、批量下载离线安装包：**

定义需要下载的模块

```
cat pythonInstall.txt 

pyahocorasick
pymysql
pypinyin
gevent
flask
flask_cors

```

批量下载离线安装包

```
pip3 download -d python_packages -r pythonInstall.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple/

# -r 指定安装模块名称存放文件
# -i 指定安装源

```

离线安装

```
pip3 install --no-index --find-links=python_packages -r pythonInstall.txt

```

**3、指定版本下载**

```
pip3 download --no-deps --platform linux_x86_64 -d python_packages lightgbm==3.2.0

```

**4、安装tar包**

先解压在安装

```
tar -xvf file.tar.bz
python setup.py install

```

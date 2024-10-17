
--- 
title:  Python: Could NOT find PythonLibs (如何查找你的python路径)) 
tags: []
categories: [] 

---
## 查找python对应lib和inc

### 1. 背景

使用cmake编译文件的时候报错

```
CMake Error at /usr/local/share/cmake-3.14/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS)

```

### 2. 解决方法

如果是anaconda激活对应的环境,如果不是,直接在终端中输入python或者python3 (需要决定需要查找的python版本)

如果是python 2版本, 输入以下代码

```
root@c10fab84fca7:/usr/Downloads/felaim# python
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; from distutils.sysconfig import get_python_inc
&gt;&gt;&gt; print(get_python_inc())
/usr/include/python2.7
&gt;&gt;&gt; import distutils.sysconfig as sysconfig
&gt;&gt;&gt; print(sysconfig.get_config_var('LIBDIR'))
/usr/lib
&gt;&gt;&gt; 

```

可以看到python的include文件在

```
/usr/include/python2.7

```

python的lib文件在

```
/usr/lib

```

python3的同理

最后在编译的时候添加上对应的参数设置

```
cmake -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib

```

或者直接这样写

```
$ cmake .. \
-DPYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")  \
-DPYTHON_LIBRARY=$(python -c "import distutils.sysconfig as sysconfig; print(sysconfig.get_config_var('LIBDIR'))")

```

如果是anaconda要激活对应环境运行.

参考地址
1. 
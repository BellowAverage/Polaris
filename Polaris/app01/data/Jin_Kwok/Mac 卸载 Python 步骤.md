
--- 
title:  Mac 卸载 Python 步骤 
tags: []
categories: [] 

---
### 1.查看当前 Python 版本

以 python3.11 为例

```
$ python3 -V 

Python 3.11.4
```

### 2.**删除 Python 框架**

**先在目录** /Library/Frameworks/Python.framework/Versions/ 下确定 python3.11 框架存在，而后执行命令删除，需要注意的是，在执行删除命令时可能需要输入密码，不必犹豫，直接输入开机密码即可。

```
ls /Library/Frameworks/Python.framework/Versions/
3.11

sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.11
```

### **3.删除 Python 应用目录**

```
cd /Applications
sudo rm -rf Python\ 3.11/
```

### **4.删除/usr/local/bin 目录下指向的 Python 的连接**

```
cd /usr/local/bin/ 

sudo rm -rf 所有python相关的文件
```

### 5.**删除 python 的环境路径**

```
$ vim ~/.bash_profile
删除其中 Python 的路径
```

至此，Python 就删除干净了，你可以进一步安装新版本的 Python了。


--- 
title:  升级Python3.6到Python3.7 
tags: []
categories: [] 

---
```
python

```

1、安装Python3.7

```
sudo apt-get install python3.7
```

2、为了方便使用，建议创建 首先把之前的软连接删除：

```
sudo rm -rf /usr/bin/python3
sudo rm -rf /usr/bin/pip3
```

查看Python3.7安装路径：

```
which python3.7
#假设返回路径为 "Python3Path"
```

然后创建新的软连接：

```
#添加python3的软链接
sudo ln -s  "Python3Path" /usr/bin/python3
#添加 pip3 的软链接
sudo ln -s  "Python3Path" /usr/bin/pip3
#测试是否安装成功了
python

```



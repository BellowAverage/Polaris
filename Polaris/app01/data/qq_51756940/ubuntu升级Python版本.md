
--- 
title:  ubuntu升级Python版本 
tags: []
categories: [] 

---
**一、已有Python版本**

1.使用以下命令查找系统上所有安装的 Python 版本

```
ls /usr/bin/python*

```

<img alt="" height="51" src="https://img-blog.csdnimg.cn/4890d164afcc453597822dea2e1b9e26.png" width="670">

2.使用以下命令更改 Python 3 的符号链接

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

```

<img alt="" height="42" src="https://img-blog.csdnimg.cn/8281baf70ae8410c8fad80a5953281e3.png" width="700">

 3.使用以下命令检查 Python 3 符号链接的当前版本

```
python3 --version

```

<img alt="" height="40" src="https://img-blog.csdnimg.cn/f39893abddf5470196dff41a9b073910.png" width="239">



**二、下载所需版本**

1. 使用以下命令安装软件包

```
sudo apt-get update
sudo apt-get install software-properties-common
```

2.添加 deadsnakes PPA 存储库，该存储库包含最新的 Python 版本

```
sudo add-apt-repository ppa:deadsnakes/ppa

```

3.安装 Python 3.10

```
sudo apt install python3.10

```

4.更新 Python 3 的符号链接，以便将其设置为默认版本

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

```

4.使用以下命令更改默认 Python 3 版本

```
sudo update-alternatives --config python3

```

该命令将显示所有可用的 Python 3 版本。输入所选版本的编号并按 Enter 键

<img alt="" height="210" src="https://img-blog.csdnimg.cn/c29f8b55a0b24453a8e8fa03043ceb2d.png" width="745">

5. 使用以下命令检查 Python 3 符号链接的当前版本

```
python3 --version

```

<img alt="" height="41" src="https://img-blog.csdnimg.cn/cbc3f3a863fc4d11aa1fbd0faf686550.png" width="254">



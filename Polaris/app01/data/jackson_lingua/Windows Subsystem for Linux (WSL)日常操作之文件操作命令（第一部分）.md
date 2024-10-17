
--- 
title:  Windows Subsystem for Linux (WSL)日常操作之文件操作命令（第一部分） 
tags: []
categories: [] 

---
## Windows Subsystem for Linux (WSL)日常操作之文件操作命令（第一部分）

在Windows 10或11中安装完毕Linux子系统（即Windows Subsystem for Linux, 简称WSL）后，我们可以开始做文件操作了。

### 1. 在Windows搜索栏中，输入”WSL”，点击选择“管理员身份运行”，进入WSL命令行窗口；

可以看到Linux欢迎画面，和当前安装的Linux发行版ubuntu版本为22.04.3 LTS版：

<img src="https://img-blog.csdnimg.cn/577575ddfde5461eaec05e6a0831e39a.png" alt="在这里插入图片描述">

### 2. 进行Linux基本命令操作：

##### 1) 查看当前目录（即当前所在位置）：

```
pwd

```

<img src="https://img-blog.csdnimg.cn/adf858d8ab944e2b86a746c82d200b98.png" alt="在这里插入图片描述"> 显示当前目录为：/mnt/c/WINDOWS/system32, 硬盘的C:卷标挂载到了/mnt/目录下。如果改变目录到D:，则需要执行几个命令：

##### 2) 修改目录到根目录：

cd /

##### 3) 进入到D:\myPython:

```
cd /mnt/d/myPython

```

<img src="https://img-blog.csdnimg.cn/d691361b8e0b4103b3d55daff4778dc3.png" alt="在这里插入图片描述">

##### 4) 查看当前目录的文件情况

```
ls

```

<img src="https://img-blog.csdnimg.cn/7c9dd8685619404a8963bf545f4d18b7.png" alt="在这里插入图片描述"> 接下来分步执行命令如下：

##### 5）创建目录A

```
mkdir A

```

##### 6）创建文件1.txt

```
touch 1.txt

```

##### 7）复制文件1.txt到2.txt

```
cp 1.txt 2.txt

```

##### 8）查看当前目录文件

```
ls

```

##### 9）在A目录下创建子目录B

```
mkdir A/B

```

##### 10）改变目录到/A/B

```
cd ../A/B

```

<img src="https://img-blog.csdnimg.cn/f3b5453c3a2e4c2e92bc6a1d2a8aab61.png" alt="在这里插入图片描述"> 改变目录返回到/newfolder, 继续以下命令。

##### 11）创建目录AAA

```
mkdir AAA

```

##### 12）创建文件AAA.txt

```
touch AAA.txt

```

##### 13）复制AAA.txt到BBB.txt

```
cp AAA.txt BBB.txt

```

##### 14）查看当前目录

```
ls

```

<img src="https://img-blog.csdnimg.cn/013860a5802743448a69169b44f5abed.png" alt="在这里插入图片描述"> 显示存在AAA.txt和BBB.txt文件。

好的，目前为止，你已经成功迈开第一步！ 接下来，会介绍文件操作其它命令，敬请关注。😊

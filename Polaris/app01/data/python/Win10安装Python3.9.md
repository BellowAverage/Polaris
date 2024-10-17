
--- 
title:  Win10安装Python3.9 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- - <ul><li>- - - - - 


### 1.下载Python3.9.1

Python 安装包下载地址：

打开该链接，点击下图中的版本号或者`Download`按钮进入对应版本的下载页面，滚动到最后即可看到各个平台的 Python 安装包。

<img src="https://img-blog.csdnimg.cn/20210109223134349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

这里点击安装最新版的Python 3.9.1

<img src="https://img-blog.csdnimg.cn/20210109223150219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

对前缀的说明：
-  以`Windows installer (64-bit)`开头的是 64 位的 Python 安装程序； -  以`Windows installer (32-bit)`开头的是 32 位的 Python 安装程序。 
对后缀的说明：
- `embeddable zip file`表示`.zip`格式的绿色免安装版本，可以直接嵌入（集成）到其它的应用程序中；- `executable installer`表示`.exe`格式的可执行程序，这是完整的离线安装包，一般选择这个即可；- `web-based installer`表示通过网络安装的，也就是说下载到的是一个空壳，安装过程中还需要联网下载真正的 Python 安装包。
这里我选择的是，也即 64 位的完整的离线安装包。

### 2.安装Python3.9.1

#### Python 安装向导

双击下载得到的 python-3.9.1-amd64.exe，就可以正式开始安装 Python 了

<img src="https://img-blog.csdnimg.cn/20210109223202154.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

勾选`Add Python 3.9 to PATH`，这样可以将 Python 命令工具所在目录添加到系统 Path 环境变量中，以后开发程序或者运行 Python 命令会非常方便。

Python 支持两种安装方式，默认安装和自定义安装：
- 默认安装会勾选所有组件，并安装在 C 盘；- 自定义安装可以手动选择要安装的组件，并安装到指定盘符。
这里我们选择自定义安装。点击`Customize installation`进行入下一步

#### 选择要安装的 Python 组件

<img src="https://img-blog.csdnimg.cn/20210109223211625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
- Documentation 离线的 `.chm` 格式文档，必须保留。英文还 `OK` 的小伙伴可以直接看这份文档，比所有书都靠谱。看英文有压力的，平时随时查查标准库模块用法什么的是极好的。- pip Python 包下载工具，必须保留。- tcl/tk and IDLE ，说来话长，保留就对了。- Python test suite，这个可以没有，当然留下来也没关系。- py launcher。这里额外注意的是 `for all user` 选项，可以选择是否对所有用户安装。如果对所有用户安装，则需要 `administrator` 的权限。
没有特殊要求的话，保持默认即可，也就是全部勾选。

#### 选择安装目录

点击`Next`继续，选择安装目录。

<img src="https://img-blog.csdnimg.cn/20210109223220273.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
- Install for all user，是否对所有人安装，如果是，需要 `administrator` 的权限，并且安装路径会有所不同。- 关联文件到 Python，这个保持原样即可。它就是把 `.py` 文件和 `python` 程序关联起来，这样双击 `.py` 文件的时候，自动就用 `python` 去执行了。- 创建快捷方式，保持原样即可。- 添加 Python 到环境变量，第 2 次修改的机会- 预编译标准库，一次性的把标准库的 `.py` 都预编译成 `.pyc`，没什么必要，会多花费安装时间，不选- 两个 download debug xxx ，不知道哪里会用到，都不选
**注意**：安装路径文件夹名称均不能含有中文字符

选择好你常用的安装目录，点击`Install`，等待几分钟。

#### 禁用系统的Path长度自动限制

安装成功后结束界面可能会出现`Disable path length limit`的按钮，有的话点一下就好了，作用是**禁用系统的Path长度自动限制**，能给我们避免很多的麻烦。

<img src="https://img-blog.csdnimg.cn/20210109223230493.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

点击`Close`，至此，python安装完成

<img src="https://img-blog.csdnimg.cn/20210109223238782.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 3.验证安装成功

安装完成以后，打开 Windows 的命令行程序（命令提示符），同时按下**Windows+R**，**输入cmd**，进入dos窗口

<img src="https://img-blog.csdnimg.cn/20210109223247449.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

在窗口中输入`python`命令（注意字母`p`是小写的），如果出现 Python 的版本信息，并看到命令提示符`&gt;&gt;&gt;`，就说明安装成功了。

#### 运行 Python 命令

<img src="https://img-blog.csdnimg.cn/20210109223257724.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

运行 python 命令启动的是 python 交互式编程环境，我们可以在`&gt;&gt;&gt;`后面输入代码，并立即看到执行结果。

#### 在 Python 交互式环境中编写代码

<img src="https://img-blog.csdnimg.cn/20210109223304616.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RoaW5rV29u,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

按下`Ctrl+Z`快捷键，或者输入`exit()`命令即可退出交互式编程环境，回到 Windows 命令行程序。

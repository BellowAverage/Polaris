
--- 
title:  《 Python笔记》— Python+Pycharm安装pip install PyQt5(error: Microsoft Visual C++ 14.0)失败解决办法 
tags: []
categories: [] 

---


#### 目录
- - <ul><li>- - - <ul><li>- 


## Python+Pycharm安装PyQt5失败

### 1 安装命令

```
pip install PyQt5

```

### 2 报错信息

```
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools":
    https://visualstudio.microsoft.com/visual-cpp-build-tools/

```

<img src="https://img-blog.csdnimg.cn/ea91575311444fa89d868412a6a585c2.png" alt="在这里插入图片描述">

### 3 解决办法

下载并安装 Microsoft C++ Build Tools

#### 3.1 下载方法

以Windows10为例 下载Microsoft C++ Build Tools链接地址：  打开网页后，根据如下指引，下载 Microsoft C++ Build Tools ①点击下载 ②输入Visual Studio 2015 with update 3 ③点击搜索 ④核对下载项：Visual C++ Build Tools for Visual Studio 2015 with Update 3 ，选择DVD格式 ⑤点击Download

如果没有微软账号可以通过如下网盘链接下载：

<img src="https://img-blog.csdnimg.cn/2615d0fdb7f34f73b73c64e6dcdc987a.png" alt="在这里插入图片描述">

#### 3.2 安装方法

① 下载完成打开下载目录，是一个.iso文件 <img src="https://img-blog.csdnimg.cn/9014d8ca996e4423b950c438cb9ff91a.png" alt="在这里插入图片描述">

② 直接解压，解压完成后得到如下文件

<mark>注意事项：</mark> 解压路径必须是非中文字符路径 <img src="https://img-blog.csdnimg.cn/7d89d61537444702965f02dd9114afaf.png" alt="在这里插入图片描述">

③ 双击运行 VisualCppBuildTools_Full.exe 文件，默认安装即可，等待安装完成 <img src="https://img-blog.csdnimg.cn/6d4d339720cb4a0990593dc04f7e5070.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ea0170d497a4470b8274dc1355b0bb18.png" alt="在这里插入图片描述">

### 4 验证效果

建议先更新pip，如是最新版本可略过，命令如下

```
python -m pip install -U pip
python -m pip install --upgrade pip 

```

再次安装

```
pip install PyQt5

```

成功安装 <img src="https://img-blog.csdnimg.cn/ef94b994c72e430aa334256f1dfb7509.png" alt="在这里插入图片描述">

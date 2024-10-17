
--- 
title:  Win10 Anaconda 新建环境安装python-pcl 
tags: []
categories: [] 

---
### 一、前言

Windows环境下安装pcl在github仓库的readme中说进入下载最新编译成功的whl文件就可以轻松实现(号称最简易的安装实现），但是appveyor只保留最近一个月的编译结果，后期再无更新，且删除了三个月前的全部文件，需要从其他途径下载；第二个就是在导包运行代码的时候会提示找不到dll的错误，也需要手动下载，然后放到相应的目录中。

至于VS环境下安装C++ 版本的pcl也可以按照下面提供的步骤安装实现对于python下的安装，记录一下安装步骤，避免再次走弯路。

### 二、安装流程补充

1、python-pcl编译界面所包含的 .whl 文件多数不能用，以下给出两个版本网盘地址（幸运~）

百度网盘地址1 （python3.7 版本， 提取码 pcl3 ）：百度网盘地址2（python3.6版本, 提取码 rphc）：



刚刚找到直接编译好的whl文件新地址，

可以基于该地址下载合适的python-pcl，无需一定要在网盘下载。

2、利用 Anaconda 创建虚拟环境，注意虚拟环境 python 版本应设置为 3.7，即输入：

conda create -n pytorch_pcl python=3.7

相应的若是安装3.6版本， conda create -n pytorch_pcl python=3.6

注：如果原有的虚拟环境 python 版本也是3.7或3.6，安装对应版本时直接在原有虚拟环境中也是一样，不用重新创建。

3、将下载到的 python_pcl-0.3.0rc1-cp37-cp37m-win_amd64.whl 文件放入所创建的 python版本为3.7的虚拟环境的 Scripts 文件夹下，具体如下：

D:\Anaconda3\Scripts

然后，在此文件夹下打开 cmd，执行 pip 操作，输入：pip install python_pcl-0.3.0rc1-cp37-cp37m-win_amd64.whl 即可安装成功。

也可以在Anaconda Prompt 下 运行如下命令：

<img alt="" height="198" src="https://img-blog.csdnimg.cn/584b08fa202340428bf89d81901d6a5b.png" width="663">

 conda create -n python_pcl_37 python=3.7

activate python_pcl_37

pip install python_pcl-0.3.0rc1-cp37-cp37m-win_amd64.whl



4.安装完成后导入 import pcl时提示报错

Traceback (most recent call last):   File "&lt;stdin&gt;", line 1, in &lt;module&gt;   File "D:\Anaconda3\envs\python36\lib\site-packages\pcl\__init__.py", line 16, in &lt;module&gt;     from ._pcl import * ImportError: DLL load failed: 找不到指定的模块。

按照的思路才知道pcl是要依赖于OpenNI2.dll的，我以前没安装过OpenNI2所以出现这个错误

我先是直接pip安装了OpenNI2但是根本找不到.dll文件

所以需要去官网下载： 

然后安装对应的OpenNI-Windows-x64-2.2.msi 到指定路径 D:\Program Files\

然后在D:\Program Files\OpenNI2\Samples\Bin这个位置里面找到OpenNI2.dll

复制到D:\Anaconda3\Lib\site-packages\pcl这个里面

<img alt="" height="734" src="https://img-blog.csdnimg.cn/6329561b7a0f4eb0b90356c29e55f03c.png" width="856">



再试一次就导包就可以使用了

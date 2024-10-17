
--- 
title:  Linux之miniconda的安装和使用 
tags: []
categories: [] 

---
## 一、miniconda简介

  Miniconda和Anaconda都是由Continuum Analytics开发的Python发行版。二者的主要区别在于它们所自带的软件包集合的大小。Miniconda是一个免费的conda最低安装程序。它是Anaconda的一个小型引导程序版本，只包括conda、Python、它们都依赖的包，以及少量其他有用的包（如pip、zlib和其他一些包）。这使得Miniconda在安装过程中体积更小，更适合那些希望精细控制其环境和软件包的用户。如果您需要更多的软件包，请使用conda-install命令从Anaconda的公共repo中默认提供的数千个软件包进行安装，或者从其他渠道进行安装，如conda-forge或bioda。
- Miniconda： Miniconda是Anaconda提供的最小安装程序。如果您想自己安装大多数软件包，请使用此安装程序。- Anaconda版本： Anaconda Distribution是一个功能齐全的安装程序，它附带了一套用于数据科学的软件包，以及Anaconda Navigator，一个用于处理conda环境的GUI应用程序。
  软件安装要求：
- 支持的操作系统：Windows、macOS或Linux- 对于Miniconda：400 MB磁盘空间- 对于Anaconda：下载和安装至少3 GB磁盘空间- 适用于Windows：适用于Python 3.9的Windows 8.1或更新版本，或适用于Python 3.8的Windows Vista或更新版本
  博主实验环境如下：
- 操作系统：centos7.9- miniconda版本：2024.02-27- Conda ：24.1.2- Python 3.12.1
## 二、安装步骤

### 1、下载miniconda软件包

  可以登录官网下载最新版本的安装包，也可以直接使用下面命令下载。可以看出来miniconda软件包比anaconda3小了很多，anaconda3安装包有将近1G大小，而miniconda3只有一百多兆。

>  
 [yunwei@yws55 ~]$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh <img src="https://img-blog.csdnimg.cn/direct/6bd8febb162d49ca99f92b3880d8e889.png" alt="在这里插入图片描述"> 


### 2、添加执行权限

  添加执行权限

>  
 [yunwei@yws55 ~]$ chmod u+x Miniconda3-latest-Linux-x86_64.sh 


### 3、执行安装程序

  执行安装程序，执行安装程序需要输入两次回车键、两次yes即可完成。 <img src="https://img-blog.csdnimg.cn/direct/c2aa0a48be0b40f496a1042e9f0664d0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/3f4ee40a573e49b7bfb26b46217bb7b5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1e0fb3abd55a419b930a09c79b2b3ec1.png" alt="在这里插入图片描述">

>  
 [yunwei@yws55 ~]$ sh Miniconda3-latest-Linux-x86_64.sh … 


### 4、更新环境变量

  安装完成后会将conda命令写入环境变量中，可以退出会话重新连接或者使用source ~/.bashrc使环境变量生效。

>  
 [yunwei@yws55 ~]$ source ~/.bashrc (base) [yunwei@yws55 ~]$ <img src="https://img-blog.csdnimg.cn/direct/e3ef678a21984880944852585dbb367b.png" alt="在这里插入图片描述"> 


### 5、查看base环境大小

  miniconda也会创建一个base环境，lib包下是主要安装软件包，只有300M+大小。 <img src="https://img-blog.csdnimg.cn/direct/ce2f220912fd4b4f84c2fd006f4b9c92.png" alt="在这里插入图片描述">

>  
 #miniconda3的base环境安装的软件包数量 (base) yunwei@yws55:~/anaconda3/envs$ conda list |wc -l 560 #anaconda3的base环境安装的软件包数量 (base) [yunwei@yws55 envs]$ conda list |wc -l 76 


### 6、查看conda版本

  环境变量生效后，conda命令就可以直接执行了，查看conda版本，当前为最新的conda24.1.2。

>  
 (base) [yunwei@yws55 miniconda3]$ conda --version conda 24.1.2 


### 7、创建一个虚拟环境

  创建一个python3.11版本的虚拟环境，默认是安装3.11.x中当前最新版本，例如当前安装的是3.11.8。区别主要就是base环境的区别，按需的虚拟环境miniconda和anaconda是一样的。

>  
 (paddleocr) [yunwei@yws55 miniconda3]$ conda create -n paddleocr python=3.11 … (paddleocr) [yunwei@yws55 miniconda3]$ python --version Python 3.11.8 <img src="https://img-blog.csdnimg.cn/direct/6e0606c0db544d419bbabf5a86e46d1e.png" alt="在这里插入图片描述"> 


## 三、conda命令示例

  miniconda安装完成之后日常虚拟环境创建、管理和软件包的安装、卸载等都是通过pip或者conda进行，跟anaconda是一样的。如下是常用命令示例。

### 1、使用conda info查看虚拟环境列表

>  
 #conda info -e 


### 2、使用conda create创建虚拟环境

>  
 #conda create -n test python=3.7 


### 3、使用conda activate激活虚拟环境

>  
 #conda activate test 


### 4、使用conda deactivate退出虚拟环境

>  
 #conda deactivate 


### 5、使用conda remove删除虚拟环境

>  
 #conda remove -n test --all 


### 6、重命名虚拟环境

>  
 #conda create -n 新环境名字 --clone 老环境名字 


### 7、查看虚拟环境安装的包

>  
 #conda list -n test 


### 8、删除依赖

>  
 #conda clean -p 包名 #删除没有用的包 conda clean -t #删除缓存包 conda clean -y -all #删除所有的安装包及cache 


### 9、安装指定软件包

>  
 #conda install Flask==1.1.2 


### 10、更新软件包

>  
 #conda update Flask 


### 11、按照requirements.txt文件安装所需的包

>  
 #conda install --file requirements.txt #pip3 install -r requirements.txt 


### 12、导出当前环境的包信息

>  
 #conda env export &gt; environment.yaml #conda env export &gt; requirements.txt #pip3 freeze &gt; /tmp/requirements.txt 


### 13、根据requirements文件创建虚拟环境

>  
 #conda env create -f=/path/to/requirements.txt -n test 


### 14、查看conda源配置信息

>  
 #conda config --show-sources 


### 15、添加conda源

>  
 #conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main 


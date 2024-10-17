
--- 
title:  RTX3060+win10+CUDA11.2+cudnn8.2.0+pytorch1.8.0 环境——个人配置经验 
tags: []
categories: [] 

---
主要参考博客  

**注意文章最后有更新（2022.7.8更新）！！！！！** **前面部分是按照之前按照顺序来的，大家看完之后再进行安装，不可写一步做一步（有的是有问题的）！！！**

配置时间：2021.10.25 以下是我亲测有效的使用 RTX 3060 的各部分安装版本 电脑系统：window 10 python版本：3.6.13 pytorch版本：1.8.0 CUDA版本：11.2 cuDNN版本：8.2.0.53

以下是我个人安装教程，仅供参考，如果出现新问题我恐怕可不能解决，谨慎参考，大神请随意~

**注意，我的安装顺序可能有问题！！！ 其他博客的顺序如下： 1、安装Anaconda 2、安装CUDA和cuDNN 3、 下载Pytorch**



#### 文章目录
- - - - - - - - <ul><li>


## 第一步：安装Anaconda

点进官网下载 https://www.anaconda.com/products/individual

我下载的版本是： <img src="https://img-blog.csdnimg.cn/811818764cb54cf79b84d570e2ae7410.png" alt="在这里插入图片描述"> 根据提示安装即可。

## 第二步：新建环境

1、打开anaconda prompt <img src="https://img-blog.csdnimg.cn/5cb75937017d4f90914f963a37615b3d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 2、命令行输入：`conda create --name pytorch_gpu python=3.6`

python_gpu为anaconda下虚拟环境名称，可自定义，python=3.6为选择安装的python版本。

这里我忘记截图了，和里面的流程是一样的。 <img src="https://img-blog.csdnimg.cn/74db218d17f24a9bad54bf005a9fdc8e.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> proceed选择y，回车, 等待相关包下载，可以看到在安装完成之后，信息提示： <img src="https://img-blog.csdnimg.cn/1ab247b09d8a4580a9cc5703a86bed4f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

3、如果要启用创建的环境，输入指令：`conda activate pytorch_gpu` 关闭该环境的话，输入指令：`conda deactivate`

## 第三步：安装pytorch

**失败尝试1**： 在刚刚创建的环境中安装pytorch, 在pytorch 官网 https://pytorch.org/get-started/locally/ 找到对应的下载指令进行下载，选择与自己环境匹配的，如下是我的环境配置： <img src="https://img-blog.csdnimg.cn/76ae1000151e4d949532bada7cdd7c66.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

在已经激活的环境中输入上图红框中的命令：

```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch

```

默认pytorch官网为下载源，下载速度太慢，很容易报错，所以更改为清华大学镜像，命令行输入下面的命令：

```
#添加Anaconda的清华镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
#设置搜索时显示通道地址
config --set show_channel_urls yes  

```

<img src="https://img-blog.csdnimg.cn/f8291410ac754a9e9d71041fd55fc22e.png" alt="在这里插入图片描述"> 然后在输入： conda install pytorch torchvision cudatoolkit=11.3 注意要把后面的-c pytorch去掉，不然还是使用的默认源下载。

根据提示安装后，进行测试：

```
import torch
torch.cuda.is_available()

```

返回 **False** <img src="https://img-blog.csdnimg.cn/04ee6f7c49064810b55682fb39c73785.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2db9715eb05244c0b8879877a9291577.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/7f7d153608ac45d0ae848ce4804de039.png" alt="在这里插入图片描述">

**原因分析1：清华源下载的可能是cpu版本的** 输入命令：`conda list` <img src="https://img-blog.csdnimg.cn/caef63c0f5eb4b0893981a319492abdb.png" alt="在这里插入图片描述"> 还有查看安装的信息： <img src="https://img-blog.csdnimg.cn/4c5a6dbbef494a9183afa38255266f77.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 确实好像是装成了cpu的版本

卸载命令：`conda uninstall xxx //卸载xxx包`

```
conda uninstall pytorch

```

注：如果要删除自定义源更换回conda的默认源，直接删除channels即可，命令如下：

```
conda config --remove-key channels

```

**检查版本对应**

怀疑是不是官网给的pytorch对应的cudatoolkit=11.3版本太高了，开始仔细检查版本对应 cmd下输入命令：`nvidia-smi` <img src="https://img-blog.csdnimg.cn/1baf8b13e8b84fcb9b241c5bede8c0b0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 之前也有怀疑过显卡驱动问题，于是根据**自己的电脑**官网教程（惠普官方显卡驱动更新）进行更新到最新显卡驱动并重启。 <img src="https://img-blog.csdnimg.cn/0d57392bedb847da903a74bb231872e9.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 可以看到 Driver Version：462.80 CUDA Version：11.2

也可参考博客查看cuda版本 <img src="https://img-blog.csdnimg.cn/d57478e7495a4f9e8fdbe23f5237f9c0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

进入官网检查版本对应 https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html <img src="https://img-blog.csdnimg.cn/0c49e3003fbe447fb47c08b6654f1729.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 接下来检查pytorch对应版本是否有问题，进入官网https://pytorch.org/get-started/previous-versions/ <img src="https://img-blog.csdnimg.cn/966c1ab9359f4e9bbda9a1221a6ea2bb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 只有11.1版本的，我将其修改为11.2先尝试一下，输入命令：

```
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.2 -c pytorch -c conda-forge

```

安装提示安装后，进行测试：

```
import torch
torch.cuda.is_available()

```

<img src="https://img-blog.csdnimg.cn/d5aeced83dbe4ef59c39359167620e05.png" alt="在这里插入图片描述"> 应该是可以了。

## 第四步：Cuda安装

一开始我以为我的电脑上自带CUDA，所以不用装的，但是后来发现这样好像没法安装cudnn，为了保险起见，我打算再次**安装CUDA和cuDNN**

**1、进入官网检查版本对应** https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html <img src="https://img-blog.csdnimg.cn/0c49e3003fbe447fb47c08b6654f1729.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> **2、下载安装包** CUDA下载网站，无需注册 https://developer.nvidia.com/cuda-toolkit-archive

第一次下载： <img src="https://img-blog.csdnimg.cn/edaad2c24ff74573a746e80010a57cc3.png" alt="在这里插入图片描述"> 打开CUDA安装包 <img src="https://img-blog.csdnimg.cn/c6186a0cab6f4647a9560923400bd4df.png" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/6f01abff4a204635887ef1d55ae42412.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/0e692d655117403b890b008fefc033f5.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

安装失败，提示版本不兼容，网上说要卸载原来电脑的所有驱动，太冒险了，而且我之前安装也没有卸载。 <img src="https://img-blog.csdnimg.cn/098b843c94744c02baeebe30341f5234.png" alt="在这里插入图片描述">

重新下载比较新一点的版本，挣扎一下，没想到成功安装~ <img src="https://img-blog.csdnimg.cn/c956b5f0e7704b6e863a18cb4dba2884.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/131381ca8a7d44bcbe8ea04b1eb1ecf8.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d0bf03759f81411ba5046bf2fa53409c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 第五步： cudnn安装

**1、检查cudnn是否安装** cmd下输入命令：`nvcc -V` 如果已经安装会出现详细信息

**2、下载安装包** cuDNN网址 https://developer.nvidia.com/cuDnn

下载cuDNN需要注册NVIDIA账号并登录，我使用163邮箱可以正常收发邮件。

邮箱验证完后，补全一些信息即可。

<img src="https://img-blog.csdnimg.cn/b72bb52769b84d1dac0d3e1388269b3d.png" alt="在这里插入图片描述"> 我下载的是版本：cudnn8.2.0 <img src="https://img-blog.csdnimg.cn/79e28f0870774058b63a18e238710859.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/03e77d3d8ee0448eb53d25391f286afb.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

**3、建议安装CUDA之前先安装VS**

不知道为什么，网上教程这样建议的，于是我还是安装了，**一定不要装在c盘！！！！！** 可选VS2013，体量小。 我直接官网下载，装的VS2019版本。

**4、安装cudnn** 安装CUDA完毕后

解压cuDNN压缩包，复制以下所有内容。 <img src="https://img-blog.csdnimg.cn/1f9dd535bd64450e9b6cc76a99bc3996.png" alt="在这里插入图片描述"> 打开路径 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2

将刚才复制的内容粘贴到该文件夹。这里我忘记截图了，与相似，大体上是这样 <img src="https://img-blog.csdnimg.cn/6f6201059c3648338d8c6b38d0463763.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ba4543e688da4a12bafc86b3774b50a0.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 完成。

## 测试

全部安装好后测试，参考博客 

```
import torch

torch.cuda.is_available()       # cuda是否可用

torch.cuda.current_device()     # 返回当前设备索引

torch.cuda.device_count()       # 返回GPU的数量

torch.cuda.get_device_name(0)   # 返回gpu名字，设备索引默认从0开始

```

<img src="https://img-blog.csdnimg.cn/8e546405c72c4592b8b88ab1513e857b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

大功告成！ <img src="https://img-blog.csdnimg.cn/ce49fa9e1ad440b5a2bd50590f94d203.png" alt="在这里插入图片描述">

有小伙伴需要： <img src="https://img-blog.csdnimg.cn/79e28f0870774058b63a18e238710859.png" alt="在这里插入图片描述"> 网盘链接： 链接：https://pan.baidu.com/s/1VjY2IpFZ9m6F_7MjFye9RA?pwd=41bj 提取码：41bj

## 注意注意（2022.7.8更新）：

不可行（装的cpu版本的）

```
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.2 -c pytorch -c conda-forge

```

可行

```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch

```

<img src="https://img-blog.csdnimg.cn/20de06442f474bc593669b0c05558767.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/48096bc114534c8abbf1e38298a9ae47.png" alt="在这里插入图片描述">

有可能和评论区一样，是之前pytorch版本的问题。

<img src="https://img-blog.csdnimg.cn/8c911cfccdbb4d1ab0acae62b79909b3.png" alt="在这里插入图片描述">

```
 #例如安装scipy时使用豆瓣的源
    pip install --index-url https://pypi.douban.com/simple scipy

```

### 克隆环境

如果要启用创建的环境：

```
conda activate pytorch_gpu

```

关闭该环境的话：

```
conda deactivate

```

查看环境

```
conda info --envs
# 或者
conda env list

```

删除环境：其中yyy是要卸载的环境名

```
conda uninstall -n yyy --all 

```

把本地的AAA环境克隆成BBB

```
conda create -n BBB --clone AAA

```

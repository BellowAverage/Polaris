
--- 
title:  Windows11家庭版上安装Hyper-V并导入虚拟机的方法 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- 


一般我们新买的电脑默认自带的是Windows家庭版。这个版本是没有Hyper-V的。如果安装自带Hyper-V的版本，则需要另外购买。但是我们还是有办法在Windows11的家庭版上安装和启用Hyper-V的。

## 安装启用Hyper-V

### 下载并安装

复制下面内容到名字是“Hyper-V Installer.cmd”的文件中。

```
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum &gt;hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^&gt;nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL

```

然后**使用“以管理员身份运行”该脚本**。 <img src="https://img-blog.csdnimg.cn/direct/57137049fb254c918ce9da010274fb84.png" alt="请添加图片描述"> 下载安装过程如下 <img src="https://img-blog.csdnimg.cn/direct/6802dcceba31495da069664633de4c6d.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/92833590400047f3a74f3c842e6e4d10.png" alt="请添加图片描述"> 最后我们输入Y并重启电脑。

### 启用

重启电脑后进入“启用或关闭Windows功能”，勾选Hyper-V。然后点击“确定”，待准备好后，重启系统。 <img src="https://img-blog.csdnimg.cn/direct/e98c598a202c4429adfb51f4250cdc29.png" alt="请添加图片描述"> 这样我们就可以看到Hyper-V管理器了。

## 导入虚拟机

由于之前一次误操作，我把Windows 11 家庭版设置为预览版（Preview）版。这个版本不能回退到稳定版，除非重新安装操作系统。但是我又没有原版的安装镜像，且系统上安装的软件比较多，不想再重装。 <img src="https://img-blog.csdnimg.cn/direct/77df081c5a374bf4910c01260222e188.png" alt="请添加图片描述">

Preview版会不定期更新操作系统，而且每次更新都会导致之前安装和启用的Hyper-V丢失。于是不得不在每次更新后重新执行一次Hyper-V的安装流程。这个过程并不复杂，但是对于已经部署好的虚拟机，则需要重新导入。这个过程自主操作的地方很多，很容易出问题。 <img src="https://img-blog.csdnimg.cn/direct/e6a70a5bacda4ac3b2b825358dcf64d7.png" alt="请添加图片描述"> 注意选择虚拟机的文件夹，这儿选择到Hyper-V目录下一级即可，不可以多也不可以少。 <img src="https://img-blog.csdnimg.cn/direct/a939772753504c69b839b80ae654d278.png" alt="请添加图片描述"> 然后我们选择“还原虚拟机”。 <img src="https://img-blog.csdnimg.cn/direct/0b041333518549529da53f2ab7bc2859.png" alt="请添加图片描述"> 因为我习惯性把所有可以调整的默认安装在C盘的文件，安装到D盘，且不修改目录结构。这样在“选择目标”这一项时，我只要习惯性的把和C盘修改成D盘就行。这个和个人习惯有关，大家还是要找到自己的“虚拟机配置文件夹”。 <img src="https://img-blog.csdnimg.cn/direct/8be40d8af248482f803259e234153941.png" alt="请添加图片描述"> 在“选择存储文件夹”时，保持默认不变。 最后我们就可以看到之前安装的虚拟机了。如果之前虚拟机没有关机，则打开时还是处于开机状态。 <img src="https://img-blog.csdnimg.cn/direct/75ca424914e348cbbfaf6c1bf51642fe.png" alt="请添加图片描述">

## 代码地址



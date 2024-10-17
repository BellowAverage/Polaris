
--- 
title:  打包pyinstaller生成的python桌面应用为windows安装包的方法教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用nsis制作windows安装包的方法。 日期：2022年12月7日 作者：任聪聪 


### 一、准备材料

#### 1.nsis软件

nsis是一款生成windows安装包的一款压缩工具

下载地址：

#### 2.一个使用pyinstaller生成的python图形化工具文件

<img src="https://img-blog.csdnimg.cn/3a5e8540821e4e8ca0584515d32d1789.png" alt="在这里插入图片描述">

### 二、安装nsis操作说明

#### 步骤一、打开网站点击download

<img src="https://img-blog.csdnimg.cn/1fcc8301c12c428e855f2bf7b7a5693b.png" alt="在这里插入图片描述">

#### 步骤二、进入下载界面,等待时间归零，将自动下载到download文件下

<img src="https://img-blog.csdnimg.cn/a741d1f4c0104e098e10c7d65dc7faf4.png" alt="在这里插入图片描述">

#### 步骤三、打开我们的安装包

<img src="https://img-blog.csdnimg.cn/43fee10011fc45c088c2d9ccaeb340fd.png" alt="在这里插入图片描述"> next <img src="https://img-blog.csdnimg.cn/3da0f047b96f42439997345c299084b6.png" alt="在这里插入图片描述"> 默认选项一直点下去，进入到设置目录界面，选择一个自己的目录，然后继续next

<img src="https://img-blog.csdnimg.cn/2e09f96047fa4645beba9f06d9c9de6e.png" alt="在这里插入图片描述"> 安装完毕，打开软件 <img src="https://img-blog.csdnimg.cn/e7573facddc948cca65abb40119bc301.png" alt="在这里插入图片描述"> 打开后的样子 <img src="https://img-blog.csdnimg.cn/16c594ae884a4ef8a105a88bcbf8ba8b.png" alt="在这里插入图片描述">

### 三、使用pyinstaller打包图形应用

#### 3.1打包应用

使用命令：

```
pyinstaller  -F -w -i favicon.ico 你的脚本或者main文件.py

```

<img src="https://img-blog.csdnimg.cn/009d8cb9476c4f8595597b8a7594e8cc.png" alt="在这里插入图片描述">

### 四、利用nisi的zip形式文件制作安装包

#### 4.1 找到dist文件目录

说明：一定要把所需的exe执行的相关文件都复制进去这样安装后应用才可以运行 <img src="https://img-blog.csdnimg.cn/4b11b4ef5b9e461da7471ff563b7983a.png" alt="在这里插入图片描述">

#### 4.2打包dist为zip格式文件

<img src="https://img-blog.csdnimg.cn/49ce135b485248828d65c92387689c15.png" alt="在这里插入图片描述"> 名字取名叫setup，格式选择zip

#### 4.3 利用nsis打包zip为exe安装包

打开nsis 点击 installer based on .zip file <img src="https://img-blog.csdnimg.cn/a50db0e17b2b48e4bf1396f87c744fa1.png" alt="在这里插入图片描述"> 进入配置界面，可以默认不更改因人而异 <img src="https://img-blog.csdnimg.cn/38bb09dd8d124652bd14ff173b0e83fc.png" alt="在这里插入图片描述"> 点击创建，我这里使用的是默认的配置 <img src="https://img-blog.csdnimg.cn/6c1344f782e54c929a5bd884cf4ded12.png" alt="在这里插入图片描述"> loading 等待一会 <img src="https://img-blog.csdnimg.cn/5672d38b48d146e39aed52fc7cedc2fc.png" alt="在这里插入图片描述"> 创建完毕这里便可以看到我们的安装包文件了 <img src="https://img-blog.csdnimg.cn/08499ce2fca54b7f8e9561fdd5831ba3.png" alt="在这里插入图片描述"> 打开的效果如下 <img src="https://img-blog.csdnimg.cn/fcefb7188402475a914073ef48e9a751.png" alt="在这里插入图片描述"> 安装后的效果如下 <img src="https://img-blog.csdnimg.cn/cc88a4e00c914c19a1906b4ad1759d5d.png" alt="在这里插入图片描述">

### 五、nsis的安装向导及应用参数配置的使用说明

#### 5.1 安装向导的操作说明

需要使用到 HM VNISEdit 编辑器工具，如下 <img src="https://img-blog.csdnimg.cn/9c52bb31e5ab44d0bbd6cee3e87b282e.png" alt="在这里插入图片描述">

#### 5.2 操作说明

打开软件后进入到界面，选择文件，点击新建脚本向导 <img src="https://img-blog.csdnimg.cn/41d74d5435d7438db402c7c4f84968aa.png" alt="在这里插入图片描述"> 点击下一步进入到配置界面，按照自己的软件信息进行配置即可。 <img src="https://img-blog.csdnimg.cn/a65bad1c2c3a4b58b5b1522b63daa4f5.png" alt="在这里插入图片描述"> 后面的配置没有特殊要求可以按照默认进行选择，直至全部设置完毕，生成一个如下的脚本 <img src="https://img-blog.csdnimg.cn/95836106a04f405987f242611d568ba0.png" alt="在这里插入图片描述"> 同时在你保存脚本的同目录下也会有一个setup.exe的安装包 <img src="https://img-blog.csdnimg.cn/d0f1917f1b49403aada32c509d2f7aaf.png" alt="在这里插入图片描述">

打开这个安装包的效果如下。 <img src="https://img-blog.csdnimg.cn/0a80ae4cb63041ce94742403fe42f1bc.png" alt="在这里插入图片描述"> 同时桌面和windows右侧菜单也会生成一个快捷方式（windows自带的程序卸载工具中也会有我们的软件图标和信息）如下。 <img src="https://img-blog.csdnimg.cn/74a550998c554dab84f349d1973fc475.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1fe0b3554c6844c5a4441b52af44003b.png" alt="在这里插入图片描述">

至此，大功告成！

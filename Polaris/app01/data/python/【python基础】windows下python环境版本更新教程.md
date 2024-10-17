
--- 
title:  【python基础】windows下python环境版本更新教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解python旧版本更新新版本的方法和说明 作者：任聪聪 适用人群：python新手 


python更新共有两种常见的方法：一是可以通过命令行【linux服务器、mac、win系统】、二是可以通过重新安装【windows、mac、linux图形化系统中】进行更新，**本次我们只讲解windows下通过安装包进行更新的方法。**

### 通过安装包进行更新

这里我们当前的python版本为3.9 <img src="https://img-blog.csdnimg.cn/90405402c51949af8eaf15d6942b7459.png" alt="在这里插入图片描述"> 而我们目前需要升级到3.10，所以我们需要先去官网下载 python的官网：

#### 步骤一、打开并进入官网找到download

<img src="https://img-blog.csdnimg.cn/0922d63a2fe24978b0502330e6fede1a.png" alt="在这里插入图片描述">

#### 步骤二、找到适合自己的系统位数的版本

<img src="https://img-blog.csdnimg.cn/ee6f1b09991a4411982aff1b8df2a4bb.png" alt="在这里插入图片描述"> loading <img src="https://img-blog.csdnimg.cn/7cfbb4568db54b0291ac125a75b292e9.png" alt="在这里插入图片描述">

#### 步骤三、开始默认路径进行更新

<img src="https://img-blog.csdnimg.cn/e48d0cc802e34ad5b59e58e19fe5df7b.png" alt="在这里插入图片描述"> 勾选path后，点击install now <img src="https://img-blog.csdnimg.cn/e38cb078022345b7a2719dea3cf4fa97.png" alt="在这里插入图片描述"> loading等待安装完毕 <img src="https://img-blog.csdnimg.cn/015fe04a8a1d4386914cb8cc6af076f2.png" alt="在这里插入图片描述"> 安装完毕 <img src="https://img-blog.csdnimg.cn/7145ae981fd443138949a2b9797040a4.png" alt="在这里插入图片描述">

### 测试下是否成功升级<img src="https://img-blog.csdnimg.cn/96b6a859cf2d4170b351ce2eac808a43.png" alt="在这里插入图片描述">

说明：这时候你会发现python3.9还是之前的版本，那么这里我们就需要进行修改环境变量了。

#### 步骤一、打开搜索框输入环境变量

<img src="https://img-blog.csdnimg.cn/54dbb2d8f950408b99fb3ddea6b09375.png" alt="在这里插入图片描述"> 点击打开 <img src="https://img-blog.csdnimg.cn/a065c9bed9664d0886c57934457c515e.png" alt="在这里插入图片描述">

#### 步骤二、找到环境变量的设置并选择

<img src="https://img-blog.csdnimg.cn/6b8fb4f830514ba28fec59a945b48724.png" alt="在这里插入图片描述">

#### 步骤三、双击路径弹出编辑框

<img src="https://img-blog.csdnimg.cn/6ec580c2abea4bd6a353657225283afe.png" alt="在这里插入图片描述"> tips：提示，无特殊要求，不需要配置系统变量 <img src="https://img-blog.csdnimg.cn/72283f6961c94b5792e4673349e9bc2d.png" alt="在这里插入图片描述">

#### 步骤四、找到这两个旧的路径

<img src="https://img-blog.csdnimg.cn/da002cfdabfb468fbd6c98927b7fdcff.png" alt="在这里插入图片描述">

#### 步骤五、点击编辑进行修改，将python310的目录更换好并点击保存

<img src="https://img-blog.csdnimg.cn/c6d5c5fe05f44bcca565da58483e0a8d.png" alt="在这里插入图片描述">

测试一下，如果提示是3.10的版本，那么就说明，配置新的版本完成！ <img src="https://img-blog.csdnimg.cn/2a409d3700bf4efb983d03b1d1cdc4a6.png" alt="在这里插入图片描述">

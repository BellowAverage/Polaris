
--- 
title:  GIT的下载和配置 
tags: []
categories: [] 

---
这个我看的是网课。加上我自己整理的一部分。个人认为bilibili狂神说的是最详细的。

下载的话，直接百度：<img src="https://img-blog.csdnimg.cn/e84eb60630c7443abe0665de8fe37349.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">第一个就是官方网站，如果速度慢的话就是中文镜像。 在安装的时候会自动添加到Path，所以不需要自己写。

安装成功以后会有： <img src="https://img-blog.csdnimg.cn/4d111c14f1994846bb27eecdd0233aab.png" alt="在这里插入图片描述">

感觉这个工具的作用是：在windows下虚拟了一个linux，使用liunx命令来操作Git。 个人考虑可以用这个模拟linux操作，不需要实际机器了…… 个人测试了一下：su无法运行，top无法运行，ps -ef可以。ipconfig可以。大多数的非系统命令和一部分系统命令可以运行。不错不错。

在文件夹下面可以操作: <img src="https://img-blog.csdnimg.cn/3d704e3609f0443f842354219e0b59e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 如果使用的话，就会在对应路径生成git bash。路径pwd即为打开的位置。 <img src="https://img-blog.csdnimg.cn/deb00fc108d243d9a2655a451ddbe6f9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> ——————————————————————————————————

对于基本的git命令，直接输入：git即可。 <img src="https://img-blog.csdnimg.cn/31b367c3b5de489d820b7e6d5bc50306.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">———————————————————————————————————— 如果想知道自己的仓库的位置，直接输入git init <img src="https://img-blog.csdnimg.cn/21ddf29e243441d29daeb73ab9d531de.png" alt="在这里插入图片描述"> git的参数查询：git config --global --list，其中这些是全角的变量。 <img src="https://img-blog.csdnimg.cn/9f25c885338941f3ba9dfbb4e36c2109.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 修改某个键值： git config --global XXX.XXX 修改一下用户名: git config --global user.name

在下载git的时候，会有一个git文件。 <img src="https://img-blog.csdnimg.cn/981adb6479bf4248a3ac2be704759b21.png" alt="在这里插入图片描述">

这个是git参数的。 如果想修改git的话，直接拖拽这个.git即可，就会把git配置到对应的路径。 ————————————————————————————————————————

git新建的时候有一个文件： <img src="https://img-blog.csdnimg.cn/a5bd80603b82433ab9e20b7ab63072f3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">里面需要配置所有没有用的都忽略掉。

———————————————————————————— 在新建的时候，只有一个master分支。 如果需要切换git的话，新建分支在： <img src="https://img-blog.csdnimg.cn/1fc3c4c1cf3347e08050d8f943304776.png" alt="在这里插入图片描述">

切换分支： <img src="https://img-blog.csdnimg.cn/c57bf6e209f64593b72be0dd3dcbb9f7.png" alt="在这里插入图片描述"> 分支合并： <img src="https://img-blog.csdnimg.cn/2245ad9443d74437b11813f20ff06cdb.png" alt="在这里插入图片描述">

——————————————————————————————

文件默认是不跟踪的，跟踪是 git add .跟踪所有文件。（ignore除外） 如果提交到本地，那么就是： git commit 提交到远端数据： git commit

拉取代码： git clone

———————————————————————————————— github有个自己的框架：<img src="https://img-blog.csdnimg.cn/e0ff13d929ce40819be494f838da9418.png" alt="在这里插入图片描述"> 这个操作也是一样的。 不过一直国内没啥速度……操作基本上也差不多。

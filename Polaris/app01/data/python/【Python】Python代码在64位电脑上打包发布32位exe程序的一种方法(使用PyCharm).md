
--- 
title:  【Python】Python代码在64位电脑上打包发布32位exe程序的一种方法(使用PyCharm) 
tags: []
categories: [] 

---
## 1. 背景

现在的电脑大多都是64位的，开发者安装的 Python 也多是64位的，所以使用 pyinstaller打包出的exe也是64位的。

有时候用户的电脑是古老的windows7 32位系统，那么是无法运行我们打包出的64位exe软件的。这个时候就需要我们安装使用32位的Python来打包和发布软件。

<img alt="" height="143" src="https://img-blog.csdnimg.cn/f6836f8a941147678eb4f5dfd3cfd89a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_18,color_FFFFFF,t_70,g_se,x_16" width="569">



本文即说明在普通的已经安装有64位Python和PyCharm的开发环境下，如何简洁干净的安装 32位 Python，并顺利打包和发布 32位的软件。

## 

## 2. 配置32位Python解释器

### 2.1 当前电脑配置

Window 10 64位，Python 3.7 64位，PyCharm 社区版。

### 2.2 下载 32位 Python

 在上找一个适合的版本下载。或者简单点，可以用我安装使用的这个版本：，适合win7和win10的32位安装版。

### 2.2 安装时的注意事项

安装该python 32位版本的过程中，注意不要配置环境变量。

因为我们安装32位的Python仅仅是用来创建虚拟python环境，不是当作主力Python使用的。如果把这个32位版本，加入到了系统环境变量 PATH，我们电脑的默认python就从以前使用的 64位 变成 新安装的 32位 版的了。

下面是安装的配置选项截图。

<img alt="" height="378" src="https://img-blog.csdnimg.cn/64a2e8ec66b84172b07600166d07d7ca.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="617">

<img alt="" height="377" src="https://img-blog.csdnimg.cn/a64a436003d8491ba78acc0ed96b135a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_19,color_FFFFFF,t_70,g_se,x_16" width="611">

【注意勾选 Install for all users】

【注意不要勾选 Add Python to environment variables】

 这样，我们的32位 Python就已经安装好了，它会被安装到 C:\Program Files (x86)\Python38-32 文件夹内。

### 2.3 配置PyCharm

下面我们来配置PyCharm。

在PyCharm选中Project项目，依次点击File-Setting-Project-Python Interpreter。查看本项目在用的Python解释器配置情况和已安装的第三方库。可以看到当前在使用的 64位 Python。

<img alt="" height="477" src="https://img-blog.csdnimg.cn/b571aa00f73f4d7dafccda641a658f59.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1121">

下面，我们来新增一个 Python解释器环境。 （解释器类似于翻译器，对于同一段代码，不同的解释器环境解释出来的Python结果不同。同样一句“你好”，汉英解释器会解释成 hello，汉日解释器会解释成 こんにちは）

1. 依次点击：齿轮-&gt;Add

2. 在界面中操作： 

Location: 直接修改文件夹名称

Base Interpreter：选择刚安装的 32 位的 Python.exe

<img alt="" height="347" src="https://img-blog.csdnimg.cn/cec0a0078e934414b24c245b4623d016.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="991">

 然后，就能看到该项目出现了2个Python环境，每个环境下面的Package是不一样的。

<img alt="" height="345" src="https://img-blog.csdnimg.cn/aa94f7fe8cd1476a857ffe4cfaa7ce9a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1150">

下面我们为 32位的 Python环境安装 第三方库 Package。

Python Interpreter处选中刚配置好的 32位Python，点击下方 + 号，安装自己需要的第三方库。注意，要把自己用到的第三方库全都重新安装一遍（与64位python的第三方库是隔离的）。

<img alt="" height="352" src="https://img-blog.csdnimg.cn/fa5017ae7e3b49999dd3f16303ee58cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1162">



**注意**：pyinstaller库是必须要安装的，有了它，我们的软件才能打包成exe发布。其它的包，比如PyQt5是我项目中用到的，不是必须安装的。



常用的第三方库安装后如下图。

<img alt="" height="646" src="https://img-blog.csdnimg.cn/e8f434f91d184de9aa3e214f66e951df.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1037">

 这样，该项目的32位Python解释器环境就配置好了。

### 2.4 试验

我们来试验一下。右键点击随便一个 xxx.py ，选择 open in -&gt; Terminal。

<img alt="" height="740" src="https://img-blog.csdnimg.cn/9d5ffcad608b4e38ba69026aa1a5b9b5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_17,color_FFFFFF,t_70,g_se,x_16" width="535">

然后在 Terminal 中输入 python ，查看结果。

如果如下图一样，显示的是我们刚安装的 Python 3.8.10 并且 出现 32 bit 就说明该项目的 32位 Python 解释器环境是确实配置好了。

<img alt="" height="220" src="https://img-blog.csdnimg.cn/b2394f1b44424a6daa7826d4eef4c569.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="923">

如果显示的还是以前的64位python，那可能是  File-Setting-Project-Python Interpreter 这里没有选中我们新配置的python环境。如下图所示，要选中那个 32位的Python，然后确定。

<img alt="" height="345" src="https://img-blog.csdnimg.cn/aa94f7fe8cd1476a857ffe4cfaa7ce9a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1150">

## 

## 3. 标准的python软件打包和发布流程

该流程可参考：

此处列出快捷且关键的步骤。

### 3.1 打包命令

其原理很简单，就是使用命令：

```
pyinstaller -F -w main.py
```

>  
 -F, –onefile 打包成一个exe文件。 -D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）。 -c, –console, –nowindowed 使用控制台，无界面(默认) -w, –windowed, –noconsole 使用窗口，无控制台 


关键的点在于使用哪个(which) pyinstaller.exe。

### 3.2 实际操作

在PyCharm中，首先确保该项目的解释器是 32位 解释器。

<img alt="" height="345" src="https://img-blog.csdnimg.cn/aa94f7fe8cd1476a857ffe4cfaa7ce9a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="1150">

然后右键点击你将要打包的py文件，该文件必须是程序入口文件（带有 if __name__ == __main__ 代码），找到Open in terminal点一下，Pycharm底部会出现Terminal窗口。

<img alt="" height="367" src="https://img-blog.csdnimg.cn/de14f3de40614fdda29a3e10b4fbcc5c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="736">

<img alt="" height="677" src="https://img-blog.csdnimg.cn/9ba18899f9e34edb9ef5acef291b6c7f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_18,color_FFFFFF,t_70,g_se,x_16" width="578">

 <img alt="" height="90" src="https://img-blog.csdnimg.cn/756c3581d2284a8884f80b6c4b0af36f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_14,color_FFFFFF,t_70,g_se,x_16" width="459">

输入命令：

```
pyinstaller -F -w main.py
```

 <img alt="" height="109" src="https://img-blog.csdnimg.cn/1fb41638da494d5e8b8ead498d610ac3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_20,color_FFFFFF,t_70,g_se,x_16" width="711">

稍等片刻，就会在 dist 文件夹内发现打包好的 exe 软件。

<img alt="" height="248" src="https://img-blog.csdnimg.cn/9b0421aa40e74cf393672669b263c084.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAcWlsZWkyMDEw,size_10,color_FFFFFF,t_70,g_se,x_16" width="325">

### 3.3 交付

将打包好的.exe文件放入项目所在文件夹，将所有需要的素材（图片、音乐等）一起发送，压缩成包。对方解压后，即可当作绿色软件运行。

**注意**：在Python代码中使用 相对路径 索引/使用的 文件，都必须按对应文件夹路径 放置在 .exe 周围。如在 xxx.py 中使用了 ./assert/mypic.png 文件，则 .exe 旁边必须也要有 ./assert/mypic.png文文件夹及文件。如果yyy.py 代码中使用 loadui(‘mydlg.ui’) 方式加载了 mydlg.ui 文件，同样的，mydlg.ui 也要复制到 .exe 同文件夹内。

## 4. 其它

之所以能这么操作，其实使用到了Python虚拟运行环境。我们刚才在PyCharm中新增的就是 virtualenv 软件虚拟出的32位python运行环境。详细了解参考：。

>  
 虚拟运行环境有以下优点： 
 - 使得不同Python应用的开发环境相互独立- 开发环境升级不影响其他应用的开发环境，也不会影响全局的环境（默认开发环境是全局开发环境）,因为虚拟环境是将全局环境进行私有的复制，当我在虚拟环境进行 pip install 时，只会安装到选择的虚拟环境中。- 它可以防止系统中出现包管理混乱和版本的冲突 




如有疑难问题，可评论留言。


--- 
title:  Python环境全家桶（永久使用） 
tags: []
categories: [] 

---
## 一、Python安装

本人一直是Java爱好者，第一次接触python，周围做爬虫或者信息AI开发的小伙伴都说Python语言简单，所以多学一点是没有坏处的，接下来是一个完全不懂Python的小白对安装和使用Python等一系列工作的记录，让您体验Python的“Hello World”

### 1.1下载

官网：，下载对应环境的版本。

<img alt="" height="935" src="https://img-blog.csdnimg.cn/20210611092356906.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

 目前，Python有两个版本[2.x和3.x]，这两个版本是不兼容的，目前，3.x版本越来越普及。

<img alt="" height="935" src="https://img-blog.csdnimg.cn/20210611093735706.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 1.2安装

<img alt="" height="412" src="https://img-blog.csdnimg.cn/20210611094151681.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670"><img alt="" height="412" src="https://img-blog.csdnimg.cn/20210611094232374.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670">

【报错】：

<img alt="" height="412" src="https://img-blog.csdnimg.cn/20210611094449364.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670">

解决方法：把上一步的for all user 的对勾取消掉!

<img alt="" height="412" src="https://img-blog.csdnimg.cn/2021061109461358.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670">

### 1.3安装成功

<img alt="" height="412" src="https://img-blog.csdnimg.cn/20210611094709531.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670"><img alt="" height="412" src="https://img-blog.csdnimg.cn/2021061109475169.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="670">

### 1.4配置环境变量

<img alt="" height="675" src="https://img-blog.csdnimg.cn/20210611095427931.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 1.5测试

win+R:

<img alt="" height="237" src="https://img-blog.csdnimg.cn/20210611095520593.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="413">

输入python,进入python开发环境：

<img alt="" height="643" src="https://img-blog.csdnimg.cn/20210611095533995.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="901">

测试Hello World:

<img alt="" height="643" src="https://img-blog.csdnimg.cn/20210611095704673.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="901">

在python命令下，print是可以省略的，就像这样：

<img alt="" height="643" src="https://img-blog.csdnimg.cn/20210611100004343.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="901">

## 二、开发工具

在安装 Python 后，会自动安装一个 IDLE。它是一个 Python Shell（可以在打开的 IDLE 窗口的标题栏上看到），也就是一个通过输入文本与程序交互的途径，程序开发人员可以利用 Python Shell 与 Python 交互。初学者建议一开始可以使用 IDLE 来编写代码。<img alt="" height="567" src="https://img-blog.csdnimg.cn/20210615121002389.png" width="237">

整理了一些 IDLE 中常用的快捷键，方便新人快速上手：

|**快捷键**|**说明**|**适用于**
|------
|F1|打开 Python 帮助文档|Python 文件窗口和 Shell 窗口均可用
|Alt + P|浏览历史命令（上一条）|仅 Shell 
|Alt + N|浏览历史命令（下一条）|仅 Shell
|Alt + /|自动补全前面曾经出现过的单词，如果之前有多个单词具有相同前缀，可以连续按该快捷键，在多个单词中循环选择| Python 、 Shell  
|Alt + 3|注释代码块|Python 
|Alt + 4|取消注释代码块|Python 
|Alt + G|转到某一行|Python 
|Ctrl + Z|撤销一步操作|Python 、Shell 
|Ctrl + Shift + Z|恢复上一次的撤销操作|Python 、 Shell 

**俗话说：“磨刀不误砍柴工”，好的工具给效率带来的提升不是从 1 到 1.1 倍速，而是从 1 到 10 倍速。在这里我也不推荐太多，就推荐 2 个比较常用也是Python开发用的最多的第三方开发工具：**

### 2.1Sublime Text

>  
 Sublime Text 具有漂亮的用户界面和强大的功能，例如代码缩略图，Python 的插件，代码段等。还可自定义键绑定，菜单和工具栏。 
 Sublime Text 的主要功能包括：拼写检查，书签，完整的 Python API ， Goto 功能，即时项目切换，多选择，多窗口等等。 
 Sublime Text 是一个跨平台的编辑器，同时支持 Windows、Linux、Mac OS X等操作系统。   


下载地址：

<img alt="" height="501" src="https://img-blog.csdnimg.cn/20210611100607640.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1195">

<img alt="è¿éåå¾çæè¿°" src="https://img-blog.csdn.net/20180730173641415?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTIzOTY5NTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

### 2.2PyCharm（个人推荐）

>  
 PyCharm 是由 JetBrains 打造的一款 Python IDE。 
 PyCharm 具备一般 Python IDE 的功能，比如：调试、语法高亮、项目管理、代码跳转、智能提示、自动完成、单元测试、版本控制等。 
 PyCharm 还提供了一些很好的功能用于 Django 开发，同时支持 Google App Engine，更酷的是，PyCharm 支持 IronPython。  


下载地址：

<img alt="" height="450" src="https://img-blog.csdnimg.cn/20210611101139771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

#### 2.2.1安装

<img alt="" height="390" src="https://img-blog.csdnimg.cn/20210611101440752.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="503"><img alt="" height="390" src="https://img-blog.csdnimg.cn/20210611101732217.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="503"><img alt="" height="390" src="https://img-blog.csdnimg.cn/20210611101743327.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="503">

#### 2.2.2激活

搜索：**vrg123PyCharm**

<img alt="" height="371" src="https://img-blog.csdnimg.cn/affc7d35e52740ef8b4149bcde9bb32b.png" width="1127">

按照操作进行即可。

结果：<img alt="" height="594" src="https://img-blog.csdnimg.cn/d6d16a6241ae49578e0d1ee1e5390f4a.png" width="977">



### 2.3使用

#### 2.3.1.设置python解释器

<img alt="" height="712" src="https://img-blog.csdnimg.cn/20210611184818761.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="998">

其它相关配置：

## 三、pip使用

pip 是 Python 的包安装程序。其实，pip 就是 Python 标准库（The Python Standard Library）中的一个包，只是这个包比较特殊，用它可以来管理 Python 标准库（The Python Standard Library）中其他的包。pip 支持从 PyPI，版本控制，本地项目以及直接从分发文件进行安装。pip 是一个命令行程序。 安装 pip 后，会向系统添加一个 pip 命令，该命令可以从命令提示符运行。就像vue的npm，java的maven。目前，pip 是 The Python Packaging Authority (PyPA) 推荐的 Python 包管理工具！

### 我需要安装pip吗？

如果您使用从下载的 Python 2 &gt;=2.7.9 或 Python 3 &gt;=3.4，或者如果您 在由或创建的中工作，则 pip 已经安装。只要确保。

使用以下命令检查pip是否安装：

```
C:\&gt; py -m pip --version
pip X.Y.Z from ...\site-packages\pip (python X.Y)
```

**pip太慢：**

>  
 pip install -i  --upgrade tensorflow-gpu 


 永久设置：
- linux系统
```

vim ~/.pip/pip.conf
 
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
- windows系统
`在user目录中创建一个pip目录，如：C:\Users\pip，新建文件pip.ini，添加一下内容：`

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

##  四、安装anaconda（anaconda3）

### 4.0Linux安装

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

```
 bash Miniconda3-latest-Linux-x86_64.sh
```

<img alt="" height="192" src="https://img-blog.csdnimg.cn/direct/e41716d70f814604b8b14c1e715ecd1b.png" width="832">

<img alt="" height="178" src="https://img-blog.csdnimg.cn/direct/c05d82d5af4043a18c6c22f805f755d7.png" width="1200">

 <img alt="" height="211" src="https://img-blog.csdnimg.cn/direct/a5edadfdd2c34c7e9e4695b98c29c47e.png" width="1200">

<img alt="" height="183" src="https://img-blog.csdnimg.cn/direct/974d4891f2e84a4aa461fbb85a370448.png" width="694">

<img alt="" height="543" src="https://img-blog.csdnimg.cn/direct/118433f7faff4b6db6b3e3649f05850b.png" width="934">

<img alt="" height="432" src="https://img-blog.csdnimg.cn/direct/b84f6e95820e43d38a93007466002ecf.png" width="976">

>  
 **激活刚安装完成的软件：** 
 一般安装软件完成后需要重启，在Linux叫激活，有两种方式，**第一种**是重新登录服务器，**第二种**是输入以下命令： 
 <pre>`source ~/.bashrc`</pre> 


>  
  **检查conda是否安装成功** 
 <pre><code class="language-bash">conda --help
#调用出来说明安装成功</code></pre> 


>  
 **配置conda镜像：** 
 <pre><code class="language-bash"># 下面这三行配置官网的channel地址
conda config --add channels r 
conda config --add channels conda-forge 
conda config --add channels bioconda
##以上三句命令一次性复制粘贴或是单独复制粘贴到服务器</code></pre> 
   


>  
   
 <pre><code class="language-bash">#（1）下面这四行配置清华大学的conda的channel地址，国内用户推荐
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes</code></pre> 


### 4.1Windows下载



<img alt="" height="881" src="https://img-blog.csdnimg.cn/20210629152741564.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 4.2安装

双击安装程序

<img alt="" height="390" src="https://img-blog.csdnimg.cn/20210629152946635.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="503">

### 4.3配置环境变量

之前已经配置了python3的环境，而Python和anaconda都是Python环境，所以要删除Python3的环境，改为anaconda的【在系统环境变量PATH中配置】。

#### 4.3.1配置conda

```
#以下配置更换自己的安装路径
D:\001TCHUHU\anaconda\Library\bin
```

<img alt="" height="51" src="https://img-blog.csdnimg.cn/20210629154844343.png" width="446">

#### 4.3.2配置anaconda

```
D:\001TCHUHU\anaconda\Scripts
```

#### <img alt="" height="44" src="https://img-blog.csdnimg.cn/20210629155538151.png" width="438">

>  
 **配置Anaconda镜像库：** 
 conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
 conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ 
 conda config --set show_channel_urls yes 


>  
 **Anaconda和conda的区别：** 
 Anaconda 是一个集成各类Python工具的集成平台，它本身不是一个开发工具，它只是将很多第三方的开发环境集成到一起。 
 conda是一个包管理和环境管理工具，它的包管理与pip类似，可以用来管理Python的第三方包；环境管理能够允许用户使用不同版本Python，并灵活切换。 


#### 4.3.3配置Python解释器

```
D:\001TCHUHU\anaconda
```

<img alt="" height="203" src="https://img-blog.csdnimg.cn/20210629155328431.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="919">

###  4.4将安装好的Python加入到anaconda

#### 4.4.1查询conda里的环境

```
conda env list
conda info -e
conda info --envs
```

<img alt="" height="338" src="https://img-blog.csdnimg.cn/20210629160254183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="695">

** 激活环境**

<img alt="" height="211" src="https://img-blog.csdnimg.cn/20210629160806302.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

```
# 激活环境
activate  base
```

<img alt="" height="137" src="https://img-blog.csdnimg.cn/20210629161049767.png" width="1200">

```
# 关闭环境
deactivate
```

<img alt="" height="126" src="https://img-blog.csdnimg.cn/20210629161203175.png" width="728">

通过这个可以看出：Python3.8.8解释器是在base环境中的。

#### 4.4.2添加Python

**1.创建一个环境**

```
conda create -n python37 python=3.7
```

<img alt="" height="846" src="https://img-blog.csdnimg.cn/20210629161820986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1071">

 输入：y，然后回车！

<img alt="" height="424" src="https://img-blog.csdnimg.cn/20210629162020354.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

 查看anaconda里的环境：

<img alt="" height="166" src="https://img-blog.csdnimg.cn/20210629162114418.png" width="625">

<img alt="" height="195" src="https://img-blog.csdnimg.cn/20210629162523506.png" width="1033">

#### 4.4.3替换Python

**1.查看anaconda里的Python**

<img alt="" height="98" src="https://img-blog.csdnimg.cn/20210629162954646.png" width="993">

是3.7.10，而我们之前手动安装的版本是3.9.5。

此时，将3.9.5的文件夹拷贝一下：

<img alt="" height="427" src="https://img-blog.csdnimg.cn/20210629163144933.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="700">

 复制到环境里的python37文件夹里：

<img alt="" height="389" src="https://img-blog.csdnimg.cn/20210629163350552.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="693">

<img alt="" height="294" src="https://img-blog.csdnimg.cn/20210629163429476.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="463">

查看python37里的python版本：

### <img alt="" height="126" src="https://img-blog.csdnimg.cn/20210629163642381.png" width="910"> 4.5conda命令

#### 4.5.1查看环境

```
conda env list
conda info -e
conda info --envs
```

#### 4.5.2创建环境

```
conda create -n python37 python=3.7

conda create --name python37 python=3.7
```

#### 4.5.3删除环境

```
conda remove --name python37 --all
```

#### 4.5.4激活环境

```
activate python37
```

#### 4.5.5关闭环境

```
deactivate
```

#### 4.5.6查看环境安装包

```
conda list -n your_env_name
```

##  五、Jupyter Notebook

### 5.1什么是Jupyter Notebook？

Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。—— 

简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中**直接编写代码**和**运行代码**，代码的**运行结果**也会直接在代码块下显示的程序。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

### 5.2**Jupyter Notebook的主要特点**

① 编程时具有**语法高亮**、**缩进**、**tab补全**的功能。

② 可直接通过浏览器运行代码，同时在代码块下方展示运行结果。

③ 以富媒体格式展示计算结果。富媒体格式包括：HTML，LaTeX，PNG，SVG等。

④ 对代码编写说明文档或语句时，支持Markdown语法。

⑤ 支持使用LaTeX编写数学性说明。

### 5.3**Anaconda安装**

前提：安装Jupyter Notebook的前提是需要安装了Python

```
#创建一个环境
create -n jupyter python=3.7

#查看当前环境
conda env list

#使用jupyter环境
activate jupyter

#安装jupyter工具
conda install jupyter notebook

#启动jupyter
jupyter notebook
```

<img alt="" height="333" src="https://img-blog.csdnimg.cn/20210629175205950.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

<img alt="" src="https://img-blog.csdnimg.cn/20181124132003624.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI3ODI1NDUx,size_16,color_FFFFFF,t_70">

### 5.4修改Jupyter配置

#### 5.4.1修改默认目录

上边的图就是默认目录，接下来我们修改它：

```
jupyter-notebook  --generate-config
```

<img alt="" height="53" src="https://img-blog.csdnimg.cn/20210629180355299.png" width="746">

修改配置文件**jupyter_notebook_config.py**：

```
## The directory to use for notebooks and kernels.
#  Default: '存放的文件夹'
c.NotebookApp.notebook_dir = ''
```

>  
 **注意事项：** 
 1.文件夹必须先创建好，比如这里F盘下面的myjupyter文件夹要先创建好；不然会jupyter初始化时会找不到目录 
 2.要取消注释，前面的#要去掉 
 3.要注意文件名不可以是数字 


保存文件并关闭。

<img alt="" height="350" src="https://img-blog.csdnimg.cn/20210629181332811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

#### 5.4.2自动补全

安装之前关闭jupyter:

```
#安装
pip install jupyter_contrib_nbextensions -i https://pypi.tuna.tsinghua.edu.cn/simple 
#使用
jupyter contrib nbextension install --user
#安装
pip install --user jupyter_nbextensions_configurator -i https://pypi.tuna.tsinghua.edu.cn/simple
#使用
jupyter contrib nbextension install --user --skip-running-check
```

打开jupyter:

<img alt="" height="787" src="https://img-blog.csdnimg.cn/20210701172330779.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="1200">

### 5.5notebook基本操作

<img alt="" height="543" src="https://img-blog.csdnimg.cn/85b35e4002c5486eb802069f5edea95c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

### 5.6markDownn语法

<img alt="" height="639" src="https://img-blog.csdnimg.cn/6741f010e6e94de4a2a2b811257ad2b6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

### 5.7juoyter Notebook切换虚拟环境

```
activate base  #激活环境

conda install nb_conda_kernels 

conda install ipykernel

conda deactivate

conda activate base

jupyter notebook
```

 <img alt="" height="436" src="https://img-blog.csdnimg.cn/direct/697ffea9a43c45e58ac1ca54ee0bcd28.png" width="429">

 <img alt="" height="561" src="https://img-blog.csdnimg.cn/direct/3e272afefd934947ab19c4cce6fa1956.png" width="475">

## 六、安装包时的问题解决

以安装jieba 中文分词包为例。

>  
 使用anconda install  jieba 时，遇到问题：Collecting package metadata (current_repodata.json): done，具体错误： 


<img alt="" height="607" src="https://img-blog.csdnimg.cn/direct/7d760689d57d4dacbf6372ce7fa9a45d.png" width="1200">

>  
 原因：conda只能安装python的官方包，而如同jieba，itchat等第三方包要使用pip去安装，但是在随后的匹配安装过程中还是报错，有可能是网速的愿意，也有可能是你没用管理员权限去运行命令行的原因，总之，多试几次。有时，还有可能是你的pip版本比较低，升级一下也有可能解决问题。 


>  
 解决方法：【手动安装】 
 jieba包下载： 
 - 将压缩包解压到anaconda的pkgs目录。- 使用cmd切换目录至比如我的D:/anaconda/pkgs/jieba-0.42，使用activate 激活环境，执行  python setup.py install   即可。 


<img alt="" height="280" src="https://img-blog.csdnimg.cn/direct/b95691981e4d4c96b2a77ecb54e16d07.png" width="1041">

>  
  查看已安装包：conda list 


 <img alt="" height="482" src="https://img-blog.csdnimg.cn/direct/131b9bb29137472fb565ba5b84e34787.png" width="1200">

 安装成功！

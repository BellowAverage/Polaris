
--- 
title:  「Python入门」python环境搭建及VScode使用python运行方式 
tags: []
categories: [] 

---
​ ​

>  
 活动地址： 




#### 文章目录
- - - <ul><li>- - - - - - - - - 


## 前言

Python 是一种简单易学并且结合了解释性、编译性、互动性和面向对象的脚本语言。Python提供了高级数据结构，它的语法和动态类型以及解释性使它成为广大开发者的首选编程语言。 **Python 是解释型语言：** 开发过程中没有了编译这个环节。类似于PHP和Perl语言。 **Python 是交互式语言：** 可以在一个 Python 提示符 &gt;&gt;&gt; 后直接执行代码。 **Python 是面向对象语言:** Python支持面向对象的风格或代码封装在对象的编程技术。

## 一、 python环境搭建

### 1.1 python下载安装

此次安装主要针对windows开发，以Windows系统为例。Python官网 <img src="https://img-blog.csdnimg.cn/047fcb66ae7648e38bcbfa56e11f4608.png#pic_center" alt="在这里插入图片描述">

>  
 注：自己需要的版本进行下载即可，但是建议大家不要下载最新版本。本文选用了v3.7.4的稳定版本。 


<img src="https://img-blog.csdnimg.cn/c436b75c40804c0abe0da0ef9b0c3eca.png#pic_center" alt="在这里插入图片描述"> 如上图所示，包含三种安装类型（`压缩文件解压缩安装`、`exe程序安装`、`在线安装`），本文建议选择第二种`exe程序安装`，配置上简易方便。

### 1.2 python安装

下载完成后，双击.exe即可进入安装界面。 **step1：** `Add Python to PATH`请手动勾选（目的是将Python的安装路径添加到系统环境变量的Path变量中），选择`customize Installation`按钮，进入自定义安装。 <img src="https://img-blog.csdnimg.cn/f10f9b2d930b4101a499a9b62b93a197.png#pic_center" alt="在这里插入图片描述"> **step2：** 点击`Next`按钮进入下一步 <img src="https://img-blog.csdnimg.cn/af907775cd974982afa3c044129f1c7f.png#pic_center" alt="在这里插入图片描述"> **step3：** 点击`Browse`按钮选择自己开发软件安装的位置（建议选择D盘根目录下新建的python文件夹，简洁明了，后续还需要在系统PATH配置）。点击`Install`按钮进行安装。 <img src="https://img-blog.csdnimg.cn/e10920636d0248be9e1cce187684ab70.png#pic_center" alt="在这里插入图片描述"> step4： 等待安装进程，进入安装成功界面，点击`clsoe`按钮关闭即可。 <img src="https://img-blog.csdnimg.cn/338fc743348d4ef6b25269340054bde1.png#pic_center" alt="在这里插入图片描述">

### 1.3 python环境变量配置

桌面【我的电脑】→右击选择【属性】→【高级系统设置】→【环境变量】→【系统变量】选中Path，再点击【编辑】按钮→点击空白行，再点击【浏览】按钮并选中1.2 step3自己开发软件安装的位置。

<img src="https://img-blog.csdnimg.cn/6921966497534ecba70c95a8fc5f5f39.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c38befe72db6413bb1903c76fd02b122.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5bc40db3189d4eb6b1bea59b1b80c560.png#pic_center" alt="在这里插入图片描述">

### 1.4 python版本指令

打开cmd 进入命令窗口，输入指令并回车 ，出现python版本，即可确认安装成功。

```
python --version

```

<img src="https://img-blog.csdnimg.cn/0037779386734422a22f154f33152504.png#pic_center" alt="在这里插入图片描述">

>  
 **python安装后找不到的可能情况及解决办法：** 1、先关闭cmd，然后重新打开，再输入“python --version”并回车，如果可以了，那就说明cmd打开后安装的； 2、点击下载的安装包，选择repair，根据提示重新来一次； 3、若没有出现python版本，应该是环境变量没有设置好，打开系统环境变量的Path变量，查看是否有Python的目录。若没有，那就手动配置环境变量。 


<img src="https://img-blog.csdnimg.cn/61a52c68027f4c3d96278d270dec8863.png#pic_center" alt="在这里插入图片描述">

## 二、VScode使用python

### 2.1 VScode下载

VScode下载，直接默认配置安装即可，此处不再一一赘述。 <img src="https://img-blog.csdnimg.cn/850f355bdae94f2598a0b80af7569748.png" alt="在这里插入图片描述">

### 2.2 安装python插件

如图所示，在扩展商店输入Python关键词，安装第一个Python插件。 <img src="https://img-blog.csdnimg.cn/79385dbe80724ab49b98b481fe9f5609.png#pic_center" alt="在这里插入图片描述">

### 2.3 选择python解释器

在VScode界面下，按键盘快捷键：`F1`（或者`Ctrl+Shift+P`），在VScode界面上方会显示下图中的文本框，如果列表项较多可以输入 `Python: Select Interpreter`过滤查询。 <img src="https://img-blog.csdnimg.cn/042d7d1b843d45d49d3659eb3f8cb2e3.png#pic_center" alt="在这里插入图片描述"> python解释器出现后，请点击再选择自己对于目录下的`python.exe` <img src="https://img-blog.csdnimg.cn/68c8b34f6e55467fbdae22d9676cceed.png#pic_center" alt="在这里插入图片描述">

### 2.4 相关指令

VScode终端安装库

```
python --version // 版本查看
python // 打开cmd直接编译
pip install XXX // 终端安装库
pip install flake8 // 常用第三方库安装 flake8
pip install yapf// 常用第三方库安装 yapf
pip list // 查看安装的所有库

```

<img src="https://img-blog.csdnimg.cn/a87170b5f7f845ad89b8063e3f88732d.png#pic_center" alt="在这里插入图片描述">

## 三、python运行方式

起航，美好的一天从hello word，I’m coming开始。

### 3.1 进入交互模式

```
// tips：小试牛刀，引入re模块操作，匹配以hello word开头的语句
python // 打开cmd，输入python，点击回车 进入交互模式
import re // 引入正则
result = re.match("hello word","hello word,I'm coming")
result.group() // =&gt;返回值 'hello word'

```

<img src="https://img-blog.csdnimg.cn/260e6ec5d2234132bb83208d4623d8ad.png" alt="在这里插入图片描述">

>  
 退出交互模式，直接输入 `exit()` 或者`quit()` 即可 


### 3.2 通过脚本输出

通过编辑器，编写脚本文件，命名为 hello.py，在命令行模式下输入 python hello.py 即可实现

```
print('hello World!') // 新建hello.py，输入需要打印的内容并保存 

```

控制台输入

```
python hello.py // =&gt; hello World

```

<img src="https://img-blog.csdnimg.cn/d7b6598d63494cf38b13999a4ad63a98.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/348d07c1f880473a8690e47322367c0e.png" alt="在这里插入图片描述">

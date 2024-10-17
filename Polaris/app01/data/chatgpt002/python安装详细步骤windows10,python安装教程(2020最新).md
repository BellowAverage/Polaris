
--- 
title:  python安装详细步骤windows10,python安装教程(2020最新) 
tags: []
categories: [] 

---
大家好，给大家分享一下python安装详细步骤windows10，很多人还不知道这一点。下面详细解释一下。现在让我们来看看！



<img alt="" height="1067" src="https://img-blog.csdnimg.cn/img_convert/115aedba7a813b06803c343df7e438b9.jpeg" width="800">

第一次接触Python，可能是爬虫或者是信息AI开发的小朋友，都说Python 语言简单，那么多学一些总是有好处的，下面从一个完全不懂的Python 的小白来安装Python 等一系列工作的记录，并且遇到的问题也会写出，让完全不懂的小白也可上手安装，并且完成第一个Hello world代码。

#### [Python 安装]

目前，Python有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的。由于3.x版越来越普及，我们的教程将以最新的Python 3.9版本为基础。

1：进入Python的官方下载页面

http://www.python.org/download/

<img alt="" src="https://img-blog.csdnimg.cn/2020110615252856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

出现很多版本的，我们选择最新的版本3.9.0

<img alt="" src="https://img-blog.csdnimg.cn/20201106152935987.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

下载完成后点击运行，会出现安装界面，记得勾上

<img alt="" src="https://img-blog.csdnimg.cn/20201106153248369.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

出现这个就安装成功了

<img alt="" src="https://img-blog.csdnimg.cn/20201106153455828.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

2：运行Python

安装成功后，打开命令提示符窗口（win+R,在输入cmd回车），敲入python后，会出现两种情况：

###### 情况一：

<img alt="" src="https://img-blog.csdnimg.cn/20201106153718882.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

出现这个表示python安装成功。你看到提示符 &gt;&gt;&gt; 就表示我们已经在Python交互式环境中了，可以输入任何Python代码，回车后会立刻得到执行结果。现在，输入exit()并回车，就可以退出Python交互式环境（或直接关掉命令行窗口也可以）。

###### 情况二：

得到一个错误：

我这里就不演示了，因为我是安装成功的，我还是演示一下，用错误的pythonn来代替python来用，这样才会提示出错误信息。

<img alt="" src="https://img-blog.csdnimg.cn/20201106154112228.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 3：配置环境变量 这是因为Windows会根据一个Path的环境变量设定的路径去查找python.exe，如果没找到，就会报错。如果在安装时漏掉了勾选Add Python 3.9 to PATH，那就要手动把python.exe所在的路径添加到Path中。 如果发现忘记勾选或者是不会设置PATH路径那么，你重新安装一遍记得勾选上Add Python 3.9 to PATH就ok了。(第2步：出现错误的信息一般都是没有配置环境变量导致的)

4：步骤：右键我的电脑–&gt;选择属性–&gt;选择高级系统设置–&gt;选择右下角的环境变量

<img alt="" src="https://img-blog.csdnimg.cn/20201106155849628.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

环境变量主要有用户变量和系统变量，需要设置的环境变量就在这两个变量中 用户变量是将自己的下载的程序可以在cmd命令中使用，把程序的绝对路径写到用户变量中即可使用

<img alt="" src="https://img-blog.csdnimg.cn/20201106160207793.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106161024440.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 5： 测试输出 win+R ，输入cmd 回车

<img alt="" src="https://img-blog.csdnimg.cn/20201106161400107.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

输入python回车，进入python开发环境

<img alt="" src="https://img-blog.csdnimg.cn/20201106161450420.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> . 需要注意的是调用函数（打印 等）需要括号，不然会提示

<img alt="" src="https://img-blog.csdnimg.cn/2020110616175229.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 直接在print后面加一段文字来输出的话，需要给文字加上双引号或者单引号。大家发现，print除了打印文字之外，还能输出各种数字、运算结果、比较结果等。你们试着自己print一些别的东西，看看哪些能成功，哪些会失败，有兴趣的话再猜一猜失败的原因。 . 其实在python命令行下，print是可以省略的，默认就会输出每一次命令的结果。就像这样：

#### <img alt="" src="https://img-blog.csdnimg.cn/20201106161947338.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> [ 安装开发工具 ]

安装PyCharm工具，网上可以下载，很多资源，也有免安装的版本，解压就可以用，我现在演示的是需要进行安装的Pycharm开发工具。

<img alt="" src="https://img-blog.csdnimg.cn/20201106213416777.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213436330.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213453137.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213510181.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213524152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

第一次打开pycharm会显示这个

<img alt="" src="https://img-blog.csdnimg.cn/2020110621354438.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213557480.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213608308.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/2020110621363760.png#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106213654337.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106214024855.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

这样选着会有一个venv文件夹，新建项目时默认是新建一个虚拟环境

<img alt="" src="https://img-blog.csdnimg.cn/20201106214821141.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106220006584.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

不需要venv的虚拟环境文件夹，选着第二个选项并且设置python的环境，默认是没有的哦

<img alt="" src="https://img-blog.csdnimg.cn/20201106224154631.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

点击下一步完成空项目的创建

<img alt="" src="https://img-blog.csdnimg.cn/20201106224311714.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

创建一个文件夹用于分类管理

<img alt="" src="https://img-blog.csdnimg.cn/20201106224358472.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

创建一个python文件里面可以写python语句

<img alt="" src="https://img-blog.csdnimg.cn/20201106224505524.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201106224751650.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 来运行一下python代码，打印第一句python代码，Hello World 哈哈哈！！！

<img alt="" src="https://img-blog.csdnimg.cn/20201106225512593.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

pyCharm的插件

###### 汉化插件的下载

因为PyCharm进去是英文状态，所以下载这个汉化插件之后，重新启动就会显示为中文状态 . 打开File-&gt;Settings… 会跳出窗口

<img alt="" src="https://img-blog.csdnimg.cn/20201107100734219.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

在选择“marketplace”接着在输入框中输入“Chinese”后即可找到汉化插件，点击“install”进行下载

<img alt="" src="https://img-blog.csdnimg.cn/20201107100939536.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201107101129576.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 点击重启

<img alt="" src="https://img-blog.csdnimg.cn/20201107101348762.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201107101520445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

#### [ pip的使用 ]

假设我要安装Selenium Selenium 的安装很简单，可采用如下方式。

pip install selenium

<img alt="" src="https://img-blog.csdnimg.cn/20201107094052543.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"> 直接通过命令窗口输入，不需要进入python环境的命令行，然后输入上面的语句就可以进行selenium的安装。

Selenium安装好之后，python并不能直接使用，它需要与浏览器进行对接。这里拿Chrome浏览器为例。若想使用Selenium成功调用Chrome浏览器完成相应的操作，需要通过ChromeDriver来驱动。

```
 链接：http://npm.taobao.org/mirrors/chromedriver/  
        或https://chromedriver.storage.googleapis.com/index.html  

```

（版本要和谷歌版本一样）

我的是86.0.4240版本那你就要去下载这个版本

<img alt="" src="https://img-blog.csdnimg.cn/20201107094306296.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201107094357425.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center"><img alt="" src="https://img-blog.csdnimg.cn/20201107094405400.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

下载完成后，解压并且复制到python环境的根目录 文件夹下

<img alt="" src="https://img-blog.csdnimg.cn/20201107094517464.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

<img alt="" src="https://img-blog.csdnimg.cn/20201107095713996.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

并且通过cmd命令行运行chromedriver，不报错则成功

<img alt="" src="https://img-blog.csdnimg.cn/20201107094648931.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

###### pip版本的更新

python -m pip install --upgrade pip

注意：不需要在python环境的命令行，而是使用cmd命令行进行的更新

<img alt="" src="https://img-blog.csdnimg.cn/20201107095001756.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1NTAyMzM2,size_16,color_FFFFFF,t_70#pic_center">

#### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，Python自动化测试学习等教程。带你从零基础系统性的学好Python！

>  
  👉（**安全链接，放心点击**） 
 

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/92cdaf1c0daf6df498665305ae2df152.png">

##### 一、Python大礼包

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/8701c941057946119577d49e708b8a3d.png">

##### 二、 **Python电子书**

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/f053e2cea1c3aeb91029492603be0dcd.png">

##### 三、入门学习视频

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/e0106a2ebc87d23666cd0a4b476be14d.png">

##### 四、 **Python爬虫秘笈**

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/3dae97e6d5f9c59431531a86abbc1ec9.gif">

##### 五、 **数据分析全套资源**

<img alt="图片" src="https://img-blog.csdnimg.cn/img_convert/015d2714f10863c8ada5fd8a27117433.png">

##### 六、python副业兼职与全职路线

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f0f125fc73a644369b21733fd96d658f.png">

**上述这份完整版的Python全套学习资料已经上传CSDN官方，如果需要可以微信扫描下方CSDN官方认证二维码 即可领取**

>  
  👉（**安全链接，放心点击**） 
 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/221e47b5cc7f32b3c655e03c05a252d8.png">

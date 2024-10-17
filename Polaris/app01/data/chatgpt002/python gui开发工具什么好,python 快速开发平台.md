
--- 
title:  python gui开发工具什么好,python 快速开发平台 
tags: []
categories: [] 

---
大家好，小编来为大家解答以下问题，python开发技术详解(全27集),5，python gui开发工具什么好，今天让我们一起来看看吧！



<img alt="" height="500" src="https://img-blog.csdnimg.cn/img_convert/d16c6992005bea7a66dbe5888ef534c4.jpeg" width="970">

Source code download: 

### 系列文章目录

如果没有接触过tk开发的同学，学习可参考以下文章：









### 写在前面

`适用对象 适用于学习了TKinter并不想太麻烦写GUI代码，也不想用其他工具和框架 比如wxPython,PyQt4的同学。 适用于界面不太复杂的小程序开发，界面复杂的还是适用wxPython等框架吧。 因为TKinter为Python标准库，使用TKinter完成的Python程序可以称为 “绿色软件”，不需要目标机器上安装wxPython,PyQt4等框架，只要有Python 的机器就能运行。 如果软件逻辑不是很复杂，通常一个*.py搞定，不像其他框架，需要几个文件。`

我在爬取到某个软件接口后打算写个程序，于是了解到了tk，并且上手程度不难，看了前几个文章就搞懂了，于是开发出了这么难看的应用程序：<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/255f0dd7daa54787bfac1f7cd37379cc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

对于我来说，可能兴趣都在爬虫部分，对于设计并不感冒，在了解到 所有框架后 并没有适合我这种例子开发的，今早上遇到了个软件：python-tkinter助手.exe<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/22902458713e4511a65dcfbe62756688.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

优缺点：缺点，画图时不可以删除画错了就要全部清空 =,= 优点：可以生成代码

不可以撤销，就显得有点呆，下午在csdn了解到vb可视化开发，搜索了很多文章，结果却不尽人意，下载付费阻挡了我学习进度，还好我在互联网找到了，也就是今天的主角 vb可视化开发GUI，既然没有全面的教程，那我就自己来！

`提示：文章末尾会有资源下载链接！！`



##### 文章目录
- - - - <li> 
    <ul>- - - - - 


### 一、安装VB6和visualtkinter插件

下载好后的文件如图所示：<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d08de6d07bec4ebb80a5420ece2e78ba.png"> 第一步，将vb6迷你版 安装到你的电脑(略)<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/648d30795b684c65b6f78cf43aeb910f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_10,color_FFFFFF,t_70,g_se,x_16"> 第二步，安装tk插件，Setup for VisualTkinter

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cee14006949242b2b114e9542d7003c6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_10,color_FFFFFF,t_70,g_se,x_16"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6ba612bf959b4b009aff6f4aad907ea1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_16,color_FFFFFF,t_70,g_se,x_16"> 扩展（执行第三步前请先按此操作进行） 在vb6添加外接程序<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a9253c96c44041158633c658995b8726.png">

第三步，打开vb6 迷你版，出现<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7bdd4fc071384d8ab005b0efa16bf1f1.png">

说明安装成功了<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0201b2b4120545869de2392c8743470b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

### 二、使用步骤

#### 1.新建一个EXE程序

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/34e99204836e4126a3416ab1f69426f0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_16,color_FFFFFF,t_70,g_se,x_16"><img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/aa64d27fd21f43aeafb066413b33af3a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

#### 2.设计一个登录

新建一个登录框<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2174d13a186246c699c4dd202f4ba23b.png">

#### 3.修改属性

选中属性，会弹出，详细的属性值，可以修改编辑<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dd3510fdc1904e02ac922a43fb7a5093.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

#### 4.生成python代码

点击上方的<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3d24134f003a4b70a8633c77e594b6ad.png">

即可浏览生成的代码<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fee7d058827943be989a8e380f306823.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

```
#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('1264x761')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0., rely=0.011, relwidth=0.096, relheight=0.024)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.101, rely=0.011, relwidth=0.096, relheight=0.024)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='登录', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.209, rely=0.011, relwidth=0.045, relheight=0.022)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass


```

#### 5.pycharm运行代码

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a3ee77cb7ed743faa95dc4d15ebbfab9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_12,color_FFFFFF,t_70,g_se,x_16"> 发现报错不要慌，仔细看看，这个是py2.x版本的不影响py3使用 看下运行结果：<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ca28417453314a14b682312554166f38.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5b635a6P5aSn6a2U546L,size_20,color_FFFFFF,t_70,g_se,x_16">

如果要打包成exe 文件 可以移步看看这里！





### 部分控件的使用说明（重要）

>  
  Label，标签条在VB和Python中基本一样。如果不启用ttk，则在文本中插入\n来换行， 如果启用了ttk，则只支持单行文本(多行可以使用Message控件实现)。 
 

>  
  CommandButton 对应Python的Button，没有太多区别。 为了代码简洁，窗体的退出按钮可以设置Cancel属性为True，然后程序自动生成 对应Tkinter的destroy回调，这样就不需要再实现一个回调函数。 在VB里面字母前增加一个"&amp;"符号可以直接绑定一个快捷键Alt+对应字母， VisualTkinter也支持此设置，自动生成对应的事件绑定代码。 其他控件比如Checkbox等有"标题"属性的控件一样如此处理。 
 

>  
  TextBox Python文本框有两种：Entry和Text，如果VB的TextBox的MultiLine=False，则 生成Entry，否则生成Text。 
 

>  
  Frame 对应Python的LabelFrame控件，做为其他控件的容器，或做为界面元素视觉分类。 
 

>  
  CheckBox 多选按钮对应Python的Checkbutton。 
 

>  
  OptionButton 单选按钮对应Python的Radiobutton。 
 

>  
  ComboBox 组合框在Tkinter中没有对应的控件，比较类似的只有OptionMenu，类似ComboBox 的Style=2 (Dropdown List)时的表现，一个下拉列表，只能在列表中选择一个值， 不能直接输入。所以建议在VB的ComboBox中写下所有的下拉列表值。 如果启用了TTK主题扩展库支持，则直接对应到TTK的Combobox，外形和行为基本 一致。 
 

>  
  ListBox 列表框对应Python的Listbox，行为也类似，可以在设计阶段设置初始列表。 如果需要滚动，则在适当位置创建滚动条，然后在Addin界面选择其xscrollcommand 和yscrollcommand属性为对应滚动条的.set方法。 
 

>  
  HScrollBar, VScrollBar 滚动条在Python中为Scrollbar，通过设置orient来控制水平还是垂直。 
 

>  
  Slider 类似对应Python中的Scale。 
 

更多请看文件内的说明！！

### 插件自带的使用方法
1.  首先注册此插件，可以使用自带的安装程序，或自己手动完成。 1.  打开VB6，新建一个标准EXE工程，在窗体上设计自己的GUI布局，这个工作估计没有VB基础的同学都可以完成，同时可以设置相应的控件属性。 1.  如果使用自带安装程序安装了插件，现在VB的工具条上应该有一个新图标（一片橙红色羽毛），如果没有，到菜单"外接程序"|“外接程序管理器” 里面启动Visual Tkinter，Visual Tkinter图标和菜单应该会出现。 1.  启动Visual Tkinter后，先按“刷新窗体列表”按钮，列出当前工程的所有窗体和控件列表。 1.  逐个确认各控件的输出属性，在要输出的选项前打钩，如果必要，可以在属性列表中双击修改属性的值。（一般情况不需要再修改控件属性）。 VisualTkinter尽量的将VB控件属性翻译成Tkinter控件属性，比如字体、颜色 初始值、外观、状态等，甚至包括按钮类和菜单的快捷键设置等待。 当然了，如果部分属性没有对应关系的，需要在VisualTkinter界面上设置。 2.6 按“生成代码”按钮则在代码预览窗口生成代码，可以双击代码预览窗口 放大阅读，也可以直接修改代码。 2.7 确认完成后可以将代码拷贝到剪贴板或保持到文件。 布局可以使用百分比定位（相对定位）或绝对坐标定位（按像素定位）， 百分比定位为有一个好处，主界面大小变化后，控件也可以相对变化大小。 如果不希望主界面大小变化后控件跟随变化，可以选择绝对坐标定位。 注：如果修改了以前设计的界面，可以选择仅输出main函数或界面生成类。 不影响外部已经实现的逻辑代码。 2.8 如果程序有多个GUI界面，可以在VB工程中添加窗体，就可以选择产生 哪个窗体的对应代码。 2.9 针对结构化代码，如果要在Python代码中引用和修改其他控件的值， 可以使用全局字典gComps，这个字典保存了所有的GUI元素和一些对应的 控件变量，可以直接使用形如gComps[“Text1Var”].set(“new Text”)的代码 来访问对应控件。 如果输出的是面向对象代码，则可以在界面派生类Application中直接访问 对应的控件。 2.10 一般的GUI框架都会将UI部分和逻辑代码部分分别放在不同的文件中，在 逻辑代码文件中导入UI文件，实现修改UI不影响逻辑代码。因为对于实现 简单的程序来说，我偏爱单文件，所以我将UI类和逻辑代码类都放在同一个 文件中，在修改界面后，你可以直接覆盖对应的Application_ui类即可实现 界面的变更，不过如果增加了新的事件回调函数，需要在子类Application 中增加才行。 
### 总结

`文章简单的记录了，python tk 可视化GUI开发经历，希望能对你有用，这是一个VB6的ADDIN（外接程序），用于使用VB6开发工具直接拖放控件， 直接可视化完成Python的TKinter的GUI布局和设计，可以在VB界面上设置 控件的一些属性，最终自动生成必要的代码（包括回调函数框架），代码 生成后仅需要在对应的回调函数中增加相应的逻辑功能代码即可。 这个工具支持绝大部分TKiner控件，可应付一般GUI的需求。 `



****

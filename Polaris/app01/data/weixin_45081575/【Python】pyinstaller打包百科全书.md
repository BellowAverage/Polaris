
--- 
title:  【Python】pyinstaller打包百科全书 
tags: []
categories: [] 

---
## 前言

>  
 记录`pyinstaller`打包中的常用命令和报错。 


详细的还是去官网自己看吧，这里只记录打包中常用到的命令。 如果我这里帮助不到你， 官网在这里：https://github.com/pyinstaller/pyinstaller

这两篇文章基本覆盖100%的报错了， 参考这里： https://hackmd.io/@quency/B1QmM5-OD 还有这里：https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/

## 知识点📖📖

**安装模块**

```
pip install pyinstaller

```

查看命令，如何使用

```
pyinstaller -h

```

<img src="https://img-blog.csdnimg.cn/35718e7115da48cebfd8ca883a165b90.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/abcaad0a7723494d8294ec642ba84eae.png" alt="在这里插入图片描述">

注意图中圈出来的 `What to generete` 和 `Windows and Mac OS X specific options`，用的比较多的也就只有它们

|options|解释
|------
|**-F**|打包成一个文件捆绑的可执行文件（默认打包为一个文件夹，不建议
|**-n、–name**|指定名称打包程序名称（默认值为脚本的基本名称）
|**–add-data**|添加文件或文件夹（注意看格式要求
|**-w**|不显示控制台窗口
|**-i**|指定.exe程序的图标

这些命令都可以组合使用！！！

## 实现

具体的命令使用以下命令进行查看

```
pyinstaller -h

```

### 打包要略

这里展示多种打包的方式，看似多种，实际上是一种。 通用的命令是

```
pyinstaller scripts.py

```

现在脚本名为`demo.py`，则输入 `pyinstller demo.py`，如下动图所示

<img src="https://img-blog.csdnimg.cn/1092a5e8b6764b2b977549914c3ac983.gif" alt="">

打包成功后，**（因为没有指定路径）** 会在当前文件夹下生成一些文件和文件夹
- 除了红色框选出来的文件外，其他的都是`pyinstaller`生成的。- 接下来就可以在 **dist -&gt; demo**，找到 `demo.exe`，就可以运行了
<img src="https://img-blog.csdnimg.cn/02356f13fddc4483bb2b073bea547d31.png" alt="在这里插入图片描述">

#### 基础打包

**demo.py**

```
# -*- coding: utf-8 -*-
for i in range(10):
    _str = input('输入任意内容: ')
    print(_str)


```

在命令行中输入：`pyinstaller demo.py`，等待打包完成；

接着打开 **dist -&gt; demo**，找到 `demo.exe`，双击运行它，效果如下图所示 <img src="https://img-blog.csdnimg.cn/a9c8b3a29d0740bb82faa246258bb85a.gif" alt="">

通过上面可以发现，默认生成的 `.exe` 文件，带有
- 控制台窗口- `.exe` 执行程序在文件夹里面- 默认**ico**图标
值得注意的是，这里 `.exe`是无法脱离当前文件夹执行的，这个非常不好。；我更偏爱于生成单个可执行的 `.exe`，所以后面生成单个可执行文件。

#### 单个执行文件 &amp; 去除控制台窗口

>  
 有些程序，并不需要控制台窗口 


上面说到，通过
- -F：指定单个执行文件，- -w：去除控制台窗口
**demo.py**
- 这段代码执行后会生成以当前年月日时分秒命名的.txt文件
```
import datetime

exec_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

with open(file=f'{<!-- -->exec_time}.txt', mode='w', encoding='utf-8') as f:
    f.write('hello world!')
    

```

在命令行中输入：`pyinstaller demo.py -F -w`，等待打包完成；

接着打开 **dist**，找到 `demo.exe`，双击运行它，效果如下图所示

<img src="https://img-blog.csdnimg.cn/48d8dbbd9fb14fc89f41605c747896f9.gif" alt="">

通过上面可以发现，文件没有是单个可执行文件，且不会弹出控制台窗口了。

#### 指定ico图标 &amp; 任务栏图标

>  
 给`.exe`加上一个好看的图标，不使用默认的图标。`.exe`图标跟任务栏图标一致。 


**demo.py**

```
# -*- coding: utf-8 -*-
for i in range(10):
    _str = input('输入任意内容: ')
    print(_str)


```

在命令行中输入：`pyinstaller demo.py -F -i demo.ico`，等待打包完成；

接着打开 **dist**，找到 `demo.exe`，可以看到`.exe`的图标和指定的`ico`是一致的。
- **demo.ico** 在这里是一张16×16像素的ico图。
<img src="https://img-blog.csdnimg.cn/f4772a332f494dcebe152fb9a14d9feb.png" alt="">

运行效果如下图所示：
- 可以看到，任务栏的图标也是改变了的。
<img src="https://img-blog.csdnimg.cn/198c33a7f3324a6fbd7859cb4b313bd2.gif" alt="在这里插入图片描述">

#### Qt 指定任务栏图标

譬如在打包 **pyside2、pyqt5**等**GUI**程序时候， 有时候用上述的命令，`.exe`的图标并不会作用于任务栏，则使用以下的代码。
- 将这段代码放置在最前面，然后使用`setWindowIcon()`设置好`.exe`的图标，后面任务栏的图标就会跟随 `.ico`了。
```
# 任务栏ico与工具左上角ico同步
try:
    # Only exists on Windows.
    from ctypes import windll
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == '__main__':
    # 窗口按照dpi拉伸
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 设置ico，绝对路径指定路径或相对路径都可以
    app.setWindowIcon(QtGui.QIcon("C:\Users\John\Desktop\demo.ico"))
	...

```

## 后话

本次分享就到这里，🐱‍🏍🐱‍🏍 see you~


--- 
title:  【Python & Other】一网打尽 Python复制文本&文件到剪切板 
tags: []
categories: [] 

---
## 前言

>  
 在使用`uiautomation`操作微信发送信息时候，**难点**在于发送文件。发送文件，靠的是复制到剪切板，然后再从剪切板粘贴发送。 本文吧啦一下在Windows系统中关于Python复制文件到剪切板的操作。 


花了挺多时间，但是不管怎么找，始终都找不着Python复制文件到剪切板的方法。 于是另辟蹊径，从Windows系统上下手，然后再利用Python去调用Windows系统的命令，曲线救国，从而达到Python复制我呢见到剪切板的方法。 多动一下自己那个🐷脑袋，问题总是可以解决的🐱‍🏍🐱‍🏍

## 知识点📖📖

文中用到的命令都可以在  找到相应的解释，有疑问请找它，不要来问我！！！

**复制文本**
- cmd窗口：`echo text | clip`- Python模块：`pyperclip`
**复制文件**
- 借助工具 xclip：`echo file_path | xclip /copy`- 借助PowerShell命令：`Get-Item file_path | Set-Clipboard`
## 实现

### 复制文本

这里介绍两种方法
- Windows系统命令- Python模块pyperclip
#### `Windows系统命令`

在Windows系统中，cmd窗口输入以下命令可以将`text文本`复制到剪切板

```
echo text | clip

```

在Python中，可以使用os模块来执行cmd命令
- 将`text`替换成需要复制到剪切板的文本即可
```
import os
os.system('echo text | clip')

```

#### `pyperclip`

在Python中，有模块是支持复制文本到剪切版的

```
pip install pyperclip

```

使用的话，也是很简单

```
import pyperclip

#　复制文本到剪切板
pyperclip.copy('The text to be copied to the clipboard.')

# 获取剪切板的文本
text = pyperclip.paste()
print(text)	# 'The text to be copied to the clipboard.'


```

### 复制文件

<mark>！！！可以很负责任地说，别处找不着这么好且这么多的方法~</mark> <mark>！！！可以很负责任地说，别处找不着这么好且这么多的方法~</mark> <mark>！！！可以很负责任地说，别处找不着这么好且这么多的方法~</mark>

这里介绍几种方法，
- xclip工具- PowerShell命令二则
#### `xclip工具`

>  
 这个方法一次只能复制一个文件到剪切板 


首先， 下载`xclip工具`。

然后，将它添加到系统环境变量（可选操作，可不添加。

**示例如下**

<img src="https://img-blog.csdnimg.cn/1e76c0030cec4f6ea6a3e49318ae28b9.png" alt="">

当前文件夹中有一份 `demo.txt文件`，现在需要将它复制到剪切板 在当前文件夹地址栏输入`cmd`（其它方式也行 然后输入

```
echo demo.txt | xclip /copy

```

<img src="https://img-blog.csdnimg.cn/ca20bf21022e4918b17f017123b29675.png" alt="">

以上，就可以将文件复制到剪切板了~~

使用Python的os模块去调用如下：

```
import os
os.system('echo demo.txt | xclip /copy')

```

#### `PowerShell命令二则`

>  
 这个方法一次只能复制一个文件到剪切板 这个虽然是PowerShell的命令，但却是使用cmd窗口去执行的。 


##### 第一则

代码如下：

```
set "file=你的文件全路径"

powershell -sta "$sc=New-Object System.Collections.Specialized.StringCollection;$sc.Add('%file%');Add-Type -Assembly 'System.Windows.Forms';[System.Windows.Forms.Clipboard]::SetFileDropList($sc);"

```

在cmd窗口中输入以上代码，即可将你指定的文件复制到剪切版了。 将它改写成 `.bat可执行` 文件，如下

**demo.bat**

```
@ECHO OFF
set file=%1
powershell -sta "$sc=New-Object System.Collections.Specialized.StringCollection;$sc.Add('%file%');Add-Type -Assembly 'System.Windows.Forms';[System.Windows.Forms.Clipboard]::SetFileDropList($sc);"

```

代码释义： 第一行：`.bat可执行`文件默认写法 第二行：`%1` 为接收外部的第一个传参，接收文件的路径 第三行：复制文件到剪切板

然后再使用 Python去调用它

```
import os

os.system('demo.bat 文件的绝对路径')

```

以上，即可将文件复制到剪切板了。

##### 第二则

>  
 这个方法一次可复制多个文件到剪切板，建议用这个方法！！！ 


这里借助的是**PowerShell**，所以需要打开**PowerShell** 去执行。

如下图： <img src="https://img-blog.csdnimg.cn/2a8507766f9c47229eb1254583c00bfe.png" alt=""> 执行的命令如下：

复制单个文件到剪切板

```
Get-Item demo.txt | Set-Clipboard

```

复制多个文件到剪切板（用逗号隔开

```
Get-Item demo.txt,demo2.txt | Set-Clipboard

```

使用Python调用，如下

```
import subprocess

args = ['powershell', 'Get-Item 文件路径,文件路径,... | Set-Clipboard']
subprocess.Popen(args=args)

```

## 后话

本文介绍到此， see you.🎈🎈

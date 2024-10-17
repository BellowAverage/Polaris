
--- 
title:  用 Python 写个计算器 
tags: []
categories: [] 

---
我们常见的计算辅助工具有两种，一种是古人发明的算盘，另一种就是我们现代人发明的计算器，与算盘相比，计算器无论是便利性还是计算速度都是优于算盘的，本文我们使用 Python 来实现一个简易的计算器。

### 实现

我们几乎每个人都用过计算器，大家对于计算器应该都是比较熟悉的，计算器整体也是比较简单的，主要包括：显示器、键盘、运算的逻辑处理等，计算器的图形界面我们使用 `tkinter` 库实现，下面看一下具体实现过程。

首先，我们画一个主窗口，代码实现如下：

```
# 创建主窗口
tk = tkinter.Tk()
# 设置窗口大小和位置
tk.geometry('300x210+500+200')
# 不允许改变窗口大小
tk.resizable(False, False)
# 设置窗口标题
tk.title('计算器')

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/f9a1958194e7456a74a4906db72bcfa3.png" alt=""> 我们接着画显示器，代码实现如下：

```
# 自动刷新字符串变量，可用 set 和 get 方法进行传值和取值
contentVar = tkinter.StringVar(tk, '')
# 创建单行文本框
contentEntry = tkinter.Entry(tk, textvariable=contentVar)
# 设置文本框为只读
contentEntry['state'] = 'readonly'
# 设置文本框坐标及宽高
contentEntry.place(x=20, y=10, width=260, height=30)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/780abec446434086ddc78a40ae415d2f.png" alt=""> 再接着画键盘，代码实现如下：

```
# 按钮显示内容
bvalue = ['C', '+', '-', '//', '2', '0', '1', '√', '3', '4', '5', '*', '6', '7', '8', '.', '9', '/', '**', '=']
index = 0
# 将按钮进行 5x4 放置
for row in range(5):
    for col in range(4):
        d = bvalue[index]
        index += 1
        btnDigit = tkinter.Button(tk, text=d, command=lambda x=d: onclick(x))
        btnDigit.place(x=20 + col * 70, y=50 + row * 30, width=50, height=20)

```

看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/433d2a869b0a6167d6270f252d557c66.png" alt=""> 界面画完了，我们看一下处理运算逻辑的代码，如下所示：

```
# 点击事件
def onclick(btn):
    # 运算符
    operation = ('+', '-', '*', '/', '**', '//')
    # 获取文本框中的内容
    content = contentVar.get()
    # 如果已有内容是以小数点开头的，在前面加 0
    if content.startswith('.'):
        content = '0' + content  # 字符串可以直接用+来增加字符
    # 根据不同的按钮作出不同的反应
    if btn in '0123456789':
        # 按下 0-9 在 content 中追加
        content += btn
    elif btn == '.':
        # 将 content 从 +-*/ 这些字符的地方分割开来
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            # 信息提示对话框
            tkinter.messagebox.showerror('错误', '重复出现的小数点')
            return
        else:
            content += btn
    elif btn == 'C':
        # 清除文本框
        content = ''
    elif btn == '=':
        try:
            # 对输入的表达式求值
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式有误')
            return
    elif btn in operation:
        if content.endswith(operation):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == '√':
        # 从 . 处分割存入 n，n 是一个列表
        n = content.split('.')
        # 如果列表中所有的都是数字，就是为了检查表达式是不是正确的
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    # 将结果显示到文本框中
    contentVar.set(content)

```

整体实现完了之后，我们来演示一下，看一下效果： <img src="https://img-blog.csdnimg.cn/img_convert/9b1606ea6e5968bd8599ed6f3a400415.gif" alt=""> 是不是有内味了。

### 打包

为了更加方便的使用，我们可以将 Python 代码打包成 exe 文件，打包我们使用 pyinstaller，安装用 `pip install pyinstaller` 命令即可。

打包时我们使用 `pyinstaller --onefile --nowindowed counter.py` 命令即可，此时打包生成的文件是使用的默认图标，如果我们想指定自己的图标可以添加参数 `--icon="xxx\xxx.ico"`，打包生成的文件在 dist 目录，如下图所示： <img src="https://img-blog.csdnimg.cn/img_convert/0dea6191d9c2a0bea144a49bf5825272.png" alt=""> 此时，我们直接运行 exe 文件就行了。

### 总结

本文我们使用 Python 实现了一个简易的计算器，大家如果有兴趣的话，可以尝试添加更多的功能以及对键盘进行个性化修改。

源码在公众号 **Python小二** 后台回复 **200616** 获取。

>  
 本文非首发于个人号 


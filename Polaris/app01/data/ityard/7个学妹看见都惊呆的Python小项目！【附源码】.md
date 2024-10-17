
--- 
title:  7个学妹看见都惊呆的Python小项目！【附源码】 
tags: []
categories: [] 

---
版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。本文链接：

https://blog.csdn.net/xw1680/article/details/116201057

## 界面应用

### 1、计算器

1. 案例介绍

本例利用 Python 开发一个可以进行简单的四则运算的图形化计算器，会用到 Tkinter 图形组件进行开发。主要知识点：Python Tkinter 界面编程；计算器逻辑运算实现。本例难度为初级，适合具有 Python 基础和 Tkinter 组件编程知识的用户学习。

2. 设计原理

要制作一个计算器，首先需要知道它由哪些部分组成。示意如下图所示。<img src="https://img-blog.csdnimg.cn/img_convert/0765ed3f2805ab8134d867c5dac15604.png" alt="0765ed3f2805ab8134d867c5dac15604.png">从结构上来说，一个简单的图形界面，需要由界面组件、组件的事件监听器(响应各类事件的逻辑)和具体的事件处理逻辑组成。界面实现的主要工作是创建各个界面组件对象，对其进行初始化，以及控制各组件之间的层次关系和布局。

3. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/4c3b0b555ebb7a7648e56dded33da84e.gif" alt="4c3b0b555ebb7a7648e56dded33da84e.gif">4. 示例源码

```
import tkinter
import math
import tkinter.messagebox




class Calculator(object):
    # 界面布局方法
    def __init__(self):
        # 创建主界面，并且保存到成员属性中
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('计算器')
        # 设置显式面板的变量
        self.result = tkinter.StringVar()
        self.result.set(0)
        # 设置一个全局变量  运算数字和f符号的列表
        self.lists = []
        # 添加一个用于判断是否按下运算符号的标志
        self.ispresssign = False
        # 界面布局
        self.menus()
        self.layout()
        self.root.mainloop()


    # 计算器菜单界面摆放


    def menus(self):
        # 添加菜单
        # 创建总菜单
        allmenu = tkinter.Menu(self.root)
        # 添加子菜单
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        filemenu.add_command(
            label='标准型(T)            Alt+1', command=self.myfunc)
        filemenu.add_command(
            label='科学型(S)            Alt+2', command=self.myfunc)
        filemenu.add_command(
            label='程序员(P)            Alt+3', command=self.myfunc)
        filemenu.add_command(label='统计信息(A)        Alt+4', command=self.myfunc)
        # 添加分割线
        filemenu.add_separator()
        # 添加选项卡
        filemenu.add_command(label='历史记录(Y)      Ctrl+H', command=self.myfunc)
        filemenu.add_command(label='数字分组(I)', command=self.myfunc)
        # 添加分割线
        filemenu.add_separator()
        # 添加选项卡
        filemenu.add_command(
            label='基本(B)             Ctrl+F4', command=self.myfunc)
        filemenu.add_command(label='单位转换(U)      Ctrl+U', command=self.myfunc)
        filemenu.add_command(label='日期计算(D)      Ctrl+E', command=self.myfunc)
        menu1 = tkinter.Menu(filemenu, tearoff=0)
        menu1.add_command(label='抵押(M)', command=self.myfunc)
        menu1.add_command(label='汽车租赁(V)', command=self.myfunc)
        menu1.add_command(label='油耗(mpg)(F)', command=self.myfunc)
        menu1.add_command(label='油耗(l/100km)(U)', command=self.myfunc)
        filemenu.add_cascade(label='工作表(W)', menu=menu1)
        allmenu.add_cascade(label='查看(V)', menu=filemenu)


        # 添加子菜单2
        editmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        editmenu.add_command(label='复制(C)         Ctrl+C', command=self.myfunc)
        editmenu.add_command(label='粘贴(V)         Ctrl+V', command=self.myfunc)
        # 添加分割线
        editmenu.add_separator()
        # 添加选项卡
        menu2 = tkinter.Menu(filemenu, tearoff=0)
        menu2.add_command(label='复制历史记录(I)', command=self.myfunc)
        menu2.add_command(
            label='编辑(E)                      F2', command=self.myfunc)
        menu2.add_command(label='取消编辑(N)            Esc', command=self.myfunc)
        menu2.add_command(label='清除(L)    Ctrl+Shift+D', command=self.myfunc)
        editmenu.add_cascade(label='历史记录(H)', menu=menu2)
        allmenu.add_cascade(label='编辑(E)', menu=editmenu)


        # 添加子菜单3
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        # 添加选项卡
        helpmenu.add_command(label='查看帮助(V)       F1', command=self.myfunc)
        # 添加分割线
        helpmenu.add_separator()
        # 添加选项卡
        helpmenu.add_command(label='关于计算器(A)', command=self.myfunc)
        allmenu.add_cascade(label='帮助(H)', menu=helpmenu)


        self.root.config(menu=allmenu)


    # 计算器主界面摆放


    def layout(self):
        # 显示屏
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=(
            '宋体', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)
        # 功能按钮MC
        button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
        button_mc.place(x=5, y=95, width=50, height=50)
        # 功能按钮MR
        button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
        button_mr.place(x=60, y=95, width=50, height=50)
        # 功能按钮MS
        button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
        button_ms.place(x=115, y=95, width=50, height=50)
        # 功能按钮M+
        button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
        button_mjia.place(x=170, y=95, width=50, height=50)
        # 功能按钮M-
        button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
        button_mjian.place(x=225, y=95, width=50, height=50)
        # 功能按钮←
        button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)
        # 功能按钮CE
        button_ce = tkinter.Button(
            self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)
        # 功能按钮C
        button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)
        # 功能按钮±
        button_zf = tkinter.Button(self.root, text='±', command=self.zf)
        button_zf.place(x=170, y=150, width=50, height=50)
        # 功能按钮√
        button_kpf = tkinter.Button(self.root, text='√', command=self.kpf)
        button_kpf.place(x=225, y=150, width=50, height=50)
        # 数字按钮7
        button_7 = tkinter.Button(
            self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        # 数字按钮8
        button_8 = tkinter.Button(
            self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        # 数字按钮9
        button_9 = tkinter.Button(
            self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        # 功能按钮/
        button_division = tkinter.Button(
            self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        # 功能按钮%
        button_remainder = tkinter.Button(
            self.root, text='//', command=lambda: self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        # 数字按钮4
        button_4 = tkinter.Button(
            self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        # 数字按钮5
        button_5 = tkinter.Button(
            self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        # 数字按钮6
        button_6 = tkinter.Button(
            self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        # 功能按钮*
        button_multiplication = tkinter.Button(
            self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        # 功能按钮1/x
        button_reciprocal = tkinter.Button(
            self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        # 数字按钮1
        button_1 = tkinter.Button(
            self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        # 数字按钮2
        button_2 = tkinter.Button(
            self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        # 数字按钮3
        button_3 = tkinter.Button(
            self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        # 功能按钮-
        button_subtraction = tkinter.Button(
            self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        # 功能按钮=
        button_equal = tkinter.Button(
            self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)
        # 数字按钮0
        button_0 = tkinter.Button(
            self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        # 功能按钮.
        button_point = tkinter.Button(
            self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        # 功能按钮+
        button_plus = tkinter.Button(
            self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)


    # 计算器菜单功能


    def myfunc(self):
        tkinter.messagebox.showinfo('', '预留接口，学成之后，你是不是有冲动添加该功能.')


    # 数字方法
    def pressnum(self, num):
        # 全局化变量
        # 判断是否按下了运算符号
        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
            # 重置运算符号的状态
            self.ispresssign = False
        if num == '.':
            num = '0.'
        # 获取面板中的原有数字
        oldnum = self.result.get()
        # 判断界面数字是否为0
        if oldnum == '0':
            self.result.set(num)
        else:
            # 连接上新按下的数字
            newnum = oldnum + num


            # 将按下的数字写到面板中
            self.result.set(newnum)


    # 运算函数
    def presscalculate(self, sign):
        # 保存已经按下的数字和运算符号
        # 获取界面数字
        num = self.result.get()
        self.lists.append(num)
        # 保存按下的操作符号
        self.lists.append(sign)
        # 设置运算符号为按下状态
        self.ispresssign = True


    # 获取运算结果


    def pressequal(self):
        # 获取所有的列表中的内容（之前的数字和操作）
        # 获取当前界面上的数字
        curnum = self.result.get()
        # 将当前界面的数字存入列表
        self.lists.append(curnum)
        # 将列表转化为字符串
        calculatestr = ''.join(self.lists)
        # 使用eval执行字符串中的运算即可
        endnum = eval(calculatestr)
        # 将运算结果显示在界面中
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()


    # 暂未开发说明


    def wait(self):
        tkinter.messagebox.showinfo('', '更新中......')


    # ←按键功能


    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num &gt; 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')


    # ±按键功能


    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)


    # 1/x按键功能


    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()


    # C按键功能


    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)


    # √按键功能


    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # 清空运算列表
        self.lists.clear()




# 实例化对象
my_calculator = Calculator()
```

### 

### 

### 2、记事本

1. 案例介绍

tkinter 是 Python下面向 tk 的图形界面接口库，可以方便地进行图形界面设计和交互操作编程。tkinter 的优点是简单易用、与 Python 的结合度好。tkinter 在 Python 3.x 下默认集成，不需要额外的安装操作；不足之处为缺少合适的可视化界面设计工具，需要通过代码来完成窗口设计和元素布局。

本例采用的 Python 版本为 3.8，如果想在 python 2.x下使用 tkinter，请先进行安装。需要注意的是，不同 Python 版本下的 tkinter 使用方式可能略有不同，建议采用 Python3.x 版本。

本例难度为中级，适合具有 Python 基础和 Tkinter 组件编程知识的用户学习。

2. 示例效果

<img src="https://img-blog.csdnimg.cn/img_convert/0be9917107d0df5e71cf87f90f190bec.gif" alt="0be9917107d0df5e71cf87f90f190bec.gif">3. 示例源码

```
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os


filename = ""




def author():
    showinfo(title="作者", message="Python")




def power():
    showinfo(title="版权信息", message="课堂练习")




def mynew():
    global top, filename, textPad
    top.title("未命名文件")
    filename = None
    textPad.delete(1.0, END)




def myopen():
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        top.title("记事本" + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()




def mysave():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        mysaveas()




def mysaveas():
    global filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    top.title("记事本 " + os.path.basename(f))




def cut():
    global textPad
    textPad.event_generate("&lt;&lt;Cut&gt;&gt;")




def copy():
    global textPad
    textPad.event_generate("&lt;&lt;Copy&gt;&gt;")




def paste():
    global textPad
    textPad.event_generate("&lt;&lt;Paste&gt;&gt;")




def undo():
    global textPad
    textPad.event_generate("&lt;&lt;Undo&gt;&gt;")




def redo():
    global textPad
    textPad.event_generate("&lt;&lt;Redo&gt;&gt;")




def select_all():
    global textPad
    # textPad.event_generate("&lt;&lt;Cut&gt;&gt;")
    textPad.tag_add("sel", "1.0", "end")




def find():
    t = Toplevel(top)
    t.title("查找")
    t.geometry("260x60+200+250")
    t.transient(top)
    Label(t, text="查找：").grid(row=0, column=0, sticky="e")
    v = StringVar()
    e = Entry(t, width=20, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="不区分大小写", variable=c).grid(row=1, column=1, sticky='e')
    Button(t, text="查找所有", command=lambda: search(v.get(), c.get(),
                                                  textPad, t, e)).grid(row=0, column=2, sticky="e" + "w", padx=2,
                                                                       pady=2)


    def close_search():
        textPad.tag_remove("match", "1.0", END)
        t.destroy()


    t.protocol("WM_DELETE_WINDOW", close_search)




def mypopup(event):
    # global editmenu
    editmenu.tk_popup(event.x_root, event.y_root)




def search(needle, cssnstv, textPad, t, e):
    textPad.tag_remove("match", "1.0", END)
    count = 0
    if needle:
        pos = "1.0"
        while True:
            pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
            if not pos:
                break
            lastpos = pos + str(len(needle))
            textPad.tag_add("match", pos, lastpos)
            count += 1
            pos = lastpos
        textPad.tag_config('match', fg='yellow', bg="green")
        e.focus_set()
        t.title(str(count) + "个被匹配")




top = Tk()
top.title("记事本")
top.geometry("600x400+100+50")


menubar = Menu(top)


# 文件功能
filemenu = Menu(top)
filemenu.add_command(label="新建", accelerator="Ctrl+N", command=mynew)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=myopen)
filemenu.add_command(label="保存", accelerator="Ctrl+S", command=mysave)
filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=mysaveas)
menubar.add_cascade(label="文件", menu=filemenu)


# 编辑功能
editmenu = Menu(top)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z", command=undo)
editmenu.add_command(label="重做", accelerator="Ctrl+Y", command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl+V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl+F", command=find)
editmenu.add_command(label="全选", accelerator="Ctrl+A", command=select_all)
menubar.add_cascade(label="编辑", menu=editmenu)


# 关于 功能
aboutmenu = Menu(top)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command=power)
menubar.add_cascade(label="关于", menu=aboutmenu)


top['menu'] = menubar


# shortcutbar = Frame(top, height=25, bg='light sea green')
# shortcutbar.pack(expand=NO, fill=X)
# Inlabe = Label(top, width=2, bg='antique white')
# Inlabe.pack(side=LEFT, anchor='nw', fill=Y)


textPad = Text(top, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)


# 热键绑定
textPad.bind("&lt;Control-N&gt;", mynew)
textPad.bind("&lt;Control-n&gt;", mynew)
textPad.bind("&lt;Control-O&gt;", myopen)
textPad.bind("&lt;Control-o&gt;", myopen)
textPad.bind("&lt;Control-S&gt;", mysave)
textPad.bind("&lt;Control-s&gt;", mysave)
textPad.bind("&lt;Control-A&gt;", select_all)
textPad.bind("&lt;Control-a&gt;", select_all)
textPad.bind("&lt;Control-F&gt;", find)
textPad.bind("&lt;Control-f&gt;", find)


textPad.bind("&lt;Button-3&gt;", mypopup)
top.mainloop()
```

### 3、登录和注册

1. 案例介绍

本例设计一个用户登录和注册模块，使用 Tkinter 框架构建界面，主要用到画布、文本框、按钮等组件。涉及知识点：Python Tkinter 界面编程、pickle 数据存储。本例实现了基本的用户登录和注册互动界面，并提供用户信息存储和验证。

pickle 是 python 语言的一个标准模块，安装 python 后已包含 pickle 库，不需要单独再安装。pickle 模块实现了基本的数据序列化和反序列化。通过 pickle 模块的序列化操作能够将程序中运行的对象信息保存到文件中去，永久存储；通过 pickle 模块的反序列化操作，能够从文件中创建上一次程序保存的对象。

本例难度为中级，适合具有 Python 基础和 Tkinter 组件编程知识的用户学习。

2. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/3afd2d039c5f892b5ab7210ab814dd79.png" alt="3afd2d039c5f892b5ab7210ab814dd79.png"><img src="https://img-blog.csdnimg.cn/img_convert/a22c9620d92e1482caa9eff3c8d51ada.png" alt="a22c9620d92e1482caa9eff3c8d51ada.png">3. 示例源码

```
import tkinter as tk
import pickle
import tkinter.messagebox
from PIL import Image, ImageTk


# 设置窗口---最开始的母体窗口
window = tk.Tk()  # 建立一个窗口
window.title('欢迎登录')
window.geometry('450x300')  # 窗口大小为300x200


# 画布
canvas = tk.Canvas(window, height=200, width=900)
# 加载图片
im = Image.open("images/01.png")
image_file = ImageTk.PhotoImage(im)
# image_file = tk.PhotoImage(file='images/01.gif')
image = canvas.create_image(100, 40, anchor='nw', image=image_file)
canvas.pack(side='top')


# 两个文字标签，用户名和密码两个部分
tk.Label(window, text='用户名').place(x=100, y=150)
tk.Label(window, text='密  码').place(x=100, y=190)


var_usr_name = tk.StringVar()  # 讲文本框的内容，定义为字符串类型
var_usr_name.set('amoxiang@163.com')  # 设置默认值
var_usr_pwd = tk.StringVar()


# 第一个输入框-用来输入用户名的。
# textvariable 获取文本框的内容
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 第二个输入框-用来输入密码的。
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)




def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)


    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(
                title='欢迎光临', message=usr_name + '：请进入个人首页，查看最新资讯')
        else:
            tk.messagebox.showinfo(message='错误提示：密码不对，请重试')
    else:
        is_sign_up = tk.messagebox.askyesno('提示', '你还没有注册，请先注册')
        print(is_sign_up)
        if is_sign_up:
            usr_sign_up()




# 注册按钮
def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        # 上面是获取数据，下面是查看一下是否重复注册过
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            if np != npf:
                tk.messagebox.showerror('错误提示', '密码和确认密码必须一样')
            elif nn in exist_usr_info:
                tk.messagebox.showerror('错误提示', '用户名早就注册了！')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('欢迎', '你已经成功注册了')
                window_sign_up.destroy()


    # 点击注册之后，会弹出这个窗口界面。
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('欢迎注册')
    window_sign_up.geometry('360x200')  # 中间是x，而不是*号


    # 用户名框--这里输入用户名框。
    new_name = tk.StringVar()
    new_name.set('amoxiang@163.com')  # 设置的是默认值
    tk.Label(window_sign_up, text='用户名').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=100, y=10)


    # 新密码框--这里输入注册时候的密码
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密  码').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=100, y=50)


    # 密码确认框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='确认密码').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(
        window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=100, y=90)


    btn_confirm_sign_up = tk.Button(
        window_sign_up, text=' 注  册 ', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=120, y=130)




# 创建注册和登录按钮
btn_login = tk.Button(window, text=' 登  录 ', command=usr_login)
btn_login.place(x=150, y=230)  # 用place来处理按钮的位置信息。
btn_sign_up = tk.Button(window, text=' 注  册 ', command=usr_sign_up)
btn_sign_up.place(x=250, y=230)


window.mainloop()
```

### 

## 游戏开发

### 1、2048

1. 游戏简介

2048 是一款比较流行的数字游戏。游戏规则：每次可按上、下、左、右方向键滑动数字，每滑动一次，所有数字都会往滑动方向靠拢，同时在空白位置随机出现一个数字，相同数字在靠拢时会相加。不断叠加最终拼出 2048 这个数字算成功。

2048 最早于 2014年3月20日发行。原版 2048 首先在 GitHub 上发布，原作者是 Gabriele Cirulli，后被移植到各个平台。

本例难度为初级，适合具有 Python 基础和 Pygame 编程知识的用户学习。

2. 设计原理

这个游戏的本质是二维列表，就以 4*4 的二位列表来分析关键的逻辑以及实现。二维列表如下图：<img src="https://img-blog.csdnimg.cn/img_convert/c221aa64985df315c20db5360f80b3df.png" alt="c221aa64985df315c20db5360f80b3df.png">

所有的操作都是对这个二维列表的数据的操作。分为上下左右四个方向。先说向左的方向(如图)。<img src="https://img-blog.csdnimg.cn/img_convert/d41f510b0eacadd5e8bac93751aa634e.png" alt="d41f510b0eacadd5e8bac93751aa634e.png">向左操作的结果如下图；当向左的方向是，所有的数据沿着水平方向向左跑。<img src="https://img-blog.csdnimg.cn/img_convert/485ca8fbec8e89ad8e2d5f0c4321320d.png" alt="485ca8fbec8e89ad8e2d5f0c4321320d.png">

水平说明操作的是二维列表的一行，而垂直操作的则是二位列表的一列。这样就可以将二维列表的操作变成遍历后对一维列表的操作。向左说明数据的优先考虑的位置是从左开始的。这样就确定了一维列表的遍历开始的位置。

上面第 2 个图共四行，每一个行都能得到一个列表。

```
list1：[0,0,2,0]
list2：[0,4,2,0]
list3：[0,0,4,4]
list4：[2,0,2,0]
```

这样一来向左的方向就变成。从上到下获得每一行的列表，方向向左。参数(row,left)。<img src="https://img-blog.csdnimg.cn/img_convert/cb53282cd716d8a5c6e900841fb12dde.png" alt="cb53282cd716d8a5c6e900841fb12dde.png">其他的三个方向在开始的时候记住是怎样获得以为列表的，等操作完才放回去这样就能实现了。

3. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/9dbf72c10babc7604654cc19aaf27f89.png" alt="9dbf72c10babc7604654cc19aaf27f89.png">4. 示例源码

```
import random
import sys
import pygame
from pygame.locals import *


PIXEL = 150
SCORE_PIXEL = 100
SIZE = 4




# 地图的类




class Map:
    def __init__(self, size):
        self.size = size
        self.score = 0
        self.map = [[0 for i in range(size)] for i in range(size)]
        self.add()
        self.add()


    # 新增2或4，有1/4概率产生4
    def add(self):
        while True:
            p = random.randint(0, self.size * self.size - 1)
            if self.map[int(p / self.size)][int(p % self.size)] == 0:
                x = random.randint(0, 3) &gt; 0 and 2 or 4
                self.map[int(p / self.size)][int(p % self.size)] = x
                self.score += x
                break


    # 地图向左靠拢，其他方向的靠拢可以通过适当旋转实现，返回地图是否更新
    def adjust(self):
        changed = False
        for a in self.map:
            b = []
            last = 0
            for v in a:
                if v != 0:
                    if v == last:
                        b.append(b.pop() &lt;&lt; 1)
                        last = 0
                    else:
                        b.append(v)
                        last = v
            b += [0] * (self.size - len(b))
            for i in range(self.size):
                if a[i] != b[i]:
                    changed = True
            a[:] = b
        return changed


    # 逆时针旋转地图90度
    def rotate90(self):
        self.map = [[self.map[c][r]
                     for c in range(self.size)] for r in reversed(range(self.size))]


    # 判断游戏结束
    def over(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.map[r][c] == 0:
                    return False
        for r in range(self.size):
            for c in range(self.size - 1):
                if self.map[r][c] == self.map[r][c + 1]:
                    return False
        for r in range(self.size - 1):
            for c in range(self.size):
                if self.map[r][c] == self.map[r + 1][c]:
                    return False
        return True


    def moveUp(self):
        self.rotate90()
        if self.adjust():
            self.add()
        self.rotate90()
        self.rotate90()
        self.rotate90()


    def moveRight(self):
        self.rotate90()
        self.rotate90()
        if self.adjust():
            self.add()
        self.rotate90()
        self.rotate90()


    def moveDown(self):
        self.rotate90()
        self.rotate90()
        self.rotate90()
        if self.adjust():
            self.add()
        self.rotate90()


    def moveLeft(self):
        if self.adjust():
            self.add()




# 更新屏幕




def show(map):
    for i in range(SIZE):
        for j in range(SIZE):
            # 背景颜色块
            screen.blit(map.map[i][j] == 0 and block[(i + j) % 2]
                        or block[2 + (i + j) % 2], (PIXEL * j, PIXEL * i))
            # 数值显示
            if map.map[i][j] != 0:
                map_text = map_font.render(
                    str(map.map[i][j]), True, (106, 90, 205))
                text_rect = map_text.get_rect()
                text_rect.center = (PIXEL * j + PIXEL / 2,
                                    PIXEL * i + PIXEL / 2)
                screen.blit(map_text, text_rect)
    # 分数显示
    screen.blit(score_block, (0, PIXEL * SIZE))
    score_text = score_font.render((map.over(
    ) and "Game over with score " or "Score: ") + str(map.score), True, (106, 90, 205))
    score_rect = score_text.get_rect()
    score_rect.center = (PIXEL * SIZE / 2, PIXEL * SIZE + SCORE_PIXEL / 2)
    screen.blit(score_text, score_rect)
    pygame.display.update()




map = Map(SIZE)
pygame.init()
screen = pygame.display.set_mode((PIXEL * SIZE, PIXEL * SIZE + SCORE_PIXEL))
pygame.display.set_caption("2048")
block = [pygame.Surface((PIXEL, PIXEL)) for i in range(4)]
# 设置颜色
block[0].fill((152, 251, 152))
block[1].fill((240, 255, 255))
block[2].fill((0, 255, 127))
block[3].fill((225, 255, 255))
score_block = pygame.Surface((PIXEL * SIZE, SCORE_PIXEL))
score_block.fill((245, 245, 245))
# 设置字体
map_font = pygame.font.Font(None, int(PIXEL * 2 / 3))
score_font = pygame.font.Font(None, int(SCORE_PIXEL * 2 / 3))
clock = pygame.time.Clock()
show(map)


while not map.over():
    # 12为实验参数
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    # 接收玩家操作
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w] or pressed_keys[K_UP]:
        map.moveUp()
    elif pressed_keys[K_s] or pressed_keys[K_DOWN]:
        map.moveDown()
    elif pressed_keys[K_a] or pressed_keys[K_LEFT]:
        map.moveLeft()
    elif pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        map.moveRight()
    show(map)


# 游戏结束
pygame.time.delay(3000)
```

### 

### 2、贪吃蛇

1. 案例介绍

贪吃蛇是一款经典的益智游戏，简单又耐玩。该游戏通过控制蛇头方向吃蛋，从而使得蛇变得越来越长。

通过上下左右方向键控制蛇的方向，寻找吃的东西，每吃一口就能得到一定的积分，而且蛇的身子会越吃越长，身子越长玩的难度就越大，不能碰墙，不能咬到自己的身体，更不能咬自己的尾巴，等到了一定的分数，就能过关，然后继续玩下一关。

本例难度为中级，适合具有 Python 基础和 Pygame 编程知识的用户学习。

2. 设计要点

游戏是基于 PyGame 框架制作的，程序核心逻辑如下：

游戏界面分辨率是 640*480，蛇和食物都是由 1 个或多个 20*20 像素的正方形块儿(为了方便，下文用点表示 20*20 像素的正方形块儿) 组成，这样共有 32*24 个点，使用 pygame.draw.rect 来绘制每一个点；

初始化时蛇的长度是 3，食物是 1 个点，蛇初始的移动的方向是右，用一个数组代表蛇，数组的每个元素是蛇每个点的坐标，因此数组的第一个坐标是蛇尾，最后一个坐标是蛇头；游戏开始后，根据蛇的当前移动方向，将蛇运动方向的前方的那个点 append 到蛇数组的末位，再把蛇尾去掉，蛇的坐标数组就相当于往前挪了一位；如果蛇吃到了食物，即蛇头的坐标等于食物的坐标，那么在第 2 点中蛇尾就不用去掉，就产生了蛇长度增加的效果；食物被吃掉后，随机在空的位置(不能与蛇的身体重合) 再生成一个；通过 PyGame 的 event 监控按键，改变蛇的方向，例如当蛇向右时，下一次改变方向只能向上或者向下；当蛇撞上自身或墙壁，游戏结束，蛇头装上自身，那么蛇坐标数组里就有和舌头坐标重复的数据，撞上墙壁则是蛇头坐标超过了边界，都很好判断；其他细节：做了个开始的欢迎界面；食物的颜色随机生成；吃到实物的时候有声音提示等。

3. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/42cf32217f87c0868ff1b6e9e17c9d98.png" alt="42cf32217f87c0868ff1b6e9e17c9d98.png">

4. 示例源码

```
import pygame
from os import path
from sys import exit
from time import sleep
from random import choice
from itertools import product
from pygame.locals import QUIT, KEYDOWN




def direction_check(moving_direction, change_direction):
    directions = [['up', 'down'], ['left', 'right']]
    if moving_direction in directions[0] and change_direction in directions[1]:
        return change_direction
    elif moving_direction in directions[1] and change_direction in directions[0]:
        return change_direction
    return moving_direction




class Snake:
    colors = list(product([0, 64, 128, 192, 255], repeat=3))[1:-1]


    def __init__(self):
        self.map = {(x, y): 0 for x in range(32) for y in range(24)}
        self.body = [[100, 100], [120, 100], [140, 100]]
        self.head = [140, 100]
        self.food = []
        self.food_color = []
        self.moving_direction = 'right'
        self.speed = 4
        self.generate_food()
        self.game_started = False


    def check_game_status(self):
        if self.body.count(self.head) &gt; 1:
            return True
        if self.head[0] &lt; 0 or self.head[0] &gt; 620 or self.head[1] &lt; 0 or self.head[1] &gt; 460:
            return True
        return False


    def move_head(self):
        moves = {
            'right': (20, 0),
            'up': (0, -20),
            'down': (0, 20),
            'left': (-20, 0)
        }
        step = moves[self.moving_direction]
        self.head[0] += step[0]
        self.head[1] += step[1]


    def generate_food(self):
        self.speed = len(
            self.body) // 16 if len(self.body) // 16 &gt; 4 else self.speed
        for seg in self.body:
            x, y = seg
            self.map[x // 20, y // 20] = 1
        empty_pos = [pos for pos in self.map.keys() if not self.map[pos]]
        result = choice(empty_pos)
        self.food_color = list(choice(self.colors))
        self.food = [result[0] * 20, result[1] * 20]




def main():
    key_direction_dict = {
        119: 'up',  # W
        115: 'down',  # S
        97: 'left',  # A
        100: 'right',  # D
        273: 'up',  # UP
        274: 'down',  # DOWN
        276: 'left',  # LEFT
        275: 'right',  # RIGHT
    }


    fps_clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    snake = Snake()
    sound = False
    if path.exists('eat.wav'):
        sound_wav = pygame.mixer.Sound("eat.wav")
        sound = True
    title_font = pygame.font.SysFont('simsunnsimsun', 32)
    welcome_words = title_font.render(
        '贪吃蛇', True, (0, 0, 0), (255, 255, 255))
    tips_font = pygame.font.SysFont('simsunnsimsun', 20)
    start_game_words = tips_font.render(
        '点击开始', True, (0, 0, 0), (255, 255, 255))
    close_game_words = tips_font.render(
        '按ESC退出', True, (0, 0, 0), (255, 255, 255))
    gameover_words = title_font.render(
        '游戏结束', True, (205, 92, 92), (255, 255, 255))
    win_words = title_font.render(
        '蛇很长了，你赢了！', True, (0, 0, 205), (255, 255, 255))
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('贪吃蛇')
    new_direction = snake.moving_direction
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == 27:
                    exit()
                if snake.game_started and event.key in key_direction_dict:
                    direction = key_direction_dict[event.key]
                    new_direction = direction_check(
                        snake.moving_direction, direction)
            elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 213 &lt;= x &lt;= 422 and 304 &lt;= y &lt;= 342:
                    snake.game_started = True
        screen.fill((255, 255, 255))
        if snake.game_started:
            snake.moving_direction = new_direction  # 在这里赋值，而不是在event事件的循环中赋值，避免按键太快
            snake.move_head()
            snake.body.append(snake.head[:])
            if snake.head == snake.food:
                if sound:
                    sound_wav.play()
                snake.generate_food()
            else:
                snake.body.pop(0)
            for seg in snake.body:
                pygame.draw.rect(screen, [0, 0, 0], [
                    seg[0], seg[1], 20, 20], 0)
            pygame.draw.rect(screen, snake.food_color, [
                snake.food[0], snake.food[1], 20, 20], 0)
            if snake.check_game_status():
                screen.blit(gameover_words, (241, 310))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
            elif len(snake.body) == 512:
                screen.blit(win_words, (33, 210))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
        else:
            screen.blit(welcome_words, (240, 150))
            screen.blit(start_game_words, (246, 310))
            screen.blit(close_game_words, (246, 350))
        pygame.display.update()
        fps_clock.tick(snake.speed)




if __name__ == '__main__':
    main()
```

### 3、俄罗斯方块

1. 案例介绍

俄罗斯方块是由 4 个小方块组成不同形状的板块，随机从屏幕上方落下，按方向键调整板块的位置和方向，在底部拼出完整的一行或几行。这些完整的横条会消失，给新落下来的板块腾出空间，并获得分数奖励。没有被消除掉的方块不断堆积，一旦堆到顶端，便告输，游戏结束。

本例难度为高级，适合具有 Python 进阶和 Pygame 编程技巧的用户学习。

2. 设计要点

边框――由 15*25 个空格组成，方块就落在这里面。

盒子――组成方块的其中小方块，是组成方块的基本单元。

方块――从边框顶掉下的东西，游戏者可以翻转和改变位置。每个方块由 4 个盒子组成。

形状――不同类型的方块。这里形状的名字被叫做 T, S, Z ,J, L, I , O。如下图所示：

<img src="https://img-blog.csdnimg.cn/img_convert/68bfa9d8763b57576d91057eb9f8f38f.png" alt="68bfa9d8763b57576d91057eb9f8f38f.png"><img src="https://img-blog.csdnimg.cn/img_convert/c29b6014e5c7950ffd87905e9e7f52d5.png" alt="c29b6014e5c7950ffd87905e9e7f52d5.png">

模版――用一个列表存放形状被翻转后的所有可能样式。全部存放在变量里，变量名字如 S or J。

着陆――当一个方块到达边框的底部或接触到在其他的盒子话，就说这个方块着陆了。那样的话，另一个方块就会开始下落。

3. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/c68d2fa87aa3e8983fabe18acf5badd0.gif" alt="c68d2fa87aa3e8983fabe18acf5badd0.gif">4. 示例源码

```
import pygame
import random
import os


pygame.init()


GRID_WIDTH = 20
GRID_NUM_WIDTH = 15
GRID_NUM_HEIGHT = 25
WIDTH, HEIGHT = GRID_WIDTH * GRID_NUM_WIDTH, GRID_WIDTH * GRID_NUM_HEIGHT
SIDE_WIDTH = 200
SCREEN_WIDTH = WIDTH + SIDE_WIDTH
WHITE = (0xff, 0xff, 0xff)
BLACK = (0, 0, 0)
LINE_COLOR = (0x33, 0x33, 0x33)


CUBE_COLORS = [
    (0xcc, 0x99, 0x99), (0xff, 0xff, 0x99), (0x66, 0x66, 0x99),
    (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
    (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (0xff, 0xff, 0x33),
    (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (0xff, 0x99, 0x00)
]


screen = pygame.display.set_mode((SCREEN_WIDTH, HEIGHT))
pygame.display.set_caption("俄罗斯方块")
clock = pygame.time.Clock()
FPS = 30


score = 0
level = 1


screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]


# 设置游戏的根目录为当前文件夹
base_folder = os.path.dirname(__file__)




def show_text(surf, text, size, x, y, color=WHITE):
    font_name = os.path.join(base_folder, 'font/font.ttc')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)




class CubeShape(object):
    SHAPES = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
    I = [[(0, -1), (0, 0), (0, 1), (0, 2)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]]
    J = [[(-2, 0), (-1, 0), (0, 0), (0, -1)],
         [(-1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, 1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (1, 0)]]
    L = [[(-2, 0), (-1, 0), (0, 0), (0, 1)],
         [(1, 0), (0, 0), (0, 1), (0, 2)],
         [(0, -1), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (-1, 0)]]
    O = [[(0, 0), (0, 1), (1, 0), (1, 1)]]
    S = [[(-1, 0), (0, 0), (0, 1), (1, 1)],
         [(1, -1), (1, 0), (0, 0), (0, 1)]]
    T = [[(0, -1), (0, 0), (0, 1), (-1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, -1)]]
    Z = [[(0, -1), (0, 0), (1, 0), (1, 1)],
         [(-1, 0), (0, 0), (0, -1), (1, -1)]]
    SHAPES_WITH_DIR = {
        'I': I, 'J': J, 'L': L, 'O': O, 'S': S, 'T': T, 'Z': Z
    }


    def __init__(self):
        self.shape = self.SHAPES[random.randint(0, len(self.SHAPES) - 1)]
        # 骨牌所在的行列
        self.center = (2, GRID_NUM_WIDTH // 2)
        self.dir = random.randint(0, len(self.SHAPES_WITH_DIR[self.shape]) - 1)
        self.color = CUBE_COLORS[random.randint(0, len(CUBE_COLORS) - 1)]


    def get_all_gridpos(self, center=None):
        curr_shape = self.SHAPES_WITH_DIR[self.shape][self.dir]
        if center is None:
            center = [self.center[0], self.center[1]]


        return [(cube[0] + center[0], cube[1] + center[1])
                for cube in curr_shape]


    def conflict(self, center):
        for cube in self.get_all_gridpos(center):
            # 超出屏幕之外，说明不合法
            if cube[0] &lt; 0 or cube[1] &lt; 0 or cube[0] &gt;= GRID_NUM_HEIGHT or \
                    cube[1] &gt;= GRID_NUM_WIDTH:
                return True


            # 不为None，说明之前已经有小方块存在了，也不合法
            if screen_color_matrix[cube[0]][cube[1]] is not None:
                return True


        return False


    def rotate(self):
        new_dir = self.dir + 1
        new_dir %= len(self.SHAPES_WITH_DIR[self.shape])
        old_dir = self.dir
        self.dir = new_dir
        if self.conflict(self.center):
            self.dir = old_dir
            return False


    def down(self):
        # import pdb; pdb.set_trace()
        center = (self.center[0] + 1, self.center[1])
        if self.conflict(center):
            return False


        self.center = center
        return True


    def left(self):
        center = (self.center[0], self.center[1] - 1)
        if self.conflict(center):
            return False
        self.center = center
        return True


    def right(self):
        center = (self.center[0], self.center[1] + 1)
        if self.conflict(center):
            return False
        self.center = center
        return True


    def draw(self):
        for cube in self.get_all_gridpos():
            pygame.draw.rect(screen, self.color,
                             (cube[1] * GRID_WIDTH, cube[0] * GRID_WIDTH,
                              GRID_WIDTH, GRID_WIDTH))
            pygame.draw.rect(screen, WHITE,
                             (cube[1] * GRID_WIDTH, cube[0] * GRID_WIDTH,
                              GRID_WIDTH, GRID_WIDTH),
                             1)




def draw_grids():
    for i in range(GRID_NUM_WIDTH):
        pygame.draw.line(screen, LINE_COLOR,
                         (i * GRID_WIDTH, 0), (i * GRID_WIDTH, HEIGHT))


    for i in range(GRID_NUM_HEIGHT):
        pygame.draw.line(screen, LINE_COLOR,
                         (0, i * GRID_WIDTH), (WIDTH, i * GRID_WIDTH))


    pygame.draw.line(screen, WHITE,
                     (GRID_WIDTH * GRID_NUM_WIDTH, 0),
                     (GRID_WIDTH * GRID_NUM_WIDTH, GRID_WIDTH * GRID_NUM_HEIGHT))




def draw_matrix():
    for i, row in zip(range(GRID_NUM_HEIGHT), screen_color_matrix):
        for j, color in zip(range(GRID_NUM_WIDTH), row):
            if color is not None:
                pygame.draw.rect(screen, color,
                                 (j * GRID_WIDTH, i * GRID_WIDTH,
                                  GRID_WIDTH, GRID_WIDTH))
                pygame.draw.rect(screen, WHITE,
                                 (j * GRID_WIDTH, i * GRID_WIDTH,
                                  GRID_WIDTH, GRID_WIDTH), 2)




def draw_score():
    show_text(screen, u'得分：{}'.format(score), 20, WIDTH + SIDE_WIDTH // 2, 100)




def remove_full_line():
    global screen_color_matrix
    global score
    global level
    new_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
    index = GRID_NUM_HEIGHT - 1
    n_full_line = 0
    for i in range(GRID_NUM_HEIGHT - 1, -1, -1):
        is_full = True
        for j in range(GRID_NUM_WIDTH):
            if screen_color_matrix[i][j] is None:
                is_full = False
                continue
        if not is_full:
            new_matrix[index] = screen_color_matrix[i]
            index -= 1
        else:
            n_full_line += 1
    score += n_full_line
    level = score // 20 + 1
    screen_color_matrix = new_matrix




def show_welcome(screen):
    show_text(screen, u'俄罗斯方块', 30, WIDTH / 2, HEIGHT / 2)
    show_text(screen, u'按任意键开始游戏', 20, WIDTH / 2, HEIGHT / 2 + 50)




running = True
gameover = True
counter = 0
live_cube = None
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if gameover:
                gameover = False
                live_cube = CubeShape()
                break
            if event.key == pygame.K_LEFT:
                live_cube.left()
            elif event.key == pygame.K_RIGHT:
                live_cube.right()
            elif event.key == pygame.K_DOWN:
                live_cube.down()
            elif event.key == pygame.K_UP:
                live_cube.rotate()
            elif event.key == pygame.K_SPACE:
                while live_cube.down() == True:
                    pass
            remove_full_line()


    # level 是为了方便游戏的难度，level 越高 FPS // level 的值越小
    # 这样屏幕刷新的就越快，难度就越大
    if gameover is False and counter % (FPS // level) == 0:
        # down 表示下移骨牌，返回False表示下移不成功，可能超过了屏幕或者和之前固定的
        # 小方块冲突了
        if live_cube.down() == False:
            for cube in live_cube.get_all_gridpos():
                screen_color_matrix[cube[0]][cube[1]] = live_cube.color
            live_cube = CubeShape()
            if live_cube.conflict(live_cube.center):
                gameover = True
                score = 0
                live_cube = None
                screen_color_matrix = [[None] * GRID_NUM_WIDTH for i in range(GRID_NUM_HEIGHT)]
        # 消除满行
        remove_full_line()
    counter += 1
    # 更新屏幕
    screen.fill(BLACK)
    draw_grids()
    draw_matrix()
    draw_score()
    if live_cube is not None:
        live_cube.draw()
    if gameover:
        show_welcome(screen)
    pygame.display.update()
```

### 

### 4、连连看

1. 案例介绍

连连看是一款曾经非常流行的小游戏。游戏规则：
1. 点击选中两个相同的方块。1. 两个选中的方块之间连接线的折点不超过两个(接线由X轴和Y轴的平行线组成)。1. 每找出一对，它们就会自动消失。1. 连线不能从尚未消失的图案上经过。1. 把所有的图案全部消除即可获得胜利。
2. 设计思路
1. 生成成对的图片元素。1. 将图片元素打乱排布。1. 定义什么才算 `相连`(两张图片的连线不多于3跟直线，或者说转角不超过2个)。1. 实现 `相连` 判断算法。1. 消除图片元素并判断是否消除完毕。
3. 示例效果<img src="https://img-blog.csdnimg.cn/img_convert/7cdbbd538dd1fae835fe563ec50075c2.gif" alt="7cdbbd538dd1fae835fe563ec50075c2.gif">4. 示例源码

```
from tkinter import *
from tkinter.messagebox import *
from threading import Timer
import time
import random




class Point:
    # 点类
    def __init__(self, x, y):
        self.x = x
        self.y = y




# --------------------------------------




'''
判断选中的两个方块是否可以消除
'''




def IsLink(p1, p2):
    if lineCheck(p1, p2):
        return True
    if OneCornerLink(p1, p2):  # 一个转弯（折点）的联通方式
        return True
    if TwoCornerLink(p1, p2):  # 两个转弯（折点）的联通方式
        return True
    return False




# ---------------------------
def IsSame(p1, p2):
    if map[p1.x][p1.y] == map[p2.x][p2.y]:
        print("clicked at IsSame")
        return True
    return False




def callback(event):  # 鼠标左键事件代码
    global Select_first, p1, p2
    global firstSelectRectId, SecondSelectRectId


    # print ("clicked at", event.x, event.y,turn)
    x = (event.x) // 40  # 换算棋盘坐标
    y = (event.y) // 40
    print("clicked at", x, y)


    if map[x][y] == " ":
        showinfo(title="提示", message="此处无方块")
    else:


        if Select_first == False:
            p1 = Point(x, y)
            # 画选定（x1,y1)处的框线
            firstSelectRectId = cv.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, width=2, outline="blue")
            Select_first = True
        else:
            p2 = Point(x, y)
            # 判断第二次点击的方块是否已被第一次点击选取，如果是则返回。
            if (p1.x == p2.x) and (p1.y == p2.y):
                return
            # 画选定（x2,y2)处的框线
            print('第二次点击的方块', x, y)
            # SecondSelectRectId=cv.create_rectangle(100,20,x*40+40,y*40+40,width=2,outline="yellow")
            SecondSelectRectId = cv.create_rectangle(x * 40, y * 40, x * 40 + 40, y * 40 + 40, width=2,
                                                     outline="yellow")
            print('第二次点击的方块', SecondSelectRectId)
            cv.pack()


            # 判断是否连通
            if IsSame(p1, p2) and IsLink(p1, p2):
                print('连通', x, y)
                Select_first = False
                # 画选中方块之间连接线
                drawLinkLine(p1, p2)
                # clearTwoBlock()
                # time.sleep(0.6)
                # clearFlag=True
                t = Timer(timer_interval, delayrun)  # 定时函数
                t.start()




            else:  # 重新选定第一个方块
                # 清除第一个选定框线
                cv.delete(firstSelectRectId)
                cv.delete(SecondSelectRectId)
                # print('清除第一个选定框线')
                # firstSelectRectId=SecondSelectRectId
                # p1=Point(x,y)           #设置重新选定第一个方块的坐标
                Select_first = False




timer_interval = 0.3  # 0.3秒




# --------------------------------------
def delayrun():
    clearTwoBlock()  # 清除连线及方块




def clearTwoBlock():  # 清除连线及方块
    # 延时0.1秒
    # time.sleep(0.1)
    # 清除第一个选定框线
    cv.delete(firstSelectRectId)
    # 清除第2个选定框线
    cv.delete(SecondSelectRectId)
    # 清空记录方块的值
    map[p1.x][p1.y] = " "
    cv.delete(image_map[p1.x][p1.y])
    map[p2.x][p2.y] = " "
    cv.delete(image_map[p2.x][p2.y])
    Select_first = False
    undrawConnectLine()  # 清除选中方块之间连接线




def drawQiPan():  # 画棋盘
    for i in range(0, 15):
        cv.create_line(20, 20 + 40 * i, 580, 20 + 40 * i, width=2)
    for i in range(0, 15):
        cv.create_line(20 + 40 * i, 20, 20 + 40 * i, 580, width=2)
    cv.pack()




def print_map():  # 输出map地图
    global image_map
    for x in range(0, Width):  # 0--14
        for y in range(0, Height):  # 0--14
            if (map[x][y] != ' '):
                img1 = imgs[int(map[x][y])]
                id = cv.create_image((x * 40 + 20, y * 40 + 20), image=img1)
                image_map[x][y] = id
    cv.pack()
    for y in range(0, Height):  # 0--14
        for x in range(0, Width):  # 0--14
            print(map[x][y], end=' ')
        print(",", y)




'''
* 同行同列情况消除方法 原理：如果两个相同的被消除元素之间的 空格数
spaceCount等于他们的（行/列差-1）则 两者可以联通消除
* x代表列，y代表行
* param p1 第一个保存上次选中点坐标的点对象
* param p2 第二个保存上次选中点坐标的点对象
'''




# 直接连通
def lineCheck(p1, p2):
    absDistance = 0
    spaceCount = 0
    if (p1.x == p2.x or p1.y == p2.y):  # 同行同列的情况吗？
        print("同行同列的情况------")
        # 同列的情况
        if (p1.x == p2.x and p1.y != p2.y):
            print("同列的情况")
            # 绝对距离(中间隔着的空格数)
            absDistance = abs(p1.y - p2.y) - 1
            # 正负值
            if p1.y - p2.y &gt; 0:
                zf = -1
            else:
                zf = 1
            for i in range(1, absDistance + 1):
                if (map[p1.x][p1.y + i * zf] == " "):
                    # 空格数加1
                    spaceCount += 1
                else:
                    break;  # 遇到阻碍就不用再探测了


        # 同行的情况
        elif (p1.y == p2.y and p1.x != p2.x):
            print(" 同行的情况")
            absDistance = abs(p1.x - p2.x) - 1
            # 正负值
            if p1.x - p2.x &gt; 0:
                zf = -1
            else:
                zf = 1
            for i in range(1, absDistance + 1):
                if (map[p1.x + i * zf][p1.y] == " "):
                    # 空格数加1
                    spaceCount += 1
                else:
                    break;  # 遇到阻碍就不用再探测了
        if (spaceCount == absDistance):
            # 可联通
            print(absDistance, spaceCount)
            print("行/列可直接联通")
            return True
        else:
            print("行/列不能消除！")
            return False
    else:
        # 不是同行同列的情况所以直接返回false
        return False;


    # --------------------------------------




# 第二种，直角连通
'''
直角连接，即X,Y坐标都不同的，可以用这个方法尝试连接
 param first:选中的第一个点
 param second:选中的第二个点
'''




def OneCornerLink(p1, p2):
    # 第一个直角检查点，如果这里为空则赋予相同值供检查
    checkP = Point(p1.x, p2.y)
    # 第二个直角检查点，如果这里为空则赋予相同值供检查
    checkP2 = Point(p2.x, p1.y);
    # 第一个直角点检测
    if (map[checkP.x][checkP.y] == " "):
        if (lineCheck(p1, checkP) and lineCheck(checkP, p2)):
            linePointStack.append(checkP)
            print("直角消除ok", checkP.x, checkP.y)
            return True
    # 第二个直角点检测
    if (map[checkP2.x][checkP2.y] == " "):
        if (lineCheck(p1, checkP2) and lineCheck(checkP2, p2)):
            linePointStack.append(checkP2)
            print("直角消除ok", checkP2.x, checkP2.y)
            return True
    print("不能直角消除")
    return False;




# -----------------------------------------
'''
#第三种，双直角连通
双直角联通判定可分两步走：
1. 在p1点周围4个方向寻找空格checkP
2. 调用OneCornerLink(checkP, p2)
3. 即遍历 p1 4 个方向的空格，使之成为 checkP,然后调用 OneCornerLink(checkP, 
p2)判定是否为真，如果为真则可以双直角连同，否则当所有的空格都遍历完而没有找
到一个checkP使OneCornerLink(checkP, p2)为真，则两点不能连同
具体代码：


双直角连接方法
@param p1 第一个点
@param p2 第二个点
'''




def TwoCornerLink(p1, p2):
    checkP = Point(p1.x, p1.y)
    # 四向探测开始
    for i in range(0, 4):
        checkP.x = p1.x
        checkP.y = p1.y
        # 向下
        if (i == 3):
            checkP.y += 1
            while ((checkP.y &lt; Height) and map[checkP.x][checkP.y] == " "):
                linePointStack.append(checkP)
                if (OneCornerLink(checkP, p2)):
                    print("下探测OK")
                    return True
                else:
                    linePointStack.pop()
                checkP.y += 1
            print("ssss", checkP.y, Height - 1)
            # 补充两个折点都在游戏区域底侧外部
            if checkP.y == Height:  # 出了底部，则仅需判断p2能否也达到底部边界
                z = Point(p2.x, Height - 1)  # 底部边界点
                if lineCheck(z, p2):  # 两个折点在区域外部的底侧
                    linePointStack.append(Point(p1.x, Height))
                    linePointStack.append(Point(p2.x, Height))
                    print("下探测到游戏区域外部OK")
                    return True
        # 向右
        elif (i == 2):
            checkP.x += 1
            while ((checkP.x &lt; Width) and map[checkP.x][checkP.y] == " "):
                linePointStack.append(checkP)
                if (OneCornerLink(checkP, p2)):
                    print("右探测OK")
                    return True
                else:
                    linePointStack.pop()
                checkP.x += 1
            # 补充两个折点都在游戏区域右侧外部
            if checkP.x == Width:  # 出了右侧，则仅需判断p2能否也达到右部边界
                z = Point(Width - 1, p2.y)  # 右部边界点
                if lineCheck(z, p2):  # 两个折点在区域外部的底侧
                    linePointStack.append(Point(Width, p1.y))
                    linePointStack.append(Point(Width, p2.y))
                    print("右探测到游戏区域外部OK")
                    return True
        # 向左
        elif (i == 1):
            checkP.x -= 1
            while ((checkP.x &gt;= 0) and map[checkP.x][checkP.y] == " "):
                linePointStack.append(checkP)
                if (OneCornerLink(checkP, p2)):
                    print("左探测OK")
                    return True
                else:
                    linePointStack.pop()
                checkP.x -= 1
        # 向上
        elif (i == 0):
            checkP.y -= 1
            while ((checkP.y &gt;= 0) and map[checkP.x][checkP.y] == " "):
                linePointStack.append(checkP)
                if (OneCornerLink(checkP, p2)):
                    print("上探测OK")
                    return True
                else:
                    linePointStack.pop()
                checkP.y -= 1


    # 四个方向都寻完都没找到适合的checkP点
    print("两直角连接没找到适合的checkP点")
    return False;




# ---------------------------
# 画连接线
def drawLinkLine(p1, p2):
    if (len(linePointStack) == 0):
        Line_id.append(drawLine(p1, p2))
    else:
        print(linePointStack, len(linePointStack))
    if (len(linePointStack) == 1):
        z = linePointStack.pop()
        print("一折连通点z", z.x, z.y)
        Line_id.append(drawLine(p1, z))
        Line_id.append(drawLine(p2, z))
    if (len(linePointStack) == 2):
        z1 = linePointStack.pop()
        print("2折连通点z1", z1.x, z1.y)
        Line_id.append(drawLine(p2, z1))
        z2 = linePointStack.pop()
        print("2折连通点z2", z2.x, z2.y)
        Line_id.append(drawLine(z1, z2))
        Line_id.append(drawLine(p1, z2))




# 删除连接线
def undrawConnectLine():
    while len(Line_id) &gt; 0:
        idpop = Line_id.pop()
        cv.delete(idpop)




def drawLine(p1, p2):
    print("drawLine p1,p2", p1.x, p1.y, p2.x, p2.y)
    # cv.create_line( 40+20, 40+20,200,200,width=5,fill='red')
    id = cv.create_line(p1.x * 40 + 20, p1.y * 40 + 20, p2.x * 40 + 20, p2.y * 40 + 20, width=5, fill='red')
    # cv.pack()
    return id




# --------------------------------------
def create_map():  # 产生map地图
    global map
    # 生成随机地图
    # 将所有匹配成对的动物物种放进一个临时的地图中
    tmpMap = []
    m = (Width) * (Height) // 10
    print('m=', m)
    for x in range(0, m):
        for i in range(0, 10):  # 每种方块有10个
            tmpMap.append(x)
    random.shuffle(tmpMap)
    for x in range(0, Width):  # 0--14
        for y in range(0, Height):  # 0--14
            map[x][y] = tmpMap[x * Height + y]




# --------------------------------------
def find2Block(event):  # 自动查找
    global firstSelectRectId, SecondSelectRectId
    m_nRoW = Height
    m_nCol = Width
    bFound = False;
    # 第一个方块从地图的0位置开始
    for i in range(0, m_nRoW * m_nCol):
        # 找到则跳出循环
        if (bFound):
            break


        # 算出对应的虚拟行列位置
        x1 = i % m_nCol
        y1 = i // m_nCol
        p1 = Point(x1, y1)
        # 无图案的方块跳过
        if (map[x1][y1] == ' '):
            continue
        # 第二个方块从前一个方块的后面开始
        for j in range(i + 1, m_nRoW * m_nCol):
            # 算出对应的虚拟行列位置
            x2 = j % m_nCol
            y2 = j // m_nCol
            p2 = Point(x2, y2)
            # 第二个方块不为空 且与第一个方块的动物相同
            if (map[x2][y2] != ' ' and IsSame(p1, p2)):
                # 判断是否可以连通
                if (IsLink(p1, p2)):
                    bFound = True
                    break
    # 找到后自动消除
    if (bFound):  # p1（x1,y1）与p2（x2,y2）连通
        print('找到后', p1.x, p1.y, p2.x, p2.y)
        # 画选定（x1,y1)处的框线
        firstSelectRectId = cv.create_rectangle(x1 * 40, y1 * 40, x1 * 40 + 40, y1 * 40 + 40, width=2, outline="red")
        # 画选定（x2,y2)处的框线
        secondSelectRectId = cv.create_rectangle(x2 * 40, y2 * 40, x2 * 40 + 40, y2 * 40 + 40, width=2, outline="red")
        # t=Timer(timer_interval,delayrun)#定时函数
        # t.start()


    return bFound




# 游戏主逻辑
root = Tk()
root.title("Python连连看 ")
imgs = [PhotoImage(file='images\\bar_0' + str(i) + '.gif') for i in range(0, 10)]  # 所有图标图案
Select_first = False  # 是否已经选中第一块
firstSelectRectId = -1  # 被选中第一块地图对象
SecondSelectRectId = -1  # 被选中第二块地图对象
clearFlag = False
linePointStack = []
Line_id = []
Height = 10
Width = 10
map = [[" " for y in range(Height)] for x in range(Width)]
image_map = [[" " for y in range(Height)] for x in range(Width)]
cv = Canvas(root, bg='green', width=440, height=440)
# drawQiPan( )
cv.bind("&lt;Button-1&gt;", callback)  # 鼠标左键事件
cv.bind("&lt;Button-3&gt;", find2Block)  # 鼠标右键事件
cv.pack()
create_map()  # 产生map地图
print_map()  # 打印map地图
root.mainloop()
```

往期推荐



















**如果本文对你有帮助的话，就<strong>点赞、****在看吧**！谢谢~</strong>

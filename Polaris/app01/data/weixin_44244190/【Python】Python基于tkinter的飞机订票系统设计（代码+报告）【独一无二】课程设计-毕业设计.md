
--- 
title:  【Python】Python基于tkinter的飞机订票系统设计（代码+报告）【独一无二】课程设计-毕业设计 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Python基于tkinter的飞机订票系统设计（代码+报告）【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- <ul><li>- - - -  
   </li></ul> 
  </li></ul> 
  
  


## 一、需求分析

飞机订票系统是一种为旅客提供航班信息查询、机票购买和退订等服务的应用程序。该系统旨在简化用户预订航班的流程，提高用户体验，同时为航空公司提供更有效的航班管理和客户服务。

本系统的主要目标是实现以下功能：首先，提供航班信息查询功能，包括航班号、起点、终点、出发时间、到达时间、票价以及剩余座位等信息，使用户能够方便快捷地找到符合其需求的航班。其次，实现机票购买功能，用户可以根据查询到的航班信息进行机票购买操作，选择购买数量并完成支付流程。第三，实现机票退订功能，用户可以在一定期限内对已购买的机票进行退订操作，系统会根据退订数量将相应座位释放出来。

综上所述，飞机订票系统的设计需满足用户对航班信息查询、机票购买和退订等基本需求，同时还需考虑系统的可用性、稳定性和安全性，以提供更优质的服务和更良好的用户体验。

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


## 二、系统设计与实现

### 2.1 代码设计

#### 2.2.1 登录界面

显示应用程序的图标或标志 (self.start_image): 使用了 tk.PhotoImage 对象加载了一个应用程序的图标或标志，存储在 self.start_image 中。这个图标或标志可以是应用程序的品牌标识，用于增加界面的专业感和识别度。

```
class LoginWindow:
    def __init__(self):
        self.root_login = tk.Tk()
        self.root_login.title("登入窗口")
        self.root_login.geometry("440x300+420+150")
        self.root_login.iconbitmap(LOGO_PATH)
        self.root_login.resizable(False, False)
        self.root_login["background"] = "white"
        ## widget
        self.style_login = ttk.Style()
        self.style_login.configure("login.TPanedwindow", bg="Azure")
        ## login_label(登入图片）
        self.login_image = tk.PhotoImage(file=IMAGE_PATH_login)
        self.login_label = tk.Label(self.root_login, image=self.login_image)
        self.login_label.place(x=3, y=10)

```

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


<img src="https://img-blog.csdnimg.cn/direct/db0d0bf6a60d4ba6accbf1461d716bcf.png" alt="在这里插入图片描述">

#### 2.1.2 主界面显示

显示当前用户的用户名 (self.user_label):使用了 tk.Label 控件创建了一个标签，用于显示当前用户的用户名。标签文本使用了 self.user 变量，该变量可能是在程序运行过程中从登录界面获取的用户信息。 设置了合适的字体、字号、背景色和前景色，以增强用户界面的可读性和美观性。

显示当前日期 (self.date):同样使用了 tk.Label 控件创建了另一个标签，用于显示当前日期。日期信息通过 self.cur.date() 获取，其中 self.cur 可能是一个日期时间对象，用于获取当前日期信息。同样设置了合适的字体、字号、背景色和前景色，以保持界面的统一风格。

```
    def show_image(self):
        image_window = tk.Toplevel(self.root_login)
        image_window.title("显示图片")
        image_window.geometry("400x400")
        # Load and display the image
        image_path = "image.png"  # Update with your image path
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image_window, image=photo)
        label.image = photo  # Keep a reference, otherwise image won't display
        label.pack()

```

<img src="https://img-blog.csdnimg.cn/direct/7ca0ed05476e4e96926b71b4b9a2f484.png" alt="在这里插入图片描述">

使用 ttk.Notebook 创建选项卡布局：通过 ttk.Notebook 控件创建了一个选项卡布局，即 self.notebook 对象。 ttk.Notebook 提供了一个标签页式的容器，可以在其中放置多个子页面，并通过选项卡进行切换。

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


包括三个选项卡： 可选余票：通过创建一个 tk.Frame 对象作为选项卡的子页面，命名为 self.frame1。 已选购：通过创建另一个 tk.Frame 对象作为第二个选项卡的子页面，命名为 self.frame2。 客户信息：还可能有一个名为 self.frame3 的子页面，用于显示客户信息，但在提供的代码中未展示具体实现。

```
  self.start_image = tk.PhotoImage(file=IMAGE_PATH)
  self.Lable_image = tk.Label(self.root, image=self.start_image)
  self.Lable_image.pack()
  self.user_label = tk.Label(self.root, text="当前用户：%s" % self.user, font=("华文黑体", 15, "bold"), bg="white",
                             fg="black")
  self.user_label.place(x=650, y=35)
  self.date = tk.Label(self.root, text="当前日期：{}".format(self.cur.date()), font=("华文黑体", 15, "bold"), bg="white",
                       fg="black")
  self.date.place(x=650, y=60)
  # 设定选项卡
  self.notebook = ttk.Notebook(self.root)
  self.frame1 = tk.Frame()
  self.frame2 = tk.Frame()
  self.frame3 = tk.Frame()


```

通过这种选项卡设计，用户界面得以分为不同的部分，每个选项卡对应不同的功能或信息展示，使得界面结构更加清晰，用户可以方便地切换和访问不同的功能模块。

#### 2.1.3 添加航班信息

在代码中，可选余票界面 (frame1) 和已选购界面 (frame2) 的设计如下： 可选余票界面 (frame1): 按钮设计： 信息添加、修改、删除、选票、导入文件和保存数据等按钮： Button_add: 添加航班信息的按钮。 Button_alter: 修改航班信息的按钮。 Button_delete: 删除航班信息的按钮。 Button_select: 选票的按钮。 Button_modify: 导入文件的按钮。 Button_save: 保存数据的按钮。

<img src="https://img-blog.csdnimg.cn/direct/9c1997789393491382f448db12fe744b.png" alt="在这里插入图片描述">

#### 2.1.3 查询航班信息

航班信息查询部分： 提供了航班信息查询的输入框和查询按钮： Entry_sno: 输入航班号的文本框。 Entry_start: 输入起点的文本框。 Entry_end: 输入终点的文本框。 Button_query: 查询航班信息的按钮。 Button_all: 显示全部航班信息的按钮。

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


可选余票的航班信息展示： 使用 Tree 控件显示可选余票的航班信息。 显示航班号、出发时间、到站时间、起点、终点、票价、余额和时长等信息。 <img src="https://img-blog.csdnimg.cn/direct/370138a5ea5240949492c368a317b478.png" alt="在这里插入图片描述">

#### 2.1.4 航班选票

已选购界面 (frame2): 按钮设计： 退票按钮：用于退订已购航班的按钮。 Button_cancel: 退票的按钮。

```
 # 设定选项卡
 self.notebook = ttk.Notebook(self.root)
 self.frame1 = tk.Frame()
 self.frame2 = tk.Frame()
 self.frame3 = tk.Frame()

```

已选购航班信息展示： 使用 Tree2 控件显示已选购的航班信息。 显示航班号、出发时间、到站时间、起点、终点、票价、余额和时长等信息。 <img src="https://img-blog.csdnimg.cn/direct/d32ae6d8298f4fd294fed092d62ccbce.png" alt="在这里插入图片描述">

提供已选购航班信息的查询输入框和查询按钮： 用户可以通过输入航班号等信息来查询已选购航班信息。

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


**其他界面设计：** 使用 PanedWindow 和 LabelFrame 布局组织界面，提供了合适的分割和组织布局的容器。 设定了合适的布局、大小和位置，使界面整洁美观，易于用户操作和理解。

```
self.Pane_left = tk.PanedWindow(self.frame1, width=162, bg="Azure")
self.Pane_left.pack(fill=tk.Y, side=tk.LEFT, padx=2, pady=2)

self.Button_add = tk.Button(self.Pane_left, text="信息添加", width=13, font=("华文黑体", 12, "bold"),
                            command=self.add_item)
self.Button_add.place(x=5, y=10)
self.Button_alter = tk.Button(self.Pane_left, text="信息修改", width=13, font=("华文黑体", 12, "bold"),
                              command=self.alter_item)
self.Button_alter.place(x=5, y=40)
self.Button_delete = tk.Button(self.Pane_left, text="信息删除", width=13, font=("华文黑体", 12, "bold"),
                               command=self.delete_item)
self.Button_delete.place(x=5, y=70)
self.Button_select = tk.Button(self.Pane_left, text="选票", width=13, font=("华文黑体", 12, "bold"),
                               command=self.select_item)
self.Button_select.place(x=5, y=100)
self.Button_modify = tk.Button(self.Pane_left, text="导入文件", width=13, font=("华文黑体", 12, "bold"),
                               command=self.openfile)
self.Button_modify.place(x=5, y=420)
self.Button_save = tk.Button(self.Pane_left, text="保存数据", width=13, font=("华文黑体", 12, "bold"),
                             command=self.save)
self.Button_save.place(x=5, y=450)

```

**航班操作功能设计** 选票 (select_item 方法): 弹出新窗口，提供航班信息选择界面。 用户可以在新窗口中选择需要购买的航班信息。

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


```
 def select_item(self):

     self.top_number = tk.Tk()
     self.top_number.title("select")
     label_number = tk.Label(self.top_number, text="请输入票数")
     entry_number = tk.Entry(self.top_number)
     button_number = tk.Button(self.top_number, text="确定", command=lambda: self.select_confirm(entry_number.get()))
     label_number.grid(row=0, column=0)
     entry_number.grid(row=0, column=1)
     button_number.grid(row=0, column=2)

```

**退票 (cancel_selected 方法):** 弹出新窗口，要求用户输入退票数量。 根据用户输入的数量进行退票操作。 更新已选购航班信息和待购航班信息的显示。

```
   self.Pane_left_2 = tk.PanedWindow(self.frame2, width=162, bg="Azure")
   self.Pane_left_2.pack(fill=tk.Y, side=tk.LEFT, padx=2, pady=2)
   self.Button_cancel = tk.Button(self.Pane_left_2, text="退票", width=13, font=("华文黑体", 12, "bold"),
                                  command=self.cancel_selected)
   self.Button_cancel.place(x=5, y=10)

```

<img src="https://img-blog.csdnimg.cn/direct/a4fd3b15ae9f4b408e16b10c49a5bb6c.png" alt="
">

**航班信息查询 (find_item 和 find_item2 方法):** 用户可以根据航班号、起点和终点进行航班信息的查询。 查询结果将在对应的 Treeview 控件中显示。

```
def find_item(self):
    number = self.find_text()
    if (number == 0):
        return
    else:
        self.all_seek = []
        all_item_cur = []
        for it in self.Tree.get_children():
            all_item_cur.append(self.Tree.item(it, 'values'))
        self.all_seek = all_item_cur
        for index in self.find_texts.keys():
            self.all_seek = find_item1(self.all_seek, int(index), self.find_texts[index])

        # 如果没有查询到结果，进行相应的提示
        if (len(self.all_seek) == 0):
            showinfo(title="提示", message="无查询结果，请适当修改查询条件")
        # 查询到结果，进行数据的显示
        else:
            self.load_treeview(self.all_seek)

```

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


**辅助功能设计** 数据展示与更新 (load_treeview 和 load_treeview2 方法): 根据提供的航班信息列表，将数据加载到相应的 Treeview 控件中进行展示。 包括航班号、出发时间、到站时间、起点、终点、票价、余额等信息。

```
  self.load_treeview(self.all_fight_list)
  self.load_treeview2(self.all_selected)

```

**异常处理与提示信息：** 在文件读取、航班信息加载等过程中，进行异常处理。 当出现异常时，通过消息框 (showinfo) 提示用户相关信息。

```
    def load_info(self):
        try:
            self.all_fight_list = []
            with open(file="待购航班情况.txt", mode="r", encoding="utf-8") as fd:
                # 一次读一行
                current_line = fd.readline()
                while current_line:
                    temp_list = current_line.strip().split(",")  # 长字符串分割层三个
                    self.all_fight_list.append(temp_list)
                    # 读取下一行,读完了循环就结束了
                    current_line = fd.readline()
            self.all_selected = []
            with open(file="已购航班情况.txt", mode="r", encoding="utf-8") as f:
                # 一次读一行
                current_line = f.readline()
                while current_line:
                    temp_list = current_line.strip().split(",")  # 长字符串分割层三个
                    self.all_selected.append(temp_list)
                    # 读取下一行,读完了循环就结束了
                    current_line = f.readline()
        except:
            showinfo("系统消息", "文件读取出现异常！")

```

>  
 👇👇👇 关注公众号，回复 “飞机订票系统” 获取源码👇👇👇 


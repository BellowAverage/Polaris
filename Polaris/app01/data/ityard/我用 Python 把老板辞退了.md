
--- 
title:  我用 Python 把老板辞退了 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20210701213514411.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

>  
 丝葱：怎么小二一副愁眉苦脸的样子？ 


<img src="https://img-blog.csdnimg.cn/2021070121354177.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

>  
 小二：唉 … 别说了，葱少，还不是家里用钱的地方太多，老板给的又太少，快揭不开锅了 … 


<img src="https://img-blog.csdnimg.cn/20210701213554810.gif#pic_center" alt="">

>  
 丝葱：这还不简单，给你老板写封辞职信，让他把尾款给你结了，你那边完事即刻来达万报道。不过你老板可能不会轻易同意，你要想好应对之策。 


<img src="https://img-blog.csdnimg.cn/20210701213605905.gif#pic_center" alt="">

>  
 小二：不同意是不可能的，看我用 Python 写封辞职信，让老板分分钟同意。 


<img src="https://img-blog.csdnimg.cn/20210701213616745.gif#pic_center" alt="">

先睹为快。

<img src="https://img-blog.csdnimg.cn/202107012136287.gif#pic_center" alt="" width="500">

老板无论是点关闭还是点不同意，都无法关闭窗口，最后只能无奈同意了 …

辞职信的主要功能包括：同意、不同意、关闭窗口。
- 同意：点击同意弹出提示框，点击提示框上按钮可关闭整个窗口- 不同意：点击不同意，不同意按钮移动，点击一次移动一次 …- 关闭窗口：点击 `X` 号关闭窗口，弹出羞辱提示框
下面来看一下具体代码实现。

同意代码实现如下：

```
def agree():
    win = tk.Toplevel(window)
    win.geometry("500x150+{}+{}".
                 format(int((screenwidth - width) / 2),
                        int((screenheight - height) / 2)))
    win.title("辞职")
    label = tk.Label(win, text="您耗子尾汁", font=("华文行楷", 20))
    label.pack()
    btn = tk.Button(win, text="滚出去", width=6, height=1, command=window.destroy)
    btn.pack()

```

不同意代码实现如下：

```
def disagree():
    B2.place_forget()
    B2.place(x=random.randint(100, 500), y=random.randint(100, 500))

```

关闭窗口代码实现如下：

```
def closeWindow():
    messagebox.showinfo(title="不同意关不掉", message="关不掉吧，呵呵")

```

源码在公众号 **Python小二** 后台回复 **resign** 获取。

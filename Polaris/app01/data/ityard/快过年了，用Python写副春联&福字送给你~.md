
--- 
title:  快过年了，用Python写副春联&福字送给你~ 
tags: []
categories: [] 

---
马上要过年了，用 Python 写一副春联&amp;福字送给大家，本文我们主要用到的 Python 库为 tkinter，下面一起来看一下具体实现。

首先，我们创建一个画布，代码实现如下：

```
root=Tk()
root.title('新年快乐')
canvas=Canvas(root,width=500,height=460,bg='lightsalmon')

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/49a218492dc845d585285379a9b45f5e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

我们接着写上联，主要代码实现如下：

```
for i in range(0,451):
    canvas.create_rectangle(10,3,76,i,outline='#FFA07A',fill='red')
    root.update()
	
for i in range(len(str_1)):
    canvas.create_text(40,str_2[i],text=str_1[i],fill='#FFD700',font=('楷体',30,'bold'))
    root.update()
    time.sleep(0.5)	

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/9284e640a914461baff1a2c843681ae1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

再接着写横批，主要代码实现如下：

```
for i in range(150,350):
    canvas.create_rectangle(150,3,i,62,outline='#FFA07A',fill='red')
    root.update()

for i in range(len(str_4)):
    canvas.create_text(str_5[i],33,text=str_4[i],fill='#FFD700',font=('楷体',30,'bold'))
    root.update()
    time.sleep(0.5)

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/59e43c12218047bdb006cea85005e96e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

再接着写下联，主要代码实现如下：

```
for i in range(0,451):
    canvas.create_rectangle(424,3,490,i,outline='#FFA07A',fill='red')
    root.update()

for i in range(len(str_3)):
    canvas.create_text(454,str_2[i],text=str_3[i],fill='#FFD700',font=('楷体',30,'bold'))
    root.update()
    time.sleep(0.5)

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/92528d0b3fea4fbdac07285ab928c361.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

我们再接着画一扇简单的门，主要代码实现如下：

```
for i in range(167,251):
    canvas.create_rectangle(167,130,i,441,outline='#FFA07A',fill='red')
    root.update()

for i in range(250,334):
    canvas.create_rectangle(250,130,i,441,outline='#FFA07A',fill='red')
    root.update()

```

看一下效果：

<img src="https://img-blog.csdnimg.cn/fd77f0ff258849ccb06d4ca03c84cd42.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

感觉门上有点光秃秃的，这样我们再接着在门上写两个福字，代码实现如下：

```
canvas.create_text(210,280,fill='#FFD700',text='福',font=('楷体',45,'bold'))
canvas.create_text(290,280,fill='#FFD700',text='福',font=('楷体',45,'bold'))

```

看一下最终效果：

<img src="https://img-blog.csdnimg.cn/0cad4cf240014fa7aaa337513aef5d84.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAUHl0aG9u5bCP5LqM,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="">

源码在下方公号后台回复**春联**获取~
